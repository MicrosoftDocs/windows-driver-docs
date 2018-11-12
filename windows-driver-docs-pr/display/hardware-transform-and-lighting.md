---
title: Hardware Transform and Lighting
description: Hardware Transform and Lighting
ms.assetid: b45aa56e-2d8c-412a-b581-a1e2002d4fac
keywords:
- Direct3D WDK Windows 2000 display , hardware tansform and lighting
- texture transforms WDK Direct3D
- transforms WDK Direct3D
- lighting WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Hardware Transform and Lighting


## <span id="ddk_hardware_transform_and_lighting_gg"></span><span id="DDK_HARDWARE_TRANSFORM_AND_LIGHTING_GG"></span>


Hardware acceleration of geometry operations, such as lighting and transformation, has been enabled with modifications to the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) DDI for the latest Direct X release. At the API level, devices that support vertex operations in hardware are enumerated separately from those that do rasterization only.

The existing caps structures have been extended to indicate features that may be present on a hardware-accelerated transform device. For example, the number of supported light sources is set with the **dwNumLights** member of the [**D3DLIGHTINGCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff548471) structure that is reported with the [**D3DDEVICEDESC\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff544689) structure.

Other flags are listed in the following table:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Flag</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DDEVCAPS_CANBLTSYSTONONLOCAL</p></td>
<td align="left"><p>The device supports a texture blt from system memory to nonlocal video memory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DDEVCAPS_DRAWPRIMITIVES2EX</p></td>
<td align="left"><p>The driver is DirectX 7.0-compliant by supporting extended <em>D3dDrawPrimitives2</em> capabilities.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DDEVCAPS_HWRASTERIZATION</p></td>
<td align="left"><p>The device has hardware acceleration for rasterization.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DDEVCAPS_HWTRANSFORMANDLIGHT</p></td>
<td align="left"><p>The device can support both hardware transform and lighting in hardware.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DDEVCAPS_SEPARATETEXTUREMEMORIES</p></td>
<td align="left"><p>The device is texturing from separate memory pools.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DTRANSFORMCAPS_CLIP</p></td>
<td align="left"><p>The hardware can clip while transforming.</p></td>
</tr>
</tbody>
</table>

 

Because the feature sets of hardware geometry accelerators may differ (such as the number of light sources supported), the caps structures indicate which subset of geometry operations this device performs. Zero is a valid value for the number of light sources supported, indicating that the hardware does transformations only.

Only vertices that include a vertex normal are properly lit; for vertices that do not contain a normal, a dot product of 0 is employed in all lighting calculations.

All the key state and data structures used by the software implementation of the geometry pipeline are made available at the DDI level. Some display cards only implement lighting in the hardware, and do transformation and clipping on the host processor.

The following render state types pertain only to devices that accelerate transform and lighting:

```cpp
D3DRENDERSTATE_AMBIENT
D3DRENDERSTATE_AMBIENTMATERIALSOURCE
D3DRENDERSTATE_CLIPPING
D3DRENDERSTATE_CLIPPLANEENABLE
D3DRENDERSTATE_COLORVERTEX
D3DRENDERSTATE_DIFFUSEMATERIALSOURCE
D3DRENDERSTATE_EMISSIVEMATERIALSOURCE
D3DRENDERSTATE_EXTENTS
D3DRENDERSTATE_FOGVERTEXMODE
D3DRENDERSTATE_LIGHTING
D3DRENDERSTATE_LOCALVIEWER
D3DRENDERSTATE_NORMALIZENORMALS
D3DRENDERSTATE_SPECULARMATERIALSOURCE
D3DRENDERSTATE_VERTEXBLEND
```

 

 





