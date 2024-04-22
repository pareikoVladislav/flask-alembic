from pydantic import BaseModel, conlist, field_validator


class DogCase(BaseModel):
    case_type: str
    evidence: conlist(str, min_length=1)
    victims: conlist(str, min_length=1)
    seriousness: int

    @field_validator('seriousness')
    def check_seriousness(cls, value, values):
        if 'evidence' in values and len(values['evidence']) < value:
            raise ValueError('Seriousness must be less than or equal to the number of evidences')
        return value
