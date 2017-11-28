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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_SEGMENTATION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




