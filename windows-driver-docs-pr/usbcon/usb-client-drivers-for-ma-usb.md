---
title: USB Client Drivers for Media-Agnostic (MA-USB)
description: Media-agnostic USB (MA-USB) is deprecated and will be removed in a future Windows release.
ms.date: 08/12/2026
ms.topic: concept-article
ai-usage: ai-assisted
---

# USB client drivers for media-agnostic (MA-USB)

> [!IMPORTANT]
> Media-agnostic USB (MA-USB) is deprecated. It has never been supported by Windows and was provided for evaluation only. The MA-USB host driver (`mausbhost`) and IP transport driver (`mausbip`) are no longer supported and will be removed in a future release of Windows. New designs must not take a dependency on MA-USB.

In Windows 10, version 1709, USB driver stack can send USB packets over non-USB physical mediums such as Wi-Fi by using the media-agnostic USB (MA-USB) protocol. The new feature has been designed in a way that the changes required to existing USB client drivers are minimal. That set of changes include additional information about the transport:

- For devices with isochronous/streaming endpoints, the client driver needs to know the delays associated with transfer programming and transfer completion so that the driver can make sure that the device gets the isochronous packets on time.

- The client driver can use that information to optimize their higher layer selection of protocols. For example, a display driver can use the  latency and bandwidth information to choose the best codecs and buffering schemes. Because those characteristics might change dynamically, the driver needs to determine the changes.
