---
title: Writing AVStream Minidrivers for Hardware
author: windows-driver-content
description: Writing AVStream Minidrivers for Hardware
ms.assetid: d7dc42d7-efd0-41ff-abab-d97c508a41e6
keywords: ["AVStream WDK , hardware", "hardware WDK AVStream", "AVStrMiniDeviceStart", "filter graphs WDK AVStream", "graphs WDK AVStream", "interference between graphs WDK AVStream", "encoding WDK AVStream", "decoding WDK AVStream"]
---

# Writing AVStream Minidrivers for Hardware


## <a href="" id="ddk-writing-avstream-minidrivers-for-hardware-ksg"></a>


In the vendor-supplied [*AVStrMiniDeviceStart*](https://msdn.microsoft.com/library/windows/hardware/ff556297), AVStream minidrivers that support hardware should first parse the resource list and then call [**IoConnectInterrupt**](https://msdn.microsoft.com/library/windows/hardware/ff548371) to register an interrupt service routine (ISR).

Additional steps are required if your driver supports direct memory access (DMA). If your driver implements DMA, see [AVStream DMA Services](avstream-dma-services.md).

If more than one application might build a filter graph simultaneously using your device, you must take care to prevent interference between graphs. Specifically, if you construct a graph in an application using the device, you must not interfere with an application which is using the device in a non-stop state.

You can avoid interference by loading microcode after the graph transitions into KSSTATE\_ACQUIRE. This will protect a currently running graph because a new graph will not transition into **KSSTATE\_ACQUIRE** while another graph is currently running. To receive notification of pin state changes, supply an [*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359) callback routine in the [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure.

To minimize graph start-up time, however, you may want to load microcode before the graph reaches KSSTATE\_ACQUIRE. In this case, consider loading microcode in a low priority background thread during boot. This solution does not interfere with other applications, reduces graph start time, and should not lengthen boot time if done asynchronously.

After boot, however, do not reload microcode or manipulate hardware registers until the graph reaches KSSTATE\_ACQUIRE.

To see how connection of a new graph can interfere with a running graph, consider a video capture device that supports encoding and decoding, but only performs one of these tasks at a time. The minidriver exposes an encode filter and a decode filter.

An application builds a filter graph containing the encode filter. The minidriver loads microcode for encoding at pin connection time. The filter graph starts and the hardware begins encoding.

While the hardware is encoding, another application places a decode filter in a filter graph. When the decode pins are connected, *before the pins change state into KSSTATE\_ACQUIRE*, the minidriver attempts to configure the hardware for decoding. This reconfiguration interferes with the currently active encode graph and may result in a driver instability.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Writing%20AVStream%20Minidrivers%20for%20Hardware%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


