from fastapi import APIRouter

round_router = APIRouter()


@round_router.get("/round/create", tags=["round"])
def create_round():
    """
    @brief Create a new round

    @param touranment_id The ID of the tournament
    @param start_time The start time of the round (maybe unnecessary)

    @return round_id The ID of the round
    """
    return {"round": "create"}


@round_router.put("/round/{round_id}/update/pairs", tags=["round"])
def update_round_pairs(round_id: int):
    """
    @brief Update the pairings of a round

    playerW - White player
    playerB - Black player
    score - Score of the game (-1 - no score, 0 - draw, 1 - playerW wins, 2 - playerB wins)

    @param round_id The ID of the round
    @param pairs The new pairings of the round (e.g. [(playerW, playerB, score), (playerW, playerB, score), ...])

    @return 200 on success
    """
    return {"round": round_id, "update": "pairs"}


@round_router.delete("/round/{round_id}/delete", tags=["round"])
def delete_round(round_id: int):
    """
    @brief Delete a round

    @param round_id The ID of the round

    @return 200 on success
    """
    return {"round": round_id, "delete": "delete"}


@round_router.get("/round/{round_id}", tags=["round"])
def read_round(round_id: int):
    """
    @brief Get the information of a round

    @param round_id The ID of the round

    @return An object that contains all information about a round
    """
    return {"round": round_id}


@round_router.get("/round/{round_id}/stats", tags=["round"])
def read_round_stats(round_id: int):
    """
    @brief Get the statistics of a round

    @param round_id The ID of the round

    @return An object that contains all statistics of a round
    """
    return {"round": round_id, "stats": "stats"}


@round_router.get("/round/{round_id}/pairings", tags=["round"])
def read_round_pairings(round_id: int):
    """
    @brief Get the pairings of a round

    @param round_id The ID of the round

    @return An object that contains all pairings of a round
    """
    return {"round": round_id, "pairings": "pairings"}


@round_router.post("/round/{round_id}/export", tags=["round"])
def export_round(round_id: int):
    """
    @brief Export a round

    @param round_id The ID of the round

    @return A file that contains all the information about a round (JSON for now
    """
    return {"round": round_id, "export": "export"}
