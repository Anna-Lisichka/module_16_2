from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def Get_Main_Page() -> dict:
    return {'message': "Главная страница"}


@app.get("/user/admin")
async def Get_Admin_Page() -> dict:
    return {'message': f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def Get_User_Number(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example=1)]) -> dict:
    return {'message': f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def Get_User_info(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
                        age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {'massage': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}

