import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv('books_data.csv')
rating_mapping = {
    'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5
}
df['rating'] = df['rating'].map(rating_mapping)
df['availability'] = df['availability'].apply(lambda x: 1 if x == 'In Stock' else 0)
df['price'] = pd.to_numeric(df['price'].replace('£', '', regex=True), errors='coerce')
df.dropna(subset=['price'], inplace=True)
print("Data shape after cleaning:", df.shape)
print("Missing values in each column:")
print(df.isnull().sum())
X = df[['rating', 'availability']]
y = df['price']
if X.shape[0] == 0:
    print("Not enough data after preprocessing. Check for invalid values.")
else:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    print("Linear Regression Model Evaluation:")
    print(f"Mean Absolute Error (MAE): {mae}")
    print(f"Mean Squared Error (MSE): {mse}")
    print(f"Root Mean Squared Error (RMSE): {rmse}")
    print(f"R-squared (R2): {r2}")
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, color='blue', label='Predicted vs Actual')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', lw=2, label='Ideal Prediction')
    plt.title('Actual vs Predicted Prices')
    plt.xlabel('Actual Prices')
    plt.ylabel('Predicted Prices')
    plt.legend()
    plt.show()