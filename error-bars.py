import matplotlib.pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.6, 0.9, 0.4, 0, 0.9, 0]

# capsize hata aralğını gösteren çubuğun boyutu
# yerr hata oranı içeren error dosyası 
plt.bar(range(len(drinks)), ounces_of_milk, yerr = error, capsize = 5)

plt.show()