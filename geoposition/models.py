from __future__ import unicode_literals


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], [r"^geoposition\.fields\.GeopositionField"])
except ImportError:
    pass
