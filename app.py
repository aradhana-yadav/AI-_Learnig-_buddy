import streamlit as st

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            st.success(f"Python Learning Buddy explains:\n\n{topic} is an important programming concept. It is easy to learn and is widely used in web development, AI, automation and data science.")

        elif option == "Real-Life Example":
            st.info(f"Real-life example:\n\nThink of {topic} like learning English. Once you know the basics, you can communicate with computers just as English helps you communicate with people.")

        elif option == "Generate Quiz":
            st.write("""
### Quiz

1. Python is a ______?
- A. Programming Language ✅
- B. Browser
- C. Database
- D. Operating System

2. Which function prints output?
- A. print() ✅
- B. output()
- C. display()
- D. show()

3. Python is used in?
- A. AI
- B. Data Science
- C. Web Development
- D. All of these ✅
""")

        else:
            st.write("AI Buddy Response:")
            st.write(f"You asked: {topic}\n\nThis is a demo response prepared for the capstone project.")
