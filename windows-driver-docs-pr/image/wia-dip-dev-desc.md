---
title: WIA\_DIP\_DEV\_DESC
description: The WIA\_DIP\_DEV\_DESC property contains the device description string for a WIA minidriver. The WIA service creates and maintains this property.
ms.assetid: ce10deb8-7f33-45da-8a0e-cdcd7bf08ff9
keywords: ["WIA_DIP_DEV_DESC Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_DEV_DESC
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_DEV\_DESC


The WIA\_DIP\_DEV\_DESC property contains the device description string for a WIA minidriver. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_dev_desc_si"></span><span id="DDK_WIA_DIP_DEV_DESC_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The device description string that the WIA\_DIP\_DEV\_DESC property contains is obtained from the driver's INF file. An application reads this property to get a description of the device.

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

 

 





