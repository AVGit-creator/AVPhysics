import streamlit as st
from streamlit_option_menu import option_menu

# Set page config
st.set_page_config(page_title="AVPhysics", page_icon="🔭", layout="wide")

# Navigation bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Kinematics", "About"],
    icons=["house", "graph-up", "info-circle"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f0f8ff"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px 10px",
            "--hover-color": "#add8e6",
            "color": "#1e90ff",
            "font-weight": "600",
        },
        "nav-link-selected": {
            "background-color": "#1e90ff",
            "color": "white",
            "font-weight": "700",
            "border-radius": "10px",
        },
    },
)

# ------------------------ HOME PAGE ------------------------
if selected == "Home":
    st.header("Welcome to AVPhysics 🔭")
    st.write("Physics problems with easy to follow solutions.")
    st.image(
        "nikita-palenov-THLPC4Le0-I-unsplash.jpg",
        caption="Physics Mural – by Nikita Palenov (via Unsplash)",
        use_container_width=True,
    )

# ------------------------ KINEMATICS PAGE ------------------------
elif selected == "Kinematics":
    st.header("Kinematics")
    st.write("Learn about motion, velocity, acceleration, and more.")
    tolerance = 0.10

    # --- QUESTION 1 ---
    st.subheader("Question 1")
    st.write(
        "🧱 A brick is thrown upward from the top of a building at an angle of 25° to the horizontal "
        "with an initial speed of 15 m/s. If the brick is in flight for 3.0 s, how tall is the building?"
    )

    q1_answer = 25.0
    q1_lower = q1_answer * (1 - tolerance)
    q1_upper = q1_answer * (1 + tolerance)

    if "q1_attempts" not in st.session_state:
        st.session_state.q1_attempts = 0
    if "q1_answered" not in st.session_state:
        st.session_state.q1_answered = False
    if "q1_show_solution" not in st.session_state:
        st.session_state.q1_show_solution = False

    if not st.session_state.q1_answered:
        q1_input = st.number_input("🏗️ Enter your answer for Question 1 (in meters):", min_value=0.0, step=0.5, format="%.2f", key="q1_input")
        if st.button("Submit Q1 Answer"):
            st.session_state.q1_attempts += 1
            if q1_lower <= q1_input <= q1_upper:
                st.success("✅ Correct! The building is approximately 25 meters tall.")
                st.session_state.q1_answered = True
                st.session_state.q1_show_solution = True
            elif st.session_state.q1_attempts < 3:
                st.warning(f"❌ Incorrect. Try again! ({3 - st.session_state.q1_attempts} attempts left)")
            else:
                st.error("❌ Incorrect. You've used all your attempts.")
                st.info("✅ The correct answer is: **25 meters**.")
                st.session_state.q1_answered = True
                st.session_state.q1_show_solution = True
    else:
        st.info("✅ The correct answer is: **25 meters**.")

    if st.session_state.q1_show_solution:
        with st.expander("📎 Reveal Answer (Handwritten Solution)"):
            st.image(
                "Screenshot_20250805_141534_Samsung Notes.jpg",
                caption="Q1 Handwritten Solution",
                use_container_width=True,
            )
            with st.expander("🔍 Why use Δy = viyt + ½ayt²?"):
                st.write("It relates vertical displacement to initial vertical velocity, gravity, and time.")
            with st.expander("🔍 Why subtract 0.323 m?"):
                st.write("Because that’s the height the brick rose *after* it was thrown before falling down.")
            with st.expander("🔍 Why is acceleration negative?"):
                st.write("Gravity acts downward, opposite to the direction of initial velocity (which is up).")
            with st.expander("🔍 How many significant figures should I use?"):
                st.write("Use 3 significant figures because all inputs (15.0, 3.00) have 3.")
            with st.expander("🔍 Why use sin and cos?"):
                st.write("You use `sin(θ)` to find vertical velocity and `cos(θ)` to find horizontal velocity.")

    # --- QUESTION 2 ---
    st.divider()
    st.subheader("Question 2")
    st.write(
        "🏀 A 2.00-m-tall basketball player is standing on the floor 10.0 m from the basket. "
        "If he shoots the ball at a 40.0° angle with the horizontal, at what initial speed must he throw the basketball "
        "so that it goes through the hoop without striking the backboard? The height of the basket is 3.05 m."
    )

    q2_answer = 10.7
    q2_lower = q2_answer * (1 - tolerance)
    q2_upper = q2_answer * (1 + tolerance)

    if "q2_attempts" not in st.session_state:
        st.session_state.q2_attempts = 0
    if "q2_answered" not in st.session_state:
        st.session_state.q2_answered = False
    if "q2_show_solution" not in st.session_state:
        st.session_state.q2_show_solution = False

    if not st.session_state.q2_answered:
        q2_input = st.number_input("🏀 Enter your answer for Question 2 (in m/s):", min_value=0.0, step=0.1, format="%.2f", key="q2_input")
        if st.button("Submit Q2 Answer"):
            st.session_state.q2_attempts += 1
            if q2_lower <= q2_input <= q2_upper:
                st.success("✅ Correct! The ball will go in.")
                st.session_state.q2_answered = True
                st.session_state.q2_show_solution = True
            elif st.session_state.q2_attempts < 3:
                st.warning(f"❌ Incorrect. Try again! ({3 - st.session_state.q2_attempts} attempts left)")
            else:
                st.error("❌ Incorrect. You've used all your attempts.")
                st.info("✅ The correct answer is: **10.7 m/s**.")
                st.session_state.q2_answered = True
                st.session_state.q2_show_solution = True
    else:
        st.info("✅ The correct answer is: **10.7 m/s**.")

    if st.session_state.q2_show_solution:
        with st.expander("📎 Reveal Answer (Handwritten Solution)"):
            st.image(
                "Screenshot_20250805_141559_Samsung Notes.jpg",
                caption="Q2 Handwritten Solution",
                use_container_width=True,
            )
            with st.expander("🔍 Why substitute Δx / (v * cosθ) for time?"):
                st.write("Because horizontal velocity is constant, you can solve for time using it.")
            with st.expander("🔍 Why is Δy = 1.05 m?"):
                st.write("The basket is at 3.05 m, and the player releases the ball from 2.00 m.")
            with st.expander("🔍 What is tanθ doing here?"):
                st.write("It helps link the vertical displacement using angle and horizontal motion.")
            with st.expander("🔍 How does air resistance affect this?"):
                st.write("In real life it matters, but we assume air resistance is negligible.")

    # --- QUESTION 3 ---
    st.divider()
    st.subheader("Question 3")
    st.write(
        "🪳 Antlion larvae lie at the bottom of a 5.0 cm deep, 3.8 cm radius pit. They launch grains of sand at prey trying to escape. "
        "If the antlion launches sand at a 72° angle, what launch speed is required to hit a target at the top of the pit (5.0 cm above, 3.8 cm to the right)?"
    )

    q3_answer = 1.1
    q3_lower = q3_answer * (1 - tolerance)
    q3_upper = q3_answer * (1 + tolerance)

    if "q3_attempts" not in st.session_state:
        st.session_state.q3_attempts = 0
    if "q3_answered" not in st.session_state:
        st.session_state.q3_answered = False
    if "q3_show_solution" not in st.session_state:
        st.session_state.q3_show_solution = False

    if not st.session_state.q3_answered:
        q3_input = st.number_input("🐜 Enter your answer for Question 3 (in m/s):", min_value=0.0, step=0.05, format="%.2f", key="q3_input")
        if st.button("Submit Q3 Answer"):
            st.session_state.q3_attempts += 1
            if q3_lower <= q3_input <= q3_upper:
                st.success("✅ Correct! The sand will hit the target.")
                st.session_state.q3_answered = True
                st.session_state.q3_show_solution = True
            elif st.session_state.q3_attempts < 3:
                st.warning(f"❌ Incorrect. Try again! ({3 - st.session_state.q3_attempts} attempts left)")
            else:
                st.error("❌ Incorrect. You've used all your attempts.")
                st.info("✅ The correct answer is: **1.1 m/s**.")
                st.session_state.q3_answered = True
                st.session_state.q3_show_solution = True
    else:
        st.info("✅ The correct answer is: **1.1 m/s**.")

    if st.session_state.q3_show_solution:
        with st.expander("📎 Reveal Answer (Handwritten Solution)"):
            st.image(
                "Screenshot_20250805_141607_Samsung Notes.jpg",
                caption="Q3 Handwritten Solution",
                use_container_width=True,
            )
            with st.expander("🔍 Why convert cm to meters?"):
                st.write("Physics formulas require SI units — meters, not centimeters.")
            with st.expander("🔍 Why use cos(θ) for horizontal velocity?"):
                st.write("Because the horizontal component of velocity is adjacent to the angle.")
            with st.expander("🔍 Why solve for time first?"):
                st.write("Once you know time (from x-direction), you can plug into vertical motion.")

# ------------------------ ABOUT PAGE ------------------------
elif selected == "About":
    st.header("About")
    st.write(
        "Hi, I am a fourth-year undergraduate student in biochemistry and know how hard physics can be to learn. "
        "Throughout my academic journey I have always wanted physics problems with easy solutions. "
        "However, many textbooks don't even have properly laid out solutions to follow. Here, I have designed a webpage "
        "with physics problems and handwritten solutions hoping to make your physics learning easier."
    )
    st.markdown("---")
    st.subheader("📚 Citation")
    st.write(
        "All questions and learning materials are based on:\n\n"
        "*Serway, Raymond A., and Chris Vuille. **College Physics, 11th Edition**. Cengage Learning, 2018.*"
    )
