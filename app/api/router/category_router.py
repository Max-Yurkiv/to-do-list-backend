from fastapi import APIRouter, Depends, status

from app.api.router.dependencies import get_category_service
from app.schemas.categories import CategoriesSchema, CreateCategory, UpdCategory
from app.services.categories import CategoryService

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("")
def read_categories(service: CategoryService = Depends(get_category_service)) -> list[CategoriesSchema]:
    return service.list_categories()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_category(payload: CreateCategory, service: CategoryService = Depends(get_category_service)) -> CategoriesSchema:
    return service.create_category(payload)


@router.patch("/{category_id}")
def update_category(category_id: str, payload: UpdCategory, service: CategoryService = Depends(get_category_service)) -> CategoriesSchema:
    return service.update_category(category_id, payload)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str, service: CategoryService = Depends(get_category_service)):
    service.delete_category(category_id)