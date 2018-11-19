---
title: SpbCx Interfaces
description: The SPB framework extension (SpbCx) has two interfaces.
ms.assetid: 2449BB88-1912-43F9-97E6-B56158D92E55
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SpbCx Interfaces


The SPB framework extension (SpbCx) has two interfaces. The first is an I/O request interface through which SpbCx accepts I/O requests that clients (peripheral drivers) of the SPB controller send to peripheral devices that are attached to the bus. The second interface is a device driver interface (DDI) through which SpbCx communicates with the SPB controller driver.

The two SpbCx interfaces are defined in the Spbcx.h and Spb.h header files. Spbcx.h defines the DDI between SpbCx and the SPB controller driver. Spb.h defines the SPB-specific I/O control codes that are supported by the SpbCx I/O request interface.

-   [SpbCx Device Driver Interface (DDI)](#spbcx-device-driver-interface-ddi)
-   [SPB I/O Request Interface](#spb-io-request-interface)

## SpbCx Device Driver Interface (DDI)


The SpbCx device driver interface (DDI) consists of methods that are implemented by the SPB framework extension module, Spbcx.sys, and event callback functions that the SPB controller driver implements. The SPB controller driver registers its callback functions with SpbCx during the initialization of the DDI.

To request services from SpbCx, the SPB controller driver calls the [SpbCx driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh450910). For example, the SPB controller driver calls these methods to set driver configuration options for the SPB controller, or to obtain additional information about an I/O request.

To notify the SPB controller driver of an event (for example, the arrival of an I/O request from a client), SpbCx calls an [event callback function](https://msdn.microsoft.com/library/windows/hardware/hh450911) that is implemented by the SPB controller driver.

During callbacks from SpbCx, the SPB controller driver code runs in an arbitrary thread context. After receiving an I/O request that requires processing by the SPB controller driver, SpbCx does any required preprocessing of the request before SpbCx calls an *EvtSpb*Xxx function to perform the requested operation. For example, to make a user-mode buffer available to a callback function, SpbCx might need to run in the context of the thread that originated the I/O request. (The [*EvtIoInCallerContext*](https://msdn.microsoft.com/library/windows/hardware/ff541764) function is the only callback function that cannot rely on SpbCx to preprocess requests.)

To register a set of *EvtSpb*Xxx callback functions, the SPB controller driver calls the [**SpbDeviceInitialize**](https://msdn.microsoft.com/library/windows/hardware/hh450919) method. This driver calls the [**SpbControllerSetIoOtherCallback**](https://msdn.microsoft.com/library/windows/hardware/hh450907) method to register an *EvtIoInCallerContext* callback function.

The SpbCx DDI uses the WDFDEVICE object handle type to represent the device object for an SPB controller. Include the Wdf.h header file to define WDFDEVICE and the other KMDF object handle types. In addition, the DDI uses two SPB-specific object handle types, [**SPBREQUEST**](https://msdn.microsoft.com/library/windows/hardware/hh450925) and [**SPBTARGET**](https://msdn.microsoft.com/library/windows/hardware/hh406201), which are similar to the WDFREQUEST and WDFTARGET object handle types that are defined by KMDF. An SPBREQUEST handle represents an I/O request. An SPBTARGET handle represents a logical connection to a peripheral device on the bus that has been opened for I/O operations.

Simple peripheral buses such as I²C and SPI are typically used by System on a Chip (SoC) modules, for which low pin counts are important. SoC modules are frequently used as processors in handheld devices that require low power consumption. Because SPB controller circuits consume relatively little power, the power management code in SpbCx can be relatively simple. By default, SpbCx ensures that power to the SPB controller is turned on before it calls any of the event callback methods in the SPB controller driver. For more information, see the description of the **PowerManaged** member in [**SPB\_CONTROLLER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/hh406206).

If necessary, the SPB controller driver can explicitly turn power to the controller on and off by calling the [**WdfDeviceStopIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546921) and [**WdfDeviceResumeIdle**](https://msdn.microsoft.com/library/windows/hardware/ff546838) methods.

Because the SPB controller driver is a kernel-mode driver, it should assign an appropriate security descriptor to its file objects. This descriptor prevents unauthorized access from user mode to the peripheral devices on the SPB. For example, the sample SPB controller drivers in the WDK use the following SDDL string, which provides a default level of security that is suitable for a typical SPB controller driver:

"D:P(A;;GA;;;SY)(A;;GA;;;BA)(A;;GA;;;UD)"

This SDDL string restricts access to the operating system (and its user-mode components), members of the Administrators group, and [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff560442) (UMDF) drivers. For more information about SDDL strings, see [SDDL for Device Objects](https://msdn.microsoft.com/library/windows/hardware/ff563667).

In addition, the [*EvtSpbControllerIoOther*](https://msdn.microsoft.com/library/windows/hardware/hh450805) function must validate all parameters in the custom I/O control requests that it receives from user-mode clients. For all other *EvtSpb*Xxx functions, SpbCx validates the parameters in I/O requests from user-mode clients before these parameters are passed to the SPB controller driver. For more information about device security, see [Securing Device Objects](https://msdn.microsoft.com/library/windows/hardware/ff563688).

All methods and callback functions in the SpbCx DDI that return status codes return NTSTATUS values. The driver-support methods in this DDI follow the usual conventions for KMDF interfaces, and all objects that are used by SpbCx follow the usual conventions for KMDF objects. For more information, see [Introduction to Framework Objects](https://msdn.microsoft.com/library/windows/hardware/ff544249).

## SPB I/O Request Interface


To implement the I/O request interface, SpbCx manages the I/O queue for the SPB controller and monitors this queue for I/O requests from clients of the SPB controller. These clients are user-mode and kernel-mode drivers for SPB-connected peripheral devices. Applications cannot directly communicate with SPB-connected peripheral devices through the SPB I/O request interface.

SpbCx might do all the processing for some of these I/O requests, and do preprocessing of other requests before the requests are passed to the SPB controller driver. The SPB controller driver is responsible for completing the requests that it receives from SpbCx.

Clients can send read and write requests to SPB-connected peripheral devices. In response to an [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883) request, the SPB controller transfers the specified number of bytes from a peripheral device to a client buffer. In response to an [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904) request, the SPB controller transfers the specified number of bytes from a client buffer to a peripheral device.

In addition to simple read and write operations, the SpbCx I/O request interface supports I/O transfer sequences, which combine one or more simple transfers (that is, reads and writes) into a single, atomic bus operation. During this operation, the bus is used exclusively for transfers to and from the target peripheral device, and accesses of other targets on the bus are temporarily locked out until the operation completes. SpbCx supports the [**IOCTL\_SPB\_EXECUTE\_SEQUENCE**](https://msdn.microsoft.com/library/windows/hardware/hh450857) I/O control code, which a client uses to specify a sequence of fixed-length transfers to and from a target device in a single I/O request. This I/O control request enables the controller driver to optimize a sequence of bus transfers to improve performance.

The SpbCx I/O request interface supports the [**IOCTL\_SPB\_LOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450858) and [**IOCTL\_SPB\_UNLOCK\_CONTROLLER**](https://msdn.microsoft.com/library/windows/hardware/hh450859) I/O control codes, which lock and unlock the SPB controller. These lock and unlock requests provide another way for a client to perform an I/O transfer sequence. In this case, each read or write operation in the sequence is specified by a separate read or write request. While a client has the controller locked, other clients cannot access devices on the bus. Only the client that holds the lock can perform I/O operations on the bus. For this reason, clients should lock the controller only for brief periods. A client should never leave the controller locked after a transfer sequence completes. For more information, see [I/O Transfer Sequences](https://msdn.microsoft.com/library/windows/hardware/hh450890).

In addition to the I/O control (IOCTL) codes that are supported by SpbCx, the SPB controller driver can support custom IOCTLs. Clients can send IOCTL requests to file objects that represent target devices on the bus, and these requests arrive in the I/O request queue that is managed by SpbCx. If SpbCx receives a request that has an IOCTL code that it does not support, SpbCx passes the request directly to the controller driver, which performs all handling of the request.

Kernel-mode clients of the SpbCx I/O request interface can send I/O requests at an interrupt request level (IRQL) of either PASSIVE\_LEVEL or DISPATCH\_LEVEL. User-mode clients can send I/O requests only at PASSIVE\_LEVEL. I/O completion can occur at PASSIVE\_LEVEL or DISPATCH\_LEVEL. All I/O requests can return STATUS\_PENDING.

 

 




