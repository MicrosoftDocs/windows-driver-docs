---
title: KSEVENT\_DEVICE\_PREEMPTED
description: The KSEVENT\_DEVICE\_PREEMPTED event is triggered when a device has been preempted.
keywords: ["KSEVENT_DEVICE_PREEMPTED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_DEVICE_PREEMPTED
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_DEVICE\_PREEMPTED


The **KSEVENT\_DEVICE\_PREEMPTED** event is triggered when a device has been preempted.

## <span id="ddk_ksevent_vidcap_auto_update_ks"></span><span id="DDK_KSEVENT_VIDCAP_AUTO_UPDATE_KS"></span>


### <span id="usage_summary_table"></span><span id="USAGE_SUMMARY_TABLE"></span>Usage Summary Table

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
<th>Get</th>
<th>Set</th>
<th>Target</th>
<th>Event descriptor type</th>
<th>Event value type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>No</p></td>
<td><p>Yes</p></td>
<td><p>Filter</p></td>
<td><p><a href="/previous-versions/ff561744(v=vs.85)" data-raw-source="[&lt;strong&gt;KSEVENT&lt;/strong&gt;](/previous-versions/ff561744(v=vs.85))"><strong>KSEVENT</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

## Remarks

A preemption event is triggered in the following scenario.

1.  Initially only one camera is attached to the system, and a Windows app is streaming video from the camera.
2.  A second Windows app requests that the capture stack preempt the device from the first app and give control to the second app.
3.  When this request is issued, the driver sends the **KSEVENT\_DEVICE\_PREEMPTED** event to both Windows apps.

## See also


[**KSEVENT\_DEVICE**](/windows-hardware/drivers/ddi/ks/ne-ks-ksevent_device)

[**KSEVENT\_DEVICE\_LOST**](ksevent-device-lost.md)

