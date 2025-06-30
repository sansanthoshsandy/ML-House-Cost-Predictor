import pickle

# Load trained model
with open('house_cost_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Input from user
area = int(input("📏 Enter area in sq.ft: "))
floors = int(input("🏢 Enter number of floors: "))
material = input("🏗️ Material type (normal/premium): ").lower()
paint = int(input("🎨 Include painting? (1 for Yes, 0 for No): "))
woodwork = int(input("🪵 Include woodwork? (1 for Yes, 0 for No): "))
tiles = int(input("🧱 Include tiles? (1 for Yes, 0 for No): "))

# Encode material
material_encoded = 0 if material == 'normal' else 1

# Predict
features = [[area, floors, material_encoded, paint, woodwork, tiles]]
predicted = model.predict(features)

# Show result
print(f"\n💰 Estimated House Cost: ₹{int(predicted[0]):,}")
