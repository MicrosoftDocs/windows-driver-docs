---
title: WIA\_DPS\_GLOBAL\_IDENTITY
description: The WIA\_DPS\_GLOBAL\_IDENTITY property contains the SOAP address of a web services scanner device. The WIA minidriver creates and maintains this property.
ms.assetid: 4ee25eb9-eb5b-43b2-8b35-7bc8ac45c90a
keywords: ["WIA_DPS_GLOBAL_IDENTITY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_GLOBAL_IDENTITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_GLOBAL\_IDENTITY


The WIA\_DPS\_GLOBAL\_IDENTITY property contains the SOAP address of a web services scanner device. The WIA minidriver creates and maintains this property.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA minidriver initializes this property at run time by reading the PKEY\_PNPX\_GlobalIdentity device property from the Function Instance object.

Both PKEY\_PNPX\_GlobalIdentity and PKEY\_PNPX\_ID contain a unique ID of the UPnP Device. The difference is that PKEY\_PNPX\_GlobalIdentity always contains the UUID of the root device for all Function Instances, while PKEY\_PNPX\_ID contains the UUID of the Device/Sub-Device that the Function Instance represents.

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

## See also


[**WIA\_DPS\_DEVICE\_ID**](wia-dps-device-id.md)

[**WIA\_DPS\_SERVICE\_ID**](wia-dps-service-id.md)

 

 






