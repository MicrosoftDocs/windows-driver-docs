---
title: WIA\_IPS\_BRIGHTNESS
description: The WIA\_IPS\_BRIGHTNESS property contains the current hardware brightness setting for a device.
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
ms.date: 11/28/2017
ms.localizationpriority: medium
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

 

 





