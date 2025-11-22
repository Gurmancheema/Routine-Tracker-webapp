import streamlit as st

st.set_page_config(page_title="Habit Tracker", layout="wide")
st.title("🗓️ Weekly Habit Tracker")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

st.subheader("Define your habits")
habit_text = st.text_area(
    "Enter one habit per line:",
    value="Wake up before 7\nWorkout\nRead 10 pages\nMeditate\nNo junk food\nLearn coding 1 hr\nSleep before 11",
    height=150,
)

habits = [h.strip() for h in habit_text.split("\n") if h.strip()]

st.markdown("---")

# Only show grid if we have habits
if habits:
    cols = st.columns(8)
    cols[0].markdown("**Habit**")
    for i, day in enumerate(days):
        cols[i + 1].markdown(f"**{day}**")

    habit_state = {}

    for habit in habits:
        row = st.columns(8)
        row[0].write(habit)
        habit_state[habit] = {}

        for i, day in enumerate(days):
            key = f"{habit}_{day}"
            habit_state[habit][day] = row[i + 1].checkbox("", key=key)

    with st.expander("Show raw data"):
        st.json(habit_state)
else:
    st.info("Add at least one habit above to start tracking.")
