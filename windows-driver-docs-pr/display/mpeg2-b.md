---
title: MPEG2_B
description: MPEG2_B
ms.assetid: 7d67f0ef-a5eb-40db-9f00-6f652d28e530
keywords:
- MPEG2_B restricted profile WDK DirectX VA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MPEG2\_B


## <span id="ddk_mpeg2_b_gg"></span><span id="DDK_MPEG2_B_GG"></span>


The MPEG2\_B restricted profile contains a set of features required for support of MPEG-2 video Main Profile and an associated DVD subpicture using front-end buffer-to-buffer subpicture blending. Alpha-blending source and destination surfaces are supported with width and height of at least 720 and 576, respectively. Support of this profile is currently encouraged, but not required.

Because the [MPEG2\_A](mpeg2-a.md) restricted profile is defined by a relaxation of the accelerator requirements of the MPEG2\_B profile, all accelerators that support the MPEG2\_B profile must support the MPEG2\_A profile.

The restrictions for MPEG2\_B are defined by the restrictions listed for MPEG2\_A, except for the following additional restrictions.

### <span id="Restrictions_on_DXVA_ConnectMode"></span><span id="restrictions_on_dxva_connectmode"></span><span id="RESTRICTIONS_ON_DXVA_CONNECTMODE"></span>Restrictions on DXVA\_ConnectMode

These values of the *bDXVA\_Func* variable must be supported: 1 (picture decoding), 2 (alpha-blend data loading), or 3 (alpha-blend combination).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>wRestrictedMode</strong></p></td>
<td align="left"><p>DXVA_RESTRICTED_MODE_MPEG2_B</p></td>
</tr>
</tbody>
</table>

 

### <span id="Restrictions_on_DXVA_ConfigAlphaLoad_and_DXVA_ConfigAlphaCombine"></span><span id="restrictions_on_dxva_configalphaload_and_dxva_configalphacombine"></span><span id="RESTRICTIONS_ON_DXVA_CONFIGALPHALOAD_AND_DXVA_CONFIGALPHACOMBINE"></span>Restrictions on DXVA\_ConfigAlphaLoad and DXVA\_ConfigAlphaCombine

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Structure Member</th>
<th align="left">Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>bConfigBlendType</strong> (DXVA_ConfigAlphaCombine)</p></td>
<td align="left"><p>Zero (front-end buffer-to-buffer blending)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>bConfigDataType</strong> (DXVA_ConfigAlphaLoad)</p></td>
<td align="left"><p>Zero, 1, or 3 (at the accelerator&#39;s discretion)</p></td>
</tr>
</tbody>
</table>

 

 

 





