# -*- coding: utf-8 -*-

import os
import requests

API_ENDPOINT = os.environ.get("DEEPL_URL", "https://api.deepl.com/v2")


class DeeplException(Exception):
    """Generic deepl exception."""


class MissingAuthKey(DeeplException):
    """Auth key is missing."""


class InvalidResponse(DeeplException):
    """Invalid API response."""


def translate(
    text,
    target_lang,
    auth_key=None,
    source_lang=None,
    preserve_formatting=None,
    tag_handling=None,
    non_splitting_tags=None,
    outline_detection=None,
    splitting_tags=None,
    ignore_tags=None,
):
    """Translate a source."""
    auth_key = auth_key or os.environ.get("DEEPL_KEY", None)
    if not auth_key:
        raise MissingAuthKey

    endpoint = "/".join([API_ENDPOINT, "translate"])
    params = {
        "text": text,
        "source_lang": source_lang,
        "target_lang": target_lang,
        "preserve_formatting": preserve_formatting,
        "auth_key": auth_key,
        "tag_handling": tag_handling,
        "non_splitting_tags": non_splitting_tags,
        "outline_detection": outline_detection,
        "splitting_tags": splitting_tags,
        "ignore_tags": ignore_tags,
    }
    result = requests.post(endpoint, params=params)
    if result.status_code != 200:
        raise InvalidResponse
    data = result.json()
    return data.get("translations", [])


if __name__ == "__main__":
    translations = translate(text=["Hello, World", "How are you?"], target_lang="DE")
    for item in translations:
        print(item)
