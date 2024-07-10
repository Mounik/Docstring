import os

dossier = "dossier_test"

# Create a directory named 'dossier_test' if it does not already exist.
# If the directory already exists, do nothing (because of 'exist_ok=True').
os.makedirs(dossier, exist_ok=True)
