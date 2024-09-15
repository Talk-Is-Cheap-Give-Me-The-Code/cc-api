from fastapi import APIRouter

tournament_router = APIRouter()


@tournament_router.get("/tournament/{tournament_id}", tags=["tournament"])
def read_tournament(tournament_id: int):
    """
    @brief Detailed view of a particular tournament

    @param tournament_id The ID of the tournament

    @return An object that contains all information about a tournament:
            - Name of the tournament
            - Date of the tournament
            - Location of the tournament
            - *Cross-table of the tournament (maybe in a separate endpoint)
    """
    return {"tournament": tournament_id}


@tournament_router.get("/tournament/{tournament_id}/members", tags=["tournament"])
def read_tournament_members(tournament_id: int):
    """
    @brief List of all the members of a tournament

    @param tournament_id The ID of the tournament

    @return A list of all the members of a tournament together with their current scores
    """
    return {"tournament": tournament_id, "members": "members"}


@tournament_router.put(
    "/tournament/{tournament_id}/members/update", tags=["tournament"]
)
def update_tournament_members(tournament_id: int):
    """
    @brief Update the members of a tournament

    @param tournament_id The ID of the tournament
    @param members List of members to add to the tournament

    @return 200 on success
    """
    return {"tournament": tournament_id, "update": "members"}


@tournament_router.get("/tournament/{tournament_id}/rounds", tags=["tournament"])
def read_tournament_rounds(tournament_id: int):
    """
    @brief List of all the rounds of a tournament

    @param tournament_id The ID of the tournament

    @return A list of all the rounds (id's) of a tournament
    """
    return {"tournament": tournament_id, "rounds": "rounds"}


@tournament_router.get("/tournament/{tournament_id}/export", tags=["tournament"])
def export_tournament(tournament_id: int):
    """
    @brief Export a tournament

    @param tournament_id The ID of the tournament

    @return A file that contains all the information about a tournament (JSON for now)
    """
    return {"tournament": tournament_id, "export": "export"}


@tournament_router.post("/tournament/create", tags=["tournament"])
def create_tournament():
    """
    Create a new tournament

    @param name: Name of the tournament
    @param date: Date of the tournament
    @param location: Location of the tournament
    @param members: List of members of the tournament

    @return An identifier for the newly created tournament
    """
    return {"tournament": "create"}


@tournament_router.put("/tournament/{tournament_id}/duplicate", tags=["tournament"])
def duplicate_tournament(tournament_id: int):
    """
    @brief Duplicate a tournament

    @param tournament_id The ID of the tournament

    @return An identifier for the newly duplicated tournament
    """
    return {"tournament": tournament_id, "duplicate": "duplicate"}


@tournament_router.patch("/tournament/{tournament_id}/archive", tags=["tournament"])
def archive_tournament(tournament_id: int):
    """
    @brief Archive a tournament

    @param tournament_id The ID of the tournament

    @return 200 on success
    """
    return {"tournament": tournament_id, "archive": "archive"}


@tournament_router.delete("/tournament/{tournament_id}/delete", tags=["tournament"])
def delete_tournament(tournament_id: int):
    """
    @brief Delete a tournament

    @param tournament_id The ID of the tournament

    @return 200 on success
    """
    return {"tournament": tournament_id, "delete": "delete"}
