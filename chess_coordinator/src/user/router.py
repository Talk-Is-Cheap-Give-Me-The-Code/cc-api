from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/user/profile", tags=["users"])
def read_user_profile():
    """
    @brief Detailed view of a particular user

    @return An object that contains all information about a user:
            - Name of the user
            - Email of the user
    """
    return {"user": "user profile"}


@user_router.get("/user/settings", tags=["users"])
def read_user_settings():
    """
    @brief Detailed view of a particular user's current settings

    @return An object that contains all information about a user's current settings
    """
    return {"user": "user settings"}


@user_router.patch("/user/settings/update/name", tags=["users"])
def update_user_name():
    """
    @brief Update the name of a user

    @return 200 on success
    """
    return {"user": "update name"}


@user_router.patch("/user/settings/update/email", tags=["users"])
def update_user_email():
    """
    @brief Update the email of a user

    @return 200 on success
    """
    return {"user": "update email"}


@user_router.patch("/user/settings/update/password", tags=["users"])
def update_user_password():
    """
    @brief Update the password of a user

    @return 200 on success
    """
    return {"user": "update password"}


@user_router.get("/user/tournaments", tags=["users"])
def read_user_tournaments():
    """
    @brief List of all the tournaments of a user

    @return A list of all id's of the tournaments of a user
    """
    return {"user": "user tournaments"}
