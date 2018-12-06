---
title: KSPROPERTY\_PIN\_CINSTANCES
description: The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.
ms.assetid: 0a6c0afa-1bdf-4b80-a8d7-55f13d9da74b
keywords: ["KSPROPERTY_PIN_CINSTANCES Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_PIN_CINSTANCES
api_location:
- ks.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_PIN\_CINSTANCES


The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.

## <span id="ddk_ksproperty_pin_cinstances_ks"></span><span id="DDK_KSPROPERTY_PIN_CINSTANCES_KS"></span>


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
<td><p>KSPIN_CINSTANCES</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a structure of type KSPIN\_CINSTANCES:

```cpp
typedef struct {
    ULONG PossibleCount;
    ULONG CurrentCount;
} KSPIN_CINSTANCES;
```

The following is a description of each member of the KSPIN\_CINSTANCES structure.

<span id="PossibleCount"></span><span id="possiblecount"></span><span id="POSSIBLECOUNT"></span>**PossibleCount**  
Specifies the maximum number of pins the pin factory can instantiate on the filter, or KSINTANCE\_INDETERMINATE if there is no maximum.

<span id="CurrentCount"></span><span id="currentcount"></span><span id="CURRENTCOUNT"></span>**CurrentCount**  
Specifies the current number of pins the pin factory has instantiated on the filter.

This property specifies the per-filter maximum for a given pin factory. Use the [**KSPROPERTY\_PIN\_GLOBALCINSTANCES**](ksproperty-pin-globalcinstances.md) property to specify the overall maximum for a given pin factory.

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

 

 





