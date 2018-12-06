---
title: WIA\_IPS\_MAXIMUM\_PATCH\_CODES\_PER\_PAGE
description: The WIA\_IPS\_MAXIMUM\_PATCH\_CODES\_PER\_PAGE property describes the maximum number of patch codes that the device can and should detect on one document page side when patch code detection is enabled.
ms.assetid: 91A0DAC0-D8F3-48BB-9DD4-AF50BD8F09AB
keywords: ["WIA_IPS_MAXIMUM_PATCH_CODES_PER_PAGE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MAXIMUM_PATCH_CODES_PER_PAGE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_MAXIMUM\_PATCH\_CODES\_PER\_PAGE


The **WIA\_IPS\_MAXIMUM\_PATCH\_CODES\_PER\_PAGE** property describes the maximum number of patch codes that the device can and should detect on one document page side when patch code detection is enabled.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

A value of 0 means "no maximum". The application can decrease the current value of this property in order to reduce the time spent on patch code detection and increase the scan speed.

This property is required for all Patch Code Reader items but it can be implemented as a range container containing only the value of 0 (minimum equal with maximum and set to 0, step size of 0).

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

 

 





