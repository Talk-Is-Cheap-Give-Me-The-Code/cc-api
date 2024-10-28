from fastapi import APIRouter

tournament_router = APIRouter()


@tournament_router.post("/tournament/create", tags=["tournament"])
def create_tournament():
    """
    Create a new tournament

    Args:
        name (str): Name of the tournament
        date (str): Date of the tournament
        location (str): Location of the tournament
        members (list): List of members of the tournament

    Returns:
        dict: An identifier for the newly created tournament.
    """
    return {"tournament": "create"}


@tournament_router.get("/tournament/{tournament_id}", tags=["tournament"])
def get_tournament(tournament_id: int):
    """
    Detailed view of a particular tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: An object that contains all information about a tournament:
            - Name of the tournament
            - Date of the tournament
            - Location of the tournament
            - *Cross-table of the tournament (maybe in a separate endpoint)
    """
    return {"tournament": tournament_id}


@tournament_router.get("/tournament/{tournament_id}/export", tags=["tournament"])
def export_tournament(tournament_id: int):
    """
    Export a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: A file that contains all the information about a tournament (JSON for now).
    """
    return {"tournament": tournament_id, "export": "export"}


@tournament_router.put("/tournament/{tournament_id}/duplicate", tags=["tournament"])
def duplicate_tournament(tournament_id: int):
    """
    Duplicate a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: An identifier for the newly duplicated tournament.
    """
    return {"tournament": tournament_id, "duplicate": "duplicate"}


@tournament_router.patch("/tournament/{tournament_id}/archive", tags=["tournament"])
def archive_tournament(tournament_id: int):
    """
    Archive a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict (?): 200 on success.
    """
    return {"tournament": tournament_id, "archive": "archive"}


@tournament_router.delete("/tournament/{tournament_id}/delete", tags=["tournament"])
def delete_tournament(tournament_id: int):
    """
    Delete a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: 200 on success.
    """
    return {"tournament": tournament_id, "delete": "delete"}


@tournament_router.get("/tournament/{tournament_id}/members", tags=["tournament"])
def get_tournament_members(tournament_id: int):
    """
    List of all the members of a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: A list of all the members of a tournament together with their current scores.
    """
    return {"tournament": tournament_id, "members": "members"}


@tournament_router.put(
    "/tournament/{tournament_id}/members/update", tags=["tournament"]
)
def update_tournament_members(tournament_id: int):
    """
    Update the members of a tournament.

    Args:
        tournament_id (int): The ID of the tournament.
        members (list): List of members to add to the tournament.

    Returns:
        dict: 200 on success.
    """
    return {"tournament": tournament_id, "update": "members"}


@tournament_router.get("/tournament/{tournament_id}/rounds", tags=["tournament"])
def get_tournament_rounds(tournament_id: int):
    """
    List of all the rounds of a tournament.

    Args:
        tournament_id (int): The ID of the tournament.

    Returns:
        dict: A list of all the rounds (IDs) of a tournament.
    """
    return {"tournament": tournament_id, "rounds": "rounds"}
