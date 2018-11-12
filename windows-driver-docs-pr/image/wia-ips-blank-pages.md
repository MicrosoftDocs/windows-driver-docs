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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_BLANK\_PAGES


The **WIA\_IPS\_BLANK\_PAGES** property is used to configure blank page detection. The WIA minidriver creates and maintains this property.




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
<td><p>The device detects blank pages and acts as configured through the <a href="wia-ips-job-separators.md" data-raw-source="[&lt;strong&gt;WIA_IPS_JOB_SEPARATORS&lt;/strong&gt;](wia-ips-job-separators.md)"><strong>WIA_IPS_JOB_SEPARATORS</strong></a> property. This value is valid only when the Feeder item supports the <strong>WIA_IPS_JOB_SEPARATORS</strong> property.</p></td>
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

 

 





