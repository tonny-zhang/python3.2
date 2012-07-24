class Person():
	NAME = 'Person';
	def setName (self,name):
		self.name = name;
	def getName (self,):
		return self.name;
	def say (self,):
		print(self.name + ' say "hello" to every one!');

class Scientist (Person):
	def createTool (self):
		print(self.name+" is creating tool!");
	def work (self):
		print('creating');

class Farmer(Person):
	#类中定义的方法必须至少有一个参数，接收对象本身
	def farm (self):
		print(self.name+" is a farmer!");
	def work (self):
		print('farmming');

#超级类有相同的超类，且有相同的方法时，前者会重写后者的方法
class SupperMan(Scientist,Farmer):
	pass;

one = Person();
one.setName('one');
print(one.getName());
one.say();

two = Person();
two.setName('two');
print(two.getName());
two.say();

scientist = Scientist();
scientist.setName('aiyinston');
scientist.createTool();

farmer = Farmer();
farmer.setName('nongmin');
farmer.farm();

supperMan = SupperMan();
supperMan.setName('supper');
supperMan.work();


