---
title: WIA\_IPS\_CONTRAST
description: The WIA\_IPS\_CONTRAST property contains the current hardware contrast setting for a device.
ms.assetid: 7fecfd43-212c-40e6-8520-ef1819448895
keywords: ["WIA_IPS_CONTRAST Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_CONTRAST
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_CONTRAST


The WIA\_IPS\_CONTRAST property contains the current hardware contrast setting for a device.

## <span id="ddk_wia_ips_contrast_si"></span><span id="DDK_WIA_IPS_CONTRAST_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

An application sets the WIA\_IPS\_CONTRAST property to the hardware's contrast value. The WIA minidriver creates and maintains this property.

Values for WIA\_IPS\_CONTRAST should be mapped in a range from −1000 through 1000, where −1000 corresponds to the minimum contrast, 0 corresponds to normal contrast, and 1000 corresponds to the maximum contrast.

WIA\_IPS\_CONTRAST is required for all image acquisition items.

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

 

 





