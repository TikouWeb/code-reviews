bucket = "cloud storage bucket"
os = None
TMP_SAVE_FILE_PATH = "/tmp"


def upload_file_from_path(path, dest):
    blob = bucket.blob(dest)
    blob.upload_from_filename(path)
    os.remove(path)


def download_file(path, dest):
    blob = bucket.blob(path)
    blob.download_to_filename(f"{TMP_SAVE_FILE_PATH}/{dest}")
    return f"{TMP_SAVE_FILE_PATH}/{dest}"
