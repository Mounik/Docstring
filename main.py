import os

dossier = "dossier_test"

if os.path.exists(dossier):
  os.rmdir(dossier)
else:
  os.mkdir(dossier)

