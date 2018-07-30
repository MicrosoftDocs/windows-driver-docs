---
title: KSPROPERTY\_VPCONFIG\_SCALEFACTOR
description: The KSPROPERTY\_VPCONFIG\_SCALEFACTOR property sets the video port dimensions to user-defined specifications.
ms.assetid: 0fbfedc8-9dff-4c7c-910f-507b84614e47
keywords: ["KSPROPERTY_VPCONFIG_SCALEFACTOR Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_VPCONFIG_SCALEFACTOR
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_VPCONFIG\_SCALEFACTOR


The KSPROPERTY\_VPCONFIG\_SCALEFACTOR property sets the video port dimensions to user-defined specifications.

## <span id="ddk_ksproperty_vpconfig_scalefactor_ks"></span><span id="DDK_KSPROPERTY_VPCONFIG_SCALEFACTOR_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property descriptor type</th>
<th>Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSPROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff564262)</p></td>
<td><p>[<strong>KS_AMVPSIZE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567268)</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KS\_AMVPSIZE structure that specifies the width and height of the video port.

Remarks
-------

When this property is used by KSPROPSETID\_VPVBIConfig, all property requests must return STATUS\_NOT\_IMPLEMENTED.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262)

[**KS\_AMVPSIZE**](https://msdn.microsoft.com/library/windows/hardware/ff567268)

 

 






