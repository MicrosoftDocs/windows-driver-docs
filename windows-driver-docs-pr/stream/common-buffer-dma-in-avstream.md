---
title: Common Buffer DMA in AVStream
description: Common Buffer DMA in AVStream
keywords:
- common buffer DMA WDK AVStream
- buffers WDK AVStream
- AVStream WDK , hardware
- hardware WDK AVStream
- DMA services WDK AVStream
- Direct Memory Access WDK AVStream
ms.date: 04/20/2017
---

# Common Buffer DMA in AVStream





Common buffer direct memory access (DMA) occurs when the device does not write directly to the capture buffers; instead it copies data to and from a common buffer.

To use common buffer DMA in your AVStream minidriver:

1.  Acquire a DMA adapter by calling [**IoGetDmaAdapter**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetdmaadapter), as in packet-based DMA. Do not specify KSPIN\_FLAG\_GENERATE\_MAPPINGS in the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure, and do not register your DMA adapter with AVStream. You might need to implement your own private buffer/copy scheme.

2.  Register an interrupt service routine (ISR) as described in [Writing AVStream Minidrivers for Hardware](writing-avstream-minidrivers-for-hardware.md)

If the **Flags** member of KSPIN\_DESCRIPTOR\_EX sets KSPIN\_FLAG\_DO\_NOT\_INITIATE\_PROCESSING, the following steps take place before AVStream calls [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin):

1.  The minidriver sets up its common buffer transfers.

2.  The kernel calls the ISR that the vendor has previously registered. In the ISR, the minidriver queues a deferred procedure call (DPC).

3.  When the common buffer is full, the minidriver calls [**KsPinAttemptProcessing**](/windows-hardware/drivers/ddi/ks/nf-ks-kspinattemptprocessing) from the DPC.

4.  AVStream calls the process dispatch if conditions specified by the **Flags** member of [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) are met.

Within the vendor-supplied [*AVStrMiniPinProcess*](/windows-hardware/drivers/ddi/ks/nc-ks-pfnkspin) callback routine, one possible course of action is as follows:

1.  Call [**KsPinGetLeadingEdgeStreamPointer**](/windows-hardware/drivers/ddi/ks/nf-ks-kspingetleadingedgestreampointer):

    ```cpp
    KSSTREAM_POINTER *Leading = KsPinGetLeadingEdgeStreamPointer (
                    Pin,
                    State
                   );
    ```

2.  Copy frame data to Leading-&gt;StreamHeader-&gt;Data and set the necessary flags and time stamp information in the appropriate [**KSSTREAM\_HEADER**](/windows-hardware/drivers/ddi/ks/ns-ks-ksstream_header).

3.  Call [**KsStreamPointerUnlock**](/windows-hardware/drivers/ddi/ks/nf-ks-ksstreampointerunlock) with *Eject* set to **TRUE**. (This value of *Eject* causes the stream pointer to advance.)

4.  Return STATUS\_PENDING.

AVStream then manages the queue based on the flags set by the minidriver in the [**KSPIN\_DESCRIPTOR\_EX**](/windows-hardware/drivers/ddi/ks/ns-ks-_kspin_descriptor_ex) structure.

 

