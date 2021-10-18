from typing import Optional

from fastapi_camelcase import CamelModel
from datetime import datetime

#
# class JobOptions(CamelModel):
#     name: Optional[str] = None
#     misfire_grace_time: Optional[int] = None
#     coalesce: Optional[bool] = None
#     max_runs: Optional[int] = None
#     max_instances: Optional[int] = None
#
#
# class NewsData(CamelModel):
#     guid: Optional[str] = None
#     title: Optional[str] = None
#     html_content: Optional[str] = None
#     text_content: Optional[str] = None
#     tone_type: Optional[str] = None
#     publish_date: Optional[datetime] = None
#     tone_type_probability: Optional[float] = None
