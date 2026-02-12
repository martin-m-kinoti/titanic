# Titanic Survival Prediction

## Background
On April 15, 1912, during her maiden voyage, the RMS Titanic—widely considered “unsinkable”—sank after colliding with an iceberg. Due to a shortage of lifeboats, 1,502 of the 2,224 passengers and crew lost their lives.

While chance played a role in survival, historical data suggests that certain groups of people were more likely to survive than others.

## Objective
The goal of this project is to build a predictive model that answers the question:

**“What sorts of people were more likely to survive the Titanic disaster?”**

Using passenger data, the model analyzes demographic and socioeconomic factors to identify patterns associated with survival.

## Dataset
The dataset contains passenger information such as age, gender, ticket class, fare, family relationships, port of embarkation, and cabin availability.

## Model Input Features
The trained model uses the following columns for prediction:

- `age` — Passenger age  
- `pclass` — Ticket class (1 = First, 2 = Second, 3 = Third)  
- `sex` — Gender (0 = Female, 1 = Male)  
- `sibsp` — Number of siblings/spouses aboard  
- `parch` — Number of parents/children aboard  
- `fare` — Ticket fare paid  
- `embarked` — Port of embarkation  
  - 0 = Cherbourg (C)  
  - 1 = Queenstown (Q)  
  - 2 = Southampton (S)  
- `cabin_known` — Whether cabin information is available  
  - 0 = Cabin unknown  
  - 1 = Cabin known  

## Running a Test Case
The project includes a simple test case that allows users to manually input passenger details and receive a survival prediction.

Example input flow:
```text
Enter age: 29
Enter class of passenger (1: First, 2: Second, 3: Third): 1
Enter sex (0: Female, 1: Male): 0
Enter number of siblings/spouses aboard: 0
Enter number of parents/children aboard: 0
Enter fare: 211.34
Enter embarked (0: C, 1: Q, 2: S): 0
Enter cabin known (0: No, 1: Yes): 1