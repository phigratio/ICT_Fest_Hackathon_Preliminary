"""Human-facing booking reference codes.

Codes are issued with random entropy and formatted into a short,
customer-friendly string such as ``CW-A1B2C3D4E5F6``.
"""
import uuid


def next_reference_code() -> str:
    return f"CW-{uuid.uuid4().hex[:12].upper()}"
