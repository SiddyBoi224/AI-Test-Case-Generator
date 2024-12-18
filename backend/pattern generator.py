import pandas as pd

def generate_test_cases(input_df):
    """
    Generate test cases by detecting simple patterns in input data.
    """
    output_df = input_df.copy()

    # Example logic: Extend numeric sequences
    for col in input_df.columns:
        if pd.api.types.is_numeric_dtype(input_df[col]):
            last_value = input_df[col].iloc[-1]
            new_values = [last_value + i for i in range(1, 4)]  # Generate 3 new values
            output_df = output_df.append({col: v for v in new_values}, ignore_index=True)

        elif input_df[col].dtype == 'object':  # Handle strings
            output_df[col] = input_df[col] + "_new"

    return output_df
