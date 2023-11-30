# Sample data (Replace this with your own dataset or data handling)
# Let's assume you have lists representing features and house prices
# Example data for features and corresponding house prices
features = [[1400], [1600], [1700], [1875], [1100]]  # Example feature: house area in square feet
house_prices = [245000, 312000, 279000, 308000, 199000]  # Corresponding house prices

# Simple linear regression function
def simple_linear_regression(features, target):
    n = len(features)
    sum_x = sum(features)
    sum_y = sum(target)
    sum_xy = sum([x * y for x, y in zip(features, target)])
    sum_x_sq = sum([x ** 2 for x in features])

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

# Calculate slope and intercept using simple linear regression
slope, intercept = simple_linear_regression([f[0] for f in features], house_prices)

# Function to predict house price
def predict_price(area):
    return slope * area + intercept

# Example prediction for a house area of 1500 square feet
predicted_price = predict_price(1500)
print(f"Predicted house price for an area of 1500 square feet: {predicted_price}")
