---
title: WIA\_DPC\_EXPOSURE\_METERING\_MODE
description: The WIA\_DPC\_EXPOSURE\_METERING\_MODE property specifies the mode that a camera uses to automatically adjust the exposure setting.
MS-HAID:
- 'WIA\_PropTable\_4f7f027f-aebf-4a44-96f4-fb6f06f305e1.xml'
- 'image.wia\_dpc\_exposure\_metering\_mode'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f1340ba2-984e-41a1-a6f2-56639f60d94a
keywords: ["WIA_DPC_EXPOSURE_METERING_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_METERING_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_EXPOSURE\_METERING\_MODE


The WIA\_DPC\_EXPOSURE\_METERING\_MODE property specifies the mode that a camera uses to automatically adjust the exposure setting.

## <span id="ddk_wia_dpc_exposure_metering_mode_si"></span><span id="DDK_WIA_DPC_EXPOSURE_METERING_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the constants that are valid with the WIA\_DPC\_EXPOSURE\_METERING\_MODE property.

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
<td><p>EXPOSUREMETERING_AVERAGE</p></td>
<td><p>Set the exposure based on an average of the entire scene.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMETERING_CENTERSPOT</p></td>
<td><p>Set the exposure based on a center spot.</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMETERING_CENTERWEIGHT</p></td>
<td><p>Set the exposure based on a center-weighted average.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMETERING_MULTISPOT</p></td>
<td><p>Set the exposure based on a multispot pattern.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_EXPOSURE_METERING_MODE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




