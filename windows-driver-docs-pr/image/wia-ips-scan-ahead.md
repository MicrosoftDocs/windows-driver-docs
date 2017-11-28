---
title: WIA\_IPS\_SCAN\_AHEAD
description: The WIA\_IPS\_SCAN\_AHEAD property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.
ms.assetid: 706BA423-399F-4859-BF41-10D3A88B61DD
keywords: ["WIA_IPS_SCAN_AHEAD Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_SCAN_AHEAD
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_SCAN\_AHEAD


The **WIA\_IPS\_SCAN\_AHEAD** property is used to enable scan ahead in the hardware device (scan at highest possible speed, buffering scanned images in the scanner's internal memory, transferring buffered images in parallel to the client application at an equal or lower speed). The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


**Note**  This property replaces [**WIA\_DPS\_SCAN\_AHEAD\_PAGES**](wia-dps-scan-ahead-pages.md), which is now obsolete.

 

Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_SCAN\_AHEAD** property.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WIA_SCAN_AHEAD_DISABLED</p></td>
<td><p>Scan ahead is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SCAN_AHEAD_ENABLED</p></td>
<td><p>Scan ahead is enabled. The WIA client application must download images as fast as it can. If the scan job is canceled before it is finished, some scanned documents may be lost (not yet transferred to the application).</p></td>
</tr>
</tbody>
</table>

 

This property is valid only for the Feeder item (WIA\_CATEGORY\_FEEDER) and is optional.

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

## <span id="see_also"></span>See also


[**WIA\_DPS\_SCAN\_AHEAD\_PAGES**](wia-dps-scan-ahead-pages.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_SCAN_AHEAD%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





