---
title: Splitting DMA Transfer Requests
description: Splitting DMA Transfer Requests
ms.assetid: 7d5b1649-1021-4876-a9c0-e6b156785ef2
keywords: ["I/O WDK kernel , splitting transfer requests", "splitting transfer requests", "transfer request splitting WDK kernel", "data transfers WDK kernel , splitting requests", "transferring data WDK kernel , splitting requests"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Splitting DMA Transfer Requests





Any driver might need to split up a transfer request and carry out more than one DMA transfer operation to satisfy a given IRP, depending on the following:

-   The number of [map registers](map-registers.md) returned by [**IoGetDmaAdapter**](https://msdn.microsoft.com/library/windows/hardware/ff549220)

-   The bytes of data to be transferred, contained in the **Length** member of the driver's I/O stack location for the IRP

-   The number of page boundaries, in system physical memory, for the buffer into which or from which the driver is to transfer data

-   Device-specific constraints on the driver's DMA operations. For example, the system "AT" disk driver must split up transfer requests for more than 256 sectors due to the disk controller's limitations.

A driver can determine the number of map registers needed to transfer all the data specified by an IRP as follows:

1.  Call [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539), passing a pointer to the MDL at **Irp-&gt;MdlAddress**, to get the starting virtual address for the buffer. Note that a driver must not attempt to access memory using this virtual address. The value returned by **MmGetMdlVirtualAddress** is an index into the MDL, not necessarily a valid address.

2.  Pass the returned index and the value of **Length** in the driver's I/O stack location of the IRP to the [**ADDRESS\_AND\_SIZE\_TO\_SPAN\_PAGES**](https://msdn.microsoft.com/library/windows/hardware/ff540562) macro.

If the value returned by **ADDRESS\_AND\_SIZE\_TO\_SPAN\_PAGES** is greater than the *NumberOfMapRegisters* value returned by **IoGetDmaAdapter**, the driver cannot transfer all requested data for this IRP in a single DMA operation. Instead, it must do the following:

1.  Split the buffer into pieces that are sized to suit the number of available map registers (and any device-specific DMA constraints).

2.  Carry out as many DMA operations as it takes to satisfy the transfer request.

For example, suppose **ADDRESS\_AND\_SIZE\_TO\_SPAN\_PAGES** indicates that twelve map registers are needed to satisfy a transfer request, but the *NumberOfMapRegisters* value returned by **IoGetDmaAdapter** is only five. (Assume no device-specific DMA constraints.) In this case, the driver must carry out three DMA transfer operations, calling [**MapTransfer**](https://msdn.microsoft.com/library/windows/hardware/ff554402) three times to transfer all the data requested by the IRP.

The system's DMA device drivers use various techniques to split up a DMA transfer when there are not enough map registers to satisfy an IRP with a single I/O operation. One technique to use is the following:

1.  Call [**IoAllocateMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548263) to allocate an MDL describing a portion of the user buffer.

2.  Call [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) to lock down that portion of the user buffer.

3.  Transfer the data for that portion of the buffer.

4.  Call [**MmUnlockPages**](https://msdn.microsoft.com/library/windows/hardware/ff556381) and do either of the following:
    -   If the MDL that the driver allocated in step 1 is large enough for the next piece of the transfer, call [**MmPrepareMdlForReuse**](https://msdn.microsoft.com/library/windows/hardware/ff554660) and repeat steps 2 through 4.
    -   Otherwise, call [**IoFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff549126) and repeat steps 1 through 4.

5.  Call [**MmUnlockPages**](https://msdn.microsoft.com/library/windows/hardware/ff556381) and [**IoFreeMdl**](https://msdn.microsoft.com/library/windows/hardware/ff549126) when all the data has been transferred.

If a highest-level driver cannot lock down the entire user buffer with [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) in a machine with limited memory, it can do the following:

1.  Call [**IoBuildSynchronousFsdRequest**](https://msdn.microsoft.com/library/windows/hardware/ff548330) to allocate a partial-transfer IRP and lock down a portion of the user buffer. The locked-down area is usually either a multiple of **PAGE\_SIZE** or is sized to suit the underlying device's transfer capacity.

2.  Call [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336) for the partial-transfer IRP, and call [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) to wait for an event object that the driver set up to be associated with its partial-transfer IRP, if lower drivers return STATUS\_PENDING.

3.  When it regains control, repeat steps 1 and 2 until all the data has been transferred, and, then, complete the original IRP.

When a storage class driver splits up large transfer requests for underlying SCSI port/miniport drivers, it allocates an additional IRP for each piece of the transfer request. It registers an [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routine for each driver-allocated IRP, to track the status of the full transfer request and to free the driver-allocated IRPs. Then it sends these IRPs on to the port driver using [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

Other class/port drivers can use this technique only if the class driver can determine how many map registers are available to the port driver. The port driver must store this configuration information in the registry for the paired class driver, or the paired drivers must define a private interface, using internal device I/O control requests, to pass configuration information about the number of available map registers from the port driver to the class driver.

A monolithic driver (that is, a driver not part of a class/port pair) for a DMA device must split up large transfer requests for itself. Such drivers usually split a large request into pieces and carry out a sequence of DMA operations in order to satisfy the IRP.

If a transfer request is too large for the underlying device driver to handle, a higher-level driver can call [**MmGetMdlVirtualAddress**](https://msdn.microsoft.com/library/windows/hardware/ff554539) and [**IoBuildPartialMdl**](https://msdn.microsoft.com/library/windows/hardware/ff548324), then set up a sequence of partial-transfer IRPs for underlying device drivers.

 

 




