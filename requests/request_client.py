""" API Request Client"""
# libs
import asyncio
import httpx
import ujson

# imports
# ------------------------------
# vars
x_client = httpx.AsyncClient(base_url="https://ynix-b.herokuapp.com", http2=True)
# =============================================================================


async def get_zone_list():
    """Returns Zone *List* of dictionaries, example: [{'zone_id': int, 'zone_name': str, 'region': str, 'zone_dr': int, 'zone_evasion': int, 'mob_type': str},]"""
    try:
        data = await x_client.get("/zones")
        return ujson.loads(data.content)
    except Exception as err:
        return err


# =============================================================================
async def get_zone_info(zone_id):
    """Return zone"""
    try:
        data = await x_client.get(f"/zones/{zone_id}")
        # return ujson.loads(data.content)
        return data
    except Exception as err:
        return err


# =============================================================================
async def get_class_info(class_id):
    try:
        data = await x_client.get(f"/class/{class_id}")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================
async def get_class_skill_list(class_id):
    try:
        data = await x_client.get(f"/class/{class_id}/skill_list")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================


async def run_calc(attacker, defender, skill_choice):
    try:
        data = await x_client.put(
            "/basic_calc",
            {
                "attacker_in": attacker,
                "defender_in": defender,
                "skill_id": (skill_choice),
            },
        )
        return ujson.loads(data)
    except Exception as err:
        return err


if __name__ == "__main__":
    response = asyncio.run(get_zone_info(33))
    print(response)

# data object ref
# data.content = raw response body
# data.text = response body text
# data.encoding
# data.links
# data.stream
# data.cookies
# data.headers
# data.history
# data.status_code
