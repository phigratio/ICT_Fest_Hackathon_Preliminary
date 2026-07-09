"""Side effects that accompany booking lifecycle events."""

def _send_email(kind: str, booking) -> None:
    return None


def _write_audit(kind: str, booking) -> None:
    return None


def notify_created(booking) -> None:
    _send_email("created", booking)
    _write_audit("created", booking)


def notify_cancelled(booking) -> None:
    _send_email("cancelled", booking)
    _write_audit("cancelled", booking)
