---
title: WIA\_IPS\_JOB\_SEPARATORS
description: The WIA\_IPS\_JOB\_SEPARATORS property is used to enable the detection of job separators, and to configure the action that the device executes when it detects a job separator page. The WIA minidriver creates and maintains this property.
ms.assetid: 2ECD88EB-2B6F-477D-8F37-D4EECA580FAE
keywords: ["WIA_IPS_JOB_SEPARATORS Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_JOB_SEPARATORS
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_JOB\_SEPARATORS


The **WIA\_IPS\_JOB\_SEPARATORS** property is used to enable the detection of job separators, and to configure the action that the device executes when it detects a job separator page. The WIA minidriver creates and maintains this property.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the valid values for the **WIA\_IPS\_JOB\_SEPARATORS** property.

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
<td><p>WIA_SEPARATOR_DISABLED</p></td>
<td><p>Job separators detection is disabled. This is the required default value if the property is supported.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SEPARATOR_DETECT_SCAN_CONTINUE</p></td>
<td><p>Detect job separator page, scan the separator page, and continue scanning.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_SEPARATOR_DETECT_SCAN_STOP</p></td>
<td><p>Detect job separator page, scan the separator page, and stop scanning.</p></td>
</tr>
<tr class="even">
<td><p>WIA_SEPARATOR_DETECT_NOSCAN_CONTINUE</p></td>
<td><p>Detect job separator page, do not scan (skip) the separator page, and continue scanning.</p></td>
</tr>
<tr class="odd">
<td><p>WIA_SEPARATOR_DETECT_NOSCAN_STOP</p></td>
<td><p>Detect job separator page, do not scan (skip) the separator page, and stop scanning.</p></td>
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

 

 





