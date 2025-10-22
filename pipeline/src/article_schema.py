from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class ArticleFrontMatter(BaseModel):
    title: str
    link: str
    summary: str
    tags: List[str]
    published_date: datetime = Field(alias="date") # Map to 'date' for Hugo compatibility
    content_type: str
    authors: Optional[List[str]] = None
    doi: Optional[str] = None
