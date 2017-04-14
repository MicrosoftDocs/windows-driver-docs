---
title: Common Buffer DMA in AVStream
author: windows-driver-content
description: Common Buffer DMA in AVStream
ms.assetid: 8cbadb5a-f879-4fe0-a698-cde3b9f6df83
keywords: ["common buffer DMA WDK AVStream", "buffers WDK AVStream", "AVStream WDK , hardware", "hardware WDK AVStream", "DMA services WDK AVStream", "Direct Memory Access WDK AVStream"]
---

# Common Buffer DMA in AVStream


## <a href="" id="ddk-common-buffer-dma-in-avstream-ksg"></a>


Common buffer direct memory access (DMA) occurs when the device does not write directly to the capture buffers; instead it copies data to and from a common buffer.

To use common buffer DMA in your AVStream minidriver:

1.  Acquire a DMA adapter by calling [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220), as in packet-based DMA. Do not specify KSPIN\_FLAG\_GENERATE\_MAPPINGS in the **Flags** member of the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure, and do not register your DMA adapter with AVStream. You might need to implement your own private buffer/copy scheme.

2.  Register an interrupt service routine (ISR) as described in [Writing AVStream Minidrivers for Hardware](writing-avstream-minidrivers-for-hardware.md)

If the **Flags** member of KSPIN\_DESCRIPTOR\_EX sets KSPIN\_FLAG\_DO\_NOT\_INITIATE\_PROCESSING, the following steps take place before AVStream calls [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351):

1.  The minidriver sets up its common buffer transfers.

2.  The kernel calls the ISR that the vendor has previously registered. In the ISR, the minidriver queues a deferred procedure call (DPC).

3.  When the common buffer is full, the minidriver calls [**KsPinAttemptProcessing**](https://msdn.microsoft.com/library/windows/hardware/ff563494) from the DPC.

4.  AVStream calls the process dispatch if conditions specified by the **Flags** member of [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) are met.

Within the vendor-supplied [*AVStrMiniPinProcess*](https://msdn.microsoft.com/library/windows/hardware/ff556351) callback routine, one possible course of action is as follows:

1.  Call [**KsPinGetLeadingEdgeStreamPointer**](https://msdn.microsoft.com/library/windows/hardware/ff563513):

    ```
    KSSTREAM_POINTER *Leading = KsPinGetLeadingEdgeStreamPointer (
                    Pin,
                    State
                   );
    ```

2.  Copy frame data to Leading-&gt;StreamHeader-&gt;Data and set the necessary flags and time stamp information in the appropriate [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138).

3.  Call [**KsStreamPointerUnlock**](https://msdn.microsoft.com/library/windows/hardware/ff567137) with *Eject* set to **TRUE**. (This value of *Eject* causes the stream pointer to advance.)

4.  Return STATUS\_PENDING.

AVStream then manages the queue based on the flags set by the minidriver in the [**KSPIN\_DESCRIPTOR\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff563534) structure.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Common%20Buffer%20DMA%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


