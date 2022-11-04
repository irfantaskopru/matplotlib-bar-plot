import matplotlib.pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

plt.plot(months, revenue)

ax = plt.subplot()

ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_lower = [i * 0.9 for i in revenue]
y_upper = [i * 1.1 for i in revenue]

plt.fill_between(month_names, y_lower, y_upper, alpha = 0.2) # alpha alt ve üst sınır çizgisinin saydamlığı

plt.show()