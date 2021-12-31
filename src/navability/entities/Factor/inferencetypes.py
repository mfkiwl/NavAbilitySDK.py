from dataclasses import dataclass

from marshmallow import EXCLUDE, Schema, fields, post_load

from navability.entities.Factor.distributions import Distribution


@dataclass
class InferenceType:
    """
    Base type for all factor classes.
    """

    pass


@dataclass
class PriorPose2(InferenceType):
    z: Distribution

    def __repr__(self):
        return f"<{self.__class__.__name__}(z={str(self.z)})>"

    def dump(self):
        return PriorPose2Schema().dump(self)

    def dumps(self):
        return PriorPose2Schema().dumps(self)

    # TODO: Deserializing this.


class PriorPose2Schema(Schema):
    z = fields.Method("get_packed", "set_packed", data_key="str", required=True)

    class Meta:
        ordered = True
        unknown = EXCLUDE  # Note: This is because of _version, remote and fix later.

    def get_packed(self, obj):
        return obj.z.dumpsPacked()

    def set_packed(self, obj):
        raise Exception("This has not been implemented yet.")

    # @post_load
    # def load(self, data, **kwargs):
    #     return PriorPose2(**data)


@dataclass
class Pose2Pose2(InferenceType):
    z = Distribution

    def __repr__(self):
        return f"<{self.__class__.__name__}(z={str(self.z)})>"

    def dump(self):
        return PriorPose2Schema().dump(self)

    def dumps(self):
        return PriorPose2Schema().dumps(self)

    # TODO: Deserializing this.


class Pose2Pose2Schema(Schema):
    z = fields.Method("get_packed", "set_packed", required=True, attribute="datastr")
    # datastr: fields.Method("get_packed", "set_packed", required=True)
    a: fields.Str()

    def get_packed(self, obj):
        return obj.z.dumpsPacked()

    def set_packed(self, obj):
        raise Exception("This has not been implemented yet.")

    @post_load
    def load(self, data, **kwargs):
        return PriorPose2(**data)