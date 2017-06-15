---
title: DispatchReadWrite Using Direct I/O
author: windows-driver-content
description: DispatchReadWrite Using Direct I/O
MS-HAID:
- 'DrvComps\_89d4a838-6bce-4679-a1d2-797ae9d98d4c.xml'
- 'kernel.dispatchreadwrite\_using\_direct\_i\_o'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 5174fe1f-aee5-4c8a-87a1-7f185ed4e242
keywords: ["DispatchReadWrite routine", "dispatch routines WDK kernel , DispatchReadWrite routine", "read/write dispatch routines WDK kernel", "IRP_MJ_WRITE I/O function codes", "IRP_MJ_READ I/O function codes", "data transfers WDK kernel , read/write dispatch routines", "transferring data WDK kernel , read/write dispatch routines", "direct I/O WDK kernel", "I/O WDK kernel , direct I/O"]
---

# DispatchReadWrite Using Direct I/O


## <a href="" id="ddk-dispatchreadwrite-using-direct-i-o-kg"></a>


Any lower-level device driver that sets up its device objects for direct I/O satisfies a read request by returning data transferred from its device to system physical memory, which is described by the MDL at **Irp-&gt;MdlAddress**. It satisfies a write request by transferring data from system physical memory out to its device.

Lower-level drivers must handle read/write requests asynchronously. Therefore, every lower-level driver's [*DispatchReadWrite*](https://msdn.microsoft.com/library/windows/hardware/ff543381) routine must pass [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) IRPs with valid parameters on to other driver routines, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

For read/write IRPs sent to lower-level drivers, the paged physical memory described by the MDL at **Irp-&gt;MdlAddress** has already been probed for the correct access rights to carry out the requested transfer and has already been locked down by the highest-level driver in the chain or by the I/O manager. Any intermediate or lowest-level driver that sets up its device objects for direct I/O should not call [**MmProbeAndLockPages**](https://msdn.microsoft.com/library/windows/hardware/ff554664) because this has already been done. A lowest-level driver calls [**MmGetSystemAddressForMdlSafe**](https://msdn.microsoft.com/library/windows/hardware/ff554559). (Drivers for Windows 98 call [**MmGetSystemAddressForMdl**](https://msdn.microsoft.com/library/windows/hardware/ff554556) instead. Drivers for Windows Me, Windows 2000 and later versions of Windows should use **MmGetSystemAddressForMdlSafe**.)

Any intermediate or lowest-level device driver's *DispatchReadWrite* routine should validate the parameters in its I/O stack location of read/write IRPs if it cannot trust a higher-level driver to pass down only IRPs with valid parameters. If the *DispatchReadWrite* routine finds a parameter error, it should complete the IRP with an appropriate error STATUS\_*XXX* value as already described in [Completing IRPs](completing-irps.md). If parameters are valid, an intermediate driver's *DispatchReadWrite* routine must pass the request on for further processing, according to the guidelines in [DispatchReadWrite in Higher-Level Drivers](dispatchreadwrite-in-higher-level-drivers.md).

A lowest-level device driver's *DispatchReadWrite* routine must call [**IoMarkIrpPending**](https://msdn.microsoft.com/library/windows/hardware/ff549422) with the transfer request, pass the IRP on for further processing by other driver routines, and return STATUS\_PENDING, as described in [Passing IRPs down the Driver Stack](passing-irps-down-the-driver-stack.md).

Note that a device driver's *DispatchReadWrite* routine can control the order in which IRPs are queued to its device for faster I/O throughput by calling [**IoStartPacket**](https://msdn.microsoft.com/library/windows/hardware/ff550370) with a driver-determined *Key* value. Another routine in the driver dequeues the IRP later, determines whether the requested length must be split into partial-transfer operations, and programs the device to transfer data.

In general, a device driver that must split up large transfer requests to suit the limitations of its device should postpone these operations until just before setting up the device for a given transfer request. Such a device driver's *DispatchReadWrite* routine should not check the I/O stack location of incoming IRPs for any device-specific transfer constraints, nor attempt to calculate partial-transfer ranges, when the driver can postpone these checks until just before its [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) (or other driver routine) programs the device for a transfer operation.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DispatchReadWrite%20Using%20Direct%20I/O%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


