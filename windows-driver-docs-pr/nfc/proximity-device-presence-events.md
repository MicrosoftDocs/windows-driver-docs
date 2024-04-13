---
title: Proximity Device Presence Events
description: Proximity device presence events
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# Proximity device presence events

NFP providers enable clients to receive an event whenever an NFP provider detects the arrival or departure of a proximate device (the window of the triggering action). Whenever the NFP provider detects proximity, meaning that the provider can currently communicate with one or more proximate devices, the provider needs to issue a *DeviceArrived* event. When the NFP provider can no longer communicate with any proximate devices, it needs to issue a *DeviceDeparted* event.

The NFP provider also needs to track the presence of proximate devices in order to properly ensure that a published message is only transmitted once while a device is within proximity. These events should be based on the same metric. For an NFP provider that happens to be able to communicate with multiple proximate devices simultaneously, the presence events should be the aggregate of all presence. If the provider supports 0 to N simultaneously proximate devices, the events are only delivered on transitions from 0-to-1 and 1-to-0 currently proximate devices. Note that NFC does NOT support this.

## Related topics

- [Near field communications (NFC) API reference](/windows-hardware/drivers/ddi/_nfpdrivers/)
