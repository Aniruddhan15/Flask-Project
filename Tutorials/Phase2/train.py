# save_model.py
import pickle
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load and split dataset
data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model using pickle
with open('wine_model.pkl', 'wb') as f:
    pickle.dump(model, f)
