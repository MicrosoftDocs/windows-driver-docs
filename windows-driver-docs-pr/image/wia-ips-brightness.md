---
title: WIA\_IPS\_BRIGHTNESS
description: The WIA\_IPS\_BRIGHTNESS property contains the current hardware brightness setting for a device.
MS-HAID:
- 'WIA\_PropTable\_d28d2f91-4163-4c9e-824f-b3d426bfbc50.xml'
- 'image.wia\_ips\_brightness'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 3954cf52-3bb1-4b76-9ff4-a638e1ddde83
keywords: ["WIA_IPS_BRIGHTNESS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BRIGHTNESS
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_BRIGHTNESS


The WIA\_IPS\_BRIGHTNESS property contains the current hardware brightness setting for a device.

## <span id="ddk_wia_ips_brightness_si"></span><span id="DDK_WIA_IPS_BRIGHTNESS_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_BRIGHTNESS property to the hardware's brightness value. The WIA minidriver creates and maintains this property.

Values for WIA\_IPS\_BRIGHTNESS should be mapped in a range from −1000 through 1000, where 1000 corresponds to the maximum brightness, 0 corresponds to normal brightness, and −1000 corresponds to the minimum brightness.

WIA\_IPS\_BRIGHTNESS is required for all image acquisition items.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_BRIGHTNESS%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




