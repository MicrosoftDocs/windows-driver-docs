---
title: AdapterControl Routine Requirements
author: windows-driver-content
description: AdapterControl Routine Requirements
MS-HAID:
- 'ioprogdma\_ed4a0a71-080c-42a1-902b-f97efa1ae154.xml'
- 'kernel.adaptercontrol\_routine\_requirements'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 09ce4ad8-eb1b-4fd0-9a22-4249d09584b3
keywords: ["AdapterControl routines, requirements", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
---

# AdapterControl Routine Requirements


## <a href="" id="ddk-adaptercontrol-routine-requirements-kg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20AdapterControl%20Routine%20Requirements%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


