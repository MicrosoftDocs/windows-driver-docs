---
title: KSPROPERTY\_AC3\_LANGUAGE\_CODE
description: The KSPROPERTY\_AC3\_LANGUAGE\_CODE property specifies the language code of the AC-3-encoded stream.
keywords: ["KSPROPERTY_AC3_LANGUAGE_CODE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AC3_LANGUAGE_CODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AC3\_LANGUAGE\_CODE


The KSPROPERTY\_AC3\_LANGUAGE\_CODE property specifies the language code of the AC-3-encoded stream.

## <span id="ddk_ksproperty_ac3_language_code_ks"></span><span id="DDK_KSPROPERTY_AC3_LANGUAGE_CODE_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><p><a href="/previous-versions/ff564262(v=vs.85)" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](/previous-versions/ff564262(v=vs.85))"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="/previous-versions/windows/hardware/drivers/ff537081(v=vs.85)" data-raw-source="[&lt;strong&gt;KSAC3_LANGUAGE_CODE&lt;/strong&gt;](/previous-versions/windows/hardware/drivers/ff537081(v=vs.85))"><strong>KSAC3_LANGUAGE_CODE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is a KSAC3\_LANGUAGE\_CODE structure that specifies the language code.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AC3\_LANGUAGE\_CODE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h (include Ksmedia.h)</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**KSPROPERTY**](/previous-versions/ff564262(v=vs.85))

[**KSAC3\_LANGUAGE\_CODE**](/previous-versions/windows/hardware/drivers/ff537081(v=vs.85))

