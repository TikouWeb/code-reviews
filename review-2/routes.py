from crud import CRUD

ASSESSMENT_FC_FILES_GCS_FOLDER = "assessmentFiles"


# "/assessments", methods=["POST"]
def createAssessment(assessment):
    # Ajouter gestion des exceptions
    # c'est le bon endroit pour traiter la demande
    crud = CRUD(assessment)
    letter_path = crud.copy_letter_template(assessment.get("id"))
    pdf_path = self.generate_letter()
    crud.upload_generated_letter(assessment, pdf_path)


# "/<assessment_id>/copy_entity_letter", methods=["POST"]
def copy_entity_letter(assessment_id: int):
    """Copy entity letter from template folder to assessment folder"""
    file_path = CRUD().copy_letter_template(assessment_id)
    return (
        {"message": "Entity letter copied successfully at" f" 'file_path"},
        200,
    )
