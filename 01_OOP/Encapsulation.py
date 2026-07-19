class Experiment:
	def __init__(self, name, accuracy):
		self.name = name
		self.__accuracy = 0
		self.accuracy = accuracy

	def display_info(self):
		print(f"Name : {self.name} \n Accuracy : {self.__accuracy}")

	@property
	def accuracy(self):
		return self.__accuracy

	@accuracy.setter
	def accuracy(self,value):
		if 0<=value<=100:
			self.__accuracy = value
		else:
			print("Invalid Accuracy")

exp = Experiment("DistiBERT", 92)
print(exp.accuracy)
exp.accuracy = 95
print(exp.accuracy)
exp.accuracy = 150
print(exp.accuracy)
