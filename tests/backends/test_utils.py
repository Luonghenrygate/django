from django.core.exceptions import ImproperlyConfigured
from django.db.backends.utils import truncate_name
from django.db.utils import load_backend
from django.test import SimpleTestCase
from django.utils import six


class TestLoadBackend(SimpleTestCase):
    def test_load_backend_invalid_name(self):
        msg = (
            "'foo' isn't an available database backend.\n"
            "Try using 'django.db.backends.XXX', where XXX is one of:\n"
            "    'mysql', 'oracle', 'postgresql', 'sqlite3'\n"
            "Error was: No module named %s"
        ) % "foo.base" if six.PY2 else "'foo'"
        with self.assertRaisesMessage(ImproperlyConfigured, msg):
            load_backend('foo')

    def test_truncate_name(self):
        self.assertEqual(truncate_name('some_table', 10), 'some_table')
        self.assertEqual(truncate_name('some_long_table', 10), 'some_la38a')
        self.assertEqual(truncate_name('some_long_table', 10, 3), 'some_loa38')
        self.assertEqual(truncate_name('some_long_table'), 'some_long_table')
