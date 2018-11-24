---
title: WIA\_DIP\_DEV\_NAME
description: The WIA\_DIP\_DEV\_NAME property contains the name of a device. The WIA service creates and maintains this property.
ms.assetid: 9e1bdc00-b46f-4c20-bcc4-f3caa4820983
keywords: ["WIA_DIP_DEV_NAME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_DEV_NAME
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DIP\_DEV\_NAME


The WIA\_DIP\_DEV\_NAME property contains the name of a device. The WIA service creates and maintains this property.

## <span id="ddk_wia_dip_dev_name_si"></span><span id="DDK_WIA_DIP_DEV_NAME_SI"></span>


Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The device name that is contained in the WIA\_DIP\_DEV\_NAME property is obtained from the driver's INF file. An application reads this property to obtain the name of the device.

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

 

 





