from flask import current_app


def handle_errors(message: str) -> tuple:
    fail_message = 'FAIL: {}'.format(message)
    current_app.logger.error(fail_message, exc_info=True)
    return {'status': False, 'message': fail_message}, 400
