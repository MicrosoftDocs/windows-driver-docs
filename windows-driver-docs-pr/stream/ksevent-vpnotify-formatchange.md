---
title: KSEVENT_VPNOTIFY_FORMATCHANGE
description: The KSEVENT_VPNOTIFY_FORMATCHANGE event is used to propagate an event, such as a video-format change, from the kernel-mode DVD decoder minidriver to DirectShow in user-mode.
keywords: ["KSEVENT_VPNOTIFY_FORMATCHANGE Streaming Media Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- KSEVENT_VPNOTIFY_FORMATCHANGE
api_type:
- NA
ms.date: 10/11/2021
---

# KSEVENT_VPNOTIFY_FORMATCHANGE

The **KSEVENT_VPNOTIFY_FORMATCHANGE** event is used to propagate an event, such as a video-format change, from the kernel-mode DVD decoder minidriver to DirectShow in user-mode.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Pin | [**KSE_NODE**](/windows-hardware/drivers/ddi/ks/ns-ks-kse_node) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

The minidriver can detect a change in the video-format, for example a resolution change from 640x480 to 720x480. User-mode components must be notified of this format change so that the necessary actions can take place between DirectShow filters and KsProxy.

KsProxy's VPE filter passes a user-mode event handle (created using the Win32 API CreateEvent) via this event to the minidriver, which must save the event handle.

The minidriver later sets this event handle to notify the KsProxy VPE filter, which renegotiates the connection based on the new video format.

The KsProxy VPE filter disables the event notification by sending the IOCTL_KS_DISABLE_EVENT I/O control code with the same event handle. The event handle is then closed by the VPE filter. The minidriver must not close the event handle.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index). For more information about handling stream changes, such as a video resolution change, see [Stream Changes](./stream-changes.md).
