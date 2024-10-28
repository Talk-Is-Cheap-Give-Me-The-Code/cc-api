from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/user/profile", tags=["users"])
def get_user_profile():
    """
    Detailed view of a particular user.

    Returns:
        dict: An object that contains all information about a user:
            - Name of the user
            - Email of the user
    """
    return {"user_id": 42, "name": "Magnus Carlsen", "email": "mcarlsen@example.com"}


@user_router.patch("/user/settings/update/name", tags=["users"])
def update_user_name():
    """
    Update the name of a user.

    Returns:
        status (int): 200 on success.
        message (str): A message indicating the success/error of the operation.
    """
    return {"status": 200, "message": "Name updated successfully"}


@user_router.patch("/user/settings/update/email", tags=["users"])
def update_user_email():
    """
    Update the email of a user.

    Returns:
        status (int): 200 on success.
        message (str): A message indicating the success/error of the operation.
    """
    return {"status": 200, "message": "Email updated successfully"}


@user_router.patch("/user/settings/update/password", tags=["users"])
def update_user_password():
    """
    Update the password of a user.

    Returns:
        status (int): 200 on success.
        message (str): A message indicating the success/error of the operation.
    """
    return {"status": 200, "message": "Password updated successfully"}


@user_router.get("/user/tournaments", tags=["users"])
def get_user_tournaments():
    """
    List of all the tournaments of a user.

    Returns:
        tournaments (dict): A list of all IDs of the tournaments of a user.
    """
    return {"tournaments": [1, 2, 3, 4, 5]}
