---
title: StartIo Routines in Lowest-Level Drivers
description: Describes how StartIo routines are processed in low-level drivers.
keywords: ["StartIo routines, lowest-level drivers", "I/O control requests WDK kernel", "buffered I/O WDK kernel", "direct I/O WDK kernel", "synchronization WDK IRPs"]
ms.date: 07/23/2021
---

# StartIo Routines in Lowest-Level Drivers

The I/O manager's call to a driver's dispatch routine is the first stage in satisfying a device I/O request. The [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine is the second stage. Every device driver with a *StartIo* routine is likely to call [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket) from its [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) and [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routines, and usually for a subset of the I/O control codes it supports in its [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine. The **IoStartPacket** routine adds the IRP to the device's system-supplied device queue or, if the queue is empty, immediately calls the driver's *StartIo* routine to process the IRP.

You can assume that when a driver's *StartIo* routine is called, the target device is not busy. This is because the I/O manager calls *StartIo* under two circumstances; either one of the driver's dispatch routines has just called **IoStartPacket** and the device queue was empty, or the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) routine is completing another request and has just called [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) to dequeue the next IRP.

Before the *StartIo* routine in a highest-level device driver is called, that driver's dispatch routine should have probed and locked down the user buffer, if necessary, to set up valid mapped buffer addresses in the IRP queued to its *StartIo* routine. If a highest-level device driver sets up its device objects for direct I/O (or for neither buffered nor direct I/O), the driver cannot defer locking down a user buffer to its *StartIo* routine; every *StartIo* routine is called in an arbitrary thread context at IRQL = DISPATCH_LEVEL.

> [!NOTE]
> Any buffer memory to be accessed by a driver's *StartIo* routine must be locked down or allocated from resident, system-space memory and must be accessible in an arbitrary thread context.

In general, any lower-level device driver's *StartIo* routine is responsible for calling [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) with the input IRP and then doing whatever request-specific processing is necessary to start the I/O operation on its device. Request-specific processing can include the following:

- Setting up or updating any state information about the current request that the driver maintains. The state information might be stored in the device extension of the target device object or elsewhere in nonpaged pool allocated by the driver.

    For example, if a device driver maintains an InterruptExpected Boolean for the current transfer operation, its *StartIo* routine might set this variable to **TRUE**. If the driver maintains a time-out counter for the current operation, its *StartIo* routine might set up this value, or the *StartIo* routine might queue the driver's [*CustomTimerDpc*](using-a-customtimerdpc-routine.md) routine.

    If the *StartIo* routine shares access to state information or [hardware resources](hardware-resources.md) with other driver routines, the state information or resource must be protected by a spin lock. (See [Spin Locks](./introduction-to-spin-locks.md).)

    If the *StartIo* routine shares access to state information or resources with the driver's [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine, *StartIo* must use [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine that accesses the state or resource information. (See [Using Critical Sections](using-critical-sections.md).)

- Assigning a sequence number to the IRP in case the driver must log a device I/O error while processing the IRP.

    See [Logging Errors](logging-errors.md) for more information.

- If necessary, translating the parameters in the driver's I/O stack location into device-specific values.

    For example, a disk driver might need to calculate the starting sector or byte offset to the physical disk address for a transfer operation, and whether the requested length of the transfer will cross a particular sector boundary or exceed the transfer capacity of its physical device.

- If the driver controls a removable-media device, checking for media changes before programming the device for I/O and notifying its overlying file system if the media has changed.

    For more information, see [Supporting Removable Media](supporting-removable-media.md).

- If the device uses DMA, checking whether the requested **Length** (number of bytes to be transferred, found in the driver's I/O stack location of the IRP) should be split into partial-transfer operations, as explained in [Input/Output Techniques](i-o-programming-techniques.md), assuming a closely coupled higher-level driver does not presplit large transfers for the device driver.

    The *StartIo* routine of such a device driver also can be responsible for calling [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers) and, if the driver uses packet-based DMA, for calling [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) with the driver's [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine.

    See [Adapter Objects and DMA](./introduction-to-adapter-objects.md), and [Maintaining Cache Coherency](maintaining-cache-coherency.md), for additional details.

- If the device uses PIO, mapping the base virtual address of the buffer, described in the IRP at **Irp->MdlAddress**, to a system-space address with [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe).

    For read requests, the device driver's *StartIo* routine can be responsible for calling [**KeFlushIoBuffers**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keflushiobuffers) before PIO operations begin. See [Maintaining Cache Coherency](maintaining-cache-coherency.md) for more information.

- If a non-WDM driver uses a controller object, calling [**IoAllocateController**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ioallocatecontroller) to register its [*ControllerControl*](writing-controllercontrolroutines.md) routine.

- If the driver handles cancelable IRPs, checking whether the input IRP has already been canceled.

- If an input IRP can be canceled before it is processed to completion, the *StartIo* routine must call [**IoSetCancelRoutine**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetcancelroutine) with the IRP and the entry point of the driver's [*Cancel*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_cancel) routine. The *StartIo* routine must acquire the cancel spin lock for its call to **IoSetCancelRoutine**. Alternatively, a driver can use [**IoSetStartIoAttributes**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetstartioattributes) to set the *NonCancelable* attribute for the *StartIo* routine to **TRUE**. This prevents the system from trying to cancel an IRP that has been passed to *StartIo* by a call to [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket).

As a general rule, a driver that uses buffered I/O has a simpler *StartIo* routine than one that uses direct I/O. Drivers that use buffered I/O transfer small amounts of data for each transfer request, while those that use direct I/O (whether DMA or PIO) transfer large amounts of data to or from locked-down buffers that can span physical page boundaries in system memory.

Higher-level drivers layered above physical device drivers usually set up their device objects to match those of their respective device drivers. However, a highest-level driver, particularly a file system driver, can set up device objects for neither direct nor buffered I/O.

Drivers that set up their device objects for buffered I/O can rely on the I/O manager to pass valid buffers in all IRPs it sends to the driver. Lower-level drivers that set up device objects for direct I/O can rely on the highest-level driver in their chain to pass valid buffers in all IRPs sent through any intermediate drivers to the underlying lower-level device driver.

## Using Buffered I/O in StartIo Routines

If a driver's [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), or [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine determines that a request is valid and calls [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket), the I/O manager calls the driver's [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine to process the IRP immediately if the device queue is empty. If the queue is not empty, **IoStartPacket** queues the IRP. Eventually, a call to [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) from the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine causes the I/O manager to dequeue the IRP and call the driver's *StartIo* routine.

The *StartIo* routine calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) and determines which operation must be performed to satisfy the request. It preprocesses the IRP in any way necessary before programming the physical device to carry out the I/O request.

If access to the physical device (or the device extension) must be synchronized with an [*InterruptService*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kservice_routine) routine, the *StartIo* routine must call a [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine to perform the necessary device programming. For more information, see [Using Critical Sections](using-critical-sections.md).

A physical device driver that uses buffered I/O transfers data either to or from a system-space buffer, allocated by the I/O manager, that the driver finds in each IRP at **Irp->AssociatedIrp.SystemBuffer**.

## Using Direct I/O in StartIo Routines

If a driver's [*DispatchRead*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), [*DispatchWrite*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch), or [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine determines that a request is valid and calls [**IoStartPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartpacket), the I/O manager calls the driver's *StartIo* routine to process the IRP immediately if the device queue is empty. If the queue is not empty, **IoStartPacket** queues the IRP. Eventually, a call to [**IoStartNextPacket**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostartnextpacket) from the driver's [*DpcForIsr*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_dpc_routine) or [*CustomDpc*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kdeferred_routine) routine causes the I/O manager to dequeue the IRP and call the driver's *StartIo* routine.

The *StartIo* routine calls [**IoGetCurrentIrpStackLocation**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iogetcurrentirpstacklocation) and determines which operation must be performed to satisfy the request. It preprocesses the IRP in any way necessary, such as splitting up a large DMA transfer request into partial-transfer ranges and saving state about the **Length** of an incoming transfer request that must be split. Then it programs the physical device to carry out the I/O request.

If access to the physical device (or the device extension) must be synchronized with the driver's ISR, the *StartIo* routine must use a driver-supplied *SynchCritSection* routine to perform the necessary programming. For more information, see [Using Critical Sections](using-critical-sections.md).

Any driver that uses direct I/O either reads data into or writes data from a locked-down buffer, described by a memory descriptor list (MDL), that the driver finds in the IRP at **Irp->MdlAddress**. Such a driver commonly uses buffered I/O for device control requests. For more information, see [Handling I/O Control Requests in StartIo Routines](#handling-io-control-requests-in-startio-routines).

The MDL type is an opaque type that drivers do not access directly. Instead, drivers that use PIO remap user-space buffers by calling [**MmGetSystemAddressForMdlSafe**](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmgetsystemaddressformdlsafe) with **Irp->MdlAddress** as a parameter. Drivers that use DMA also pass **Irp->MdlAddress** to support routines during their transfer operations to have the buffer addresses remapped to logical ranges for their devices.

Unless a closely coupled higher-level driver splits up large DMA transfer requests for the underlying device driver, a lowest-level device driver's *StartIo* routine must split up each transfer request that is larger than its device can manage in a single transfer operation. Drivers that use system DMA are required to split transfer requests that are too large for the system DMA controller or for their devices to handle in a single transfer operation.

If the device is a subordinate DMA device, its driver must synchronize transfers through a system DMA controller with a driver-allocated adapter object, representing the DMA channel, and a driver-supplied [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine. The driver of a bus-master DMA device also must use a driver-allocated adapter object to synchronize its transfers and must supply an *AdapterControl* routine if it uses the system's packet-based DMA support, or an [*AdapterListControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_list_control) routine if it uses the system's scatter/gather support.

Depending on the driver's design, it might synchronize transfer and device control operations on a physical device with a controller object and supply a [*ControllerControl*](writing-controllercontrolroutines.md) routine.

See [Adapter Objects and DMA](introduction-to-adapter-objects.md) and [Controller Objects](introduction-to-controller-objects.md) for more information.

## Handling I/O Control Requests in StartIo Routines

In general, only a subset of device I/O control requests are passed on from a driver's [*DispatchDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) or [*DispatchInternalDeviceControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_dispatch) routine for further processing by the driver's *StartIo* routine. The driver's *StartIo* routine only has to handle valid device control requests that require device state changes or return volatile information about the current device state.

Each new driver must support the same set of public I/O control codes as all other drivers for the same kind of device. The system defines public, device-type-specific I/O control codes for [**IRP_MJ_DEVICE_CONTROL**](./irp-mj-device-control.md) requests as buffered requests.

Consequently, physical device drivers make data transfers to or from a system-space buffer that each driver finds in the IRP at **Irp->AssociatedIrp.SystemBuffer** for device control requests. Even drivers that set up their device objects for direct I/O use buffered I/O to satisfy device control requests with public I/O control codes.

The definition of each I/O control code determines whether data transferred for that request is buffered. Any privately defined I/O control codes for driver-specific [**IRP_MJ_INTERNAL_DEVICE_CONTROL**](./irp-mj-internal-device-control.md) requests between paired drivers can define a code with method buffered, method direct, or method neither. As a general rule, any privately defined I/O control code should be defined with method neither if a closely coupled higher-level driver must allocate a buffer for that request.

## Programming the Device for I/O Operations

Usually, the *StartIo* routine in a lowest-level device driver must synchronize access to any memory or device registers it shares with the driver's ISR by using [**KeSynchronizeExecution**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kesynchronizeexecution) to call a driver-supplied [*SynchCritSection*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ksynchronize_routine) routine. The driver's *StartIo* routine uses the *SynchCritSection* routine to actually program the physical device for I/O at DIRQL. For more information, see [Using Critical Sections](using-critical-sections.md).

Before calling **KeSynchronizeExecution**, the *StartIo* routine must do any preprocessing necessary for the request. Preprocessing might include calculating an initial partial-transfer range and saving any state information about the original request for other driver routines.

If a device driver uses DMA, its *StartIo* routine usually calls [**AllocateAdapterChannel**](/windows-hardware/drivers/ddi/wdm/nc-wdm-pallocate_adapter_channel) with a driver-supplied [*AdapterControl*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_control) routine. In these circumstances, the *StartIo* routine postpones the responsibility for programming the physical device to the *AdapterControl* routine. It, in turn, can call **KeSynchronizeExecution** to have a driver-supplied *SynchCritSection* routine program the device for a DMA transfer.
