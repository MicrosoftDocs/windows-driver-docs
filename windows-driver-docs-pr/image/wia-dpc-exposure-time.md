---
title: WIA\_DPC\_EXPOSURE\_TIME
description: The WIA\_DPC\_EXPOSURE\_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.
MS-HAID:
- 'WIA\_PropTable\_90199830-d165-4862-9e1e-1db7068b8d5a.xml'
- 'image.wia\_dpc\_exposure\_time'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 78f12aaa-4b7b-4ba3-a6af-791e97581d26
keywords: ["WIA_DPC_EXPOSURE_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPC_EXPOSURE_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPC\_EXPOSURE\_TIME


The WIA\_DPC\_EXPOSURE\_TIME property corresponds to the shutter speed, in seconds that are scaled by 10,000.

## <span id="ddk_wia_dpc_exposure_time_si"></span><span id="DDK_WIA_DPC_EXPOSURE_TIME_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE or WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

Typically, a device uses the WIA\_DPC\_EXPOSURE\_TIME property only when the [**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md) property is set to EXPOSUREMODE\_MANUAL or EXPOSUREMODE\_SHUTTER\_PRIORITY.

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


[**WIA\_DPC\_EXPOSURE\_MODE**](wia-dpc-exposure-mode.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPC_EXPOSURE_TIME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





