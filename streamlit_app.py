import streamlit as st

st.markdown("<h1 style='color: red;'>LEGIT BUSINESS COMPANY</h1>", unsafe_allow_html=True)

st.write(
    "We specialise in small loans and are able to provide customers...")

# --- Create buttons ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Loan"):
        st.session_state.page = "loan"
with col2:
    if st.button("Debt Recovery"):
        st.session_state.page = "debt_recovery"
with col3:
    if st.button("Entrance Decoration"):
        st.session_state.page = "paint"

# --- Page content ---
if st.session_state.page == "loan":
    st.subheader("💵Loan")
    st.markdown("let us know how much you plan to borrow (principal amount), and how long for(Number of months)!")
    st.markdown("# *Ongoing promotion: should you choose to pay us back late, we will include a FREE Entrance Decoration for you!*")

    principal = st.number_input("Enter principal amount ($)", min_value=500.0, max_value=10000.0, step=100.0)
    months = st.number_input("Enter number of months", min_value=1, max_value=12, step=1)
    rate = 5
    final_amount = principal * (1 + rate/100) ** months
    st.write(f"Amount owed: ${final_amount:,.2f}")

    st.subheader("Borrower Information Submission")

    # Input fields
    loan_amount = st.text_input("Loan Amount")
    borrower_name = st.text_input("Borrower's Name")
    borrower_number = st.text_input("Borrower's Phone Number")
    borrower_address = st.text_area("Borrower's Address")

    import pandas as pd
    uploaded_files = st.file_uploader("Upload NRIC/Passport", accept_multiple_files=True, type="csv")
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    # Submit button
    if st.button("Submit"):
        if borrower_name and borrower_number and borrower_address:
            # Handle the submission (e.g., save to file, database, or send email)
            st.success(f"Submitted successfully!\nName: {borrower_name}\nNumber: {borrower_number}\nAddress: {borrower_address}")
            # Example: Save to CSV
            import csv
            with open('borrowers.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([borrower_name, borrower_number, borrower_address])
        else:
            st.error("Please fill in all fields before submitting.")

elif st.session_state.page == "debt_recovery":
    st.subheader("💼Debt Recovery")
    st.markdown("Tired of having to chase people for the money you owe? We buy Debt!")
    st.markdown("Our rates start at 75 cents on the dollar but do check with us how much the debt amount is for a discount!")
    st.markdown(" ")
    st.markdown("How much do they owe you?")

    amount = st.slider("less than 5000)", 500, 5000)
    payment = (75 / 100) * amount
    st.write(f"We buy at: ${payment:,.2f}")

    amount = st.slider("more than 5000", 5000, 10000)
    payment = (80 / 100) * amount
    st.write(f"We buy at: ${payment:,.2f}")

    st.subheader("Borrower Information Submission")

    # Input fields
    borrower_name = st.text_input("Borrower's Name")
    borrower_number = st.text_input("Borrower's Phone Number")
    borrower_address = st.text_area("Borrower's Address")
    borrower_relations = st.text_area("Borrower's Relations")

    import datetime
    payment_date = st.date_input("Original Payment Date", datetime.date(2019, 7, 1))

    import pandas as pd
    uploaded_files = st.file_uploader("Upload Prove of Evidence", accept_multiple_files=True, type="csv")
    for uploaded_file in uploaded_files:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    # Submit button
    if st.button("Submit"):
        if borrower_name and borrower_number and borrower_address and payment_date:
            # Handle the submission (e.g., save to file, database, or send email)
            st.success(f"Submitted successfully!\nName: {borrower_name}\nNumber: {borrower_number}\nAddress: {borrower_address}\nDate: {payment_date}")
            # Example: Save to CSV
            import csv
            with open('borrowers.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([borrower_name, borrower_number, borrower_address, borrower_relations, payment_date])
        else:
            st.error("Please fill in all fields before submitting.")

elif st.session_state.page == "paint":
    st.subheader("🟥Dynamic Entrance Aesthetic Remodelling")
    st.markdown("Have a house that you want to be marked? Please provide the details")
    st.markdown("Disclaimer, please only put your own adress wink wink")

# List of red gradients (you can add more!)
    red_shades = {
        "Bright Red": "#FF0000",
        "Crimson": "#DC143C",
        "Dark Red": "#8B0000",
        "Salmon Red": "#FA8072",
        "Firebrick": "#B22222",
        "Coral Red": "#FF4040"
}

    # Let user pick one
    choice = st.selectbox("Pick a shade of red", list(red_shades.keys()))
    color = red_shades[choice]

    # Show selected color
    st.markdown(f"### You chose: {choice}")
    st.markdown(
        f"""
        <div style="width:120px; height:120px; background-color:{color}; border-radius:10px;"></div>
        """,
            unsafe_allow_html=True
)
    st.write(f"Hex code: {color}")

    # Input fields
    name = st.text_input("Name")
    address = st.text_area("Address")

    # Submit button
    if st.button("Submit"):
        if name and address:
            # Handle the submission (e.g., save to file, database, or send email)
            st.success(f"Submitted successfully!\nName: {name}\nAddress: {address}")
            # Example: Save to CSV
            import csv
            with open('borrowers.csv', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, address])
        else:
            st.error("Please fill in all fields before submitting.")

st.subheader("How's our service?")
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s). Thank you.")

st.markdown("[Email us](mailto:legitbusiness@gmail.com)")








    
