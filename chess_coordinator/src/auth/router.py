from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.post("/auth/login", tags=["auth"])
def login():
    """
    Login to the system

    Args:
        -- TODO --

    Returns:
        dict: 200 on success
    """
    return {"auth": "login"}


@auth_router.post("/auth/register", tags=["auth"])
def register():
    """
    Register new user in the system

    Args:
        -- TODO--

    Returns:
        dict: 200 on success
    """
    return {"auth": "register"}


@auth_router.post("/auth/logout", tags=["auth"])
def logout():
    """
    Logout from the system

    Args:
        user_id (int): The ID of the user

    Returns:
        dict: 200 on success
    """
    return {"auth": "logout"}
