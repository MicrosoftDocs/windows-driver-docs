---
title: WIA\_DPC\_EXPOSURE\_MODE
description: The WIA\_DPC\_EXPOSURE\_MODE property indicates a camera's current exposure mode.
MS-HAID:
- 'WIA\_PropTable\_554f5631-e55b-46b1-8938-6ad57c893a3c.xml'
- 'image.wia\_dpc\_exposure\_mode'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 30587d4f-5836-4030-9501-7612aaff58ae
keywords: ["WIA_DPC_EXPOSURE_MODE Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_MODE
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_EXPOSURE\_MODE


The WIA\_DPC\_EXPOSURE\_MODE property indicates a camera's current exposure mode.

## <span id="ddk_wia_dpc_exposure_mode_si"></span><span id="DDK_WIA_DPC_EXPOSURE_MODE_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application changes the WIA\_DPC\_EXPOSURE\_MODE property to control the exposure mode of the camera device.

The following table describes the constants that are valid with WIA\_DPC\_EXPOSURE\_MODE.

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
<td><p>EXPOSUREMODE_APERTURE_PRIORITY</p></td>
<td><p>A user manually sets the aperture, and the camera device automatically sets the shutter speed.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_AUTO</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed.</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_MANUAL</p></td>
<td><p>A user manually sets the aperture and shutter speed.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_PROGRAM_ACTION</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for moving subject matter (in other words, scenes that contain fast motion).</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_PROGRAM_CREATIVE</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for still subject matter.</p></td>
</tr>
<tr class="even">
<td><p>EXPOSUREMODE_PORTRAIT</p></td>
<td><p>The camera device automatically sets the aperture and shutter speed, and it optimizes them for portrait photography.</p></td>
</tr>
<tr class="odd">
<td><p>EXPOSUREMODE_SHUTTER_PRIORITY</p></td>
<td><p>A user manually sets the shutter speed, and the camera device automatically sets the aperture.</p></td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_EXPOSURE_MODE%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




