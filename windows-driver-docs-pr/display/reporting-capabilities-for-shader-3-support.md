---
title: Reporting Capabilities for Shader 3 Support
description: Reporting Capabilities for Shader 3 Support
ms.assetid: 89590647-646c-47ec-a46e-e781b1b9f33e
keywords:
- shaders WDK DirectX 9.0 , shader 3.0 support
- vertex shaders WDK DirectX 9.0 , shader 3.0 support
- pixel shaders WDK DirectX 9.0 , shader 3.0 support
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Capabilities for Shader 3 Support


## <span id="ddk_reporting_capabilities_for_shader_3_support_gg"></span><span id="DDK_REPORTING_CAPABILITIES_FOR_SHADER_3_SUPPORT_GG"></span>


The DirectX 9.0 version driver for a display device that supports pixel or vertex shader version 3.0 and later must indicate that it supports the following capabilities:

### <span id="vertex_shader_3_0_and_later"></span><span id="VERTEX_SHADER_3_0_AND_LATER"></span>Vertex shader 3.0 and later

If a device supports vertex shader 3.0 and later, its driver must set the members of the D3DCAPS9 structure to the following values:

<span id="VS20Caps"></span><span id="vs20caps"></span><span id="VS20CAPS"></span>**VS20Caps**  
Set the following members of the D3DVSHADERCAPS2\_0 structure:

**DynamicFlowControlDepth** set to 24.

**NumTemps** set to 32.

**StaticFlowControlDepth** set to 4.

**Caps** set to the D3DVS20CAPS\_PREDICATION bit to indicate that predication is supported.

<span id="GuardBandLeft__GuardBandTop__GuardBandRight__GuardBandBottom"></span><span id="guardbandleft__guardbandtop__guardbandright__guardbandbottom"></span><span id="GUARDBANDLEFT__GUARDBANDTOP__GUARDBANDRIGHT__GUARDBANDBOTTOM"></span>**GuardBandLeft, GuardBandTop, GuardBandRight, GuardBandBottom**  
Set each to 8K.

<span id="VertexShaderVersion"></span><span id="vertexshaderversion"></span><span id="VERTEXSHADERVERSION"></span>**VertexShaderVersion**  
Set to 3.0.

<span id="MaxVertexShaderConst"></span><span id="maxvertexshaderconst"></span><span id="MAXVERTEXSHADERCONST"></span>**MaxVertexShaderConst**  
Set to 256.

<span id="MaxVertexShader30InstructionSlots"></span><span id="maxvertexshader30instructionslots"></span><span id="MAXVERTEXSHADER30INSTRUCTIONSLOTS"></span>**MaxVertexShader30InstructionSlots**  
Set to 512.

<span id="RasterCaps"></span><span id="rastercaps"></span><span id="RASTERCAPS"></span>**RasterCaps**  
Set the D3DPRASTERCAPS\_FOGVERTEX bit for fog support.

<span id="VertexTextureFilterCaps"></span><span id="vertextexturefiltercaps"></span><span id="VERTEXTEXTUREFILTERCAPS"></span>**VertexTextureFilterCaps**  
Set the following filter capabilities:

D3DPTFILTERCAPS\_MINFPOINT

D3DPTFILTERCAPS\_MAGFPOINT

<span id="DevCaps2"></span><span id="devcaps2"></span><span id="DEVCAPS2"></span>**DevCaps2**  
Set the D3DDEVCAPS2\_VERTEXELEMENTSCANSHARESTREAMOFFSET bit to indicate that vertex elements in a vertex declaration can share the same stream offset.

<span id="DeclTypes"></span><span id="decltypes"></span><span id="DECLTYPES"></span>**DeclTypes**  
Set the following bits to indicate the vertex data types supported by the device:

D3DDTCAPS\_UBYTE4

D3DDTCAPS\_UBYTE4N

D3DDTCAPS\_SHORT2N

D3DDTCAPS\_SHORT4N

D3DDTCAPS\_FLOAT16

D3DDTCAPS\_FLOAT16

### <span id="pixel_shader_3_0_and_later"></span><span id="PIXEL_SHADER_3_0_AND_LATER"></span>Pixel shader 3.0 and later

If a device supports pixel shader 3.0 and later, its driver must set the members of the D3DCAPS9 structure to the following values:

<span id="PS20Caps"></span><span id="ps20caps"></span><span id="PS20CAPS"></span>**PS20Caps**  
Set the following members of the D3DPSHADERCAPS2\_0 structure:

**DynamicFlowControlDepth** set to 24.

**NumTemps** set to 32.

**StaticFlowControlDepth** set to 4.

**NumInstructionSlots** set to 512.

**Caps** set to the following bits:

D3DPS20CAPS\_ARBITRARYSWIZZLE to indicate that arbitrary swizzles is supported.

D3DPS20CAPS\_GRADIENTINSTRUCTIONS to indicate that gradient instructions is supported.

D3DPS20CAPS\_PREDICATION to indicate that predication is supported.

D3DPS20CAPS\_NODEPENDENTREADLIMIT to indicate no dependent read limit.

D3DPS20CAPS\_NOTEXINSTRUCTIONLIMIT to indicate no limit on the mix of texture and math instructions.

<span id="MaxTextureWidth__MaxTextureHeight"></span><span id="maxtexturewidth__maxtextureheight"></span><span id="MAXTEXTUREWIDTH__MAXTEXTUREHEIGHT"></span>**MaxTextureWidth, MaxTextureHeight**  
Set each to 4K.

<span id="MaxTextureRepeat"></span><span id="maxtexturerepeat"></span><span id="MAXTEXTUREREPEAT"></span>**MaxTextureRepeat**  
Set to 8K.

<span id="MaxAnisotropy"></span><span id="maxanisotropy"></span><span id="MAXANISOTROPY"></span>**MaxAnisotropy**  
Set to 16.

<span id="PixelShaderVersion"></span><span id="pixelshaderversion"></span><span id="PIXELSHADERVERSION"></span>**PixelShaderVersion**  
Set to 3.0.

<span id="MaxPixelShader30InstructionSlots"></span><span id="maxpixelshader30instructionslots"></span><span id="MAXPIXELSHADER30INSTRUCTIONSLOTS"></span>**MaxPixelShader30InstructionSlots**  
Set to 512.

<span id="PrimitiveMiscCaps"></span><span id="primitivemisccaps"></span><span id="PRIMITIVEMISCCAPS"></span>**PrimitiveMiscCaps**  
Set the following bits:

D3DPMISCCAPS\_MASKZ

All the cull modes: D3DPMISCCAPS\_CULLNONE, D3DPMISCCAPS\_CULLCW, D3DPMISCCAPS\_CULLCCW.

D3DPMISCCAPS\_COLORWRITEENABLE

D3DPMISCCAPS\_CLIPPLANESCALEDPOINTS

D3DPMISCCAPS\_CLIPTLVERTS

D3DPMISCCAPS\_BLENDOP

D3DPMISCCAPS\_FOGINFVF

<span id="RasterCaps"></span><span id="rastercaps"></span><span id="RASTERCAPS"></span>**RasterCaps**  
Set the following bits:

D3DPRASTERCAPS\_MIPMAPLODBIAS

D3DPRASTERCAPS\_ANISOTROPY

D3DPRASTERCAPS\_COLORPERSPECTIVE

D3DPRASTERCAPS\_SCISSORTEST

Full depth support: D3DPRASTERCAPS\_SLOPESCALEDEPTHBIAS, D3DPRASTERCAPS\_DEPTHBIAS

<span id="ZCmpCaps"></span><span id="zcmpcaps"></span><span id="ZCMPCAPS"></span>**ZCmpCaps**  
Set the following bits for a full set of comparisons for stencil, depth and alpha test:

D3DPCMPCAPS\_NEVER

D3DPCMPCAPS\_LESS

D3DPCMPCAPS\_EQUAL

D3DPCMPCAPS\_LESSEQUAL

D3DPCMPCAPS\_GREATER

D3DPCMPCAPS\_NOTEQUAL

D3DPCMPCAPS\_GREATEREQUAL

D3DPCMPCAPS\_ALWAYS:

<span id="SrcBlendCaps__DestBlendCaps"></span><span id="srcblendcaps__destblendcaps"></span><span id="SRCBLENDCAPS__DESTBLENDCAPS"></span>**SrcBlendCaps, DestBlendCaps**  
Set the following source and destination blending modes except where noted:

D3DPBLENDCAPS\_ZERO

D3DPBLENDCAPS\_ONE

D3DPBLENDCAPS\_SRCCOLOR

D3DPBLENDCAPS\_INVSRCCOLOR

D3DPBLENDCAPS\_SRCALPHA

D3DPBLENDCAPS\_INVSRCALPHA

D3DPBLENDCAPS\_DESTALPHA

D3DPBLENDCAPS\_INVDESTALPHA

D3DPBLENDCAPS\_DESTCOLOR

D3DPBLENDCAPS\_INVDESTCOLOR

D3DPBLENDCAPS\_SRCALPHASAT (not set for **DestBlendCaps**)

D3DPBLENDCAPS\_BOTHSRCALPHA (not set for **DestBlendCaps**)

D3DPBLENDCAPS\_BOTHINVSRCALPHA (not set for **DestBlendCaps**)

D3DPBLENDCAPS\_BLENDFACTOR

<span id="TextureCaps"></span><span id="texturecaps"></span><span id="TEXTURECAPS"></span>**TextureCaps**  
Set the following texture capabilities:

D3DPTEXTURECAPS\_PERSPECTIVE

D3DPTEXTURECAPS\_TEXREPEATNOTSCALEDBYSIZE

D3DPTEXTURECAPS\_PROJECTED

D3DPTEXTURECAPS\_CUBEMAP

D3DPTEXTURECAPS\_VOLUMEMAP

D3DPTEXTURECAPS\_MIPMAP

D3DPTEXTURECAPS\_MIPVOLUMEMAP

D3DPTEXTURECAPS\_MIPCUBEMAP

<span id="TextureFilterCaps__VolumeTextureFilterCaps__CubeTextureFilterCaps"></span><span id="texturefiltercaps__volumetexturefiltercaps__cubetexturefiltercaps"></span><span id="TEXTUREFILTERCAPS__VOLUMETEXTUREFILTERCAPS__CUBETEXTUREFILTERCAPS"></span>**TextureFilterCaps, VolumeTextureFilterCaps, CubeTextureFilterCaps**  
Set the following filter capabilities for each except where noted:

D3DPTFILTERCAPS\_MINFPOINT

D3DPTFILTERCAPS\_MINFLINEAR

D3DPTFILTERCAPS\_MINFANISOTROPIC (not required for **VolumeTextureFilterCaps** and **CubeTextureFilterCaps**)

D3DPTFILTERCAPS\_MIPFPOINT

D3DPTFILTERCAPS\_MIPFLINEAR

D3DPTFILTERCAPS\_MAGFPOINT

D3DPTFILTERCAPS\_MAGFLINEAR

<span id="TextureAddressCaps"></span><span id="textureaddresscaps"></span><span id="TEXTUREADDRESSCAPS"></span>**TextureAddressCaps**  
Set the following texture address modes to indicate support at vertex and pixel stages:

D3DPTADDRESSCAPS\_WRAP

D3DPTADDRESSCAPS\_MIRROR

D3DPTADDRESSCAPS\_CLAMP

D3DPTADDRESSCAPS\_BORDER

D3DPTADDRESSCAPS\_INDEPENDENTUV

D3DPTADDRESSCAPS\_MIRRORONCE

<span id="StencilCaps"></span><span id="stencilcaps"></span><span id="STENCILCAPS"></span>**StencilCaps**  
Set the following bits to indicate support of stencil operations:

D3DSTENCILCAPS\_KEEP

D3DSTENCILCAPS\_ZERO

D3DSTENCILCAPS\_REPLACE

D3DSTENCILCAPS\_INCRSAT

D3DSTENCILCAPS\_DECRSAT

D3DSTENCILCAPS\_INVERT

D3DSTENCILCAPS\_INCR

D3DSTENCILCAPS\_DECR

D3DSTENCILCAPS\_TWOSIDED

<span id="FVFCaps"></span><span id="fvfcaps"></span><span id="FVFCAPS"></span>**FVFCaps**  
Set the D3DFVFCAPS\_PSIZE capability to indicate that the device supports point size per vertex.

<span id="TextureCaps"></span><span id="texturecaps"></span><span id="TEXTURECAPS"></span>**TextureCaps**  
Indicate that the device supports either full support or conditional nonpow-of-2 texture support. For more information, see [Reporting Capabilities for Shader 2 Support](reporting-capabilities-for-shader-2-support.md).

Must **not** set the D3DPTEXTURECAPS\_SQUAREONLY bit. That is, the device cannot be limited to square textures only.

If the device supports [Rendering to Multiple Targets Simultaneously](rendering-to-multiple-targets-simultaneously.md) (that is, the **NumSimultaneousRTs** member is set to greater than 1), its driver must set the members of the D3DCAPS9 structure to the following values:

<span id="PrimitiveMiscCaps"></span><span id="primitivemisccaps"></span><span id="PRIMITIVEMISCCAPS"></span>**PrimitiveMiscCaps**  
Set the following bits:

D3DPMISCCAPS\_INDEPENDENTWRITEMASKS

D3DPMISCCAPS\_MRTINDEPENDENTBITDEPTHS

D3DPMISCCAPS\_MRTPOSTPIXELSHADERBLENDING

<span id="MaxUserClipPlanes"></span><span id="maxuserclipplanes"></span><span id="MAXUSERCLIPPLANES"></span>**MaxUserClipPlanes**  
If vertex shader 3.0 and later is supported, set to 6.

<span id="DeclTypes"></span><span id="decltypes"></span><span id="DECLTYPES"></span>**DeclTypes**  
Set the following bits to indicate the vertex formats that the device supports if vertex shader 3.0 and later is supported:

D3DDTCAPS\_SHORT2N

D3DDTCAPS\_SHORT4N

D3DDTCAPS\_UDEC3

D3DDTCAPS\_DEC3N

 

 





