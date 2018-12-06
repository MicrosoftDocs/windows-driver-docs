---
title: WIA\_IPS\_ORIENTATION
description: The WIA\_IPS\_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.
ms.assetid: e963d0d1-020c-4ec1-8b67-a89b1fd3e545
keywords: ["WIA_IPS_ORIENTATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_ORIENTATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_ORIENTATION


The WIA\_IPS\_ORIENTATION property describes the current orientation of the document to scan. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_orientation_si"></span><span id="DDK_WIA_IPS_ORIENTATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_ORIENTATION property to define the original orientation of a page or image to be acquired. For more information about how to use WIA\_IPS\_ORIENTATION, see [**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md).

The following table describes the constants that are valid with WIA\_IPS\_ORIENTATION.

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
<td><p>LANSCAPE</p></td>
<td><p>The orientation is a 90-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
<tr class="even">
<td><p>PORTRAIT</p></td>
<td><p>The orientation is at 0 degrees.</p></td>
</tr>
<tr class="odd">
<td><p>ROT180</p></td>
<td><p>The orientation is a 180-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
<tr class="even">
<td><p>ROT270</p></td>
<td><p>The orientation is a 270-degree counterclockwise rotation, relative to the PORTRAIT orientation.</p></td>
</tr>
</tbody>
</table>

 

The WIA\_IPS\_ORIENTATION property describes the orientation of the document to scan. This property affects the current scan frame and available page sizes.

WIA\_IPS\_ORIENTATIONis different from the [**WIA\_IPS\_ROTATION**](wia-ips-rotation.md) property, which refers to a rotation that is applied to an image *after* it is scanned. So, a ROT180 value for WIA\_IPS\_ORIENTATION is different from a ROT180 value for WIA\_IPS\_ROTATION. For WIA\_IPS\_ORIENTATION, ROT180 describes the orientation of the physical document to scan, relative to the scan direction, and for WIA\_IPS\_ROTATION, ROT180 describes the rotation to apply to an image after it is scanned.

The WIA\_IPS\_ORIENTATION property is required for ADF items and optional for all other image acquisition items.

**Note**   The compatibility layer within the WIA service does not add support for WIA\_IPS\_ORIENTATION to the ADF item that is translated from a Microsoft Windows XP WIA device if the property is not supported on the child item of the device. Applications should not expect that an ADF item will always support this property and should always check if WIA\_IPS\_ORIENTATION is supported at run time.

 

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


[**WIA\_DPS\_PAGE\_SIZE**](wia-dps-page-size.md)

[**WIA\_IPS\_ROTATION**](wia-ips-rotation.md)

 

 






