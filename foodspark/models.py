from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator
import hashlib
from django.core.validators import  *
from django.core.exceptions import ValidationError
import datetime
import sms

PICKUP_TIME_FORMAT = '%H:%M'

# default order time bug hai
class Restaurant(models.Model):
	email = models.EmailField(primary_key = True)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	address = models.TextField()
	cuisine = models.CharField(null = True, max_length=100)
	# RATING = (
	# 	('1','1'),
	# 	('2','2'),
	# 	('3','3'),
	# 	('4','4'),
	# 	('5','5')
	# )
	# rating = models.CharField(null = True,max_length=1,choices = RATING)
	# countrating = models.IntegerField(default = 0)
	phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be entered in the format: '99999999'. 8 digits only.") #############look into regex
	phone = models.CharField(validators=[phone_regex],max_length=15)
	imgurl = models.CharField(max_length=1000,null=True)
	############################################################
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		assert password
		hashed = hashlib.md5(password).hexdigest()
		return self.password == hashed
	def set_password(self, password):
		self.password = password

	def __unicode__(self):
		return self.name

class Customer(models.Model):
	# userid = models.CharField(primary_key = True,max_length =50)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=200)
	email = models.EmailField(primary_key = True)
	phone_regex = RegexValidator(regex=r'^\d{8}$', message="Phone number must be entered in the format: '99999999'. 8 digits only.") #############look into regex
	phone = models.CharField(validators=[phone_regex],max_length=15,blank = True)
	def make_password(self ,password):
		assert password
		hashedpassword = hashlib.md5(password).hexdigest()
		return hashedpassword
	def check_password(self, password):
		assert password
		hashed = hashlib.md5(password).hexdigest()
		return self.password == hashed
	def set_password(self, password):
		self.password = password

	def __unicode__(self):
		return self.name

class FoodItem(models.Model):
	resid = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	cuisine = models.CharField(max_length=100)
	COURSE = (
		('s','Starter'),
		('m','Main Course'),
		('d','Desert')
	)
	course = models.CharField(max_length=1,choices=COURSE)
	price = models.FloatField()
	ordercount = models.IntegerField(default = 0)
	# image = models.ImageField(null = True) ###########################################################
	# group = models.ForeignKey()

	def __unicode__(self):
		return self.name

class Order(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	foodlist = models.CharField(max_length = 500,validators=[validate_comma_separated_integer_list],null=True)
	foodqty = models.CharField(max_length = 500,validators=[validate_comma_separated_integer_list],null=True)
	amount = models.FloatField(default = 0)
	ordertime = models.TimeField()
	pickuptime = models.TimeField()
	orderdate = models.DateField(auto_now_add=True)	
	STATUS = (
		(0,'Sent'),
		(1,'Cancelled'),
	)
	status = models.IntegerField(default=0, choices=STATUS)

	def calamount(self):
		self.amount = 0
		myl = self.foodlist.split(",")
		qty = self.foodqty.split(",")
		for x,y in zip(myl,qty):
			fitem = FoodItem.objects.get(pk=int(x))
			self.amount = self.amount + fitem.price*int(y)

	def getfooditems(self):
		myl = self.foodlist.split(",")
		items = []
		for x in myl:
			items.append(FoodItem.objects.get(pk=int(x)))
		return items

	def getqty(self):
		myl = self.foodqty.split(",")
		return myl

	def send_sms(self, cancelled=False):
		myl = self.foodlist.split(",")
		qty = self.foodqty.split(",")
		amount = 0
		text = ''
		for x,y in zip(myl,qty):
			fitem = FoodItem.objects.get(pk=int(x))
			text += ' {0}|qty={1};'.format(fitem.name, y)
			amount += fitem.price*int(y)
		text += ' total:${0}'.format(amount)
		text += ', pick-up at {0}'.format(self.pickuptime.strftime(PICKUP_TIME_FORMAT))

		# send sms to Restaurent
		if cancelled:
			header1 = 'CANCELLED!!! The order was cancelled from {0}|{1}:'.format(self.customer.name, self.customer.phone)
		else:
			header1 = 'Order from {0}|{1}:'.format(self.customer.name, self.customer.phone)
		sms.send(self.restaurant.phone, header1+text)

		# send sms to Customer
		if cancelled:
			header2 = 'CANCELLED!!! You have cancelled the order from {0}|{1}:'.format(self.restaurant.name, self.restaurant.phone)
		else:
			header2 = 'You have ordered from {0}|{1}:'.format(header2, self.restaurant.name, self.restaurant.phone)
		sms.send(self.customer.phone, header2+text)

class Cart(models.Model):
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
 	fooditem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
 	foodqty = models.IntegerField()
