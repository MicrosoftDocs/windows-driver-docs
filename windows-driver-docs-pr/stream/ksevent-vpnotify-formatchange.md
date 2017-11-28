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
<td><p>[<strong>KSE_NODE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561937)</p></td>
<td><p>[<strong>KSEVENTDATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561750)</p></td>
</tr>
</tbody>
</table>

 

The minidriver can detect a change in the video-format, for example a resolution change from 640x480 to 720x480. User-mode components must be notified of this format change so that the necessary actions can take place between DirectShow filters and KsProxy.

KsProxy's VPE filter passes a user-mode event handle (created using the Win32 API CreateEvent) via this event to the minidriver, which must save the event handle.

The minidriver later sets this event handle to notify the KsProxy VPE filter, which renegotiates the connection based on the new video format.

The KsProxy VPE filter disables the event notification by sending the IOCTL\_KS\_DISABLE\_EVENT I/O control code with the same event handle. The event handle is then closed by the VPE filter. The minidriver must not close the event handle.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](https://msdn.microsoft.com/library/windows/hardware/ff560877). For more information about handling stream changes, such as a video resolution change, see [Stream Changes](https://msdn.microsoft.com/library/windows/hardware/ff568284).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSEVENT_VPNOTIFY_FORMATCHANGE%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




