"""Fetch translation text from a deepl-fastapi API."""
# pylint: disable=invalid-name
from itertools import cycle
from typing import Optional

import httpx
from logzero import logger

url_ = "https://hf.space/embed/mikeee/gradio-deepl/+/api/predict"
timeout_ = httpx.Timeout(10)

langs = [
    "en",
    "zh",
    "ja",
    "bg",
    "cs",
    "da",
    "et",
    "fi",
    "fr",
    "de",
    "el",
    "hu",
    "id",
    "it",
    "lv",
    "lt",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "es",
    "sv",
    "tr",
]
lang_names = [
    "English",
    "Chinese (simpl.)",
    "Japanese",
    "Bulgarian",
    "Czech",
    "Danish",
    "Estonian",
    "Finnish",
    "French",
    "German",
    "Greek",
    "Hungarian",
    "Indonesian",
    "Italian",
    "Latvian",
    "Lithuanian",
    "Polish",
    "Portuguese",
    "Romanian",
    "Russian",
    "Slovak",
    "Slovenian",
    "Spanish",
    "Swedish",
    "Turkish",
]
lang_dict = dict(zip(langs, lang_names))
spaces = cycle(range(6))


def fetch_deepl(
    text: str,
    from_lang: str = "en",
    to_lang: str = "zh",
    url: Optional[str] = None,
    timeout: Optional[httpx.Timeout] = None,
) -> str:
    """Fetch translation text from a deepl-fastapi API.

    >>> '测试' in fetch_deepl("test this")
    True
    >>> 'Test' in fetch_deepl("测试一下", 'en', 'zh')
    True
    """
    if url is None:
        url = url_
    try:
        url = url.strip()
    except Exception as exc:
        logger.error(exc)
        url = url_

    try:
        from_lang = str(from_lang).strip()
    except Exception as exc:
        logger.error(exc)
        from_lang = "auto"
    try:
        to_lang = str(to_lang).strip()
    except Exception as exc:
        logger.error(exc)
        if from_lang not in ["zh"]:
            to_lang = "zh"
        else:
            to_lang = "en"

    if from_lang not in ["auto"] + langs:
        logger.warning(" from_lang (%s) not supported (%s)", from_lang, lang_dict)
        logger.info("We let nature take its cours...")
    if to_lang not in langs:
        logger.warning(" to_lang (%s) not supported (%s)", to_lang, lang_dict)
        logger.info("We let nature take its cours...")

    if timeout is None:
        timeout = timeout_

    # attach difference spaces + "_" for each call
    data = {"data": [f"{text}{' ' * next(spaces)}_", from_lang, to_lang]}
    try:
        resp = httpx.post(url, json=data, timeout=timeout)
        resp.raise_for_status()
    except Exception as exc:
        logger.error(exc)
        raise
    try:
        jdata = resp.json()
    except Exception as exc:
        logger.error(exc)
        raise

    try:
        res = jdata.get("data")[0]
    except Exception as exc:
        logger.error(exc)
        raise

    # remove _ and spaces
    return res.replace("_", "").strip()
