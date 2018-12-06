---
title: WIA\_IPS\_MAXIMUM\_BARCODES\_PER\_PAGE
description: The WIA\_IPS\_MAXIMUM\_BARCODES\_PER\_PAGE property describes the maximum number of barcodes that the device can and should detect on one document page side when barcode detection is enabled.
ms.assetid: 9DA59D24-3483-4663-8B6A-54EC53A3466D
keywords: ["WIA_IPS_MAXIMUM_BARCODES_PER_PAGE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MAXIMUM_BARCODES_PER_PAGE
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 05/22/2018
ms.localizationpriority: medium
---

# WIA\_IPS\_MAXIMUM\_BARCODES\_PER\_PAGE


The **WIA\_IPS\_MAXIMUM\_BARCODES\_PER\_PAGE** property describes the maximum number of barcodes that the device can and should detect on one document page side when barcode detection is enabled.




Property Type: VT\_UI4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

A value of 0 means "no maximum." The application can decrease the current value of this property in order to reduce the time spent on barcode detection and increase the scan speed.

This property is required for all Barcode Reader items, but it can be implemented as a range container containing only the value of 0 (minimum equal with maximum and set to 0, step size of 0).

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

 

 





