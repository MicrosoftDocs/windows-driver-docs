---
title: WIA\_DPC\_SHARPNESS
description: The WIA\_DPC\_SHARPNESS property indicates the perceived sharpness of a captured image.
ms.assetid: 6fb78506-f4fe-481c-b1ea-0f4fedcdca1a
keywords: ["WIA_DPC_SHARPNESS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_SHARPNESS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPC\_SHARPNESS


The WIA\_DPC\_SHARPNESS property indicates the perceived sharpness of a captured image.

## <span id="ddk_wia_dpc_sharpness_si"></span><span id="DDK_WIA_DPC_SHARPNESS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST or WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_DPC\_SHARPNESS property can use either a list of values or a range of values. The minimum value represents the least amount of sharpness, and the maximum value represents the maximum sharpness. Typically, a value in the middle of the range represents normal, or default, sharpness.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





