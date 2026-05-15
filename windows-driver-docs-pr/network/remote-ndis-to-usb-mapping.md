---
title: Remote NDIS To USB Mapping Overview
description: Learn how USB remote NDIS devices use CDC interfaces for communication and data transfer. Explore setup, control, and data flow.
ms.date: 07/08/2025
ms.topic: concept-article
---

# Remote NDIS To USB mapping overview

A USB Remote NDIS device uses the USB Communication Device Class (CDC) with two interfaces. The Communication Class interface, which is Abstract Control, and the Data Class interface work together as a single unit that represents the USB Remote NDIS device. The Communication Class interface has one endpoint for event notification and uses the shared bidirectional control endpoint for control messages. The Data Class interface has two bulk endpoints for data traffic.

>[!NOTE]
> You need to know the Universal Serial Bus (USB) Specification versions 1.1 and 2.0. For reference, see the USB Communication Device Class (CDC) Specifications at https://www.usb.org/documents.


This section covers:

[USB-level initialization](usb-level-initialization.md)

[USB-level termination](usb-level-termination.md)

[Control channel characteristics](control-channel-characteristics.md)

[Data channel characteristics](data-channel-characteristics.md)

[Power management](power-management.md)

[Timer constants](timer-constants.md)

[USB 802.3 device sample](usb-802-3-device-sample.md)






