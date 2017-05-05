---
title: Pin-Centric Processing
author: windows-driver-content
description: Pin-Centric Processing
ms.assetid: 0b6a02c2-e672-4568-a890-491c721ec3a7
keywords:
- pin-centric filters WDK AVStream
- AVStream pin-centric filters WDK
- filter types WDK AVStream
- AVStrMiniPinProcess
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Pin-Centric Processing


## <a href="" id="ddk-pin-centric-processing-ksg"></a>


When writing an AVStream minidriver, you provide filters that use one of two processing paradigms: pin-centric processing or [filter-centric processing](filter-centric-processing.md).

Pin-centric processing means that AVStream calls the minidriver's pin process dispatch routine when new frames arrive in the pin queue.

Filter-centric processing means that AVStream calls the minidriver's filter process dispatch routine when there are data frames available on each instantiated pin. Note that these definitions specify default behavior; minidrivers can modify the default behavior by setting flags in the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

In general, software filters use filter-centric processing and hardware filters use pin-centric processing. For instance, hardware that transforms or renders data could route data on a pin-centric filter. There are rare cases in which these roles may be reversed.

To supply a pin-centric filter, the minidriver provides a pointer to an *AVStrMiniPinProcess* callback routine in each [**KSPIN\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff563535) structure; do not supply a processing dispatch in the [**KSFILTER\_DISPATCH**](https://msdn.microsoft.com/library/windows/hardware/ff562554) structure.

If the minidriver does not modify flag settings in the KSPIN\_DESCRIPTOR\_EX structure, AVStream calls the vendor-supplied [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) callback routine in three situations:

-   The pin transitions into the minimum processing state. Frames must already exist in the queue, and the pin must transition from less than the minimum processing state into at least the minimum processing state.

-   New frames arrive. The pin must be in at least the minimum processing state and there must be no frames at or ahead of the leading edge.

-   Minidriver explicitly calls [**KsPinAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff563494).

By default, pause is the minimum processing state.

In addition, AVStream does not call the pin process dispatch if the pin's AND gate is closed. If you use the **KSGATE***Xxx* routines to add additional off inputs to the pin's AND gate, for instance, your process dispatch will not be called.

When AVStream calls *AVStrMiniPinProcess*, it provides a pointer to the pin object that has available data. The minidriver's processing dispatch can then acquire a [leading edge pointer](leading-and-trailing-edge-stream-pointers.md) by calling [**KsPinGetLeadingEdgeStreamPointer**](https://msdn.microsoft.com/library/windows/hardware/ff563513). Minidrivers then manipulate stream data using the [stream pointer](stream-pointers.md) API.

Minidrivers that use pin-centric processing can modify when AVStream calls the *AVStrMiniPinProcess* dispatch by setting flags in the relevant [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure. Flag descriptions on the KSPIN\_DESCRIPTOR\_EX reference page are particularly relevant to vendors who are implementing pin-centric filters.

Processing attempts may fail if the minidriver is holding the [processing mutex](processing-mutex-in-avstream.md) through [**KsPinAcquireProcessingMutex**](https://msdn.microsoft.com/library/windows/hardware/ff563488). Problems may also arise if the minidriver directly manipulates a gate by using the **KSGATE***\** calls.

The [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083) in the MSDN Code Gallery is a pin-centric capture driver for a simulated piece of hardware. The Avshws sample shows how to implement [DMA through AVStream](avstream-dma-services.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Pin-Centric%20Processing%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


