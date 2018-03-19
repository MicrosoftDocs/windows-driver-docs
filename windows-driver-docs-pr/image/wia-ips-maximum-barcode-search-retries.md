---
title: WIA\_IPS\_MAXIMUM\_BARCODE\_SEARCH\_RETRIES
description: The WIA\_IPS\_MAXIMUM\_BARCODE\_SEARCH\_RETRIES property describes the maximum number of retries the reader attempts if no barcode can be found when barcode detection is enabled.
ms.assetid: AA9255D2-6B3B-4539-8C9C-7B0B84E2417D
keywords: ["WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES Imaging Devices"]
topic_type:
- apiref
api_name:
- WIA_IPS_MAXIMUM_BARCODE_SEARCH_RETRIES
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

# WIA\_IPS\_MAXIMUM\_BARCODE\_SEARCH\_RETRIES


The **WIA\_IPS\_MAXIMUM\_BARCODE\_SEARCH\_RETRIES** property describes the maximum number of retries the reader attempts if no barcode can be found when barcode detection is enabled.

## <span id="ddk_wia_ipa_depth_si"></span><span id="DDK_WIA_IPA_DEPTH_SI"></span>


Property Type: VT\_I4

Valid Values: WIA\_PROP\_RANGE

Access Rights: Read/Write

Remarks
-------

This property is required for all Barcode Reader items. The property can be implemented to support a range containing one single value, including 0 (no retries).

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

 

 





