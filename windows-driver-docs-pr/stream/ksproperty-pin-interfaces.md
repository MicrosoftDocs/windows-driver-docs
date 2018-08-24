---
title: KSPROPERTY\_PIN\_INTERFACES
description: This property returns the list of interfaces supported by pins instantiated by a specific pin factory.
ms.assetid: 5a49c685-d086-4827-87a3-67d1fa80452a
keywords: ["KSPROPERTY_PIN_INTERFACES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_INTERFACES
api_location:
- ks.h
api_type:
- HeaderDef
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_INTERFACES


This property returns the list of interfaces supported by pins instantiated by a specific pin factory.

## <span id="ddk_ksproperty_pin_interfaces_ks"></span><span id="DDK_KSPROPERTY_PIN_INTERFACES_KS"></span>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Property Descriptor Type</th>
<th>Property Value Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Yes</p></td>
<td><p>No</p></td>
<td><p>Pin</p></td>
<td><p>[<strong>KSP_PIN</strong>](https://msdn.microsoft.com/library/windows/hardware/ff566722)</p></td>
<td><p>A [<strong>KSMULTIPLE_ITEM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563441) structure, followed by a sequence of [<strong>KSPIN_INTERFACE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff563537) structures.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

Specify KSPROPERTY\_PIN\_INTERFACES using KSP\_PIN, where the **PinId** member specifies the pin factory for which to return available interfaces.

This property returns the interfaces ordered by class driver preference.

Stream minidrivers do not need to handle this property directly; the stream class driver handles this property using stream request blocks to query for more information.

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
<td>Ks.h (include Ks.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

[**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537)

 

 






