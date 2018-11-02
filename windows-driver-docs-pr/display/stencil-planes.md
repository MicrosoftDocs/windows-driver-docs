---
title: Stencil Planes
description: Stencil Planes
ms.assetid: a2abe78b-7755-45fc-ba02-f2809db5da3e
keywords:
- Direct3D WDK Windows 2000 display , stencil planes
- stencil planes WDK Direct3D
- per-pixel drawing WDK Direct3D
- special effects WDK Direct3D
- geometry rendering WDK Direct3D
- outlining WDK Direct3D
- shadowing WDK Direct3D
- decals WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stencil Planes


## <span id="ddk_stencil_planes_gg"></span><span id="DDK_STENCIL_PLANES_GG"></span>


Stencil planes enable and disable drawing on a per-pixel basis. They are typically used in multipass algorithms to achieve special effects, such as decals, outlining, shadows, and constructive solid geometry rendering.

Some hardware designed to accelerate Direct3D implements stencil planes. The special effects enabled by stencil planes are useful for entertainment applications.

Stencil planes are assumed to be embedded in the z-buffer data.

In DirectX 5.0, applications found the available z-buffer bit depths using the DDBD\_*Xx* flags set in the **dwDeviceZBufferBitDepth** member of the [**D3DDEVICEDESC\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff544689) structure. To support z-buffers with stencil and z-buffer bit depths that cannot be represented using the existing DDBD\_*Xx* flags, DirectX 6.0 and later versions have a new API entry point, **IDirect3D7::EnumZBufferFormats** (described in the Direct3D SDK documentation), which returns an array of DDPIXELFORMAT structures describing the possible z-buffer/stencil pixel formats. The [**DDPIXELFORMAT**](https://msdn.microsoft.com/library/windows/hardware/ff550274) structure includes the following new z-buffer-related members:

<span id="dwStencilBitDepth"></span><span id="dwstencilbitdepth"></span><span id="DWSTENCILBITDEPTH"></span>**dwStencilBitDepth**  
Specifies the number of stencil bits (as an integer, not as a DDBD\_*Xx* flag value).

<span id="dwZBitMask"></span><span id="dwzbitmask"></span><span id="DWZBITMASK"></span>**dwZBitMask**  
Specifies which bits the z-value occupies. If nonzero, this mask means that the z-buffer is a standardized unsigned integer z-buffer format.

<span id="dwStencilBitMask"></span><span id="dwstencilbitmask"></span><span id="DWSTENCILBITMASK"></span>**dwStencilBitMask**  
Specifies which bits the stencil value occupies.

A new flag, DDPF\_STENCILBUFFER, indicates the presence of stencil bits within the z-buffer. The **dwZBufferBitDepth** member, which existed previously, gives the total number of z-buffer bits including the stencil bits.

DirectX 6.0 and later versions drivers should still set the appropriate DDBD\_*Xx* flags in **dwDeviceZBufferBitDepth** for the z-only z-buffer formats they support. If stencil planes are not supported and the DDBD\_*Xx* flags can represent all available z-buffer formats, then setting these flags is sufficient, because they are translated into DDPIXELFORMAT by **IDirect3D7::EnumZBufferFormats**. Otherwise, the Direct3D driver must respond to a [**DdGetDriverInfo**](https://msdn.microsoft.com/library/windows/hardware/ff549404) query that uses the GUID\_ZPixelFormats GUID by returning a buffer in which the first DWORD indicates the number of valid z-buffer DDPIXELFORMAT structures, followed by the DDPIXELFORMAT structures themselves.

New render states associated with stencil planes are shown in the following table, which lists the render state, the type associated with the render state's value, and a description. For more details on these render states, see the DirectX SDK documentation.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Render State</th>
<th align="left">Type</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DRENDERSTATE_STENCILFUNC</p></td>
<td align="left"><p>D3DCMPFUNC</p></td>
<td align="left"><p>Comparison function. The test passes if the following expression is true:</p>
<p>(ref &amp; mask) OPERATION (stencil &amp; mask) where <em>ref</em> is the reference value, <em>stencil</em> is the value in the stencil buffer, and <em>mask</em> is the value of D3DRENDERSTATE_STENCILMASK.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DRENDERSTATE_STENCILREF</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>Reference value used in the stencil test.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DRENDERSTATE_STENCILMASK</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>Mask value used in the stencil test.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DRENDERSTATE_STENCILWRITEMASK</p></td>
<td align="left"><p>DWORD</p></td>
<td align="left"><p>Write mask applied to any values written to the stencil buffer.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DRENDERSTATE_STENCILFAIL</p>
<p>D3DRENDERSTATE_STENCILZFAIL</p>
<p>D3DRENDERSTATE_STENCILPASS</p></td>
<td align="left"><p>D3DSTENCILOP</p></td>
<td align="left"><p>These new render states are defined, respectively, to inform the hardware about what to do when the stencil test fails, when the stencil test passes but the z-test fails, and when both the stencil and z-tests pass. The values of these new render states can be set to enumerators of the D3DSTENCILOP enumerated type, which specify the desired stencil operation to be performed. For more information about D3DSTENCILOP, see the DirectX SDK documentation.</p></td>
</tr>
</tbody>
</table>

 

 

 





