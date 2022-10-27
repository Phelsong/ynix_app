""" API Request Client"""
# libs
import httpx
import ujson

# imports
# ------------------------------
# vars
x_client = httpx.AsyncClient(base_url="https://ynix-b.herokuapp.com")
# =============================================================================


async def get_zone_list():
    try:
        data = x_client.get("/zones")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================
async def get_zone_info():
    try:
        data = await x_client.get("/zones/{zoneid}/info")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================
async def get_class_info(classId):
    try:
        data = await x_client.get("/class/{classid}")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================
async def get_class_skill_list(classId):
    try:
        data = await x_client.get("/class/{classId}/skill_list")
        return ujson.loads(data)
    except Exception as err:
        return err


# =============================================================================


async def get_class_skill_info(classId, skillId):
    pass
