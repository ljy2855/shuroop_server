import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
import json
import device

#TODO view에서 호출해도 쓰레드 무시되는 버그
 
async def borrow_signal(place_id):
  # 웹 소켓에 접속을 합니다.
    async with websockets.connect(f"ws://localhost:8000/ws/devices/{place_id}/",origin="http://127.0.0.1:8000") as websocket:

      data = await websocket.recv() # JSON data를 str로 그대로 긁어온다.
      data_dict = json.loads(data) # JSON form으로 된 string data를 dict 형태로 만든다
      message = data_dict["message"]
      if message == "borrow" or message == "init_borrow":
        device.close()
      elif message == "return" or message == "init_return":
        device.open()

      await websocket.send(json.dumps({"message": "borrow complete"}))
    
      print("borrow success")


async def return_signal(place_id):
    async with websockets.connect(f"ws://localhost:8000/ws/devices/{place_id}/",origin="http://127.0.0.1:8000") as websocket:
      
      data = await websocket.recv() # JSON data를 str로 그대로 긁어온다.
      data_dict = json.loads(data) # JSON form으로 된 string data를 dict 형태로 만든다
      message = data_dict["message"]
      if message == "borrow" or message == "init_borrow":
        device.close()
      elif message == "return" or message == "init_return":
        device.open()
        
        await websocket.send(json.dumps({"message": "return complete"}))
    
        print("return success")