---
title: WIA\_IPS\_SEGMENTATION
description: The WIA\_IPS\_SEGMENTATION property indicates if segmentation is to be performed during a scan. The WIA minidriver creates and maintains this property.
ms.assetid: 4e801aa4-a85f-4439-8a8d-990e6cbf81e4
keywords: ["WIA_IPS_SEGMENTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SEGMENTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_SEGMENTATION


The WIA\_IPS\_SEGMENTATION property indicates if segmentation is to be performed during a scan. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the values that are defined for the WIA\_IPS\_SEGMENTATION property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_USE_SEGMENTATION_FILTER</p></td>
<td><p>The application should use the segmentation filter for multi-region scanning.</p></td>
</tr>
<tr class="even">
<td><p>WIA_DONT_USE_SEGMENTATION_FILTER</p></td>
<td><p>The driver creates the child items itself for multi-region scanning. This situation typically occurs if a scanner uses fixed frames for multi-region scanning.</p></td>
</tr>
</tbody>
</table>

 

You must implement WIA\_IPS\_SEGMENTATION for scanner flatbed and film items if they support the creation of child items with a segmentation filter or if the driver itself creates child items for fixed frames.

You can package a driver with a segmentation filter and still have WIA\_IPS\_SEGMENTATION set to WIA\_DONT\_USE\_SEGMENTATION\_FILTER for one of its items (for example, the film item). This situation could occur if the scanner uses fixed frames for film scanning, but not for scanning from the flatbed.

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

 

 





