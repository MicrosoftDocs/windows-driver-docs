---
title: WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION
description: The WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property indicates if a device supports the creation of child items.
MS-HAID:
- 'WIA\_PropTable\_50bc67d6-4304-43b8-8f6b-59602d5c2f80.xml'
- 'image.wia\_ips\_supports\_child\_item\_creation'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 77358889-d2c4-410f-b553-2dae2f7b27e3
keywords: ["WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION


The WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property indicates if a device supports the creation of child items. The WIA minidriver creates and maintains this property

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

Items that support the [**WIA\_IPS\_SEGMENTATION**](wia-ips-segmentation.md) property and the WIA\_USE\_SEGMENTATION\_FILTER value must also support the WIA\_IPS\_SUPPORTS\_CHILD\_ITEM\_CREATION property and have it set to **TRUE**.

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


[**WIA\_IPS\_SEGMENTATION**](wia-ips-segmentation.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_SUPPORTS_CHILD_ITEM_CREATION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





