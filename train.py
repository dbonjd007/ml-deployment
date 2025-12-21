import joblib
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]

model = LinearRegression()
model.fit(X,y)
joblib.dump(model, "model.pkl")
print("Model saved")