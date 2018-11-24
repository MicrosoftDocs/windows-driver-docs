---
title: KSPROPERTY\_AEC\_MODE
description: The KSPROPERTY\_AEC\_MODE property is used to control an AEC node's mode of operation. This is an optional property of an AEC node (KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL).
ms.assetid: 79f0d655-4764-454f-8867-6cf1b5cedc82
keywords: ["KSPROPERTY_AEC_MODE Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AEC_MODE
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AEC\_MODE


The KSPROPERTY\_AEC\_MODE property is used to control an AEC node's mode of operation. This is an optional property of an AEC node ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)).

## <span id="ddk_ksproperty_aec_mode_ks"></span><span id="DDK_KSPROPERTY_AEC_MODE_KS"></span>


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
<td align="left"><p>Pin</p></td>
<td align="left"><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG and can be set to one of the following mode constants from header file Ksmedia.h:

-   AEC\_MODE\_PASS\_THROUGH

    In pass-through mode, the AEC node allows capture and render data to simply pass through the node without being modified.

-   AEC\_MODE\_HALF\_DUPLEX

    The AEC algorithm is running in half-duplex mode, which is similar in operation to a speaker phone. In this mode, the speaker volume is muted whenever the local person's speech has a higher volume level than the remote person's.

-   AEC\_MODE\_FULL\_DUPLEX

    The AEC algorithm is running in full-duplex mode.

Pass-through mode is the default. When the filter containing the AEC node is created or the node is reset, the node is initially configured to operate in pass-through mode.

In the initial release of Windows XP, the AEC algorithm that the [AEC system filter](https://msdn.microsoft.com/library/windows/hardware/ff536174) uses does not support the half-duplex mode.

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AEC\_MODE property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Requirements
------------

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


[**KSNODEPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff537143)

[**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)

 

 






