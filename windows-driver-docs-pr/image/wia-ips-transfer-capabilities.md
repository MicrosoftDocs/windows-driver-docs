---
title: WIA\_IPS\_TRANSFER\_CAPABILITIES
description: The WIA\_IPS\_TRANSFER\_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_2f748821-673c-4d8b-ba86-f9715de16e60.xml'
- 'image.wia\_ips\_transfer\_capabilities'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 937e3e54-6ad3-46bb-bd00-e0812c64e539
keywords: ["WIA_IPS_TRANSFER_CAPABILITIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_TRANSFER_CAPABILITIES
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_TRANSFER\_CAPABILITIES


The WIA\_IPS\_TRANSFER\_CAPABILITIES property indicates if a device can transfer parent and child items together. The WIA minidriver creates and maintains this property.

Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constant that is valid with the WIA\_IPS\_TRANSFER\_CAPABILITIES property

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_TRANSFER_CHILDREN_SINGLE_SCAN</p></td>
<td><p>The device can transfer the parent and child items together or the device must make a separate scan for each item and each child item.</p></td>
</tr>
</tbody>
</table>

 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_TRANSFER_CAPABILITIES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




