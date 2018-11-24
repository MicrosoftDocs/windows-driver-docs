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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_INTERFACES


This property returns the list of interfaces supported by pins instantiated by a specific pin factory.

## <span id="ddk_ksproperty_pin_interfaces_ks"></span><span id="DDK_KSPROPERTY_PIN_INTERFACES_KS"></span>


### Usage Summary Table

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566722" data-raw-source="[&lt;strong&gt;KSP_PIN&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff566722)"><strong>KSP_PIN</strong></a></p></td>
<td><p>A <a href="https://msdn.microsoft.com/library/windows/hardware/ff563441" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563441)"><strong>KSMULTIPLE_ITEM</strong></a> structure, followed by a sequence of <a href="https://msdn.microsoft.com/library/windows/hardware/ff563537" data-raw-source="[&lt;strong&gt;KSPIN_INTERFACE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff563537)"><strong>KSPIN_INTERFACE</strong></a> structures.</p></td>
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

## See also


[**KSP\_PIN**](https://msdn.microsoft.com/library/windows/hardware/ff566722)

[**KSMULTIPLE\_ITEM**](https://msdn.microsoft.com/library/windows/hardware/ff563441)

[**KSPIN\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff563537)

 

 






