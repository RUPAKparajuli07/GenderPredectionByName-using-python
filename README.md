# Gender Predictor Application Documentation

## Introduction

The Gender Predictor application is a simple graphical user interface (GUI) built using the Tkinter library in Python. The purpose of this application is to predict the gender (male or female) based on the given name. The prediction is made using a predefined list of male and female names and some basic rules.

## Prerequisites

Before running the application, make sure you have Python installed on your system. The application uses the Tkinter library, which is included in the standard Python library.

## Usage

1. **Run the Application:**
   - Execute the script in a Python environment.

     ```bash
     python gender_predictor.py
     ```

2. **Interface:**
   - The application window will appear with an input field for entering a name, a button for prediction, and a field for displaying the predicted gender.

3. **Enter Name:**
   - Type the name you want to predict in the entry field labeled "Enter name."

4. **Predict Gender:**
   - Click the "Predict" button to initiate the prediction process.

5. **View Result:**
   - The predicted gender will be displayed in the entry field labeled "Predicted gender."

## Prediction Logic

The application predicts gender based on the following rules:

- If the entered name matches a name in the predefined list of boys' names, it predicts "male."
- If the entered name matches a name in the predefined list of girls' names, it predicts "female."
- If the name ends with 'a', it predicts "female."
- If the name ends with 'o', it predicts "male."
- If none of the above conditions are met, it predicts "unknown."

## Application Components

### Labels

1. **"Enter name":**
   - A label indicating the purpose of the entry field for name input.

2. **"Predicted gender":**
   - A label indicating the purpose of the entry field for displaying the predicted gender.

### Entry Fields

1. **Name Entry:**
   - An entry field for users to input the name they want to predict.

2. **Result Entry:**
   - An entry field displaying the predicted gender. This field is read-only and is updated after each prediction.

### Button

1. **Predict Button:**
   - A button triggering the prediction process when clicked.

## Styling

The application uses a simple style configuration to set the font, background, and foreground colors for labels, entry fields, and buttons.

## Conclusion

The Gender Predictor application provides a straightforward interface for predicting the gender associated with a given name. The prediction logic is based on predefined lists of names and simple rules. The application is designed to be user-friendly and easily understandable.
