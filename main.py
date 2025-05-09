from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.index import router
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from api.users.model import User


async def init_db():
    try:
        client = AsyncIOMotorClient("mongodb+srv://matteocarrarateo:uDTaDOFCiDnDPK2F@cluster-jac.8slg1.mongodb.net/?tlsAllowInvalidCertificates=true")
        # Ping the server to confirm connection
        await client.server_info()

        # Initialize beanie
        await init_beanie(database=client.ATM, document_models=[User])

        print("Successfully connected to the database on port")

    except Exception as e:
        print(f"Failed to connect to the database. Error: {str(e)}")
        raise  # Re-raise the exception to handle it in the FastAPI app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    # Add any cleanup code here if needed


app = FastAPI(lifespan=lifespan)
app.include_router(router)