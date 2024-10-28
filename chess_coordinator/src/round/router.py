from fastapi import APIRouter

round_router = APIRouter()


@round_router.post("/round/create", tags=["round"])
def create_round():
    """
    Create a new round.

    Args:
        tournament_id (int): The ID of the tournament.
        start_time (str): The start time of the round (maybe unnecessary).

    Returns:
        dict: An identifier for the newly created round.
    """
    return {"round": "create"}


@round_router.get("/round/{round_id}", tags=["round"])
def get_round(round_id: int):
    """
    Get the information of a round.

    Args:
        round_id (int): The ID of the round.

    Returns:
        dict: An object that contains all information about a round.
    """
    return {"round": round_id}


@round_router.delete("/round/{round_id}/delete", tags=["round"])
def delete_round(round_id: int):
    """
    Delete a round.

    Args:
        round_id (int): The ID of the round.

    Returns:
        dict: 200 on success.
    """
    return {"round": round_id, "delete": "delete"}


@round_router.post("/round/{round_id}/export", tags=["round"])
def export_round(round_id: int):
    """
    Export a round.

    Args:
        round_id (int): The ID of the round.

    Returns:
        dict: A file that contains all the information about a round (JSON for now).
    """
    return {"round": round_id, "export": "export"}


@round_router.get("/round/{round_id}/stats", tags=["round"])
def get_round_stats(round_id: int):
    """
    Get the statistics of a round.

    Args:
        round_id (int): The ID of the round.

    Returns:
        dict: An object that contains all statistics of a round.
    """
    return {"round": round_id, "stats": "stats"}


@round_router.get("/round/{round_id}/pairings", tags=["round"])
def get_round_pairings(round_id: int):
    """
    Get the pairings of a round.

    Args:
        round_id (int): The ID of the round.

    Returns:
        dict: An object that contains all pairings of a round.
    """
    return {"round": round_id, "pairings": "pairings"}


@round_router.put("/round/{round_id}/update/pairs", tags=["round"])
def update_round_pairs(round_id: int):
    """
    Update the pairings of a round.

    Args:
        round_id (int): The ID of the round.
        pairs (list): The new pairings of the round (e.g. [(playerW, playerB, score), (playerW, playerB, score), ...]).

    Returns:
        dict: 200 on success.
    """
    return {"round": round_id, "update": "pairs"}
