---
title: WIA\_IPA\_DEPTH
description: The WIA\_IPA\_DEPTH property contains the bit depth setting of an image. The WIA minidriver creates and maintains this property.
ms.assetid: 90f7983c-296f-4dfc-90d3-886881a907af
keywords: ["WIA_IPA_DEPTH Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_DEPTH
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_DEPTH


The WIA\_IPA\_DEPTH property contains the bit depth setting of an image. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPA\_DEPTH property to determine the bit depth setting of an image. An application may also set this property to the desired bit depth, or to the WIA\_DEPTH\_AUTO value.

If you can set the device to only a single value, create a WIA\_PROP\_LIST type and place the valid value in it.

The WIA\_DEPTH\_AUTO value (defined as 0 bits per pixel) is valid for all programmable image data source items, including the Flatbed and Feeder. When this value is supported by the WIA mini-driver the WIA application client can set **WIA\_IPA\_DEPTH** to this value in order to enable automatic color detection at the device.

When the **WIA\_IPA\_DEPTH** property is set to WIA\_DEPTH\_AUTO, the WIA mini-driver must update the [**WIA\_IPA\_DATATYPE**](wia-ipa-datatype.md) property on the same item to WIA\_DATA\_AUTO (which must be a supported value if the device supports automatic color). When the **WIA\_IPA\_DATATYPE** value WIA\_DATA\_AUTO is supported, the **WIA\_IPA\_DEPTH** value WIA\_DEPTH\_AUTO is no longer optional and becomes a required value.

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

 

 





