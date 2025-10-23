from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class ArticleFrontMatter(BaseModel):
    title: str
    link: str
    summary: str
    tags: List[str]
    date: datetime = Field(alias="published_date") # Use 'date' for Hugo compatibility, 'published_date' for internal alias
    content_type: str
    authors: Optional[List[str]] = None
    doi: Optional[str] = None
