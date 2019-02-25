---
title: Texturing Requirements
description: Texturing Requirements
ms.assetid: 5fb64c9e-1c6d-4a8a-9a8f-7d4ed6d5c301
keywords:
- texture sizes WDK Direct3D
- texture filtering WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Texturing Requirements


## <span id="ddk_texturing_requirements_gg"></span><span id="DDK_TEXTURING_REQUIREMENTS_GG"></span>


This section lists requirements for texture sizes and texture filtering. There are also texture-related requirements for the **IDirect3DDevice7::ValidateDevice** method.

### <span id="texture_sizes"></span><span id="TEXTURE_SIZES"></span>Texture Sizes

The following are requirements for texture sizes:

1.  The driver must expose its minimum and maximum texture dimensions through the **dwMinTextureWidth**, **dwMinTextureHeight**, **dwMaxTextureWidth**, and **dwMaxTextureHeight** members of the D3DDEVICEDESC7 structure. This structure is defined in the Direct3D SDK documentation.

2.  If the hardware has an aspect ratio restriction on its textures, that ratio must be present in the **dwMaxTextureAspectRatio** member of the D3DDEVICEDESC7 structure.

3.  If the device supports only texture dimensions that are powers of two, then it must set the **dwTextureCaps** member of the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) structure to contain the D3DPTEXTURECAPS\_POW2 flag for the appropriate primitive type (line or triangle).

4.  If the device can support two-dimensional (2D) textures (that is, not volume or cube textures) of an arbitrary size when the texture addressing mode for the texture stage is set to D3DTADDRESS\_CLAMP, the texture wrapping for the texture stage is disabled (D3DRENDERSTATE\_WRAP*n* set to 0), and MIP mapping is not in use, then it must set the D3DPTEXTURECAPS\_NONPOW2CONDITIONAL flag.

5.  If the device only supports textures whose dimensions are equal, then it must set the **dwTextureCaps** member of the [**D3DPRIMCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff549034) structure to contain the D3DPTEXTURECAPS\_SQUAREONLY flag for the appropriate primitive type (line or triangle).

If the device supports textures of an arbitrary size without restrictions other than those described in the first and second requirements, then it must not set any of the flags described in the third, fourth, and fifth requirements.

### <span id="texture_filtering"></span><span id="TEXTURE_FILTERING"></span>Texture Filtering

Filters that magnify and minify textures must be enabled and disabled through the D3DTSS\_MAGFILTER and D3DTSS\_MINFILTER texture stage states. This filtering must not be performed automatically when these states are disabled. For more information about the D3DTSS\_*Xxx* texture stage states, see the D3DTEXTURESTAGESTATETYPE enumerated type in the Direct3D SDK documentation.

Texture MIP mapping must be enabled and disabled through the D3DTSS\_MIPFILTER texture stage state. If this state is disabled, but the texture was created as a MIP map, the device must use only the top level of the MIP map. MIP mapped filtering must not be performed when this state is disabled.

If the device supports anisotropic filtering, the maximum anisotropy level must be exported through the value of the **dwMaxAnisotropy** member of the D3DDEVICEDESC7 structure (defined in the Direct3D SDK documentation). Furthermore, the device must accept any setting from 1 through **dwMaxAnisotropy** in the D3DTSS\_MAXANISOTROPY texture stage state.

The device must be able to apply all supported filter modes to textures of any supported format. For example, if MIP mapping is supported with other texture formats, MIP map filtering of YUV textures should be able to be performed.

**Note**   DirectX 9.0 and later applications can use values in the D3DSAMPLERSTATETYPE enumeration to control the characteristics of sampler texture-related render states. In DirectX 8.0 and earlier, these sampler states were included in the D3DTEXTURESTAGESTATETYPE enumeration. The runtime maps user-mode sampler states (D3DSAMP\_*Xxx*) to kernel-mode D3DTSS\_*Xxx* values so that drivers are not required to process user-mode sampler states. For more information about D3DSAMPLERSTATETYPE, see the latest DirectX SDK documentation.

 

### <span id="idirect3ddevice7_validatedevice"></span><span id="IDIRECT3DDEVICE7_VALIDATEDEVICE"></span>IDirect3DDevice7::ValidateDevice

If a device supports a particular combination of texture stage state blending operations and operands in a single pass, then the device must return DD\_OK from a call to the **IDirect3DDevice7::ValidateDevice** method (described in the Direct3D SDK documentation) for each such combination.

If a device does not support a particular combination of texture stage state blending operations in a single pass, or does not support one or more of the blending operations or operands, then it must return one of the error codes allowable for the **IDirect3DDevice7::ValidateDevice** method. Invalid blending operations cannot silently fail the **IDirect3DDevice7::ValidateDevice** method.

 

 





