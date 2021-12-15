---
title: KSEVENT_DEVICE_PREEMPTED
description: The KSEVENT_DEVICE_PREEMPTED event is triggered when a device has been preempted.
keywords: ["KSEVENT_DEVICE_PREEMPTED Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_DEVICE_PREEMPTED
api_type:
- NA
ms.date: 10/11/2021
---

# KSEVENT_DEVICE_PREEMPTED

The **KSEVENT_DEVICE_PREEMPTED** event is triggered when a device has been preempted.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Filter | [**KSEVENT**](/windows-hardware/drivers/stream/ksevent-structure) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

## Remarks

A preemption event is triggered in the following scenario.

1. Initially only one camera is attached to the system, and a Windows app is streaming video from the camera.

1. A second Windows app requests that the capture stack preempt the device from the first app and give control to the second app.

1. When this request is issued, the driver sends the **KSEVENT_DEVICE_PREEMPTED** event to both Windows apps.

## See also

[**KSEVENT_DEVICE**](/windows-hardware/drivers/ddi/ks/ne-ks-ksevent_device)

[**KSEVENT_DEVICE_LOST**](ksevent-device-lost.md)
