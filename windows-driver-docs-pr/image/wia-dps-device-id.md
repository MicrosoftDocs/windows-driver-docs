---
title: WIA\_DPS\_DEVICE\_ID
description: The WIA\_DPS\_DEVICE\_ID property contains a unique Function Instance identifier for a web services scanner device.
ms.assetid: 48c45b94-86b1-41b5-89bc-e3270ad56d7e
keywords: ["WIA_DPS_DEVICE_ID Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_DEVICE_ID
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_DPS\_DEVICE\_ID


The WIA\_DPS\_DEVICE\_ID property contains a unique Function Instance identifier for a web services scanner device. This identifier represents the web service on the scanner device with which the WIA minidriver is communicating. No assumptions about the form of this identifier should be made. The WIA minidriver creates and maintains this property.

WIA applications can use the value of WIA\_DPS\_DEVICE\_ID to find, using the Function Discovery API, the Function Instance object that represents the web services scanner device used in the current WIA session.

Property Type: VT\_BSTR

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The WIA minidriver initializes this property at run time by reading the PKEY\_PNPX\_ID device property from the Function Instance object.

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


[**WIA\_DPS\_GLOBAL\_IDENTITY**](wia-dps-global-identity.md)

[**WIA\_DPS\_SERVICE\_ID**](wia-dps-service-id.md)

 

 






