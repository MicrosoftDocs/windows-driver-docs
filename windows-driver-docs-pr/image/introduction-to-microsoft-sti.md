---
title: Introduction to Microsoft STI
description: Introduction to Microsoft STI
ms.assetid: b329dbbc-28c5-47df-9ced-33180415b7c6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Introduction to Microsoft STI





Microsoft STI is made up of the following primary components:

-   A [Still Image Event Monitor](overview-of-sti-components.md#ddk-still-image-event-monitor-si), which monitors all installed still image devices and receives notification when [Still Image Device Events](still-image-device-events.md) occur. An event typically indicates that a device is ready to transmit image data. The event monitor also keeps track of all registered applications and can start an application when an event is detected.

-   A set of vendor-supplied, [User-Mode Still Image Minidrivers](overview-of-sti-components.md#ddk-user-mode-still-image-minidrivers-si) that can detect device activity and notify the still image event monitor of that activity through still image device events. These minidrivers also pass image data from kernel-mode drivers to upper level software.

-   A [Scanners and Cameras Control Panel](overview-of-sti-components.md#ddk-scanners-and-cameras-control-panel-si), which allows users to assign specific still image device events to specific applications. In this way, the event monitor will know which application to start when it detects an event. Control Panel also lets users test still image devices.

An [Imaging Application](overview-of-sti-components.md#ddk-imaging-application-si) can register itself as *push-model aware*, meaning it can be activated by the Event Monitor when a still image device is ready to transmit an image.

Imaging applications typically read image data streams by calling a high-level [Image Acquisition API](overview-of-sti-components.md#ddk-image-acquisition-api-si), such as TWAIN. Device-specific subcomponents of the image acquisition API, such as TWAIN data sources, use an interface into the user-mode still image minidrivers to perform I/O operations.

Microsoft STI defines several [Still Image COM Interfaces](still-image-com-interfaces.md) that allow STI components to communicate with each other.

The next section provides more information about these and other [Microsoft STI Components](microsoft-sti-components.md).

 

 




