## Streamlit stuff
- stateless -> need to store info in **sessions**, which are stored in cookies
    - sessions are bound to browser tab (session_state)
- program reruns on reload and user input (submit without reload)
- streamlit does not tell us about infinite loops running in the background. However, they keep the rest of the function from being executed