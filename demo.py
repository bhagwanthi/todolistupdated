import streamlit as st

def display_predictions(user_data):
    # Placeholder prediction logic based on user_data and ideal_data
    prediction_text = f"Prediction based on input features and ideal data: {user_data}"
    st.write(prediction_text)

    # Placeholder reasoning logic (replace with actual reasoning code)
    reasoning_text = "Reasoning behind the prediction..."
    st.write(reasoning_text)

def main():
    # Set page width to a wider layout
    st.set_page_config(layout="wide")

    # Initialize user_data and ideal_data in session state if not already initialized
    if 'data' not in st.session_state:
        st.session_state['data'] = {
            'Age': '',
            'Title': '',
            'Meeting Frequency': '',
            'Meeting Duration': 0,
            'Closed Deals': '',
            'Email Intent': '',
            'Calls Frequency': '',
            'Calls Duration': 0,
            'Campaign Frequency': '',
            'Years of Experience': '',
            'Contact Role Tagged': '',
            'Value Score': '',
            'Mood Score': '',
            'Engagement Score': '',
            'Stages Involved In': [],
            'Popular Keywords': '',
            'Ideal Age': '',
            'Ideal Title': '',
            'Ideal Meeting Frequency': '',
            'Ideal Meeting Duration': 0,
            'Ideal Closed Deals': '',
            'Ideal Email Intent': '',
            'Ideal Calls Frequency': '',
            'Ideal Calls Duration': 0,
            'Ideal Campaign Frequency': '',
            'Ideal Years of Experience': '',
            'Ideal Contact Role Tagged': '',
            'Ideal Value Score': '',
            'Ideal Mood Score': '',
            'Ideal Engagement Score': ''
        }

    # Centered title above the two columns
    st.markdown("<h1 style='text-align: center;'>Contact Persona</h1>", unsafe_allow_html=True)

    # Define the layout with one main column divided into two sections
    col1, col2 = st.columns(2)

    # Left container for user inputs (Input Features)
    with col1:
        st.header('Input Features')
        data = st.session_state['data']
        data['Age'] = st.text_input('Age', value=data['Age'])
        data['Title'] = st.text_input('Title', value=data['Title'])
        data['Meeting Frequency'] = st.text_input('Meeting Frequency', value=data['Meeting Frequency'])
        data['Meeting Duration'] = st.number_input('Meeting Duration (min)', min_value=0, value=data['Meeting Duration'], step=1)
        data['Closed Deals'] = st.text_input('Closed Deals', value=data['Closed Deals'])
        data['Email Intent'] = st.text_input('Email Intent', value=data['Email Intent'])
        data['Calls Frequency'] = st.text_input('Calls Frequency', value=data['Calls Frequency'])
        data['Calls Duration'] = st.number_input('Calls Duration (min)', min_value=0, value=data['Calls Duration'], step=1)
        data['Campaign Frequency'] = st.text_input('Campaign Frequency', value=data['Campaign Frequency'])
        data['Years of Experience'] = st.text_input('Years of Experience', value=data['Years of Experience'])
        data['Contact Role Tagged'] = st.text_input('Contact Role Tagged', value=data['Contact Role Tagged'])
        data['Value Score'] = st.text_input('Value Score', value=data['Value Score'])
        data['Mood Score'] = st.text_input('Mood Score', value=data['Mood Score'])
        data['Engagement Score'] = st.text_input('Engagement Score', value=data['Engagement Score'])
        data['Stages Involved In'] = st.multiselect('Stages Involved In', options=[
            'qualification',
            'needs analysis',
            'value proposition',
            'identify decision makers',
            'price quote',
            'negotiation',
            'closed won',
            'closed lost'
        ], default=data['Stages Involved In'])
        data['Popular Keywords'] = st.text_input('Popular Keywords', value=data['Popular Keywords'])

    # Right container for ideal user information (Ideal User Info)
    with col2:
        st.header('Ideal User Info')
        st.text('Select Persona')
        # Dropdown for selecting persona with default option "--select--"
        persona_options = [
            '--select--',
            'Decision Maker',
            'Influencer',
            'End User',
            'Champion Customer',
            'Gatekeeper',
            'Technical Buyer'
        ]
        persona_selection = st.selectbox('Select Persona', options=persona_options)

        if persona_selection and persona_selection != '--select--':
            st.text(f"Selected Persona: {persona_selection}")
            data['Ideal Age'] = st.text_input('Ideal Age', value=data['Ideal Age'])
            data['Ideal Title'] = st.text_input('Ideal Title', value=data['Ideal Title'])
            data['Ideal Meeting Frequency'] = st.text_input('Ideal Meeting Frequency', value=data['Ideal Meeting Frequency'])
            data['Ideal Meeting Duration'] = st.number_input('Ideal Meeting Duration (min)', min_value=0, value=data['Ideal Meeting Duration'], step=1)
            data['Ideal Closed Deals'] = st.text_input('Ideal Closed Deals', value=data['Ideal Closed Deals'])
            data['Ideal Email Intent'] = st.text_input('Ideal Email Intent', value=data['Ideal Email Intent'])
            data['Ideal Calls Frequency'] = st.text_input('Ideal Calls Frequency', value=data['Ideal Calls Frequency'])
            data['Ideal Calls Duration'] = st.number_input('Ideal Calls Duration (min)', min_value=0, value=data['Ideal Calls Duration'], step=1)
            data['Ideal Campaign Frequency'] = st.text_input('Ideal Campaign Frequency', value=data['Ideal Campaign Frequency'])
            data['Ideal Years of Experience'] = st.text_input('Ideal Years of Experience', value=data['Ideal Years of Experience'])
            data['Ideal Contact Role Tagged'] = st.text_input('Ideal Contact Role Tagged', value=data['Ideal Contact Role Tagged'])
            data['Ideal Value Score'] = st.text_input('Ideal Value Score', value=data['Ideal Value Score'])
            data['Ideal Mood Score'] = st.text_input('Ideal Mood Score', value=data['Ideal Mood Score'])
            data['Ideal Engagement Score'] = st.text_input('Ideal Engagement Score', value=data['Ideal Engagement Score'])

    # Display predictions and reasoning based on user input and ideal data
    st.header('Predictions and Reasoning')
    display_predictions(data)

if __name__ == '__main__':
    main()
