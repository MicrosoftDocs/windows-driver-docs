---
title: KSEVENT_VIDCAP_AUTO_UPDATE
description: The KSEVENT_VIDCAP_AUTO_UPDATE event is triggered when a property value changes.
keywords: ["KSEVENT_VIDCAP_AUTO_UPDATE Streaming Media Devices"]
topic_type:
- apiref
api_name:
- KSEVENT_VIDCAP_AUTO_UPDATE
api_type:
- NA
ms.date: 10/11/2021
---

# KSEVENT_VIDCAP_AUTO_UPDATE

The **KSEVENT_VIDCAP_AUTO_UPDATE** event is triggered when a property value changes.

## Usage Summary Table

| Get | Set | Target | Event descriptor type | Event value type |
|--|--|--|--|--|
| No | Yes | Filter | [**KSEVENT**](/windows-hardware/drivers/stream/ksevent-structure) | [**KSEVENTDATA**](/windows-hardware/drivers/ddi/ks/ns-ks-kseventdata) |

## Remarks

Clients might register for this event to be notified if a user flips a switch on the device, changing a property value. For this event to be available, the hardware implementation must provide support for this feature.

For more information about DirectShow filters and KsProxy see [Kernel Streaming Proxy](/windows-hardware/drivers/ddi/_stream/index).
