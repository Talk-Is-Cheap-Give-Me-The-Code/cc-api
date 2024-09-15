from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.post("/auth/login", tags=["auth"])
def login():
    """
    @brief Login to the system

    @param .... TODO

    @return 200 on success
    """
    return {"auth": "login"}


@auth_router.post("/auth/register", tags=["auth"])
def register():
    """
    @brief Register new user in the system

    @param .... TODO

    @return 200 on success
    """
    return {"auth": "register"}


@auth_router.post("/auth/logout", tags=["auth"])
def logout():
    """
    @brief Logout from the system

    @param user_id The ID of the user

    @return 200 on success
    """
    return {"auth": "logout"}
