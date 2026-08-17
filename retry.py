"""Retry helper for flaky warehouse writes."""
import time


def with_retry(fn, attempts=3, backoff=0.5):
    last = None
    for i in range(attempts):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 - deliberate catch-all at the boundary
            last = exc
            time.sleep(backoff * (2 ** i))
    raise last
