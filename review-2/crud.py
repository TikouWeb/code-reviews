from services import upload_file_from_path, download_file

# import
# do not import dependencies (inject theme)
# Raph montre nous un exmple SVP
bucket = "cloud storage bucket"
blob = "blob somechere in cloud storage"
drive_service = "client drive"

ASSESSMENT_FC_FILES_GCS_FOLDER = "assessmentFiles"  # folder in cloud storage
TMP_SAVE_FILE_PATH = "/tmp"  # local temporary folder


class CRUD:
    def __init__(self, assessment=None):
        self.assessment = assessment

    # soit on type tout soit non.

    # unused paramas
    # does not return value
    # passer en param le blob
    def copy_letter_template(self, assessment_id: str, bucket):
        bucket.copy_blob(
            blob,
            bucket,
            f"{ASSESSMENT_FC_FILES_GCS_FOLDER}/{self.assessment['id']}/letter_template.docx",
        )
        return f"{ASSESSMENT_FC_FILES_GCS_FOLDER}/{self.assessment['id']}/letter_template.docx"

    # Does not respect single responsiblities
    def upload_generated_letter(self, assessment, letter_path):
        # letter_pdf_path = self.generate_letter()

        upload_file_from_path(
            f"{TMP_SAVE_FILE_PATH}/tmp_{self.assessment['id']}.pdf",
            f"{ASSESSMENT_FC_FILES_GCS_FOLDER}/{assessment['id']}/generated_letter.pdf",
        )

    def generate_letter(self):
        # Get template from Cloud Storage
        tmp_path = f"tmp_{self.assessment['id']}.docx"
        dest = download_file(
            f"{ASSESSMENT_FC_FILES_GCS_FOLDER}/{self.assessment['id']}/letter_template.docx",
            tmp_path,
        )

        # Replace value in template
        self._replace_docx_content(dest)

        # Download docx as pdf (from upload in Drive)
        drive_service.download_docx_as_pdf(dest, dest.replace("docx", "pdf"))
        return dest.replace("docx", "pdf")
