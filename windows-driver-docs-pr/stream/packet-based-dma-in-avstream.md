---
title: Packet-based DMA in AVStream
description: Packet-based DMA in AVStream
ms.assetid: 4246819e-d8d6-4302-9477-675ca181b1e3
keywords:
- AVStream WDK , hardware
- hardware WDK AVStream
- DMA services WDK AVStream
- Direct Memory Access WDK AVStream
- packet-based DMA WDK AVStream
- scatter/gather DMA WDK AVStream
- capture buffers WDK AVStream
- buffers WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Packet-based DMA in AVStream





Packet-based direct memory access (DMA) occurs when your minidriver reads data directly from and writes data directly to capture buffers received from user mode. The [AVStream Simulated Hardware Sample Driver (AVSHwS)](http://go.microsoft.com/fwlink/p/?linkid=256083) in the Windows Driver Kit samples demonstrates how to build an AVStream minidriver that performs this type of DMA.

To implement a packet-based DMA scheme:

1.  Specify KSPIN\_FLAG\_GENERATE\_MAPPINGS in the **Flags** member of relevant [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structures. Note that this flag should only be used by a bus master with scatter/gather support.

2.  Register an interrupt service routine (ISR) as described in [Writing AVStream Minidrivers for Hardware](writing-avstream-minidrivers-for-hardware.md).

Then in the [*AVStrMiniDeviceStart*](https://msdn.microsoft.com/library/windows/hardware/ff556297) start dispatch:

1.  Set up a DMA adapter object using [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220).

2.  Register the DMA adapter object with AVStream by calling [**KsDeviceRegisterAdapterObject**](https://msdn.microsoft.com/library/windows/hardware/ff561687).

The minidriver specifies the maximum size for a single scatter/gather mapping by providing a *MaxMappingByteCount* parameter in the call to [**KsDeviceRegisterAdapterObject**](https://msdn.microsoft.com/library/windows/hardware/ff561687).

If any scatter/gather mapping exceeds this maximum size, AVStream automatically breaks the mapping into several scatter/gather mappings, each of which is no larger than the size specified in *MaxMappingByteCount*.

You must also provide an [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) callback routine. The driver writer should choose appropriate functionality for this callback. As one example, you could do the following:

1.  Call [**KsPinGetLeadingEdgeStreamPointer**](https://msdn.microsoft.com/library/windows/hardware/ff563513).

2.  Clone the leading edge by calling [**KsStreamPointerClone**](https://msdn.microsoft.com/library/windows/hardware/ff567129).

3.  Program DMA hardware based on the clone.

4.  Call [**KsStreamPointerAdvanceOffsets**](https://msdn.microsoft.com/library/windows/hardware/ff567126) or [**KsStreamPointerAdvance**](https://msdn.microsoft.com/library/windows/hardware/ff567125) to advance the leading edge.

5.  Repeat from step 2 as needed for additional frames.

When the hardware interrupts for DMA completion, the kernel calls the ISR that the vendor has previously registered. In the ISR, the minidriver queues a deferred procedure call (DPC).

Your DPC should update **DataUsed** and possibly other members of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure. The DPC might then call [**KsStreamPointerDelete**](https://msdn.microsoft.com/library/windows/hardware/ff567130) to delete the clone and release the associated frame.

Alternatively, the DPC could advance the clone pointer if only part of the frame is completed. To do this, call [**KsStreamPointerAdvanceOffsets**](https://msdn.microsoft.com/library/windows/hardware/ff567126).

If necessary to resume processing, call [**KsPinAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff563494).

Note that if a mapping is less than one physical page in length, it is not guaranteed to reside on a single physical page.

 

 




