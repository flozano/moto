from mock import patch
import sure  # flake8: noqa

from moto.server import main


def test_wrong_arguments():
    try:
        main(["name", "test1", "test2", "test3"])
        assert False, ("main() when called with the incorrect number of args"
                       " should raise a system exit")
    except SystemExit:
        pass


@patch('moto.server.app.run')
def test_right_arguments(app_run):
    main(["name", "s3"])
    app_run.assert_called_once_with(port=None)


@patch('moto.server.app.run')
def test_port_argument(app_run):
    main(["name", "s3", 8080])
    app_run.assert_called_once_with(port=8080)
