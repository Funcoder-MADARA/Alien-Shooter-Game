'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_NV_viewport_swizzle'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_NV_viewport_swizzle',error_checker=_errors._error_checker)
GL_VIEWPORT_SWIZZLE_NEGATIVE_W_NV=_C('GL_VIEWPORT_SWIZZLE_NEGATIVE_W_NV',0x9357)
GL_VIEWPORT_SWIZZLE_NEGATIVE_X_NV=_C('GL_VIEWPORT_SWIZZLE_NEGATIVE_X_NV',0x9351)
GL_VIEWPORT_SWIZZLE_NEGATIVE_Y_NV=_C('GL_VIEWPORT_SWIZZLE_NEGATIVE_Y_NV',0x9353)
GL_VIEWPORT_SWIZZLE_NEGATIVE_Z_NV=_C('GL_VIEWPORT_SWIZZLE_NEGATIVE_Z_NV',0x9355)
GL_VIEWPORT_SWIZZLE_POSITIVE_W_NV=_C('GL_VIEWPORT_SWIZZLE_POSITIVE_W_NV',0x9356)
GL_VIEWPORT_SWIZZLE_POSITIVE_X_NV=_C('GL_VIEWPORT_SWIZZLE_POSITIVE_X_NV',0x9350)
GL_VIEWPORT_SWIZZLE_POSITIVE_Y_NV=_C('GL_VIEWPORT_SWIZZLE_POSITIVE_Y_NV',0x9352)
GL_VIEWPORT_SWIZZLE_POSITIVE_Z_NV=_C('GL_VIEWPORT_SWIZZLE_POSITIVE_Z_NV',0x9354)
GL_VIEWPORT_SWIZZLE_W_NV=_C('GL_VIEWPORT_SWIZZLE_W_NV',0x935B)
GL_VIEWPORT_SWIZZLE_X_NV=_C('GL_VIEWPORT_SWIZZLE_X_NV',0x9358)
GL_VIEWPORT_SWIZZLE_Y_NV=_C('GL_VIEWPORT_SWIZZLE_Y_NV',0x9359)
GL_VIEWPORT_SWIZZLE_Z_NV=_C('GL_VIEWPORT_SWIZZLE_Z_NV',0x935A)
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glViewportSwizzleNV(index,swizzlex,swizzley,swizzlez,swizzlew):pass
