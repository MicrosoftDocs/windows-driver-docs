---
title: WIA\_DPS\_MAX\_SCAN\_TIME
description: The WIA\_DPS\_MAX\_SCAN\_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.
MS-HAID:
- 'WIA\_PropTable\_cf8f1c13-5a1f-462c-8150-fbc2ff9359dd.xml'
- 'image.wia\_dps\_max\_scan\_time'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 28c24b1b-9318-46d2-86eb-f948247de8ab
keywords: ["WIA_DPS_MAX_SCAN_TIME Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_DPS_MAX_SCAN_TIME
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_DPS\_MAX\_SCAN\_TIME


The WIA\_DPS\_MAX\_SCAN\_TIME property contains the maximum time to scan a single page with the current property settings, in milliseconds.

## <span id="ddk_wia_dps_max_scan_time_si"></span><span id="DDK_WIA_DPS_MAX_SCAN_TIME_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read-only

Remarks
-------

An application reads the WIA\_DPS\_MAX\_SCAN\_TIME property to estimate how much the time it will take to scan a page. This estimate is helpful when you are determining the conditions of a device that has stopped responding. The WIA minidriver creates and maintains this property.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_DPS_MAX_SCAN_TIME%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




