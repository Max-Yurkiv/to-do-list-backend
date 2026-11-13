from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.categories import CategoryRepository
from app.schemas.categories import CategoriesSchema, CreateCategory, UpdCategory


class CategoryService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.repo = CategoryRepository(db)

    def _get_or_404(self, category_id: str):
        category = self.repo.get_by_id(category_id)
        if category is None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Category not found")
        return category

    def list_categories(self) -> list[CategoriesSchema]:
        return [CategoriesSchema.model_validate(c) for c in self.repo.get_all()]

    def create_category(self, data: CreateCategory) -> CategoriesSchema:
        category = self.repo.create(name=data.name)
        self.db.commit()
        return CategoriesSchema.model_validate(category)

    def update_category(self, category_id: str, data: UpdCategory) -> CategoriesSchema:
        category = self._get_or_404(category_id)
        if data.name is not None:
            category.name = data.name
        self.db.commit()
        return CategoriesSchema.model_validate(category)

    def delete_category(self, category_id: str) -> None:
        category = self._get_or_404(category_id)
        self.repo.delete(category)
        self.db.commit()