---
title: KSPROPERTY\_SOUNDDETECTOR\_STREAMINGSUPPORT
description: The KSPROPERTY\_SOUNDDETECTOR\_STREAMINGSUPPORT property indicates whether or not streaming is supported.
keywords: ["KSPROPERTY_SOUNDDETECTOR_STREAMINGSUPPORT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SOUNDDETECTOR_STREAMINGSUPPORT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 09/24/2019
ms.localizationpriority: medium
---

# KSPROPERTY\_SOUNDDETECTOR\_STREAMINGSUPPORT

The **KSPROPERTY\_SOUNDDETECTOR\_STREAMINGSUPPORT** property indicates whether or not streaming is supported.

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
<td align="left"><p>No</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty" data-raw-source="[&lt;strong&gt;KSSOUNDDETECTORPROPERTY&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-kssounddetectorproperty)"><strong>KSSOUNDDETECTORPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

The property value is a BOOL indicating whether or not streaming is supported.

A driver which supports this read property and returns false is indicating that only voice onset is supported without the associated burst audio stream.

A driver which does not support this property, or supports this property and returns true, is indicating that it supports bursting the audio data which triggered the keyword detection.

All detectors must support buffering and burst streaming the audio data which triggered the hardware keyword detection, and fail this request or set this value to true.

## Remarks
This property is for future use. There is currently no OS support for detectors which do voice onset only.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum supported client</p></td>
<td align="left"><p>Windows 10 Version 1903</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also

[**KSPROPERTY\_SOUNDDETECTOR\_PATTERNS**](ksproperty-sounddetector-patterns.md)

[**KSSOUNDDETECTORPROPERTY**](/windows-hardware/drivers/ddi/ksmedia/)
