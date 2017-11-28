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

## <span id="see_also"></span>See also


[**WIA\_IPS\_DESKEW\_X**](wia-ips-deskew-x.md)

[**WIA\_IPS\_XEXTENT**](wia-ips-xextent.md)

[**WIA\_IPS\_XPOS**](wia-ips-xpos.md)

[**WIA\_IPS\_YEXTENT**](wia-ips-yextent.md)

[**WIA\_IPS\_YPOS**](wia-ips-ypos.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_DESKEW_Y%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





