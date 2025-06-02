from fastapi import APIRouter

router = APIRouter(
    prefix="/healthcheck",
    tags=["Health Check"],
)


@router.get("/")
def health_check():
    return {"status": "ok"}
