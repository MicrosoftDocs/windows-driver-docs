---
title: WIA\_IPS\_PATCH\_CODE\_READER
description: The WIA\_IPS\_PATCH\_CODE\_READER property is used to enable patch code detection. This property is required for all Patch code Reader items.
ms.assetid: 8F008388-9822-44DC-B022-0822A8204740
keywords: ["WIA_IPS_PATCH_CODE_READER Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_PATCH_CODE_READER
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPS\_PATCH\_CODE\_READER


The **WIA\_IPS\_PATCH\_CODE\_READER** property is used to enable patch code detection. This property is required for all Patch code Reader items.




Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/Write

Remarks
-------

The following table describes the required values for the **WIA\_IPS\_PATCH\_CODE\_READER** property.

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
<td><p>WIA_PATCH_CODE_READER_DISABLED</p></td>
<td><p>Patch code detection is disabled. This is the required default value.</p></td>
</tr>
<tr class="even">
<td><p>WIA_PATCH_CODE_READER_AUTO</p></td>
<td><p>Patch code detection is enabled. The patch code reader location is automatically selected by the device at runtime depending on the active scan input source.</p></td>
</tr>
</tbody>
</table>

 

The [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) property is also required for all Patch Code Reader items.

The following table describes the required values for the [**WIA\_IPA\_FORMAT**](wia-ipa-format.md) property when it is implemented on a Patch Code Reader item.

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
<td><p>WiaImgFmt_XmlPat</p></td>
<td><p>Patch code metadata is transferred as an XML file whose content is compliant with the WIA Patch Code Metadata Schema.</p></td>
</tr>
<tr class="even">
<td><p>WiaImgFmt_RawPat</p></td>
<td><p>Patch code metadata is transferred as a WIA Patch Code Metadata Raw Format file.</p></td>
</tr>
</tbody>
</table>

 

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

 

 





