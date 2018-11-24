---
title: WIA\_IPS\_THRESHOLD
description: The WIA\_IPS\_THRESHOLD property contains the current hardware threshold setting for a device. The WIA minidriver creates and maintains this property.
ms.assetid: 1d315168-5434-4e99-9e54-cb6e279df3e7
keywords: ["WIA_IPS_THRESHOLD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_THRESHOLD
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_THRESHOLD


The WIA\_IPS\_THRESHOLD property contains the current hardware threshold setting for a device. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ips_threshold_si"></span><span id="DDK_WIA_IPS_THRESHOLD_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/write

Remarks
-------

You should map values for the WIA\_IPS\_THRESHOLD property in a range from 0 through 255. The default value is 128.

An application sets WIA\_IPS\_THRESHOLD to change the hardware threshold value. This value is valid only if the [**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md) property is equal to WIA\_DATA\_THRESHOLD. If a device does not allow WIA\_DATA\_THRESHOLD to be changed, it should report the default value of 128.

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

## See also


[**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md)

 

 






