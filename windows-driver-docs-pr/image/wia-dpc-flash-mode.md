---
title: WIA\_DPC\_FLASH\_MODE
description: The WIA\_DPC\_FLASH\_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.
ms.assetid: 04c58111-09a7-4cd0-b60b-a65197c0931d
keywords: ["WIA_DPC_FLASH_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_FLASH_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_FLASH\_MODE


The WIA\_DPC\_FLASH\_MODE property defines the current flash mode setting for a camera device. The device driver enumerates the supported values of this property, and an application writes this property to set the flash mode for the camera device.

## <span id="ddk_wia_dpc_flash_mode_si"></span><span id="DDK_WIA_DPC_FLASH_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

The following table describes the six that are valid with this property.

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
<td><p>FLASHMODE_AUTO</p></td>
<td><p>The camera device determines the proper flash settings.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_EXTERNALSYNC</p></td>
<td><p>The camera device is configured to synchronize with external flash units.</p></td>
</tr>
<tr class="odd">
<td><p>FLASHMODE_FILL</p></td>
<td><p>The camera device is configured to flash regardless of current lighting conditions.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_OFF</p></td>
<td><p>The camera device is configured <em>not</em> to flash for any picture taken.</p></td>
</tr>
<tr class="odd">
<td><p>FLASHMODE_REDEYE_AUTO</p></td>
<td><p>The camera device determines the proper flash settings by using red-eye reduction, regardless of current lighting conditions.</p></td>
</tr>
<tr class="even">
<td><p>FLASHMODE_REDEYE_FILL</p></td>
<td><p>The camera device is configured to use red-eye reduction and flash regardless of current lighting conditions.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_FLASH_MODE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




