from fastapi import APIRouter

from . import auth, coins

router = APIRouter()
router.include_router(auth.router)
router.include_router(coins.router)