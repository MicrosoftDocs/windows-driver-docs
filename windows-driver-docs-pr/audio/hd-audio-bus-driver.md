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
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

During device enumeration, the HD Audio bus driver detects the codecs that are attached to the HD Audio controller's HD Audio Link. For each codec, the bus driver loads one function driver (if available) for each function group that it finds within the codec. For information about function groups, see the Intel High Definition Audio Specification at the [Intel HD Audio](http://go.microsoft.com/fwlink/p/?linkid=42508) website.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20HD%20Audio%20Bus%20Driver%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


