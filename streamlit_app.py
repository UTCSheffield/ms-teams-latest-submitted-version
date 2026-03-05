import streamlit as st

st.set_page_config(page_title="Teams Assignment Archive", layout="wide")

st.title("Teams Assignment Archive Tool")

st.sidebar.header("Configuration")


# --- Team Selection with Sticky Deselection ---
st.sidebar.subheader("Select Teams")

# Example team list (replace with API call in future)
example_teams = [
	"Maths Department",
	"Physics Department",
	"Cyber EPQ",
	"Robotics Club",
	"Staff Room",
	"Other Team"
]

# Use session state to persist selection
if "selected_teams" not in st.session_state:
	st.session_state.selected_teams = example_teams.copy()

selected = st.sidebar.multiselect(
	"Teams you want to include:",
	options=example_teams,
	default=st.session_state.selected_teams,
	help="Deselect teams not relevant to your department. Selection will be remembered."
)
st.session_state.selected_teams = selected

st.sidebar.write(f"Selected teams: {', '.join(selected) if selected else 'None'}")

# Placeholder for output location picker
st.sidebar.subheader("Output Location")
st.sidebar.write("Output location picker will go here.")

# Placeholder for mode toggle
st.sidebar.subheader("Mode")
st.sidebar.write("Mode toggle (links/archive) will go here.")

# Placeholder for date range and student filter
st.sidebar.subheader("Filters")
st.sidebar.write("Date range and student filter will go here.")

# Main area for progress/status
st.header("Progress & Status")
st.write("Progress bar and status display will go here.")

# Footer
st.markdown("---")
st.caption("GitHub Copilot - Teams Assignment Archive UI Scaffold")
