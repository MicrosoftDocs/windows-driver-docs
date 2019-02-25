---
title: HD Audio Bus Driver
description: HD Audio Bus Driver
ms.assetid: a08f4304-467b-45cf-8026-87f41b408692
keywords:
- HD Audio, Universal Audio Architecture
- High Definition Audio (HD Audio), Universal Audio Architecture
- UAA WDK
- Universal Audio Architecture WDK
- bus drivers WDK audio
- HD Audio, bus driver
- High Definition Audio (HD Audio), bus driver
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HD Audio Bus Driver


The HD Audio bus driver is the only software component that directly accesses the hardware registers of the HD Audio bus interface controller. The bus driver exposes the HD Audio DDI that its children--instances of the function drivers that control the audio and modem codecs--can use to program the HD Audio controller hardware. In addition, the bus driver manages the HD Audio Link hardware resources, which include the DMA engines and bus bandwidth. Function drivers allocate and free these resources through the HD Audio DDI.

The HD Audio bus driver:

-   Queries the codecs on the bus and creates children to manage the codecs.

-   Handles interrupt service routines (ISRs) for unsolicited responses and propagates the unsolicited responses to its children.

-   Passes commands from its children to the codecs and retrieves responses from the codecs.

-   Sets up the DMA engines that transfer data to or from the cyclic buffers.

-   Manages bus bandwidth resources on the HD Audio Link.

-   Provides access to the wall clock register and link position registers.

-   Provides synchronized starting and stopping of groups of streams.

The HD Audio bus driver does not provide:

-   An interface for programming a DSP or additional registers that are not defined in the Intel High Definition Audio Specification.

-   Prioritized bandwidth management.

During device enumeration, the HD Audio bus driver detects the codecs that are attached to the HD Audio controller's HD Audio Link. For each codec, the bus driver loads one function driver (if available) for each function group that it finds within the codec. For information about function groups, see the Intel High Definition Audio Specification at the [Intel HD Audio](https://go.microsoft.com/fwlink/p/?linkid=42508) website.

 

 




