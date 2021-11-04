from fastapi import APIRouter

router = APIRouter(prefix="/products")


@router.get("/")
def get_product():
    return "it's product"