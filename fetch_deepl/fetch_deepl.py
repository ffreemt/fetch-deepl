"""Fetch translation text from a deepl-fastapi API."""
from typing import Optional

import httpx
from logzero import logger

url_ = "https://hf.space/embed/mikeee/gradio-deepl/+/api/predict"
timeout_ = httpx.Timeout(10)


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

    if timeout is None:
        timeout = timeout_

    data = {"data": [text, from_lang, to_lang]}
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

    return res
