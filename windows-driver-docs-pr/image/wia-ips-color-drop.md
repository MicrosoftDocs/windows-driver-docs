---
title: WIA\_IPS\_COLOR\_DROP
description: The WIA\_IPS\_COLOR\_DROP property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.
ms.assetid: A0F14FDF-194D-4948-B9D8-F3E0C2E34618
keywords: ["WIA_IPS_COLOR_DROP Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_COLOR_DROP
api_location:
- Wiadef.h
api_type:
- HeaderDef
---

# WIA\_IPS\_COLOR\_DROP


The **WIA\_IPS\_COLOR\_DROP** property is used to configure color filtering for the image data acquired from the hardware device. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_COLOR\_DROP** property.

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
<td><p>WIA_COLOR_DROP_DISABLED</p></td>
<td><p>Color drop is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_COLOR_DROP_RED</p></td>
<td><p>The Red channel is dropped in the amount described by [<strong>WIA_IPS_COLOR_DROP_RED</strong>](wia-ips-color-drop-red.md).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COLOR_DROP_GREEN</p></td>
<td><p>The Green channel is dropped in the amount described by [<strong>WIA_IPS_COLOR_DROP_GREEN</strong>](wia-ips-color-drop-green.md).</p></td>
</tr>
<tr class="even">
<td><p>WIA_COLOR_DROP_BLUE</p></td>
<td><p>The Blue channel is dropped in the amount described by [<strong>WIA_IPS_COLOR_DROP_BLUE</strong>](wia-ips-color-drop-blue.md).</p></td>
</tr>
<tr class="odd">
<td><p>WIA_COLOR_DROP_RGB</p></td>
<td><p>The Red, Green, and/or Blue channels are dropped in the amounts specified by [<strong>WIA_IPS_COLOR_DROP_RED</strong>](wia-ips-color-drop-red.md), [<strong>WIA_IPS_COLOR_DROP_GREEN</strong>](wia-ips-color-drop-green.md), and [<strong>WIA_IPS_COLOR_DROP_BLUE</strong>](wia-ips-color-drop-blue.md).</p></td>
</tr>
</tbody>
</table>

 

This property is valid for all programmable image data source items, including Flatbed (WIA\_CATEGORY\_FLATBED) and Feeder (WIA\_CATEGORY\_FEEDER) and is optional. When the property is supported, WIA\_COLOR\_DROP\_DISABLED is the required default value.

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_COLOR_DROP%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




