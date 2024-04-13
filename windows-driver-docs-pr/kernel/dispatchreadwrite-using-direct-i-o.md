---
title: DispatchReadWrite Using Direct I/O
description: DispatchReadWrite Using Direct I/O
keywords: ["DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines", "direct I/O WDK kernel", "I/O WDK kernel , direct I/O"]
ms.date: 06/16/2017
---

# DispatchReadWrite Using Direct I/O





Any lower-level device driver that sets up its device objects for direct I/O satisfies a read request by returning data transferred from its device to system physical memory, which is described by the MDL at **Irp-&gt;MdlAddress**. It satisfies a write request by transferring data from system physical memory out to its device.

Lower-level drivers must handle read/write requests asynchronously. Therefore, every lower-level driver's [*DispatchReadWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine must pass [**IRP\_MJ\_READ**](./irp-mj-read.md) and [**IRP\_MJ\_WRITE**](./irp-mj-write.md) IRPs with valid parameters on to other driver routines, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

For read/write IRPs sent to lower-level drivers, the paged physical memory described by the MDL at **Irp-&gt;MdlAddress** has already been probed for the correct access rights to carry out the requested transfer and has already been locked down by the highest-level driver in the chain or by the I/O manager. Any intermediate or lowest-level driver that sets up its device objects for direct I/O should not call [**MmProbeAndLockPages**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmprobeandlockpages) because this has already been done. A lowest-level driver calls [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe). (Drivers for Windows 98 call [**MmGetSystemAddressForMdl**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdl) instead. Drivers for Windows Me, Windows 2000 and later versions of Windows should use **MmGetSystemAddressForMdlSafe**.)

Any intermediate or lowest-level device driver's *DispatchReadWrite* routine should validate the parameters in its I/O stack location of read/write IRPs if it cannot trust a higher-level driver to pass down only IRPs with valid parameters. If the *DispatchReadWrite* routine finds a parameter error, it should complete the IRP with an appropriate error STATUS\_*XXX* value as already described in [Completing IRPs](completing-irps.md). If parameters are valid, an intermediate driver's *DispatchReadWrite* routine must pass the request on for further processing, according to the guidelines in [DispatchReadWrite in Higher-Level Drivers](dispatchreadwrite-in-higher-level-drivers.md).

A lowest-level device driver's *DispatchReadWrite* routine must call [**IoMarkIrpPending**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iomarkirppending) with the transfer request, pass the IRP on for further processing by other driver routines, and return STATUS\_PENDING, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

Note that a device driver's *DispatchReadWrite* routine can control the order in which IRPs are queued to its device for faster I/O throughput by calling [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket) with a driver-determined *Key* value. Another routine in the driver dequeues the IRP later, determines whether the requested length must be split into partial-transfer operations, and programs the device to transfer data.

In general, a device driver that must split up large transfer requests to suit the limitations of its device should postpone these operations until just before setting up the device for a given transfer request. Such a device driver's *DispatchReadWrite* routine should not check the I/O stack location of incoming IRPs for any device-specific transfer constraints, nor attempt to calculate partial-transfer ranges, when the driver can postpone these checks until just before its [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) (or other driver routine) programs the device for a transfer operation.

 

