import streamlit as st

def main():
    # Initialize session state for user data
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

    # Right container for displaying entered data
    with col2:
        st.header('Entered Data')

        # Display user entered data after submission
        if submit_button:
            st.subheader('User Entered Data:')
            st.write(f"Age: {st.session_state['user_data']['Age']}")
            st.write(f"Title: {st.session_state['user_data']['Title']}")
            st.write(f"Meeting Frequency: {st.session_state['user_data']['Meeting Frequency']}")
            st.write(f"Meeting Duration: {st.session_state['user_data']['Meeting Duration']} min")
            st.write(f"Closed Deals: {st.session_state['user_data']['Closed Deals']}")
            st.write(f"Email Intent: {st.session_state['user_data']['Email Intent']}")
            st.write(f"Calls Frequency: {st.session_state['user_data']['Calls Frequency']}")
            st.write(f"Calls Duration: {st.session_state['user_data']['Calls Duration']} min")
            st.write(f"Campaign Frequency: {st.session_state['user_data']['Campaign Frequency']}")
            st.write(f"Years of Experience: {st.session_state['user_data']['Years of Experience']}")
            st.write(f"Contact Role Tagged: {st.session_state['user_data']['Contact Role Tagged']}")
            st.write(f"Value Score: {st.session_state['user_data']['Value Score']}")
            st.write(f"Mood Score: {st.session_state['user_data']['Mood Score']}")
            st.write(f"Engagement Score: {st.session_state['user_data']['Engagement Score']}")
            st.write(f"Stages Involved In: {', '.join(st.session_state['user_data']['Stages Involved In'])}")
            st.write(f"Popular Keywords: {st.session_state['user_data']['Popular Keywords']}")

if __name__ == '__main__':
    main()
