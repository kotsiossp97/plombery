from fastapi import APIRouter, Response

router = APIRouter(
    prefix="/healthcheck",
    tags=["Health Check"],
)


@router.get("/")
def health_check():
    return Response(content={"status": "ok"}, media_type="application/json")
