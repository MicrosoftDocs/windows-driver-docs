---
title: KSPROPERTY\_TELEPHONY\_CALLCONTROL
description: The KSPROPERTY\_TELEPHONY\_CALLCONTROL property is used to start and terminate a phone call.
ms.assetid: AAC2A218-9A2D-4EFE-B609-5078028B2426
keywords: ["KSPROPERTY_TELEPHONY_CALLCONTROL Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_CALLCONTROL
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TELEPHONY\_CALLCONTROL


The KSPROPERTY\_TELEPHONY\_CALLCONTROL property is used to start and terminate a phone call.

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
<td align="left"><p>No</p></td>
<td align="left"><p>Yes</p></td>
<td align="left"><p>Filter</p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff564262" data-raw-source="[&lt;strong&gt;KSPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff564262)"><strong>KSPROPERTY</strong></a></p></td>
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/mt169883" data-raw-source="[&lt;strong&gt;KSTELEPHONY_CALLCONTROL&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt169883)"><strong>KSTELEPHONY_CALLCONTROL</strong></a></p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_TELEPHONY\_CALLCONTROL property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

KSPROPERTY\_TELEPHONY\_CALLCONTROL contains information about CallType and CallControlOp.

TELEPHONY\_CALLCONTROLOP\_ENABLE will start cellular call from audio driver perspective, update jack state for associated cellular bidi endpoint to active, save call type and update the call state to Enabled.

TELEPHONY\_CALLCONTROLOP\_DISABLE will terminate cellular call from audio driver perspective, update jack state for associated cellular bidi endpoint to unplugged and update call state to Disabled. Call type is ignored in this case.

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

 

 





