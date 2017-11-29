---
title: WIA\_IPS\_SCAN\_AHEAD\_CAPACITY
description: The WIA\_IPS\_SCAN\_AHEAD\_CAPACITY describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.
ms.assetid: 7A80964D-B0A4-4D6B-A320-4DE0A700E1A9
keywords: ["WIA_IPS_SCAN_AHEAD_CAPACITY Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SCAN_AHEAD_CAPACITY
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# WIA\_IPS\_SCAN\_AHEAD\_CAPACITY


The **WIA\_IPS\_SCAN\_AHEAD\_CAPACITY** describes the maximum number of pages that the scanner can scan ahead (and store in the internal scanner memory buffer) at the current scan job settings (the current document size, scan resolution, data type, file format, compression, and so on). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_NONE

Access Rights: Read/Write

Remarks
-------

When the [**WIA\_IPS\_SCAN\_AHEAD**](wia-ips-scan-ahead.md) property is supported, this property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER), and is optional.

A value of 0 means "undefined/unknown number of pages."

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_SCAN_AHEAD_CAPACITY%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




