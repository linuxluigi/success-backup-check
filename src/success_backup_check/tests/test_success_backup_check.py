import pytest
import success_backup_check


def test_project_defines_author_and_version():
    assert hasattr(success_backup_check, '__author__')
    assert hasattr(success_backup_check, '__version__')
