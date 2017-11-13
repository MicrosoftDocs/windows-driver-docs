---
title: WIA\_DPS\_VERTICAL\_BED\_REGISTRATION
description: The WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property contains the registration, or vertical alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.
MS-HAID:
- 'WIA\_PropTable\_5c4f48cb-6ac6-4db2-87d4-7adaf24fecd8.xml'
- 'image.wia\_dps\_vertical\_bed\_registration'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 58c1bfb2-1f61-4910-ac6d-189aa203c370
keywords: ["WIA_DPS_VERTICAL_BED_REGISTRATION Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_VERTICAL_BED_REGISTRATION
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_VERTICAL\_BED\_REGISTRATION


The WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property contains the registration, or vertical alignment and edge detection, for documents that are placed on the flatbed of a scanner. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_dps_vertical_bed_registration_si"></span><span id="DDK_WIA_DPS_VERTICAL_BED_REGISTRATION_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPS\_VERTICAL\_BED\_REGISTRATION property.

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
<td><p>BOTTOM_JUSTIFIED</p></td>
<td><p>The paper is bottom-aligned.</p></td>
</tr>
<tr class="even">
<td><p>CENTERED</p></td>
<td><p>The paper is centered.</p></td>
</tr>
<tr class="odd">
<td><p>TOP_JUSTIFIED</p></td>
<td><p>The paper is top-aligned.</p></td>
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
<td><p>Obsolete in Windows Vista and later operating systems and should no longer be used. However, this property is still defined in Windows Vista for compatibility with applications and devices designed for Windows Server 2003, Windows XP, and previous versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**WIA\_DPS\_HORIZONTAL\_BED\_REGISTRATION**](wia-dps-horizontal-bed-registration.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_VERTICAL_BED_REGISTRATION%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





