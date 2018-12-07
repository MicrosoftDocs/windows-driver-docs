---
title: KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE
description: The KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE property is used to communicate to the audio driver that single-radio voice call continuity (SRVCC) is beginning or ending.
ms.assetid: 9CEDAFE7-014F-4670-958D-6D3687D2D24A
keywords: ["KSPROPERTY_TELEPHONY_PROVIDERCHANGE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_TELEPHONY_PROVIDERCHANGE
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE


The **KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE** property is used to communicate to the audio driver that single-radio voice call continuity (SRVCC) is beginning or ending.

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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/mt169885" data-raw-source="[&lt;strong&gt;KSTELEPHONY_PROVIDERCHANGE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/mt169885)"><strong>KSTELEPHONY_PROVIDERCHANGE</strong></a></p></td>
</tr>
</tbody>
</table>

 

The property value is of type [**KSTELEPHONY\_PROVIDERCHANGE**](https://msdn.microsoft.com/library/windows/hardware/mt169885), which specifies the phone call type and the type of provider change operation.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A **KSPROPERTY\_TELEPHONY\_PROVIDERCHANGE** property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The audio stack uses the [**KSTELEPHONY\_PROVIDERCHANGE**](https://msdn.microsoft.com/library/windows/hardware/mt169885) property to indicate the start and the end of SRVCC to the audio driver. This property communicates the call type (LTE packet-switched, WLAN packet-switched, or circuit-switched) and the provider change operation (begin, end, or cancel) to driver. The call type is ignored when the provider operation is for ending the SRVCC.

When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_BEGIN**, the driver updates that provider’s call state to **TELEPHONY\_CALLSTATE\_PROVIDERTRANSITION**. When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_END**, the driver updates that provider’s call state to **TELEPHONY\_CALLSTATE\_ENABLED**. During SRVCC, the driver must continue to use the associated [**KSNODETYPE\_TELEPHONY\_BIDI**](ksnodetype-telephony-bidi.md) endpoint, and it does not change the jack states of this endpoint. When the provider change operation is **TELEPHONY\_PROVIDERCHANGEOP\_CANCEL**, SRVCC is being canceled, and the driver should revert back to a pre-SRVCC call.

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

 

 





