"""1st try"""
# import streamlit as st
# from rclone_python import rclone

# RCLONE_CONFIG = "./rclone.conf"

# rclone.set_config_file(RCLONE_CONFIG)

# remotes = rclone.get_remotes()

# if remotes:
#     remote_name = remotes[0] # Use the first one found (e.g., 'my-dropbox:')
#     st.success(f"Found remote: {remote_name}")
    
#     # Try listing
#     try:
#         files = rclone.ls(f"{remote_name}omkar-internship/csv/")
#         st.write(files)
#     except Exception as e:
#         st.error(f"Error: {e}")
# else:
#     st.error("No remotes found in the config file.")

"""2nd try (Working!)"""
# import streamlit as st
# import subprocess
# import json

# RCLONE_BIN = "./rclone"          # rclone installed by your command
# RCLONE_CONFIG = "./rclone.conf" # your config file

# def run_rclone(*args):
#     """Run rclone command and return stdout"""
#     result = subprocess.run(
#         [RCLONE_BIN, "--config", RCLONE_CONFIG, *args],
#         capture_output=True,
#         text=True
#     )
#     if result.returncode != 0:
#         raise RuntimeError(result.stderr.strip())
#     return result.stdout.strip()

# st.title("Rclone Test App")

# # 1️⃣ Get remotes
# try:
#     remotes_output = run_rclone("listremotes")
#     remotes = [r for r in remotes_output.splitlines() if r]

#     if not remotes:
#         st.error("No remotes found in the config file.")
#     else:
#         remote_name = remotes[0]  # e.g. "my-dropbox:"
#         st.success(f"Found remote: {remote_name}")

#         # 2️⃣ List files
#         try:
#             files_output = run_rclone(
#                 "lsjson",
#                 f"{remote_name}omkar-internship/csv/"
#             )
#             files = json.loads(files_output)
#             st.write(files)

#         except Exception as e:
#             st.error(f"Error listing files: {e}")

# except Exception as e:
#     st.error(f"Rclone error: {e}")

"""3rd try"""
import os
import streamlit as st

# --- Rclone Path Setup ---
# Get the current directory (where your build command put the rclone binary)
current_dir = os.getcwd()

# Add this directory to the system PATH so the library can find the 'rclone' executable
if current_dir not in os.environ["PATH"]:
    os.environ["PATH"] = current_dir + os.pathsep + os.environ["PATH"]
# -------------------------

from rclone_python import rclone

RCLONE_CONFIG = "./rclone.conf"

# Ensure the config file exists before trying to set it
if os.path.exists(RCLONE_CONFIG):
    rclone.set_config_file(RCLONE_CONFIG)
    
    try:
        remotes = rclone.get_remotes()

        if remotes:
            remote_name = remotes[0] # e.g., 'my-dropbox:'
            st.success(f"Found remote: {remote_name}")
            
            # Try listing
            try:
                # Note: rclone-python 'ls' returns a list of dictionaries
                files = rclone.ls(f"{remote_name}omkar-internship/csv/")
                st.write(files)
            except Exception as e:
                st.error(f"Error during listing: {e}")
        else:
            st.error("No remotes found in the config file. Check the contents of rclone.conf.")
            
    except Exception as e:
        # This will trigger if the 'rclone' binary still isn't found
        st.error(f"Rclone binary error: {e}")
else:
    st.error(f"Config file not found at {RCLONE_CONFIG}")