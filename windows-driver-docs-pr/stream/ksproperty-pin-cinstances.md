---
title: KSPROPERTY\_PIN\_CINSTANCES
description: The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.
MS-HAID:
- 'ks-prop\_9fd40f64-ac05-44af-9a10-8e570076097a.xml'
- 'stream.ksproperty\_pin\_cinstances'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
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
---

# KSPROPERTY\_PIN\_CINSTANCES


The current number of pins this pin factory has instantiated, as well as the maximum number of pins this pin factory can instantiate, per filter.

## <span id="ddk_ksproperty_pin_cinstances_ks"></span><span id="DDK_KSPROPERTY_PIN_CINSTANCES_KS"></span>


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
<td><p>KSPIN_CINSTANCES</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This property returns a structure of type KSPIN\_CINSTANCES:

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPERTY_PIN_CINSTANCES%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




