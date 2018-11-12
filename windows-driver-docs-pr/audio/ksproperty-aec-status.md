---
title: KSPROPERTY\_AEC\_STATUS
description: The KSPROPERTY\_AEC\_STATUS property is used to monitor the status of an AEC node (KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL). This is an optional property of an AEC node.
ms.assetid: cd344367-1cb3-425a-8b22-300a85514e20
keywords: ["KSPROPERTY_AEC_STATUS Audio Devices"]
topic_type:
- apiref
api_name:
- KSPROPERTY_AEC_STATUS
api_location:
- Ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPERTY\_AEC\_STATUS


The KSPROPERTY\_AEC\_STATUS property is used to monitor the status of an AEC node ([**KSNODETYPE\_ACOUSTIC\_ECHO\_CANCEL**](ksnodetype-acoustic-echo-cancel.md)). This is an optional property of an AEC node.

## <span id="ddk_ksproperty_aec_status_ks"></span><span id="DDK_KSPROPERTY_AEC_STATUS_KS"></span>


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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff537143" data-raw-source="[&lt;strong&gt;KSNODEPROPERTY&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff537143)"><strong>KSNODEPROPERTY</strong></a></p></td>
<td align="left"><p>ULONG</p></td>
</tr>
</tbody>
</table>

 

The property value (operation data) is of type ULONG. This is a status value that can be set to the bitwise OR of one or more of the flag bits in the left column of the following table, which are defined in header file Ksmedia.h. The corresponding DSCFX\_AEC\_STATUS flags from header file Dsound.h are shown in the right column of the table. See the Microsoft Windows SDK documentation for information about these flags.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">AEC status flag</th>
<th align="left">Value</th>
<th align="left">DSCFX_AEC_STATUS flag</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>AEC_STATUS_FD_HISTORY_UNINITIALIZED</p></td>
<td align="left"><p>0x0</p></td>
<td align="left"><p>DSCFX_AEC_STATUS_HISTORY_UNINITIALIZED</p></td>
</tr>
<tr class="even">
<td align="left"><p>AEC_STATUS_FD_HISTORY_CONTINUOUSLY_CONVERGED</p></td>
<td align="left"><p>0x1</p></td>
<td align="left"><p>DSCFX_AEC_STATUS_HISTORY_CONTINUOUSLY_CONVERGED</p></td>
</tr>
<tr class="odd">
<td align="left"><p>AEC_STATUS_FD_HISTORY_PREVIOUSLY_DIVERGED</p></td>
<td align="left"><p>0x2</p></td>
<td align="left"><p>DSCFX_AEC_STATUS_HISTORY_PREVIOUSLY_DIVERGED</p></td>
</tr>
<tr class="even">
<td align="left"><p>AEC_STATUS_FD_CURRENTLY_CONVERGED</p></td>
<td align="left"><p>0x8</p></td>
<td align="left"><p>DSCFX_AEC_STATUS_CURRENTLY_CONVERGED</p></td>
</tr>
</tbody>
</table>

 

### <span id="Return_Value"></span><span id="return_value"></span><span id="RETURN_VALUE"></span>Return Value

A KSPROPERTY\_AEC\_STATUS property request returns STATUS\_SUCCESS to indicate that it has completed successfully. Otherwise, the request returns an appropriate error status code.

Remarks
-------

The three least significant bits in the AEC status flags (see preceding table) represent the convergence history (CH) of the AEC algorithm. The CH status bits can be used by a Microsoft DirectSound application to determine whether the algorithm has converged and also whether it has remained in the converged state since the time that it started processing data. Depending on the audio hardware, the AEC algorithm might fail to converge, in which case the resulting capture buffer is likely to include the echo from the speakers.

When the filter containing the AEC node is created or the node is reset, the AEC algorithm initially sets the three CH status bits to zero. This setting represents the uninitialized state, AEC\_STATUS\_FD\_HISTORY\_UNINITIALIZED.

After the AEC algorithm converges, the CH status switches to the converged state, AEC\_STATUS\_FD\_HISTORY\_CONTINUOUSLY\_CONVERGED. If the AEC algorithm ever loses convergence, the CH status switches to the diverged state, AEC\_STATUS\_FD\_HISTORY\_PREVIOUSLY\_DIVERGED. Although the status is most likely to switch to the diverged state from the converged state, it might also switch directly from the uninitialized state to the diverged state. After the CH status has switched to the diverged state, it will remain in that state until the algorithm is reset or starvation is detected.

When the [AEC system filter](https://msdn.microsoft.com/library/windows/hardware/ff536174) detects starvation at any of its four pins--capture in, capture out, render in, or render out--it resets its internal state, including the convergence history.

Note that bit 2 of the three CH status bits is not currently used.

As an alternative to using the CH status bits, the application can monitor the real-time convergence status by checking the AEC\_STATUS\_FD\_CURRENTLY\_CONVERGED flag bit. If this bit is set, the algorithm is currently converged. The algorithm can lose convergence temporarily when changes occur in the acoustic path. The real-time convergence flag is filtered to prevent such momentary losses from inappropriately switching the CH status bits to the DSCFX\_AEC\_STATUS\_FD\_HISTORY\_PREVIOUSLY\_DIVERGED state.

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

 

 






