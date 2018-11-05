---
title: WIA\_IPA\_TYMED
description: The WIA\_IPA\_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.
ms.assetid: 3490f4b8-a1ed-4ab3-b621-ed87ce8ae9ea
keywords: ["WIA_IPA_TYMED Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPA_TYMED
api_location:
- Wiadef.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# WIA\_IPA\_TYMED


The WIA\_IPA\_TYMED property contains the method setting for image transfer . The WIA minidriver creates and maintains this property.

## <span id="ddk_wia_ipa_tymed_si"></span><span id="DDK_WIA_IPA_TYMED_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_LIST

Access Rights: Read/write

Remarks
-------

An application reads the WIA\_IPA\_TYMED property to determine the minidriver's method of data transfer.

The following table describes the constants that are valid with WIA\_IPA\_TYMED.

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
<td><p>TYMED_CALLBACK</p></td>
<td><p>Transfer an image to memory, in bands.</p>
<p>This constant is obsolete for Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>TYMED_FILE</p></td>
<td><p>Transfer an image to a file.</p></td>
</tr>
<tr class="odd">
<td><p>TYMED_MULTIPAGE_CALLBACK</p></td>
<td><p>Transfer multiple images to memory, in bands.</p>
<p>This constant is obsolete for Windows Vista and later operating systems.</p></td>
</tr>
<tr class="even">
<td><p>TYMED_MULTIPAGE_FILE</p></td>
<td><p>Transfer multiple images to a file.</p></td>
</tr>
</tbody>
</table>

 

All WIA 2.0 minidrivers must set the initial value of this property to its default value, which is TYMED\_FILE.

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

 

 





