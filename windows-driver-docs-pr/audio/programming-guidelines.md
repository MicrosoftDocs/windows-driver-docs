---
title: Programming Guidelines
description: Programming Guidelines
ms.assetid: 289bdf85-9138-4920-a61f-050c51077d3e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Programming Guidelines


This section presents programming guidelines for using the HD Audio DDI versions (as defined by the [**HDAUDIO\_BUS\_INTERFACE**](https://msdn.microsoft.com/library/windows/hardware/ff536413), [**HDAUDIO\_BUS\_INTERFACE\_V2**](https://msdn.microsoft.com/library/windows/hardware/ff536418) and [**HDAUDIO\_BUS\_INTERFACE\_BDL**](https://msdn.microsoft.com/library/windows/hardware/ff536416) structures) to control audio and modem codecs that are connected to an HD Audio bus interface controller.

The HD Audio bus driver exposes one or both versions of the HD Audio DDI to its children, which are kernel-mode function drivers for the audio and modem codecs. (One of these children might be the UAA HD Audio class driver.) These drivers call the routines in the DDIs to access the hardware capabilities of the HD Audio controller device.

This section includes:

[Differences Between the HD Audio DDI Versions](differences-between-the-hd-audio-ddi-versions.md)

[Synchronous and Asynchronous Codec Commands](synchronous-and-asynchronous-codec-commands.md)

[Wall Clock and Link Position Registers](wall-clock-and-link-position-registers.md)

[Hardware Resource Management](hardware-resource-management.md)

[Synchronizing Two or More Streams](synchronizing-two-or-more-streams.md)

[Wake Enable](wake-enable.md)

[Data Copying and Caching Policy](data-copying-and-caching-policy.md)

[Querying for an HD Audio DDI](querying-for-an-hd-audio-ddi.md)

 

 




