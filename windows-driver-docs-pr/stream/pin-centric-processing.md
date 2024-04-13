---
title: Pin-Centric Processing
description: Pin-centric processing
keywords:
- pin-centric filters WDK AVStream
- AVStream pin-centric filters WDK
- filter types WDK AVStream
- AVStrMiniPinProcess
ms.date: 06/18/2020
---

# Pin-centric processing

When writing an AVStream minidriver, you provide filters that use one of two processing paradigms: pin-centric processing or [filter-centric processing](filter-centric-processing.md).

Pin-centric processing means that AVStream calls the minidriver's pin process dispatch routine when new frames arrive in the pin queue.

Filter-centric processing means that AVStream calls the minidriver's filter process dispatch routine when there are data frames available on each instantiated pin. Note that these definitions specify default behavior; minidrivers can modify the default behavior by setting flags in the [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure.

In general, software filters use filter-centric processing and hardware filters use pin-centric processing. For instance, hardware that transforms or renders data could route data on a pin-centric filter. There are rare cases in which these roles may be reversed.

To supply a pin-centric filter, the minidriver provides a pointer to an *AVStrMiniPinProcess* callback routine in each [**KSPIN\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_dispatch) structure; do not supply a processing dispatch in the [**KSFILTER\_DISPATCH**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_dispatch) structure.

If the minidriver does not modify flag settings in the KSPIN\_DESCRIPTOR\_EX structure, AVStream calls the vendor-supplied [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin) callback routine in three situations:

- The pin transitions into the minimum processing state. Frames must already exist in the queue, and the pin must transition from less than the minimum processing state into at least the minimum processing state.

- New frames arrive. The pin must be in at least the minimum processing state and there must be no frames at or ahead of the leading edge.

- Minidriver explicitly calls [**KsPinAttemptProcessing**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinattemptprocessing).

By default, pause is the minimum processing state.

In addition, AVStream does not call the pin process dispatch if the pin's AND gate is closed. If you use the **KSGATE**_Xxx_ routines to add additional off inputs to the pin's AND gate, for instance, your process dispatch will not be called.

When AVStream calls *AVStrMiniPinProcess*, it provides a pointer to the pin object that has available data. The minidriver's processing dispatch can then acquire a [leading edge pointer](leading-and-trailing-edge-stream-pointers.md) by calling [**KsPinGetLeadingEdgeStreamPointer**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetleadingedgestreampointer). Minidrivers then manipulate stream data using the [stream pointer](stream-pointers.md) API.

Minidrivers that use pin-centric processing can modify when AVStream calls the *AVStrMiniPinProcess* dispatch by setting flags in the relevant [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure. Flag descriptions on the KSPIN\_DESCRIPTOR\_EX reference page are particularly relevant to vendors who are implementing pin-centric filters.

Processing attempts may fail if the minidriver is holding the [processing mutex](processing-mutex-in-avstream.md) through [**KsPinAcquireProcessingMutex**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinacquireprocessingmutex). Problems may also arise if the minidriver directly manipulates a gate by using the **KSGATE**_\*_ calls.

The [AVStream Simulated Hardware Sample Driver (AVSHwS)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) in the Windows Driver Kit samples is a pin-centric capture driver for a simulated piece of hardware. The Avshws sample shows how to implement [DMA through AVStream](avstream-dma-services.md).
