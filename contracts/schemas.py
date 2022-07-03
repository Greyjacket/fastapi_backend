from pydantic import BaseModel
import datetime


class Contract(BaseModel):
    id: int
    attorney_id: int
    client_id: int
    property_id: int
    agents_id: int
    mortgage_applicaton_date: datetime.date
    buyer_or_seller:str
    purchase_price: float
    concessions: float
    contract_date: datetime.date
    contract_of_sale_sent: datetime.date
    attorney_approval_seller: datetime.date
    attorney_approval_buyer: datetime.date
    deposit_received: datetime.date
    deal_sheet:  datetime.date
    sold_rider:  datetime.date
    appraisal_date:  datetime.date
    mortgage_commitment_contract:  datetime.date
    mortgage_commitment_actual:  datetime.date
    clear_to_closed: datetime.date
    rate_lock_expiration: datetime.date
    utility_email: datetime.date
    fwt: datetime.date
    close_date_contract: datetime.date
    close_date_actual: datetime.date
    updated_coi: datetime.date
    pickup_sign: datetime.date
    pickup_lockbox: datetime.date
    zillow_email1: str
    zillow_email2: str
    zillow_past_sale: datetime.date
    case_closed: datetime.date
    postcards_just_listed: datetime.date
    postcards_just_sold: datetime.date

    class Config:
        orm_mode: True
