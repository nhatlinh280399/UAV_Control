import asyncio

from mavsdk import System
from mavsdk.offboard import (OffboardError, PositionNedYaw)


async def run():


    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("-- Arming")
    await drone.action.arm()

    print("-- Khoi tao setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Bat dau che do Offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Khoi dong Offboard that bai: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Up 5m ")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 5m North ")
    await drone.offboard.set_position_ned(PositionNedYaw(5.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(10)

    print("-- Turn to face East ")
    await drone.offboard.set_position_ned(PositionNedYaw(5.0, 0.0, -5.0, 90.0))
    await asyncio.sleep(3)

    print("-- Go 10m East")
    await drone.offboard.set_position_ned(PositionNedYaw(5.0, 10.0, -5.0, 90.0))
    await asyncio.sleep(15)

    print("-- Turn to face South")
    await drone.offboard.set_position_ned(PositionNedYaw(5.0, 10.0, -5.0, 180.0))
    await asyncio.sleep(3)

    print("-- Go 5m South")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 10.0, -5.0, 180.0))
    await asyncio.sleep(10)

    print("-- Turn to face West")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 10.0, -5.0, 270.0))
    await asyncio.sleep(3)

    print("-- Go 10m West")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 270.0))
    await asyncio.sleep(15)

    print("-- Turn to face North")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(3)

    print("-- Landing")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(10)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())