---
title: Introduction to Remote NDIS (RNDIS)
description: RNDIS is a bus-independent class specification for Ethernet (802.3) network devices on dynamic PnP buses.
keywords:
- Remote NDIS WDK networking
- network drivers WDK , Remote NDIS
- RNDIS
ms.date: 03/02/2023
---

# Introduction to Remote NDIS (RNDIS)





Remote NDIS (RNDIS) is a bus-independent class specification for Ethernet (802.3) network devices on dynamic Plug and Play (PnP) buses such as USB, 1394, Bluetooth, and InfiniBand. Remote NDIS defines a bus-independent message protocol between a host computer and a Remote NDIS device over abstract control and data channels. Remote NDIS is precise enough to allow vendor-independent class driver support for Remote NDIS devices on the host computer.

Microsoft Windows versions beginning with Windows XP include a Remote NDIS driver for USB devices. This NDIS miniport driver, Rndismp.sys, is implemented and maintained by Microsoft and is distributed as part of all supported Windows versions. You can find it in the %SystemRoot%\System32\drivers directory.

To use this driver with a USB device, an IHV must provide an INF file that follows the template in [Remote NDIS INF Template](remote-ndis-inf-template.md).

Remote NDIS messages are sent to a Remote NDIS device from the host, and a Remote NDIS device responds with an appropriate completion message. Messages are also sent in a unsolicited fashion from a Remote NDIS device to the host.

This section includes:

[Overview of Remote NDIS (RNDIS)](overview-of-remote-ndis--rndis-.md)

[Remote NDIS Communication](remote-ndis-communication.md)

[Remote NDIS To USB Mapping](remote-ndis-to-usb-mapping.md)


 

 
