---
title: KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT
description: The KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT property holds the result data for a match.
keywords: ["KSPROPERTY_SOUNDDETECTOR_MATCHRESULT Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_SOUNDDETECTOR_MATCHRESULT
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT


The **KSPROPERTY\_SOUNDDETECTOR\_MATCHRESULT** property holds the result data for a match.

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
<td align="left"><p><a href="/previous-versions/ff564262(v=vs.85)" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/previous-versions/ff564262(v=vs.85))"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader" data-raw-source="[&lt;strong&gt;SOUNDDETECTOR_PATTERNHEADER&lt;/strong&gt;](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader)"><strong>SOUNDDETECTOR_PATTERNHEADER</strong></a></p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A [**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader) structure followed by the result data payload.

## Remarks

The result data includes a [**SOUNDDETECTOR\_PATTERNHEADER**](/windows-hardware/drivers/ddi/ksmedia/ns-ksmedia-sounddetector_patternheader) identifying the format of the result data as well as the OEMDLLCOM object to process the result data.

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

[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

