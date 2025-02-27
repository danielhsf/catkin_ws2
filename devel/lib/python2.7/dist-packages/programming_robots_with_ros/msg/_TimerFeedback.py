# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from programming_robots_with_ros/TimerFeedback.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class TimerFeedback(genpy.Message):
  _md5sum = "f7ef31d21e406bbd1f38a63801a29be7"
  _type = "programming_robots_with_ros/TimerFeedback"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback
duration time_elapsed
duration time_remaining
"""
  __slots__ = ['time_elapsed','time_remaining']
  _slot_types = ['duration','duration']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_elapsed,time_remaining

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(TimerFeedback, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.time_elapsed is None:
        self.time_elapsed = genpy.Duration()
      if self.time_remaining is None:
        self.time_remaining = genpy.Duration()
    else:
      self.time_elapsed = genpy.Duration()
      self.time_remaining = genpy.Duration()

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
      buff.write(_get_struct_4i().pack(_x.time_elapsed.secs, _x.time_elapsed.nsecs, _x.time_remaining.secs, _x.time_remaining.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.time_elapsed is None:
        self.time_elapsed = genpy.Duration()
      if self.time_remaining is None:
        self.time_remaining = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.time_elapsed.secs, _x.time_elapsed.nsecs, _x.time_remaining.secs, _x.time_remaining.nsecs,) = _get_struct_4i().unpack(str[start:end])
      self.time_elapsed.canon()
      self.time_remaining.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4i().pack(_x.time_elapsed.secs, _x.time_elapsed.nsecs, _x.time_remaining.secs, _x.time_remaining.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.time_elapsed is None:
        self.time_elapsed = genpy.Duration()
      if self.time_remaining is None:
        self.time_remaining = genpy.Duration()
      end = 0
      _x = self
      start = end
      end += 16
      (_x.time_elapsed.secs, _x.time_elapsed.nsecs, _x.time_remaining.secs, _x.time_remaining.nsecs,) = _get_struct_4i().unpack(str[start:end])
      self.time_elapsed.canon()
      self.time_remaining.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4i = None
def _get_struct_4i():
    global _struct_4i
    if _struct_4i is None:
        _struct_4i = struct.Struct("<4i")
    return _struct_4i
