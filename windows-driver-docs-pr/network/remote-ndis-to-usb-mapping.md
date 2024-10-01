---
title: Remote NDIS To USB Mapping Overview
description: A USB Remote NDIS device is implemented as a USB Communication Device Class (CDC) device with two interfaces.
ms.date: 09/27/2024
---

# Remote NDIS To USB Mapping overview

A USB Remote NDIS device is implemented as a USB Communication Device Class (CDC) device with two interfaces. A Communication Class interface, of type Abstract Control, and a Data Class interface combine to form a single functional unit representing the USB Remote NDIS device. The Communication Class interface includes a single endpoint for event notification and uses the shared bidirectional Control endpoint for control messages. The Data Class interface includes two bulk endpoints for data traffic.

>[!NOTE]
> An understanding of the Universal Serial Bus (USB) Specification versions 1.1 and 2.0 is required. The USB Communication Device Class (CDC) Specifications are suggested as references. These documents can be found at https://www.usb.org.


This section includes the following topics:

[USB-Level Initialization](usb-level-initialization.md)

[USB-Level Termination](usb-level-termination.md)

[Control Channel Characteristics](control-channel-characteristics.md)

[Data Channel Characteristics](data-channel-characteristics.md)

[Power Management](power-management.md)

[Timer Constants](timer-constants.md)

[USB 802.3 Device Sample](usb-802-3-device-sample.md)

 

 





