# Sales Prediction Web Application

## Deployed model link :- [https://machine-learning-project-feiq.onrender.com/](https://machine-learning-project-feiq.onrender.com/).

This project is a web application that predicts sales based on several features such as `Order Priority`, `Order Quantity`, `Sales`, `Ship Mode`, `Region`, `Customer Segment`, `Product Category`, and `Product Container`. The application uses a pre-trained machine learning model to make predictions and is built using Flask.


## Features

- **Order Priority**: The priority of the order (e.g., Not Specified, High, Low, Critical, Medium).
- **Order Quantity**: The quantity of the order.
- **Sales**: The sales amount.
- **Ship Mode**: The mode of shipping (e.g., Regular Air, Express Air).
- **Region**: The region where the order is placed.
- **Customer Segment**: The segment of the customer (e.g., Corporate, Consumer, Home Office, Small Business).
- **Product Category**: The category of the product (e.g., Office Supplies, Technology, Furniture).
- **Product Container**: The type of container used for the product (e.g., Small Box, Large Box, Medium Box).

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.6+
- Flask
- Pandas
- Joblib
- Scikit-learn

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/sales-prediction-app.git
    cd sales-prediction-app
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Place your pre-trained model and scaler files in the `model/` directory:

    - `model.joblib`: Pre-trained model.
    - `robust_scaler.joblib`: Pre-trained RobustScaler.

### Running the Application

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Input the required features and click "Submit" to get the sales prediction.

## Usage

1. Input the required data into the form fields on the web interface.
2. The application will map the string labels to numerical values and scale the sales amount using a RobustScaler.
3. The pre-trained model will predict the output, which is then displayed on the web interface.

### Example

To make a prediction, input the following example data:

- **Order Priority**: High
- **Order Quantity**: 10
- **Sales**: 250.50
- **Ship Mode**: Express Air
- **Region**: West
- **Customer Segment**: Corporate
- **Product Category**: Technology
- **Product Container**: Medium Box

The predicted value will be displayed after clicking "Submit".

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The project is based on a machine learning model trained using scikit-learn and optimization with Optuna.
- HTML and Tailwind CSS are used on the frontend application.
- Flask is used for building the web application.

