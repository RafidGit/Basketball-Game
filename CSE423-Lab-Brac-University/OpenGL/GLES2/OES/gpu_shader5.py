'''OpenGL extension OES.gpu_shader5

This module customises the behaviour of the 
OpenGL.raw.GLES2.OES.gpu_shader5 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a set of new features to the OpenGL ES Shading
	Language and related APIs to support capabilities of new GPUs, extending
	the capabilities of version 3.10 of the OpenGL ES Shading Language.
	Shaders using the new functionality provided by this extension should
	enable this functionality via the construct
	
	  #extension GL_OES_gpu_shader5 : require     (or enable)
	
	This extension provides a variety of new features for all shader types,
	including:
	
	  * support for indexing into arrays of opaque types (samplers,
	    and atomic counters) using dynamically uniform integer expressions;
	
	  * support for indexing into arrays of images and shader storage blocks
	    using only constant integral expressions;
	
	  * extending the uniform block capability to allow shaders to index
	    into an array of uniform blocks;
	
	  * a "precise" qualifier allowing computations to be carried out exactly
	    as specified in the shader source to avoid optimization-induced
	    invariance issues (which might cause cracking in tessellation);
	
	  * new built-in functions supporting:
	
	    * fused floating-point multiply-add operations;
	
	  * extending the textureGather() built-in functions provided by
	    OpenGL ES Shading Language 3.10:
	
	    * allowing shaders to use arbitrary offsets computed at run-time to
	      select a 2x2 footprint to gather from; and
	    * allowing shaders to use separate independent offsets for each of
	      the four texels returned, instead of requiring a fixed 2x2
	      footprint.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/gpu_shader5.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.OES.gpu_shader5 import *
from OpenGL.raw.GLES2.OES.gpu_shader5 import _EXTENSION_NAME

def glInitGpuShader5OES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION