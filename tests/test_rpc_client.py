# pylint: disable-all

import pytest
from tests.conf import conf

from confclient import RPCClient
from confclient import RestClient
from confclient.confexcept import BadRPCRequestException


@pytest.fixture
def rpc_client():
    return RPCClient(conf["url"], conf["username"], conf["password"])


@pytest.fixture
def rest_client():
    return RestClient(conf["url"], conf["username"], conf["password"])


def test_rpc_add_user_good(rpc_client: RPCClient):

    resp = rpc_client.add_user("test_user_123", "Test User", "test@testuser.com")

    assert resp.status_code == 200


def test_rpc_add_user_bad(rpc_client: RPCClient):

    with pytest.raises(BadRPCRequestException):
        resp = rpc_client.add_user("test_user_123", "Test User", "test@testuser.com")


def test_rpc_remove_user_good(rpc_client: RPCClient):

    resp = rpc_client.remove_user("test_user_123")

    assert resp.status_code == 200


def test_rpc_remove_user_bad(rpc_client: RPCClient):

    with pytest.raises(BadRPCRequestException):
        resp = rpc_client.remove_user("test_user_12")


def test_rpc_create_group_good(rpc_client: RPCClient, rest_client: RestClient):

    rpc_client.add_group("test_group_123")

    groups = [g["groupname"] for g in rest_client.get_groups()["groups"]]

    assert "test_group_123" in groups


# TODO: Figure out how to determine if a create group fails, response doesn't seem to differ
# def test_rpc_create_group_bad(rpc_client: RPCClient):

#     with pytest.raises(BadRPCRequestException):
#         resp = rpc_client.add_group("test_group_123")


def test_rpc_remove_group_good(rpc_client: RPCClient, rest_client: RestClient):

    rpc_client.remove_group("test_group_123")

    groups = [g["groupname"] for g in rest_client.get_groups()["groups"]]

    assert "test_group_123" not in groups
