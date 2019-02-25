---
title: KSPROPERTY\_TELEPHONY\_CALLHOLD
description: The KSPROPERTY\_TELEPHONY\_CALLHOLD property is used to control the hold state of a phone call.
ms.assetid: C683A6AA-35E5-43D3-B882-B13B8A0A4043
keywords: ["KSPROPERTY_TELEPHONY_CALLHOLD Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_CALLHOLD
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TELEPHONY\_CALLHOLD


The **KSPROPERTY\_TELEPHONY\_CALLHOLD** property is used to control the hold state of a phone call.

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
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p>BOOL</p></td>
</tr>
</tbody>
</table>

 

The property value is of type BOOL and specifies whether the phone call is on hold.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_CALLHOLD** property request returns **TRUE** if the call in on hold; otherwise, it returns **FALSE**.

Remarks
-------

If you set the **KSPROPERTY\_TELEPHONY\_CALLHOLD** property with a value of **TRUE**, the phone call will be placed on hold. The expected behavior is that both transmission and reception will be muted. No data will be sent or received in this case. The audio driver will update the call state ([**TELEPHONY\_CALLSTATE**](https://msdn.microsoft.com/library/windows/hardware/mt169896)) to **TELEPHONY\_CALLSTATE\_HOLD**. If you set the **KSPROPERTY\_TELEPHONY\_CALLHOLD** property with a value of **FALSE**, the phone call will be taken off of hold state, and the call state will be updated to **TELEPHONY\_CALLSTATE\_ENABLED**.

Requirements
------------

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
<td align="left"><p>None supported</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Client</p></td>
<td align="left"><p>Windows 10 Mobile</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 





