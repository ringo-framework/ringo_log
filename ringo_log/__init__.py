import logging
from pyramid.i18n import TranslationStringFactory
from ringo.lib.i18n import translators
from ringo.lib.extension import register_modul
from ringo.lib.helpers import dynamic_import

# Import models so that alembic is able to autogenerate migrations
# scripts.
from ringo_log.model import Log

log = logging.getLogger(__name__)

modul_config = {
    "name": "log",
    "label": "",
    "clazzpath": "ringo_log.model.Log",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete"]
}


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    Log._modul_id = modul.get_value("id")
    translators.append(TranslationStringFactory('ringo_log'))
    config.add_translation_dirs('ringo_log:locale/')

