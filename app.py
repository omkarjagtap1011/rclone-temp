import streamlit as st
from rclone_python import rclone

RCLONE_CONFIG = "./rclone.conf"

rclone.set_config_file(RCLONE_CONFIG)

remotes = rclone.get_remotes()

if remotes:
    remote_name = remotes[0] # Use the first one found (e.g., 'my-dropbox:')
    st.success(f"Found remote: {remote_name}")
    
    # Try listing
    try:
        files = rclone.ls(f"{remote_name}omkar-internship/csv/")
        st.write(files)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.error("No remotes found in the config file.")