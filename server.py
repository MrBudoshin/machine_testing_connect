import re
from flask import Flask, Response, request
from jsonrpcserver import method, Success, dispatch
from jsonrpcserver.result import ErrorResult, SuccessResult
from oslash import Either

app = Flask(__name__)


@method
def do_test(data) -> Either[ErrorResult, SuccessResult]:
    """Измените название "TD-1" при смене устройства"""
    info = data.split(',')
    if info[0] == "TD-1":
        if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", info[1].lower()):
            if info[2].isdigit() and len(info[2]) == 7:
                return Success(f"0")
            else:
                return Success(f'1')
        else:
            return Success(f'2')
    else:
        return Success(f'3')


@app.route("/api", methods=["POST"])
def index():
    return Response(
        dispatch(request.get_data().decode()), content_type="application/json"
    )


if __name__ == "__main__":
    app.run()
