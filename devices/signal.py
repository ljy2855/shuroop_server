import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
import json

#TODO view에서 호출해도 쓰레드 무시되는 버그
 
async def borrow_signal(place_id):
  # 웹 소켓에 접속을 합니다.
    async with websockets.connect(f"ws://localhost:8000/ws/devices/{place_id}/",origin="http://127.0.0.1:8000") as websocket:
    # 10번을 반복하면서 웹 소켓 서버로 메시지를 전송합니다.
        await websocket.send(json.dumps({"message": "borrow"}))
    
        print("borrow success")


async def return_signal(place_id):
    async with websockets.connect(f"ws://localhost:8000/ws/devices/{place_id}/",origin="http://127.0.0.1:8000") as websocket:
    # 10번을 반복하면서 웹 소켓 서버로 메시지를 전송합니다.
        await websocket.send(json.dumps({"message": "return"}))
    
        print("return success")