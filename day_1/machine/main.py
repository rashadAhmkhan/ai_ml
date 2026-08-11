# 1. THE DATA
# x = House Size (in thousands of sq ft to keep numbers manageable)
# y = House Price (in Lakhs)
x_data = [1.0, 1.5, 2.0, 2.5]
y_data = [20.0, 30.0, 40.0, 50.0]

# 2. STARTING GUESSES
# The machine starts completely blind with random guesses for m and c.
m = 0.0
c = 0.0

# Hyperparameters (The knobs we turn to control learning)
learning_rate = 0.05
epochs = 1000  # How many times we loop through the data
n = len(x_data)

print(f"Starting Training: Initial m = {m}, c = {c}\n")

# 3. THE TRAINING LOOP (The 5-step loop in action)
for epoch in range(epochs):
    sum_error = 0
    D_m = 0  # Gradient for slope
    D_c = 0  # Gradient for intercept
    
    # Calculate predictions and gradients for all data points
    for i in range(n):
        x = x_data[i]
        y = y_data[i]
        
        # Step A: Make Prediction (y = mx + c)
        y_predicted = (m * x) + c
        
        # Step B: Measure Error
        error = y - y_predicted
        sum_error += error ** 2  # Squaring the error!
        
        # Step C: Calculate Gradients
        D_m += (-2/n) * x * error
        D_c += (-2/n) * error
        
    # Step D: Update the parameters (Improve the model)
    m = m - (learning_rate * D_m)
    c = c - (learning_rate * D_c)
    
    # Print progress every 100 epochs
    if epoch % 25 == 0:
        mse = sum_error / n
        print(f"Epoch {epoch} | Error (MSE): {mse:.4f} | m: {m:.4f}, c: {c:.4f}")

print("\nTraining Complete!")
print(f"Final Rule: Price = {m:.2f} * Size + {c:.2f}")

# 4. TEST THE MACHINE (Phase 02: Evaluation)
# Let's predict the price for a 3000 sq ft house (3.0 in our scale)
test_size = 3.0
predicted_price = (m * test_size) + c
print(f"\nPrediction for 3000 sq ft house: ₹{predicted_price:.2f} Lakhs")
