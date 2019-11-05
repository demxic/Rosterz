import json


class StationJsonEncoder(json.JSONEncoder):

    def default(self, obj):
        try:
            to_serialize = dict(
                __class__="Station",
                __args__=[],
                __kw__=dict(code=obj.code,
                            continent=obj.continent,
                            tz_city=obj.tz_city,
                            viaticum=obj.viaticum)
            )
            return to_serialize
        except AttributeError:
            return super().default(obj)
