from fastapi import APIRouter

from . import auth, coins, transactions, collections

router = APIRouter()
router.include_router(auth.router)
router.include_router(coins.router)
router.include_router(transactions.router)
router.include_router(collections.router)