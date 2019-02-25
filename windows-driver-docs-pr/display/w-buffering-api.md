---
title: W-Buffering API
description: W-Buffering API
ms.assetid: 7244d697-5200-4d37-9a75-270788c1c7f7
keywords:
- Direct3D WDK Windows 2000 display , w-buffering
- w-buffering WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# W-Buffering API


## <span id="ddk_w_buffering_api_gg"></span><span id="DDK_W_BUFFERING_API_GG"></span>


The D3DRENDERSTATE\_ZENABLE render state supports three settings from the D3DZBUFFERTYPE enumerated type.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>D3DZB_FALSE</p></td>
<td align="left"><p>Disables all depth buffering.</p></td>
</tr>
<tr class="even">
<td align="left"><p>D3DZB_TRUE</p></td>
<td align="left"><p>Enables z-buffer using perspective correct <em>z</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>D3DZB_USEW</p></td>
<td align="left"><p>Disables z-buffering but enables w-buffering, which is eye-relative <em>z</em>.</p></td>
</tr>
</tbody>
</table>

 

Because the exact format used for storing *w* varies widely, it should be assumed to be opaque.

Surface allocations and depth-fill operations work identically when using w-buffering. All z-buffer compare modes work identically in either case.

For more information, see the DirectX SDK documentation.

 

 





