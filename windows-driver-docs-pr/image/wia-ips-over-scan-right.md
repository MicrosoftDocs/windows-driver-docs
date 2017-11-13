---
title: WIA\_IPS\_OVER\_SCAN\_RIGHT
description: The WIA\_IPS\_OVER\_SCAN\_RIGHT property along with WIA\_IPS\_OVER\_SCAN\_LEFT, WIA\_IPS\_OVER\_SCAN\_TOP, and WIA\_IPS\_OVER\_SCAN\_BOTTOM are used to configure the amount of over scanning, in thousandths of an inch (0.001 \ 0034;) units, relative to the physical document.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 17259314-2102-46B9-A493-7F879A7D0604
keywords: ["WIA_IPS_OVER_SCAN_RIGHT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_OVER_SCAN_RIGHT
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_OVER\_SCAN\_RIGHT


The **WIA\_IPS\_OVER\_SCAN\_RIGHT** property along with [**WIA\_IPS\_OVER\_SCAN\_LEFT**](wia-ips-over-scan-left.md), [**WIA\_IPS\_OVER\_SCAN\_TOP**](wia-ips-over-scan-top.md), and [**WIA\_IPS\_OVER\_SCAN\_BOTTOM**](wia-ips-over-scan-bottom.md) are used to configure the amount of over scanning, in thousandths of an inch (0.001") units, relative to the physical document. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) but only when the [**WIA\_IPS\_OVER\_SCAN**](wia-ips-over-scan.md) property is supported. When it is supported, this property is required.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_OVER_SCAN_RIGHT%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




