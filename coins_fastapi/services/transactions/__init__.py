from typing import List
from fastapi import Depends, HTTPException, status
from datetime import datetime
from ...database import *

from ... import models

class TransactionsService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self) -> List[Transactions]:
        transactions: list[Transactions] = (self.session
            .query(Transactions)
        ).all()

        return transactions

    def get(self, transaction_id: int) -> Transactions:
        transaction: Transactions = self._get(transaction_id)
        return transaction

    def create(self, transaction_data: models.TransactionCreate) -> Transactions:

        coin: Coins = (self.session
            .query(Coins)
            .filter(
                Coins.id == transaction_data.coin_id,
                )
            .first()
        )
        if not coin:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        
        transaction: Transactions = Transactions(**transaction_data.dict(), datetime=datetime.now(), from_user_id=coin.owner_id)

        coin.owner_id = transaction_data.to_user_id

        self.session.add(transaction)
        self.session.add(coin)
        self.session.commit()

        return transaction

    def _get(self, transaction_id: int) -> Transactions:
        transaction: Transactions = (self.session
            .query(Transactions)
            .filter(Transactions.id == transaction_id)
            .first()
        )
        if not transaction:
            raise HTTPException(status.HTTP_404_NOT_FOUND)

        return transaction
