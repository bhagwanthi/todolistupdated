import streamlit as st

# Function to create specified fields in a column
def create_column_fields(col, fields, column_index):
    for i, field in enumerate(fields):
        # Generate a unique key based on the field name and column index
        key = f"{field}_input_{column_index}_{i}"
        
        if 'age' in field or 'frequency' in field or 'duration' in field or 'yoe' in field or 'deals' in field:
            col.number_input(field, key=key, min_value=0, step=1)
        elif 'email' in field:
            col.text_area(field, key=key)
        elif 'keywords' in field:
            col.text_area(field, key=key)
        elif 'score' in field:
            col.slider(field, key=key, min_value=0, max_value=100)
        else:
            col.text_input(field, key=key)

# Main Streamlit app
def main():
    st.set_page_config(layout="wide")  # Set page layout to wide
    st.title("Form with Submit Buttons Below Columns")
    st.write("This form has four adjacent columns with submit buttons placed below the first and third columns.")

    # Create four columns in a single row
    col1, col2, col3, col4 = st.columns(4)

    # Fields for the first column
    fields_col1 = [
        'age',
        'title',
        'meeting_frequency',
        'meeting_duration',
        'closed_deals',
        'email_intent',
        'calls_frequency',
        'calls_duration'
    ]
    create_column_fields(col1, fields_col1, 1)  # Pass 1 as column index for first column

    # Submit button for the first column
    if col1.button("Submit First Form", key="submit_form1"):
        st.success("First form submitted successfully!")

    # Divider between columns
    st.write("---")

    # Fields for the second column
    fields_col2 = [
        'campaign_frequency',
        'yoe',
        'contact_role_tagged',
        'value_score',
        'mood_score',
        'engagement_score',
        'stages_involved_in',
        'popular keywords'
    ]
    create_column_fields(col2, fields_col2, 2)  # Pass 2 as column index for second column

    # Divider between columns
    st.write("---")

    # Fields for the third column
    fields_col3 = [f'Field {i+1}' for i in range(8)]
    create_column_fields(col3, fields_col3, 3)  # Pass 3 as column index for third column

    # Submit button for the third column
    if col3.button("Submit Second Form", key="submit_form2"):
        st.success("Second form submitted successfully!")

    # Placeholder fields for the fourth column
    fields_col4 = [f'Field {i+1}' for i in range(8)]
    create_column_fields(col4, fields_col4, 4)  # Pass 4 as column index for fourth column

if __name__ == "__main__":
    main()
