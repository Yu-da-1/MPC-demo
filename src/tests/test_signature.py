# tests/test_signature.py
import pytest
from nodes.node import generate_and_verify_signature

@pytest.mark.asyncio
# テスト用のノード名を渡す
async def test_mpc_signature_verification():
    await generate_and_verify_signature("TestNode")