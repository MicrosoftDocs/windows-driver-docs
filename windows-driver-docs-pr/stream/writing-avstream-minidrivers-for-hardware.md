---
title: Writing AVStream Minidrivers for Hardware
description: Writing AVStream Minidrivers for Hardware
ms.assetid: d7dc42d7-efd0-41ff-abab-d97c508a41e6
keywords:
- AVStream WDK , hardware
- hardware WDK AVStream
- AVStrMiniDeviceStart
- filter graphs WDK AVStream
- graphs WDK AVStream
- interference between graphs WDK AVStream
- encoding WDK AVStream
- decoding WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Writing AVStream Minidrivers for Hardware





In the vendor-supplied [*AVStrMiniDeviceStart*](https://msdn.microsoft.com/library/windows/hardware/ff556297), AVStream minidrivers that support hardware should first parse the resource list and then call [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) to register an interrupt service routine (ISR).

Additional steps are required if your driver supports direct memory access (DMA). If your driver implements DMA, see [AVStream DMA Services](avstream-dma-services.md).

If more than one application might build a filter graph simultaneously using your device, you must take care to prevent interference between graphs. Specifically, if you construct a graph in an application using the device, you must not interfere with an application which is using the device in a non-stop state.

You can avoid interference by loading microcode after the graph transitions into KSSTATE\_ACQUIRE. This will protect a currently running graph because a new graph will not transition into **KSSTATE\_ACQUIRE** while another graph is currently running. To receive notification of pin state changes, supply an [*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359) callback routine in the [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure.

To minimize graph start-up time, however, you may want to load microcode before the graph reaches KSSTATE\_ACQUIRE. In this case, consider loading microcode in a low priority background thread during boot. This solution does not interfere with other applications, reduces graph start time, and should not lengthen boot time if done asynchronously.

After boot, however, do not reload microcode or manipulate hardware registers until the graph reaches KSSTATE\_ACQUIRE.

To see how connection of a new graph can interfere with a running graph, consider a video capture device that supports encoding and decoding, but only performs one of these tasks at a time. The minidriver exposes an encode filter and a decode filter.

An application builds a filter graph containing the encode filter. The minidriver loads microcode for encoding at pin connection time. The filter graph starts and the hardware begins encoding.

While the hardware is encoding, another application places a decode filter in a filter graph. When the decode pins are connected, *before the pins change state into KSSTATE\_ACQUIRE*, the minidriver attempts to configure the hardware for decoding. This reconfiguration interferes with the currently active encode graph and may result in a driver instability.

 

 




