---
title: UAA Class Drivers
description: UAA Class Drivers
ms.assetid: 57f8f6fe-53a9-4ef1-b4f6-715232e88fdf
keywords:
- HD Audio, Universal Audio Architecture
- High Definition Audio (HD Audio), Universal Audio Architecture
- UAA WDK
- Universal Audio Architecture WDK
- class drivers WDK audio
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# UAA Class Drivers


In Windows Vista, Microsoft provides UAA class drivers for audio devices that connect to either an internal bus (PCI) or an external bus (IEEE 1394 or USB). To be supported by the UAA class driver for a particular bus, a device must conform to the UAA hardware specifications for that bus. For a device on an internal bus, the UAA hardware requirements document specifies the following:

-   The HD Audio controller's register set with the minor changes that are discussed in [UAA Extensions to the HD Audio Architecture](uaa-extensions-to-the-hd-audio-architecture.md).

-   The requirements for the HD Audio codec (to be published).

For information about the requirements for UAA devices on external buses or information about UAA class drivers, see the white paper titled *Universal Audio Architecture* at the [audio technology](https://go.microsoft.com/fwlink/p/?linkid=8751) website.

The remainder of this discussion refers only to the version of the UAA class driver that controls an audio device that connects to an internal bus, implements the HD Audio hardware registers, and controls a UAA-compliant HD Audio codec. This class driver is a child of the HD Audio bus driver and uses the bus driver's baseline HD Audio DDI to program the UAA-compliant hardware.

The UAA class driver for the HD Audio codec:

-   Provides the system with a device interface for an audio codec or codecs.

-   Collects information about the digital-to-audio converters, audio-to-digital converters, and jack-presence detection pins in the codecs that are present on the HD Audio Link.

-   Initializes the audio codec or codecs with third-party commands on startup.

-   Gets and sets audio properties in the audio codecs.

-   Provides a streaming interface (mapping a stream's cyclic buffer to user mode, setting up the codec and DMA engine, and handling properties such as link position).

-   Handles power management in the audio codecs.

This class driver does not provide:

-   A way of dynamically programming audio effects nodes in the codecs.

-   Combining functions across two or more codecs to form an aggregate audio or modem device.

-   Handling of general-purpose I/O (GPIO) pins on widgets unless they are explicitly defined in the UAA hardware requirements document.

-   A plug-in model for third-party code for either programming the codecs or providing software effects.

 

 




