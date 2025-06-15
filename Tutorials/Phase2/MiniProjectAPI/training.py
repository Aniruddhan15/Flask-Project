import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

# Fake data: [bedrooms, bathrooms, area]
X = np.array([[2, 1, 1000], [3, 2, 1500], [4, 3, 2000]])
y = np.array([100000, 150000, 200000])

model = LinearRegression()
model.fit(X, y)

with open('price_model.pkl', 'wb') as f:
    pickle.dump(model, f)
