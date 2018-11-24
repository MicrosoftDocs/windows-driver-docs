---
title: Driver Support Methods in the GpioClx DDI
description: The GPIO framework extension (GpioClx) is available starting with Windows 8.
ms.assetid: 179EFB06-6122-4EB0-B9F8-D5A3089D75EE
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Support Methods in the GpioClx DDI


The GPIO framework extension (GpioClx) is available starting with Windows 8. The system-supplied methods in the GpioClx DDI are implemented in the GpioClx kernel-mode driver, Msgpioclx.sys. This driver exports entry points for the [GpioClx driver support methods](https://msdn.microsoft.com/library/windows/hardware/hh439460). Starting with Windows 8, Msgpioclx.sys is a standard component of the operating system.

At build time, GPIO controller drivers statically link to the DDI entry points in the GpioClx stub library, Msgpioclxstub.lib. At run time, this library performs the necessary driver-version negotiation to dynamically link to the corresponding entry points in Msgpioclx.sys.

A GPIO controller driver that requires a particular version of Msgpioclx.sys can safely link to a version of Msgpioclx.sys that has a higher version number. However, this driver cannot link to a version of Msgpioclx.sys that has a lower version number.

## Driver Registration


To register as a client of GpioClx, a GPIO controller driver calls the [**GPIO\_CLX\_RegisterClient**](https://msdn.microsoft.com/library/windows/hardware/hh439490) method. Typically, the driver calls this method from its [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine. During this call, the driver passes a registration packet to the method. This packet contains pointers to a set of driver-implemented event callback functions. These functions access the hardware registers in the GPIO controller device. GpioClx calls these functions to handle I/O requests and to manage interrupts.

A GPIO controller driver calls the [**GPIO\_CLX\_UnregisterClient**](https://msdn.microsoft.com/library/windows/hardware/hh439498) method to cancel its registration with GpioClx. Typically, the driver calls this method from its [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) event callback function.

## Device Object Initialization


To initialize GpioClx, the GPIO controller driver must call two GpioClx methods from its [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. The first method, [**GPIO\_CLX\_ProcessAddDevicePreDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/hh439487), must be called before the call to the [**WdfDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff545926) method, which creates the device object. The second method, [**GPIO\_CLX\_ProcessAddDevicePostDeviceCreate**](https://msdn.microsoft.com/library/windows/hardware/hh439484), must be called after the **WdfDeviceCreate** call.

## Interrupt Lock


The majority of the driver-implemented event callback functions are called only at IRQL = PASSIVE\_LEVEL by GpioClx. However, the callback functions in the following list are called either at PASSIVE\_LEVEL or DIRQL, depending on the device information that the [*CLIENT\_QueryControllerBasicInformation*](https://msdn.microsoft.com/library/windows/hardware/hh439399) callback function provides to GpioClx:

-   [*CLIENT\_ClearActiveInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439341)
-   [*CLIENT\_MaskInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439380)
-   [*CLIENT\_QueryActiveInterrupts*](https://msdn.microsoft.com/library/windows/hardware/hh439395)
-   [*CLIENT\_QueryEnabledInterrupts*](https://msdn.microsoft.com/library/windows/hardware/dn265184)
-   [*CLIENT\_UnmaskInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439435)

These functions are called from the interrupt service routine (ISR) in GpioClx, which runs either at DIRQL or PASSIVE\_LEVEL, depending on whether the GPIO controller's hardware registers are memory-mapped.

The *CLIENT\_QueryControllerBasicInformation* function provides device information in the form of a [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/hh439358) structure. If the **MemoryMappedController** flag bit is set in the **Flags** member of this structure, the GpioClx ISR calls the callback functions in the preceding list at DIRQL. Otherwise, the ISR calls all of the driver-implemented callback functions at PASSIVE\_LEVEL. For more information about this flag bit, see [Interrupt-Related Callbacks](https://msdn.microsoft.com/library/windows/hardware/hh698260).

GpioClx automatically synchronizes calls to driver-implemented callback functions that run at PASSIVE\_LEVEL and are not called from the GpioClx ISR. Thus, only one of these functions can run at a time. However, GpioClx does not automatically synchronize these PASSIVE\_LEVEL callbacks with callbacks that GpioClx makes from its ISR. The GPIO controller driver must explicitly provide such synchronization, if it is required.

To avoid potential synchronization errors, GpioClx implements an *interrupt lock* that the GPIO controller driver can acquire and release. The interrupt lock is primarily used by the driver's [*CLIENT\_EnableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439377) and [*CLIENT\_DisableInterrupt*](https://msdn.microsoft.com/library/windows/hardware/hh439371) callback functions. The driver calls the [**GPIO\_CLX\_AcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439482) method to acquire the lock, and calls the [**GPIO\_CLX\_ReleaseInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439494) method to release the lock. The driver calls these methods from a callback function that is called at PASSIVE\_LEVEL and is not called from the ISR in GpioClx. While the driver holds the lock, the GpioClx ISR cannot run. The driver should hold the lock only briefly and only during critical operations that must be synchronized with the ISR.

If the GpioClx ISR calls a driver-implemented callback function, this function does not need to acquire (or release) the interrupt lock because the ISR already holds the lock (and will release it). Calls to the [**GPIO\_CLX\_AcquireInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439482) and [**GPIO\_CLX\_ReleaseInterruptLock**](https://msdn.microsoft.com/library/windows/hardware/hh439494) methods by this function have no effect but are not treated as errors.

 

 




