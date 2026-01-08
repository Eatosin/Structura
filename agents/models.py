from pydantic import BaseModel, Field
from typing import List, Optional

# Schema 1: Invoice Extraction
class InvoiceSchema(BaseModel):
    vendor: str = Field(description="Name of the company or service provider")
    total_amount: float = Field(description="Total cost extracted")
    currency: str = Field(description="Currency code (USD, EUR, NGN)", default="USD")
    date: str = Field(description="Date of transaction (YYYY-MM-DD) or 'Unknown'")
    items: List[str] = Field(description="List of line items purchased", default_factory=list)
    is_paid: bool = Field(description="True if payment is confirmed")

# Schema 2: Resume Parsing
class ResumeSchema(BaseModel):
    name: str = Field(description="Candidate's full name")
    email: Optional[str] = Field(description="Email address")
    skills: List[str] = Field(description="Technical skills found")
    years_experience: int = Field(description="Estimated years of experience", default=0)
    summary: str = Field(description="Brief professional summary")

# Schema 3: Generic Data
class GenericSchema(BaseModel):
    key_points: List[str] = Field(description="Main takeaways")
    sentiment: str = Field(description="Positive, Neutral, or Negative")
