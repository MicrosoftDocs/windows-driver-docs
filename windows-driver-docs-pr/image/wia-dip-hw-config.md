---
title: WIA\_DIP\_HW\_CONFIG
description: The WIA\_DIP\_HW\_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.
ms.assetid: c79e9651-120c-4f99-83d2-1920f7fccc73
keywords: ["WIA_DIP_HW_CONFIG Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DIP_HW_CONFIG
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DIP\_HW\_CONFIG


The WIA\_DIP\_HW\_CONFIG property indicates the type of connection that a device is using. The WIA service creates and maintains this property, and only the WIA service can change it.

## <span id="ddk_wia_dip_hw_config_si"></span><span id="DDK_WIA_DIP_HW_CONFIG_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DIP\_HW\_CONFIG property to determine the device's connection type.

The following table describes the possible values for WIA\_DIP\_HW\_CONFIG.

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
<td><p>1</p></td>
<td><p>Generic WDM device</p></td>
</tr>
<tr class="even">
<td><p>2</p></td>
<td><p>SCSI device</p></td>
</tr>
<tr class="odd">
<td><p>4</p></td>
<td><p>USB device</p></td>
</tr>
<tr class="even">
<td><p>8</p></td>
<td><p>Serial device</p></td>
</tr>
<tr class="odd">
<td><p>16</p></td>
<td><p>Parallel device</p></td>
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
<td><p>Header</p></td>
<td>Wiadef.h (include Wiadef.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DIP_HW_CONFIG%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




