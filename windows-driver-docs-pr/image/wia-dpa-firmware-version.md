---
title: WIA\_DPA\_FIRMWARE\_VERSION
description: The WIA\_DPA\_FIRMWARE\_VERSION property contains a device firmware version. The minidriver creates and maintains this property.
ms.assetid: 868979d9-81a4-4655-915c-539771e438a6
keywords: ["WIA_DPA_FIRMWARE_VERSION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPA_FIRMWARE_VERSION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPA\_FIRMWARE\_VERSION


The WIA\_DPA\_FIRMWARE\_VERSION property contains a device firmware version. The minidriver creates and maintains this property.

## <span id="ddk_wia_dpa_firmware_version_si"></span><span id="DDK_WIA_DPA_FIRMWARE_VERSION_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value of the WIA\_DPA\_FIRMWARE\_VERSION property must be a string value, such as "1.0.4" or "1.0abc".

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
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 





