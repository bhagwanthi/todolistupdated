import streamlit as st

# Function to display prediction and reasoning based on user and ideal data
def display_predictions():
    user_data = st.session_state['user_data']
    ideal_data = st.session_state['ideal_data']

    # Combine user and ideal data
    combined_data = {**user_data, **ideal_data}

    # Perform prediction logic here (replace with your actual prediction code)
    prediction_text = f"Prediction based on data: {combined_data}"
    st.write(prediction_text)

    # Perform reasoning logic here (replace with your actual reasoning code)
    reasoning_text = "Reasoning behind the prediction..."
    st.write(reasoning_text)

def main():
    # Initialize session state for user and ideal data
    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = {
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
            'Popular Keywords': ''
        }

    if 'ideal_data' not in st.session_state:
        st.session_state['ideal_data'] = {
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
            'Ideal Engagement Score': '',
            'Ideal Stages Involved In': [],
            'Ideal Popular Keywords': ''
        }

    # Display title centered
    st.markdown("<h1 style='text-align: center;'>Contact Persona</h1>", unsafe_allow_html=True)

    # Define layout with two equal-width columns
    col1, col2 = st.columns(2)

    # Left container for user inputs (Input Features)
    with col1:
        st.header('Input Features')

        # User inputs
        with st.form(key='user_input_form'):
            st.session_state['user_data']['Age'] = st.text_input('Age', value=st.session_state['user_data']['Age'])
            st.session_state['user_data']['Title'] = st.text_input('Title', value=st.session_state['user_data']['Title'])
            st.session_state['user_data']['Meeting Frequency'] = st.text_input('Meeting Frequency', value=st.session_state['user_data']['Meeting Frequency'])
            st.session_state['user_data']['Meeting Duration'] = st.number_input('Meeting Duration (min)', min_value=0, value=st.session_state['user_data']['Meeting Duration'], step=1)
            st.session_state['user_data']['Closed Deals'] = st.text_input('Closed Deals', value=st.session_state['user_data']['Closed Deals'])
            st.session_state['user_data']['Email Intent'] = st.text_input('Email Intent', value=st.session_state['user_data']['Email Intent'])
            st.session_state['user_data']['Calls Frequency'] = st.text_input('Calls Frequency', value=st.session_state['user_data']['Calls Frequency'])
            st.session_state['user_data']['Calls Duration'] = st.number_input('Calls Duration (min)', min_value=0, value=st.session_state['user_data']['Calls Duration'], step=1)
            st.session_state['user_data']['Campaign Frequency'] = st.text_input('Campaign Frequency', value=st.session_state['user_data']['Campaign Frequency'])
            st.session_state['user_data']['Years of Experience'] = st.text_input('Years of Experience', value=st.session_state['user_data']['Years of Experience'])
            st.session_state['user_data']['Contact Role Tagged'] = st.text_input('Contact Role Tagged', value=st.session_state['user_data']['Contact Role Tagged'])
            st.session_state['user_data']['Value Score'] = st.text_input('Value Score', value=st.session_state['user_data']['Value Score'])
            st.session_state['user_data']['Mood Score'] = st.text_input('Mood Score', value=st.session_state['user_data']['Mood Score'])
            st.session_state['user_data']['Engagement Score'] = st.text_input('Engagement Score', value=st.session_state['user_data']['Engagement Score'])
            st.session_state['user_data']['Stages Involved In'] = st.multiselect('Stages Involved In', options=[
                'qualification',
                'needs analysis',
                'value proposition',
                'identify decision makers',
                'price quote',
                'negotiation',
                'closed won',
                'closed lost'
            ], default=st.session_state['user_data']['Stages Involved In'])
            st.session_state['user_data']['Popular Keywords'] = st.text_input('Popular Keywords', value=st.session_state['user_data']['Popular Keywords'])

            submit_button = st.form_submit_button('Submit')

    # Right container for ideal user information
    with col2:
        st.header('Ideal User Info')

        persona_options = [
            'Decision Maker',
            'Influencer',
            'End User',
            'Champion Customer',
            'Gatekeeper',
            'Technical Buyer'
        ]
        persona_selection = st.selectbox('Select Persona', options=[''] + persona_options)

        if persona_selection:
            with st.expander(f"{persona_selection} - Ideal Info", expanded=False):
                st.session_state['ideal_data'][f'Ideal Age'] = st.text_input('Ideal Age', value=st.session_state['ideal_data'][f'Ideal Age'])
                st.session_state['ideal_data'][f'Ideal Title'] = st.text_input('Ideal Title', value=st.session_state['ideal_data'][f'Ideal Title'])
                st.session_state['ideal_data'][f'Ideal Meeting Frequency'] = st.text_input('Ideal Meeting Frequency', value=st.session_state['ideal_data'][f'Ideal Meeting Frequency'])
                st.session_state['ideal_data'][f'Ideal Meeting Duration'] = st.number_input('Ideal Meeting Duration (min)', min_value=0, value=st.session_state['ideal_data'][f'Ideal Meeting Duration'], step=1)
                st.session_state['ideal_data'][f'Ideal Closed Deals'] = st.text_input('Ideal Closed Deals', value=st.session_state['ideal_data'][f'Ideal Closed Deals'])
                st.session_state['ideal_data'][f'Ideal Email Intent'] = st.text_input('Ideal Email Intent', value=st.session_state['ideal_data'][f'Ideal Email Intent'])
                st.session_state['ideal_data'][f'Ideal Calls Frequency'] = st.text_input('Ideal Calls Frequency', value=st.session_state['ideal_data'][f'Ideal Calls Frequency'])
                st.session_state['ideal_data'][f'Ideal Calls Duration'] = st.number_input('Ideal Calls Duration (min)', min_value=0, value=st.session_state['ideal_data'][f'Ideal Calls Duration'], step=1)
                st.session_state['ideal_data'][f'Ideal Campaign Frequency'] = st.text_input('Ideal Campaign Frequency', value=st.session_state['ideal_data'][f'Ideal Campaign Frequency'])
                st.session_state['ideal_data'][f'Ideal Years of Experience'] = st.text_input('Ideal Years of Experience', value=st.session_state['ideal_data'][f'Ideal Years of Experience'])
                st.session_state['ideal_data'][f'Ideal Contact Role Tagged'] = st.text_input('Ideal Contact Role Tagged', value=st.session_state['ideal_data'][f'Ideal Contact Role Tagged'])
                st.session_state['ideal_data'][f'Ideal Value Score'] = st.text_input('Ideal Value Score', value=st.session_state['ideal_data'][f'Ideal Value Score'])
                st.session_state['ideal_data'][f'Ideal Mood Score'] = st.text_input('Ideal Mood Score', value=st.session_state['ideal_data'][f'Ideal Mood Score'])
                st.session_state['ideal_data'][f'Ideal Engagement Score'] = st.text_input('Ideal Engagement Score', value=st.session_state['ideal_data'][f'Ideal Engagement Score'])
                st.session_state['ideal_data'][f'Ideal Stages Involved In'] = st.multiselect('Ideal Stages Involved In', options=[
                    'qualification',
                    'needs analysis',
                    'value proposition',
                    'identify decision makers',
                    'price quote',
                    'negotiation',
                    'closed won',
                    'closed lost'
                ], default=st.session_state['ideal_data'][f'Ideal Stages Involved In'])
                st.session_state['ideal_data'][f'Ideal Popular Keywords'] = st.text_input('Ideal Popular Keywords', value=st.session_state['ideal_data'][f'Ideal Popular Keywords'])

    # Display predictions and reasoning
    st.header('Predictions and Reasoning')
    display_predictions()

if __name__ == '__main__':
    main()
