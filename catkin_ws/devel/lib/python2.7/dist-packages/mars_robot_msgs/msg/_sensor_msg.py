# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from mars_robot_msgs/sensor_msg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class sensor_msg(genpy.Message):
  _md5sum = "57d6b1ca27430172008d546be1f39dfb"
  _type = "mars_robot_msgs/sensor_msg"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool laser_top_hit
bool laser_left_hit
bool laser_right_hit
bool depth_bottom_switch
bool depth_top_switch
float32 yaw
float32 mass
"""
  __slots__ = ['laser_top_hit','laser_left_hit','laser_right_hit','depth_bottom_switch','depth_top_switch','yaw','mass']
  _slot_types = ['bool','bool','bool','bool','bool','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       laser_top_hit,laser_left_hit,laser_right_hit,depth_bottom_switch,depth_top_switch,yaw,mass

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(sensor_msg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.laser_top_hit is None:
        self.laser_top_hit = False
      if self.laser_left_hit is None:
        self.laser_left_hit = False
      if self.laser_right_hit is None:
        self.laser_right_hit = False
      if self.depth_bottom_switch is None:
        self.depth_bottom_switch = False
      if self.depth_top_switch is None:
        self.depth_top_switch = False
      if self.yaw is None:
        self.yaw = 0.
      if self.mass is None:
        self.mass = 0.
    else:
      self.laser_top_hit = False
      self.laser_left_hit = False
      self.laser_right_hit = False
      self.depth_bottom_switch = False
      self.depth_top_switch = False
      self.yaw = 0.
      self.mass = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_5B2f().pack(_x.laser_top_hit, _x.laser_left_hit, _x.laser_right_hit, _x.depth_bottom_switch, _x.depth_top_switch, _x.yaw, _x.mass))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.laser_top_hit, _x.laser_left_hit, _x.laser_right_hit, _x.depth_bottom_switch, _x.depth_top_switch, _x.yaw, _x.mass,) = _get_struct_5B2f().unpack(str[start:end])
      self.laser_top_hit = bool(self.laser_top_hit)
      self.laser_left_hit = bool(self.laser_left_hit)
      self.laser_right_hit = bool(self.laser_right_hit)
      self.depth_bottom_switch = bool(self.depth_bottom_switch)
      self.depth_top_switch = bool(self.depth_top_switch)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_5B2f().pack(_x.laser_top_hit, _x.laser_left_hit, _x.laser_right_hit, _x.depth_bottom_switch, _x.depth_top_switch, _x.yaw, _x.mass))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 13
      (_x.laser_top_hit, _x.laser_left_hit, _x.laser_right_hit, _x.depth_bottom_switch, _x.depth_top_switch, _x.yaw, _x.mass,) = _get_struct_5B2f().unpack(str[start:end])
      self.laser_top_hit = bool(self.laser_top_hit)
      self.laser_left_hit = bool(self.laser_left_hit)
      self.laser_right_hit = bool(self.laser_right_hit)
      self.depth_bottom_switch = bool(self.depth_bottom_switch)
      self.depth_top_switch = bool(self.depth_top_switch)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_5B2f = None
def _get_struct_5B2f():
    global _struct_5B2f
    if _struct_5B2f is None:
        _struct_5B2f = struct.Struct("<5B2f")
    return _struct_5B2f