---
title: AdapterControl Routine Requirements
description: AdapterControl Routine Requirements
ms.assetid: 09ce4ad8-eb1b-4fd0-9a22-4249d09584b3
keywords: ["AdapterControl routines, requirements", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# AdapterControl Routine Requirements





At a minimum, an [*AdapterControl*](https://msdn.microsoft.com/library/windows/hardware/ff540504) routine must do the following:

1.  Save the input *MapRegisterBase* value along with any other context information that the driver needs to carry out one or more DMA transfer operations for the current IRP. The driver must pass the *MapRegisterBase* value to [**FlushAdapterBuffers**](https://msdn.microsoft.com/library/windows/hardware/ff545917) when each DMA transfer operation is complete.

2.  Return the appropriate [**IO\_ALLOCATION\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff550534) value:

    -   **KeepObject** if the device is a subordinate device so the driver uses system DMA.

    -   **DeallocateObjectKeepRegisters** if the device is a bus master so the driver uses packet-based, bus-master DMA.

Depending on the driver's design, its *AdapterControl* routine also can do the following before it returns control:

1.  Determine the starting location for the transfer on its device.

2.  Calculate the size of the transfer possible, given any limitations of its device due to the starting location of the transfer.

    In general, it is the responsibility of the routine that calls [**AllocateAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff540573) to determine whether a transfer request must be split up into partial transfers due to any platform-specific limitations on the *NumberOfMapRegisters* available for each DMA transfer operation, as mentioned in the preceding section and detailed in [Splitting Transfer Requests](splitting-dma-transfer-requests.md).

3.  Set up any driver-maintained state about each transfer request in the device (or controller) extension.

    For example, an *AdapterControl* routine might call [**KeSetTimer**](https://msdn.microsoft.com/library/windows/hardware/ff553286) with the entry point for a [*CustomTimerDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542983) routine that times out DMA transfer operations for the driver.

4.  Call [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) with the MDL pointer passed at **Irp-&gt;MdlAddress** to get an index for the start of the transfer, suitable for passing to [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402).

5.  Call **MapTransfer** to set up the system DMA controller or to obtain a physical-to-logical address mapping for a bus-master device.

6.  Program the driver's device for a transfer operation, by using a [*SynchCritSection*](https://msdn.microsoft.com/library/windows/hardware/ff563928) routine that is invoked by calling [**KeSynchronizeExecution**](https://msdn.microsoft.com/library/windows/hardware/ff553302). For more information, see [Using Critical Sections](using-critical-sections.md).

If a transfer request requires the driver to perform a sequence of partial-transfer operations to satisfy the current IRP, the driver's [*DpcForIsr*](https://msdn.microsoft.com/library/windows/hardware/ff544079) or [*CustomDpc*](https://msdn.microsoft.com/library/windows/hardware/ff542972) routine is typically responsible for reprogramming the device for subsequent transfer operations. An *AdapterControl* routine is called only once for each incoming transfer IRP.

The driver routine that completes the current transfer IRP, usually the *DpcForIsr* or *CustomDpc* routine, also is responsible for releasing the system DMA controller or bus-master adapter by calling [**FreeAdapterChannel**](https://msdn.microsoft.com/library/windows/hardware/ff546507) or [**FreeMapRegisters**](https://msdn.microsoft.com/library/windows/hardware/ff546513), respectively. This driver routine should make the appropriate call as soon as possible when its last partial-transfer operation is done so that drivers of subordinate DMA devices can allocate the system DMA controller or a bus-master driver can begin processing the next transfer IRP promptly.

 

 




