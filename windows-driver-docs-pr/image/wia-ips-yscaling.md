---
title: WIA\_IPS\_YSCALING
description: The WIA\_IPS\_YSCALING property indicates if scaling along the y-axis should be applied to a scan. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_ed367f7b-0c11-409b-b3ad-bb0d97fa05bd.xml'
- 'image.wia\_ips\_yscaling'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4466697b-0d8e-477e-8dd0-2b277d4fd6b3
keywords: ["WIA_IPS_YSCALING Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_YSCALING
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_YSCALING


The WIA\_IPS\_YSCALING property indicates if scaling along the y-axis should be applied to a scan. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write or read-only

Remarks
-------

Valid values for the WIA\_IPS\_YSCALING property range from 1 through 65535.

WIA\_IPS\_YSCALING indicates only scaling along the y-axis. If you want to scale an image uniformly, you must set a similar value in WIA\_IPS\_YSCALING and in the [**WIA\_IPS\_XSCALING**](wia-ips-xscaling.md) property.

Consider the following examples:

-   100, no scaling (1x, 100%). The image is not changed.

-   050, 1/2 scaling (1/2x, 50%). The image size is reduced along the y-axis by 50% (1/2 the original size).

-   200, 2x scaling (200%). The image size is enlarged along the y-axis by 200% (double).

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


[**WIA\_IPS\_XSCALING**](wia-ips-xscaling.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_YSCALING%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





