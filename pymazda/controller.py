from pymazda.connection import Connection
from pymazda.exceptions import MazdaException

class Controller:
    def __init__(self, email, password, region, websession=None):
        self.connection = Connection(email, password, region, websession)

    async def login(self):
        await self.connection.login()
    
    async def get_tac(self):
        return await self.connection.api_request("GET", "content/getTac/v4", needs_keys=True, needs_auth=False)

    async def get_language_pkg(self):
        postBody = {"platformType": "ANDROID", "region": "MNAO", "version": "2.0.4"}
        return await self.connection.api_request("POST", "junction/getLanguagePkg/v4", body_dict=postBody, needs_keys=True, needs_auth=False)

    async def get_vec_base_infos(self):
        return await self.connection.api_request("POST", "remoteServices/getVecBaseInfos/v4", body_dict={"internaluserid": "__INTERNAL_ID__"}, needs_keys=True, needs_auth=True)

    async def get_vehicle_status(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin,
            "limit": 1,
            "offset": 0,
            "vecinfotype": "0"
        }
        response = await self.connection.api_request("POST", "remoteServices/getVehicleStatus/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to get vehicle status")

        return response

    async def get_health_report(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin,
            "limit": 1,
            "offset": 0
        }

        response = await self.connection.api_request("POST", "remoteServices/getHealthReport/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to get health report")

        return response

    async def door_unlock(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/doorUnlock/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to unlock door")

        return response

    async def door_lock(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/doorLock/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to lock door")

        return response

    async def light_on(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/lightOn/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to turn light on")

        return response

    async def light_off(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/lightOff/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to turn light off")

        return response

    async def engine_start(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/engineStart/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to start engine")

        return response

    async def engine_stop(self, internal_vin):
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "internalvin": internal_vin
        }

        response = await self.connection.api_request("POST", "remoteServices/engineStop/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to stop engine")

        return response

    async def get_nickname(self, vin):
        if len(vin) != 17:
            raise MazdaException("Invalid VIN")

        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "vin": vin
        }

        response = await self.connection.api_request("POST", "remoteServices/getNickName/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to get vehicle nickname")

        return response["carlineDesc"]

    async def update_nickname(self, vin, new_nickname):
        if len(vin) != 17:
            raise MazdaException("Invalid VIN")
        if len(new_nickname) > 20:
            raise MazdaException("Nickname is too long")
        
        post_body = {
            "internaluserid": "__INTERNAL_ID__",
            "vin": vin,
            "vtitle": new_nickname
        }

        response = await self.connection.api_request("POST", "remoteServices/updateNickName/v4", body_dict=post_body, needs_keys=True, needs_auth=True)

        if response["resultCode"] != "200S00":
            raise MazdaException("Failed to update vehicle nickname")