import streamlit as st
import datetime
import pandas as pd
import os
from io import BytesIO
import random

def get_motivation():
    motivational_quotes = [
        "Believe you can and you're halfway there. – Theodore Roosevelt",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "Don't watch the clock; do what it does. Keep going. – Sam Levenson",
        "The best way to predict the future is to create it. – Peter Drucker",
        "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
        "Act as if what you do makes a difference. It does. – William James",
        "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    ]
    return random.choice(motivational_quotes)

def growth_mindset_app():
    st.title("🌱 Growth Mindset Challenge")

    st.header("Welcome to the Growth Mindset Challenge! 🚀")
    st.write(
        "A growth mindset is the belief that abilities can be developed through dedication and hard work. "
        "This web app is designed to help you track your progress, stay motivated, and cultivate a positive learning attitude. "
        "Remember, every challenge is an opportunity for growth! 🌟"
    )

    st.subheader("📅 Daily Reflection")
    date = st.date_input("Select Date", datetime.date.today())
    reflection = st.text_area("📝 What did you learn today?")
    challenges = st.text_area("💡 What challenges did you face, and how did you overcome them?")
    next_goal = st.text_area("🎯 What is your next goal for improvement?")

    if st.button("✅ Submit Reflection"):
        st.success("Reflection Saved! Keep Growing! 🚀")

    st.header("💡 Growth Mindset Tips")
    st.write("✔ Embrace challenges as learning opportunities. 💪")
    st.write("✔ Learn from mistakes instead of fearing them. 🔄")
    st.write("✔ Celebrate effort and progress over perfection. 🎉")
    st.write("✔ Stay positive and keep pushing forward! 😊")
    st.write("✔ Seek feedback and use it as a tool for improvement. �")
    st.write("✔ Visualize success and take small steps toward your goals. 🌈")
    st.write("✔ Surround yourself with positive and supportive people. 🤝")
    st.write("✔ Practice gratitude to stay motivated and focused. 🙏")

    if st.button("💖 Get Inspired"):
        st.success(get_motivation())

    st.header("📌 Track Your Progress")
    st.write("🗂 Keep a journal of your reflections and review your progress over time!")
    st.write("📊 Set weekly or monthly growth goals to measure your improvement.")
    st.write("🔄 Stay consistent and celebrate small wins!")

    progress = st.slider("📈 How motivated do you feel today?", 0, 100, 50)
    if progress >= 75:
        st.success("🔥 Amazing! Keep up the great work!")
    elif progress >= 50:
        st.info("💪 You're doing great! Keep pushing forward!")
    else:
        st.warning("🌟 Keep going! Every small effort matters!")

    st.header("🎯 Weekly Goal Setting")
    weekly_goal = st.text_area("What is your goal for this week?")
    if st.button("Set Weekly Goal"):
        st.success("Weekly goal set! Let's achieve it together! 🚀")

    st.header("📅 Monthly Reflection")
    monthly_reflection = st.text_area("Reflect on your progress this month. What went well? What could be improved?")
    if st.button("Submit Monthly Reflection"):
        st.success("Monthly reflection saved! Keep growing! 🌱")

    st.header("🙏 Gratitude Journal")
    gratitude_entry = st.text_area("What are you grateful for today?")
    if st.button("Submit Gratitude Entry"):
        st.success("Gratitude entry saved! Practicing gratitude boosts positivity! 🌟")

    st.header("📚 Resources for Growth")
    st.write("Here are some resources to help you on your growth journey:")
    st.write("- Books: 'Mindset' by Carol Dweck, 'Atomic Habits' by James Clear")
    st.write("- Podcasts: 'The Growth Mindset Podcast', 'The Tim Ferriss Show'")
    st.write("- Videos: TED Talks on growth mindset and personal development")
    st.write("- Courses: Online courses on Coursera, Udemy, or LinkedIn Learning")

    st.header("🤝 Join the Community")
    st.write("Connect with like-minded individuals and share your growth journey!")
    st.write("- Forums: Reddit communities like r/GetMotivated, r/PersonalDevelopment")
    st.write("- Social Media: Follow hashtags like #GrowthMindset, #PersonalGrowth")
    st.write("- Local Meetups: Join local groups focused on self-improvement and growth")

    st.write("---")
    st.write("Built with ❤ by Areesha Abdul Sattar | Stay motivated and keep growing! 🌱")
    st.write("📧 Contact: areesha21314@gmail.com")

# Data Sweeper App
def data_sweeper_app():
    st.title("📊 Data Sweeper")
    st.write("✨ Transform your files between CSV and Excel formats with built-in data cleaning and visualization 🧹📈")

    uploaded_files = st.file_uploader("📂 Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

    if uploaded_files:
        for file in uploaded_files:
            file_ext = os.path.splitext(file.name)[-1].lower()

            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file)
            else:
                st.error(f"❌ Unsupported file type: {file_ext}")
                continue  

            st.write(f"📄 **File Name:** {file.name}")
            st.write(f"📏 **File Size:** {file.size / 1024:.2f} KB")

            st.write("👀 Preview the Head of the Dataframe")
            st.dataframe(df.head())

            st.subheader("🧹 Data Cleaning Options")
            if st.checkbox(f"🧽 Clean Data for {file.name}"):
                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"🚫 Remove Duplicates from {file.name}"):
                        df.drop_duplicates(inplace=True)
                        st.write("✅ Duplicates Removed!")

                with col2:
                    if st.button(f"🪣 Fill Missing Values for {file.name}"):
                        numeric_cols = df.select_dtypes(include=["number"]).columns
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.write("✅ Missing Values have been Filled!")
              
            st.subheader("🔍 Select Columns to Convert")
            columns = st.multiselect(f"📌 Choose Columns for {file.name}", df.columns, default=df.columns)
            df = df[columns]

            st.subheader("📊 Data Visualization")
            if st.checkbox(f"📈 Show visualization for {file.name}"):
                numeric_data = df.select_dtypes(include="number")
                st.write("📊 Numeric Data Preview:", numeric_data)

                if not numeric_data.empty and numeric_data.shape[1] >= 1:
                    st.bar_chart(numeric_data)
                else:
                    st.warning(f"⚠️ No numeric columns found in {file.name} for visualization!")

            st.subheader("🔄 Conversion Options")
            conversion_type = st.radio(f"🔧 Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
            if st.button(f"🔃 Convert {file.name}"):
                buffer = BytesIO()
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    df.to_excel(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

                buffer.seek(0)
                st.download_button(
                    label=f"⬇️ Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )

    st.success("🎉 All files processed!")

def main():
    st.sidebar.title("🌱 Navigation")
    app_choice = st.sidebar.radio("Choose an App:", ["Data Sweeper", "Growth Mindset Challenge"])

    if app_choice == "Data Sweeper":
        data_sweeper_app()
    else:
        growth_mindset_app()

if __name__ == "__main__":
    main()