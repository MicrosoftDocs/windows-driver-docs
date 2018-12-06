---
title: WIA\_IPS\_XSCALING
description: The WIA\_IPS\_XSCALING property indicates if scaling along the x-axis should be applied to a scan. The WIA minidriver creates and maintains this property.
ms.assetid: 608ac942-4a37-4490-8715-a1e2ebc4dc64
keywords: ["WIA_IPS_XSCALING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_XSCALING
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_XSCALING


The WIA\_IPS\_XSCALING property indicates if scaling along the x-axis should be applied to a scan. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write or read-only

Remarks
-------

Valid values for the WIA\_IPS\_XSCALING property range from 1 through 65535.

WIA\_IPS\_XSCALING indicates only scaling along the x-axis. If you want to scale an image uniformly, you must set a similar value in WIA\_IPS\_XSCALING and in the [**WIA\_IPS\_YSCALING**](wia-ips-yscaling.md) property.

Consider the following examples:

-   100, no scaling (1x, 100%). The image is not changed.

-   050, 1/2 scaling (1/2x, 50%). The image size is reduced along the x-axis by 50% (1/2 the original size).

-   200, 2x scaling (200%). The image size is enlarged along the x-axis by 200% (double).

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
<td><p>Available in Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## See also


[**WIA\_IPS\_YSCALING**](wia-ips-yscaling.md)

 

 






