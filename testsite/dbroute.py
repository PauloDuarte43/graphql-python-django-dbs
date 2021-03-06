from django.conf import settings


class DbRouter:
    def db_for_read(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label, None)

    def db_for_write(self, model, **hints):
        return settings.DATABASE_APPS_MAPPING.get(model._meta.app_label, None)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return settings.DATABASE_APPS_MAPPING.get(app_label, None)