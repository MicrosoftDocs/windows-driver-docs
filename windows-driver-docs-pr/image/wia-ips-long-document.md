---
title: WIA\_IPS\_LONG\_DOCUMENT
description: The WIA\_IPS\_LONG\_DOCUMENT property is used by the WIA minidriver to report whether long document scanning is supported and by the WIA client application to enable this feature. The WIA minidriver creates and maintains this property.
ms.assetid: FEFB77EE-8377-406C-A244-84E1BEF57808
keywords: ["WIA_IPS_LONG_DOCUMENT Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_LONG_DOCUMENT
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_LONG\_DOCUMENT


The **WIA\_IPS\_LONG\_DOCUMENT** property is used by the WIA minidriver to report whether long document scanning is supported and by the WIA client application to enable this feature. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_LONG\_DOCUMENT** property.

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
<td><p>WIA_LONG_DOCUMENT_DISABLED</p></td>
<td><p>Long document scanning is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_LONG_DOCUMENT_ENABLED</p></td>
<td><p>The device scans long documents up to the device&#39;s maximum possible length. The <a href="wia-ips-page-size.md" data-raw-source="[&lt;strong&gt;WIA_IPS_PAGE_SIZE&lt;/strong&gt;](wia-ips-page-size.md)"><strong>WIA_IPS_PAGE_SIZE</strong></a> property must be set to WIA_PAGE_AUTO for this value to be accepted.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_LONG_DOCUMENT_SPLIT</p></td>
<td><p>Long documents are automatically split (and transferred as separate images) at current <a href="wia-ips-page-size.md" data-raw-source="[&lt;strong&gt;WIA_IPS_PAGE_SIZE&lt;/strong&gt;](wia-ips-page-size.md)"><strong>WIA_IPS_PAGE_SIZE</strong></a> length. The last scanned page can be shorter.</p></td>
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

 

 





