---
title: AdapterControl Routine Requirements
description: AdapterControl Routine Requirements
keywords: ["AdapterControl routines, requirements", "AdapterControl routines, writing", "adapter objects WDK kernel , writing AdapterControl routines", "DMA transfers WDK kernel , writing AdapterControl routines"]
ms.date: 07/21/2021
---

# AdapterControl Routine Requirements

At a minimum, an [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine must do the following:

1. Save the input *MapRegisterBase* value along with any other context information that the driver needs to carry out one or more DMA transfer operations for the current IRP. The driver must pass the *MapRegisterBase* value to [**FlushAdapterBuffers**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pflush_adapter_buffers) when each DMA transfer operation is complete.

1. Return the appropriate [**IO\_ALLOCATION\_ACTION**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_io_allocation_action) value:

    - **KeepObject** if the device is a subordinate device so the driver uses system DMA.

    - **DeallocateObjectKeepRegisters** if the device is a bus master so the driver uses packet-based, bus-master DMA.

Depending on the driver's design, its *AdapterControl* routine also can do the following before it returns control:

1. Determine the starting location for the transfer on its device.

1. Calculate the size of the transfer possible, given any limitations of its device due to the starting location of the transfer.

    In general, it is the responsibility of the routine that calls [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) to determine whether a transfer request must be split up into partial transfers due to any platform-specific limitations on the *NumberOfMapRegisters* available for each DMA transfer operation, as mentioned in the preceding section and detailed in [Splitting Transfer Requests](splitting-dma-transfer-requests.md).

1. Set up any driver-maintained state about each transfer request in the device (or controller) extension.

    For example, an *AdapterControl* routine might call [**KeSetTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesettimer) with the entry point for a [*CustomTimerDpc*](using-a-customtimerdpc-routine.md) routine that times out DMA transfer operations for the driver.

1. Call [**MmGetMdlVirtualAddress**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetmdlvirtualaddress) with the MDL pointer passed at **Irp->MdlAddress** to get an index for the start of the transfer, suitable for passing to [**MapTransfer**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pmap_transfer).

1. Call **MapTransfer** to set up the system DMA controller or to obtain a physical-to-logical address mapping for a bus-master device.

1. Program the driver's device for a transfer operation, by using a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that is invoked by calling [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution). For more information, see [Using Critical Sections](using-critical-sections.md).

If a transfer request requires the driver to perform a sequence of partial-transfer operations to satisfy the current IRP, the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine is typically responsible for reprogramming the device for subsequent transfer operations. An *AdapterControl* routine is called only once for each incoming transfer IRP.

The driver routine that completes the current transfer IRP, usually the *DpcForIsr* or *CustomDpc* routine, also is responsible for releasing the system DMA controller or bus-master adapter by calling [**FreeAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_adapter_channel) or [**FreeMapRegisters**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pfree_map_registers), respectively. This driver routine should make the appropriate call as soon as possible when its last partial-transfer operation is done so that drivers of subordinate DMA devices can allocate the system DMA controller or a bus-master driver can begin processing the next transfer IRP promptly.
