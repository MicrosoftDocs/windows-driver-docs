---
title: KSPROPERTY\_SOUNDDETECTOR\_ARMED
description: The KSPROPERTY\_SOUNDDETECTOR\_ARMED property is the current arming state of the detector.
keywords: ["KSPROPERTY_SOUNDDETECTOR_ARMED Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SOUNDDETECTOR_ARMED
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 09/26/2019
ms.localizationpriority: medium
---

# KSPROPERTY\_SOUNDDETECTOR\_ARMED


The **KSPROPERTY\_SOUNDDETECTOR\_ARMED** property is the current arming state of the detector.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/previous-versions/ff564262(v=vs.85)" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/previous-versions/ff564262(v=vs.85))"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

When called by [KSPROPSETID_SoundDetector](kspropsetid-sounddetector.md), the driver resets this to false when:

-   The filter interface is disabled.
-   The [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) property is set.
-   A keyword is detected.


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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty" data-raw-source="[&lt;strong&gt;KSSOUNDDETECTORPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)"><strong>KSSOUNDDETECTORPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

When called with [KSPROPSETID_SoundDetector2](kspropsetid-sounddetector2.md) the arm state will not be reset when a keyword is detected.

It is reset to false when:
- The filter interface is disabled.
- The [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) property is set


### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The property value is a BOOL indicating the arming state of the detector.

## Remarks

The OS sets this true to engage the detector.

Setting this true while no keyword patterns are set ([**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) is empty) has no effect.

Note: If this property is true, subsequently setting [**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md) automatically resets this to false, as mentioned above.

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

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

[**KSSOUNDDETECTORPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)
