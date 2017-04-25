---
title: Frame Injection
author: windows-driver-content
description: Frame Injection
ms.assetid: cdfb1763-92a8-4a60-8f49-2af34a8beca5
keywords:
- frames WDK AVStream
- injection mode WDK AVStream frames
- frame injection WDK AVStream
- pin-centric filters WDK AVStream
- filter-centric filters WDK AVStream
- empty frames WDK AVStream
- default frame behavior WDK AVStream
- overriding default frame behavior WDK streaming media
- circuits WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Frame Injection


## <a href="" id="ddk-frame-injection-ksg"></a>


By default in AVStream, a requester acquires empty frames from an allocator and places them in a queue. The minidriver then fills frames either by [pin-centric processing](pin-centric-processing.md) or [filter-centric processing](filter-centric-processing.md). The frames move across a transport to the next object in the circuit, eventually completing the circuit and returning to the requester. AVStream then reuses the frames.

Minidrivers can override this default behavior by using *injection mode*. In injection mode, the minidriver is responsible for placing frames into the circuit. Frames propagate around the circuit in the default manner. When the frames return to the AVStream object where they started, AVStream calls a minidriver-provided [*AVStrMiniFrameReturn*](https://msdn.microsoft.com/library/windows/hardware/ff556320) routine.

In this routine, the minidriver could for instance deallocate the frame, complete work pending on the return of the frame, or refill and reinject the frame.

To set injection mode, the minidriver calls [**KsPinRegisterFrameReturnCallback**](https://msdn.microsoft.com/library/windows/hardware/ff563522) and provides a pointer to its *AVStrMiniFrameReturn* routine.

*Do not call* ***KsPinRegisterFrameReturnCallback*** *unless the filter is in the stop state.*

To inject frames into the circuit, call [**KsPinSubmitFrame**](https://msdn.microsoft.com/library/windows/hardware/ff563529) or [**KsPinSubmitFrameMdl**](https://msdn.microsoft.com/library/windows/hardware/ff563530).

The diagram below shows an AVStream filter set composed of a source filter, an [*inplace*](https://msdn.microsoft.com/library/windows/hardware/ff556290#wdkgloss-inplace) transform filter, and a rendering filter with the source injecting frames.

![diagram illustrating an avstream filter set](images/inject1.png)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Frame%20Injection%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


