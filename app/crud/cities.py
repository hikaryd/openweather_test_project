from app.crud.base import CRUDBase
from app.models import Cities


class CitiesCRUD(CRUDBase[Cities]):
    pass


cities_crud = CitiesCRUD(Cities)
