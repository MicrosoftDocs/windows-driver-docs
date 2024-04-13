---
title: USB Client Drivers for Media-Agnostic (MA-USB)
description: USB device driver that sends MA-USB packets.
ms.date: 01/17/2024
---

# USB client drivers for media-agnostic (MA-USB)

> [!NOTE]
> Media-agnostic USB is not supported by Windows and is intended for evaluation only.

In Windows 10, version 1709, USB driver stack can send USB packets over non-USB physical mediums such as Wi-Fi by using the media-agnostic USB (MA-USB) protocol. The new feature has been designed in a way that the changes required to existing USB client drivers are minimal. That set of changes include additional information about the transport:

- For devices with isochronous/streaming endpoints, the client driver needs to know the delays associated with transfer programming and transfer completion so that the driver can make sure that the device gets the isochronous packets on time.

- The client driver can use that information to optimize their higher layer selection of protocols. For example, a display driver can use the  latency and bandwidth information to choose the best codecs and buffering schemes. Because those characteristics might change dynamically, the driver needs to determine the changes.
