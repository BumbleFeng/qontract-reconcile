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
query MembershipSourceRolesQuery($filter: JSON) {
  roles: roles_v1(filter: $filter) {
    name
    labels
    path
    users {
      name
      org_username
      github_username
      quay_username
      slack_username
      pagerduty_username
      aws_username
      cloudflare_user
      public_gpg_key
      tag_on_cluster_updates
      tag_on_merge_requests
    }
    bots {
      name
      description
      org_username
      github_username
      gitlab_username
      openshift_serviceaccount
      quay_username
    }
  }
}
"""


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class UserV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    org_username: str = Field(..., alias="org_username")
    github_username: str = Field(..., alias="github_username")
    quay_username: Optional[str] = Field(..., alias="quay_username")
    slack_username: Optional[str] = Field(..., alias="slack_username")
    pagerduty_username: Optional[str] = Field(..., alias="pagerduty_username")
    aws_username: Optional[str] = Field(..., alias="aws_username")
    cloudflare_user: Optional[str] = Field(..., alias="cloudflare_user")
    public_gpg_key: Optional[str] = Field(..., alias="public_gpg_key")
    tag_on_cluster_updates: Optional[bool] = Field(..., alias="tag_on_cluster_updates")
    tag_on_merge_requests: Optional[bool] = Field(..., alias="tag_on_merge_requests")


class BotV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    description: Optional[str] = Field(..., alias="description")
    org_username: Optional[str] = Field(..., alias="org_username")
    github_username: Optional[str] = Field(..., alias="github_username")
    gitlab_username: Optional[str] = Field(..., alias="gitlab_username")
    openshift_serviceaccount: Optional[str] = Field(..., alias="openshift_serviceaccount")
    quay_username: Optional[str] = Field(..., alias="quay_username")


class RoleV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    labels: Optional[Json] = Field(..., alias="labels")
    path: str = Field(..., alias="path")
    users: list[UserV1] = Field(..., alias="users")
    bots: list[BotV1] = Field(..., alias="bots")


class MembershipSourceRolesQueryQueryData(ConfiguredBaseModel):
    roles: Optional[list[RoleV1]] = Field(..., alias="roles")


def query(query_func: Callable, **kwargs: Any) -> MembershipSourceRolesQueryQueryData:
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
        MembershipSourceRolesQueryQueryData: queried data parsed into generated classes
    """
    raw_data: dict[Any, Any] = query_func(DEFINITION, **kwargs)
    return MembershipSourceRolesQueryQueryData(**raw_data)