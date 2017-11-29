---
title: WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT
description: The WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT property describes the maximum time to search for patch codes on a document page.
ms.assetid: D7DD05B2-43CA-484F-8207-4ED9C307D3AA
keywords: ["WIA_IPS_PATCH_CODE_SEARCH_TIMEOUT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PATCH_CODE_SEARCH_TIMEOUT
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

# WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT


The **WIA\_IPS\_PATCH\_CODE\_SEARCH\_TIMEOUT** property describes the maximum time to search for patch codes on a document page.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

The time unit is not specified (it can be milliseconds or tenths of a second for example) but the application can choose values in the minimum – maximum range reported by the WIA minidriver.

This property is required for all Patch Code Reader items. The property can be implemented to support a range containing one single value (meaning the application cannot change this timeout)

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_PATCH_CODE_SEARCH_TIMEOUT%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




