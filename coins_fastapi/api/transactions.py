from typing import List

from fastapi import APIRouter, Depends, status

from .. import models

from ..services.auth import check_admin
from ..services.transactions import TransactionsService


router = APIRouter(
    prefix='/transactions',
    tags=['transactions']
)

@router.get('/', response_model=List[models.Transaction])
def get_transactions(
    user: models.User = Depends(check_admin),
    transaction_service: TransactionsService = Depends()
    ):
    return transaction_service.get_many()

@router.get('/{transaction_id}', response_model=models.Transaction)
def get_transaction(
    transaction_id: int,
    user: models.User = Depends(check_admin),
    transaction_service: TransactionsService = Depends()
    ):
    return transaction_service.get(transaction_id)

@router.post('/', response_model=models.Transaction, status_code=status.HTTP_404_NOT_FOUND)
def create_transaction(
    transaction_data: models.TransactionCreate,
    user: models.User = Depends(check_admin),
    transaction_service: TransactionsService = Depends()
    ):
    return transaction_service.create(transaction_data)
