def setup_namespaces(api):
    from app.resources.version import api as version_api
    api.namespaces.clear()
    api.add_namespace(version_api)