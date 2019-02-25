---
title: WIA\_DIP\_BAUDRATE
description: The WIA\_DIP\_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.
ms.assetid: 38b7c12b-ff74-49eb-9a04-6b906dcc7d44
keywords: ["WIA_DIP_BAUDRATE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_BAUDRATE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_BAUDRATE


The WIA\_DIP\_BAUDRATE property contains the current baud rate setting for a device. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_baudrate_si"></span><span id="DDK_WIA_DIP_BAUDRATE_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The value of the WIA\_DIP\_BAUDRATE property should be "Empty" if the device is not connected by a serial cable.

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

 

 





