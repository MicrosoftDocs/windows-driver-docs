---
title: KSEVENT\_VPNOTIFY\_FORMATCHANGE
description: The KSEVENT\_VPNOTIFY\_FORMATCHANGE event is used to propagate an event, such as a video-format change, from the kernel-mode DVD decoder minidriver to DirectShow in user-mode.
ms.assetid: 4c1757ec-1453-4aaa-b246-7c255e29310d
keywords: ["KSEVENT_VPNOTIFY_FORMATCHANGE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VPNOTIFY_FORMATCHANGE
api_type:
- NA
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSEVENT\_VPNOTIFY\_FORMATCHANGE


The KSEVENT\_VPNOTIFY\_FORMATCHANGE event is used to propagate an event, such as a video-format change, from the kernel-mode DVD decoder minidriver to DirectShow in user-mode.

## <span id="ddk_ksevent_vpnotify_formatchange_ks"></span><span id="DDK_KSEVENT_VPNOTIFY_FORMATCHANGE_KS"></span>


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
<td><p>Pin</p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561937" data-raw-source="[&lt;strong&gt;KSE_NODE&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561937)"><strong>KSE_NODE</strong></a></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561750" data-raw-source="[&lt;strong&gt;KSEVENTDATA&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff561750)"><strong>KSEVENTDATA</strong></a></p></td>
</tr>
</tbody>
</table>

 

The minidriver can detect a change in the video-format, for example a resolution change from 640x480 to 720x480. User-mode components must be notified of this format change so that the necessary actions can take place between DirectShow filters and KsProxy.

KsProxy's VPE filter passes a user-mode event handle (created using the Win32 API CreateEvent) via this event to the minidriver, which must save the event handle.

The minidriver later sets this event handle to notify the KsProxy VPE filter, which renegotiates the connection based on the new video format.

The KsProxy VPE filter disables the event notification by sending the IOCTL\_KS\_DISABLE\_EVENT I/O control code with the same event handle. The event handle is then closed by the VPE filter. The minidriver must not close the event handle.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877). For more information about handling stream changes, such as a video resolution change, see [Stream Changes](https://msdn.microsoft.com/library/windows/hardware/ff568284).

 

 





