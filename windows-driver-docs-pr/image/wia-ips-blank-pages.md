---
title: WIA\_IPS\_BLANK\_PAGES
description: The WIA\_IPS\_BLANK\_PAGES property is used to configure blank page detection. The WIA minidriver creates and maintains this property.
ms.assetid: FB2EBC0D-6F09-4B64-9B79-7EE20CAF7023
keywords: ["WIA_IPS_BLANK_PAGES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_BLANK_PAGES
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

# WIA\_IPS\_BLANK\_PAGES


The **WIA\_IPS\_BLANK\_PAGES** property is used to configure blank page detection. The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_BLANK\_PAGES** property.

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
<td><p>WIA_BLANK_PAGE_DETECTION_DISABLED</p></td>
<td><p>Blank page detection is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_BLANK_PAGE_DISCARD</p></td>
<td><p>The device detects blank pages and automatically skips scanning them (discards scanned data if any) and continues scanning.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_BLANK_PAGE_JOB_SEPARATOR</p></td>
<td><p>The device detects blank pages and acts as configured through the [<strong>WIA_IPS_JOB_SEPARATORS</strong>](wia-ips-job-separators.md) property. This value is valid only when the Feeder item supports the <strong>WIA_IPS_JOB_SEPARATORS</strong> property.</p></td>
</tr>
</tbody>
</table>

 

This property is optional, and is valid only for the Feeder data source item (represented in the [**WIA\_IPA\_ITEM\_CATEGORY**](wia-ipa-item-category.md) property as WIA\_CATEGORY\_FEEDER).

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20WIA_IPS_BLANK_PAGES%20%20RELEASE:%20%2811/13/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




