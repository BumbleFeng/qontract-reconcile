"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


DEFINITION = """
query TemplateCollection_v1($name: String) {
  template_collection_v1(name: $name) {
    name
    additionalMrLabels
    description
    enableAutoApproval
    forEach {
      items
    }
    variables {
      static
      dynamic {
        name
        query
      }
    }
    templates {
      name
      autoApproved
      condition
      targetPath
      createOnly
      patch {
        path
        identifier
      }
      template
      templateRenderOptions {
        trimBlocks
        lstripBlocks
        keepTrailingNewline
      }
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class TemplateCollectionForEachV1(ConfiguredBaseModel):
    items: list[Json] = Field(..., alias="items")


class TemplateCollectionVariablesQueriesV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    query: str = Field(..., alias="query")


class TemplateCollectionVariablesV1(ConfiguredBaseModel):
    static: Optional[Json] = Field(..., alias="static")
    dynamic: Optional[list[TemplateCollectionVariablesQueriesV1]] = Field(..., alias="dynamic")


class TemplatePatchV1(ConfiguredBaseModel):
    path: str = Field(..., alias="path")
    identifier: Optional[str] = Field(..., alias="identifier")


class TemplateRenderOptionsV1(ConfiguredBaseModel):
    trim_blocks: Optional[bool] = Field(..., alias="trimBlocks")
    lstrip_blocks: Optional[bool] = Field(..., alias="lstripBlocks")
    keep_trailing_newline: Optional[bool] = Field(..., alias="keepTrailingNewline")


class TemplateV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    auto_approved: Optional[bool] = Field(..., alias="autoApproved")
    condition: Optional[str] = Field(..., alias="condition")
    target_path: str = Field(..., alias="targetPath")
    create_only: Optional[bool] = Field(..., alias="createOnly")
    patch: Optional[TemplatePatchV1] = Field(..., alias="patch")
    template: str = Field(..., alias="template")
    template_render_options: Optional[TemplateRenderOptionsV1] = Field(..., alias="templateRenderOptions")


class TemplateCollectionV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    additional_mr_labels: Optional[list[str]] = Field(..., alias="additionalMrLabels")
    description: str = Field(..., alias="description")
    enable_auto_approval: Optional[bool] = Field(..., alias="enableAutoApproval")
    for_each: Optional[TemplateCollectionForEachV1] = Field(..., alias="forEach")
    variables: Optional[TemplateCollectionVariablesV1] = Field(..., alias="variables")
    templates: list[TemplateV1] = Field(..., alias="templates")


class TemplateCollection_v1QueryData(ConfiguredBaseModel):
    template_collection_v1: Optional[list[TemplateCollectionV1]] = Field(..., alias="template_collection_v1")


def query(query_func: Callable, **kwargs: Any) -> TemplateCollection_v1QueryData:
    """
    This is a convenience function which queries and parses the data into
    concrete types. It should be compatible with most GQL clients.
    You do not have to use it to consume the generated data classes.
    Alternatively, you can also mime and alternate the behavior
    of this function in the caller.

    Parameters:
        query_func (Callable): Function which queries your GQL Server
        kwargs: optional arguments that will be passed to the query function

    Returns:
        TemplateCollection_v1QueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return TemplateCollection_v1QueryData(**raw_data)
