---
title: KSPROPERTY\_SOUNDDETECTOR\_PATTERNS
description: The KSPROPERTY\_SOUNDDETECTOR\_PATTERNS property is set by the operating system to configure the keywords to be detected.
keywords: ["KSPROPERTY_SOUNDDETECTOR_PATTERNS Audio Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSPROPERTY_SOUNDDETECTOR_PATTERNS
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 09/25/2019
---

# KSPROPERTY\_SOUNDDETECTOR\_PATTERNS

The **KSPROPERTY\_SOUNDDETECTOR\_PATTERNS** property is set by the operating system to configure the keywords to be detected.

The OS sets the keyword patterns or may set this to an empty value.

When the OS sets this property, the driver automatically disarms the detector if was previously armed.

If the driver cannot satisfy a “set” request due to insufficient resources, the driver fails the request with **STATUS\_INSUFFICIENT\_RESOURCES**.

### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table - KSPROPSETID_SoundDetector

This usage table summarizes when KSPROPERTY\_SOUNDDETECTOR\_ARMED is called with [KSPROPSETID_SoundDetector](kspropsetid-sounddetector.md)

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/stream/ksproperty-structure" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](../stream/ksproperty-structure.md)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)"><strong>KSMULTIPLE_ITEM</strong></a></p></td>
</tr>
</tbody>
</table>


### <span id="Usage_Summary_Table"></span><span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table - KSPROPSETID_SoundDetector2

This usage table summarizes when KSPROPERTY\_SOUNDDETECTOR\_ARMED is called with [KSPROPSETID_SoundDetector2](kspropsetid-sounddetector2.md)

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
<th align="left">Get</th>
<th align="left">Set</th>
<th align="left">Target</th>
<th align="left">Property descriptor type</th>
<th align="left">Property value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty" data-raw-source="[&lt;strong&gt;KSSOUNDDETECTORPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)"><strong>KSSOUNDDETECTORPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item" data-raw-source="[&lt;strong&gt;KSMULTIPLE_ITEM&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)"><strong>KSMULTIPLE_ITEM</strong></a></p></td>
</tr>
</tbody>
</table>


### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The property value is a [**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item) structure followed by a sequence of 64-bit aligned detection patterns. Each pattern starts with a [**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader) followed by the pattern payload.

## Remarks

The driver shall not complete the “set” request until:

-   The detector is disarmed and subsequent “get” requests on [**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md) return false.
-   Subsequent “get” requests on [**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md) return no data.
-   The new keyword patterns are established and the keyword detector is operating on the new patterns.

The driver may keep the request pending until the above conditions are met. Also, if the device requires measurable initialization time, the driver may keep this request pending until the device is ready and the can process the request.

The OS requires this behavior to avoid race conditions between a detected a keyword and updating keyword patterns (e.g. if a keyword was detected and the KSEVENT\_SOUNDDETECTOR generated an instant before the OS updates the keywords).

The OS waits at least 2 seconds for this request to complete.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum supported server</p></td>
<td align="left"><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader)

[**SOUNDDETECTOR\_PATTERNS**](/previous-versions/windows/hardware/drivers/dn932155(v=vs.85))

[**KSPROPERTY\_SOUNDDETECTOR\_ARMED**](ksproperty-sounddetector-armed.md)

[**KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT**](ksproperty-sounddetector-matchresult.md)

[**KSPROPERTY**](../stream/ksproperty-structure.md)

[**KSMULTIPLE\_ITEM**](/windows-hardware/drivers/ddi/ks/ns-ks-ksmultiple_item)
