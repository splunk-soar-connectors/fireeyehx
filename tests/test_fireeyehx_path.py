# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fireeyehx_path import quote_hx_identifier


def test_quote_hx_identifier_rejects_invalid_values():
    for value in (None, 123, "", ".", ".."):
        try:
            quote_hx_identifier(value)
        except ValueError as error:
            assert "non-empty, non-dot string" in str(error)
        else:
            raise AssertionError(f"Expected {value!r} to be rejected")


def test_quote_hx_identifier_encodes_structural_input():
    cases = (
        ("../../indicators?", "..%2F..%2Findicators%3F"),
        ("%2e%2e%2findicators", "%252e%252e%252findicators"),
        ("%252e%252e%252findicators", "%25252e%25252e%25252findicators"),
        ("../../alerts?limit=100#fragment", "..%2F..%2Falerts%3Flimit%3D100%23fragment"),
    )
    for value, expected in cases:
        assert quote_hx_identifier(value) == expected
