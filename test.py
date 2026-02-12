# Libraries
import pickle as pkl
import warnings
warnings.filterwarnings('ignore')

# User input for data
def get_user_input():
    age = int(input("Enter age: "))
    pclass = int(input("Enter class of passenger (1: First, 2: Second, 3: Third): "))
    sex = int(input("Enter sex (0: Female, 1: Male): "))
    sisp = int(input("Enter number of siblings/spouses aboard: "))
    parch = int(input("Enter number of parents/children aboard: "))
    fare = float(input("Enter fare: "))
    embarked = int(input("Enter embarked (0: C, 1: Q, 2: S) ~ C = Cherbourg, Q = Queenstown, and S = Southampton"))
    cabin_known = int(input("Is the cabin known? (0: No, 1: Yes): "))

    return [age, pclass, sex, sisp, parch, fare, embarked, cabin_known]

# Prediction model
def prediction_model(data):
    # Load the saved model
    with open('my_model.pkl', 'rb') as f:
        model = pkl.load(f)

    params = [data]
    prediction = model.predict(params)
    return print("Predicted Survival:", "Yes" if prediction[0] == 1 else "No")

# Run the prediction model with user input
prediction_model(get_user_input())