---
title: WIA\_DPS\_SERVICE\_ID
description: The WIA\_DPS\_SERVICE\_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.
ms.assetid: ec77c2a6-0b9e-4c43-b189-7714257f3807
keywords: ["WIA_DPS_SERVICE_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_SERVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# WIA\_DPS\_SERVICE\_ID


The WIA\_DPS\_SERVICE\_ID property contains the service ID of a web services scanner device. The WIA minidriver creates and maintains this property.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA minidriver initializes this property at run time by reading the PKEY\_PNPX\_ServiceId device property from the Function Instance object.

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

## <span id="see_also"></span>See also


[**WIA\_DPS\_DEVICE\_ID**](wia-dps-device-id.md)

[**WIA\_DPS\_GLOBAL\_IDENTITY**](wia-dps-global-identity.md)

 

 






