from fastapi import APIRouter

router = APIRouter(prefix="/auth")


@router.get("/")
def get_product():
    return "it's auth"