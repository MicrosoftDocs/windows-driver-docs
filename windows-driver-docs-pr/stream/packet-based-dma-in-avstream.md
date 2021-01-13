---
title: Packet-based DMA in AVStream
description: Packet-based DMA in AVStream
keywords:
- AVStream WDK , hardware
- hardware WDK AVStream
- DMA services WDK AVStream
- Direct Memory Access WDK AVStream
- packet-based DMA WDK AVStream
- scatter/gather DMA WDK AVStream
- capture buffers WDK AVStream
- buffers WDK AVStream
ms.date: 06/18/2020
ms.localizationpriority: medium
---

# Packet-based DMA in AVStream

Packet-based direct memory access (DMA) occurs when your minidriver reads data directly from and writes data directly to capture buffers received from user mode. The [AVStream Simulated Hardware Sample Driver (AVSHwS)](/samples/microsoft/windows-driver-samples/avstream-simulated-hardware-sample-driver-avshws/) in the Windows Driver Kit (WDK) samples demonstrates how to build an AVStream minidriver that performs this type of DMA.

To implement a packet-based DMA scheme:

1. Specify KSPIN\_FLAG\_GENERATE\_MAPPINGS in the **Flags** member of relevant [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structures. Note that this flag should only be used by a bus master with scatter/gather support.

1. Register an interrupt service routine (ISR) as described in [Writing AVStream Minidrivers for Hardware](writing-avstream-minidrivers-for-hardware.md).

Then in the [*AVStrMiniDeviceStart*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnksdevicepnpstart) start dispatch:

1. Set up a DMA adapter object using [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter).

1. Register the DMA adapter object with AVStream by calling [**KsDeviceRegisterAdapterObject**](/windows-hardware/drivers/ddi/ks/nf-ks-ksdeviceregisteradapterobject).

The minidriver specifies the maximum size for a single scatter/gather mapping by providing a *MaxMappingByteCount* parameter in the call to [**KsDeviceRegisterAdapterObject**](/windows-hardware/drivers/ddi/ks/nf-ks-ksdeviceregisteradapterobject).

If any scatter/gather mapping exceeds this maximum size, AVStream automatically breaks the mapping into several scatter/gather mappings, each of which is no larger than the size specified in *MaxMappingByteCount*.

You must also provide an [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin) callback routine. The driver writer should choose appropriate functionality for this callback. As one example, you could do the following:

1. Call [**KsPinGetLeadingEdgeStreamPointer**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetleadingedgestreampointer).

1. Clone the leading edge by calling [**KsStreamPointerClone**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerclone).

1. Program DMA hardware based on the clone.

1. Call [**KsStreamPointerAdvanceOffsets**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointeradvanceoffsets) or [**KsStreamPointerAdvance**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointeradvance) to advance the leading edge.

1. Repeat from step 2 as needed for additional frames.

When the hardware interrupts for DMA completion, the kernel calls the ISR that the vendor has previously registered. In the ISR, the minidriver queues a deferred procedure call (DPC).

Your DPC should update **DataUsed** and possibly other members of the [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header) structure. The DPC might then call [**KsStreamPointerDelete**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerdelete) to delete the clone and release the associated frame.

Alternatively, the DPC could advance the clone pointer if only part of the frame is completed. To do this, call [**KsStreamPointerAdvanceOffsets**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointeradvanceoffsets).

If necessary to resume processing, call [**KsPinAttemptProcessing**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinattemptprocessing).

> [!NOTE]
> If a mapping is less than one physical page in length, it is not guaranteed to reside on a single physical page.
