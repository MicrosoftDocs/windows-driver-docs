---
title: WIA\_IPS\_DESKEW\_Y
description: The WIA\_IPS\_DESKEW\_Y property, together with the WIA\_IPS\_DESKEW\_X property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.
ms.assetid: 25aca00f-4048-4784-90a1-f1ad8c2de16a
keywords: ["WIA_IPS_DESKEW_Y Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_DESKEW_Y
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_DESKEW\_Y


The WIA\_IPS\_DESKEW\_Y property, together with the [**WIA\_IPS\_DESKEW\_X**](wia-ips-deskew-x.md) property, describes the upper two corners of a skewed image. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

The WIA\_IPS\_DESKEW\_X and WIA\_IPS\_DESKEW\_Y properties describe where the two upper corners of a skewed image are located within the bounding rectangle that the [**WIA\_IPS\_XPOS**](wia-ips-xpos.md), [**WIA\_IPS\_YPOS**](wia-ips-ypos.md), [**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md), and [**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md) properties define.

The valid values for WIA\_IPS\_DESKEW\_Y must be between 0 and (WIA\_IPS\_YEXTENT - 1). A value of 0 means that no deskew should be performed.

WIA\_IPS\_DESKEW\_Y contains the number of pixels in the y-direction from WIA\_IPS\_YPOS to the y-coordinate of the leftmost corner of the image to be deskewed.

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


[**WIA\_IPS\_DESKEW\_X**](wia-ips-deskew-x.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

 

 






