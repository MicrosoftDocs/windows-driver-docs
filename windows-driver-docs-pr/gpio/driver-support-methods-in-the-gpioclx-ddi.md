---
title: Driver Support Methods in the GpioClx DDI
description: The GPIO framework extension (GpioClx) is available starting with Windows 8.
ms.date: 04/20/2017
---

# Driver Support Methods in the GpioClx DDI


The GPIO framework extension (GpioClx) is available starting with Windows 8. The system-supplied methods in the GpioClx DDI are implemented in the GpioClx kernel-mode driver, Msgpioclx.sys. This driver exports entry points for the [GpioClx driver support methods](/previous-versions/hh439460(v=vs.85)). Starting with Windows 8, Msgpioclx.sys is a standard component of the operating system.

At build time, GPIO controller drivers statically link to the DDI entry points in the GpioClx stub library, Msgpioclxstub.lib. At run time, this library performs the necessary driver-version negotiation to dynamically link to the corresponding entry points in Msgpioclx.sys.

A GPIO controller driver that requires a particular version of Msgpioclx.sys can safely link to a version of Msgpioclx.sys that has a higher version number. However, this driver cannot link to a version of Msgpioclx.sys that has a lower version number.

## Driver Registration


To register as a client of GpioClx, a GPIO controller driver calls the [**GPIO\_CLX\_RegisterClient**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_registerclient) method. Typically, the driver calls this method from its [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine. During this call, the driver passes a registration packet to the method. This packet contains pointers to a set of driver-implemented event callback functions. These functions access the hardware registers in the GPIO controller device. GpioClx calls these functions to handle I/O requests and to manage interrupts.

A GPIO controller driver calls the [**GPIO\_CLX\_UnregisterClient**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_unregisterclient) method to cancel its registration with GpioClx. Typically, the driver calls this method from its [*EvtDriverUnload*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_unload) event callback function.

## Device Object Initialization


To initialize GpioClx, the GPIO controller driver must call two GpioClx methods from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback function. The first method, [**GPIO\_CLX\_ProcessAddDevicePreDeviceCreate**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_processadddevicepredevicecreate), must be called before the call to the [**WdfDeviceCreate**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicecreate) method, which creates the device object. The second method, [**GPIO\_CLX\_ProcessAddDevicePostDeviceCreate**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_processadddevicepostdevicecreate), must be called after the **WdfDeviceCreate** call.

## Interrupt Lock


The majority of the driver-implemented event callback functions are called only at IRQL = PASSIVE\_LEVEL by GpioClx. However, the callback functions in the following list are called either at PASSIVE\_LEVEL or DIRQL, depending on the device information that the [*CLIENT\_QueryControllerBasicInformation*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_controller_basic_information) callback function provides to GpioClx:

-   [*CLIENT\_ClearActiveInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_clear_active_interrupts)
-   [*CLIENT\_MaskInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_mask_interrupts)
-   [*CLIENT\_QueryActiveInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_active_interrupts)
-   [*CLIENT\_QueryEnabledInterrupts*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_query_enabled_interrupts)
-   [*CLIENT\_UnmaskInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_unmask_interrupt)

These functions are called from the interrupt service routine (ISR) in GpioClx, which runs either at DIRQL or PASSIVE\_LEVEL, depending on whether the GPIO controller's hardware registers are memory-mapped.

The *CLIENT\_QueryControllerBasicInformation* function provides device information in the form of a [**CLIENT\_CONTROLLER\_BASIC\_INFORMATION**](/windows-hardware/drivers/ddi/gpioclx/ns-gpioclx-_client_controller_basic_information) structure. If the **MemoryMappedController** flag bit is set in the **Flags** member of this structure, the GpioClx ISR calls the callback functions in the preceding list at DIRQL. Otherwise, the ISR calls all of the driver-implemented callback functions at PASSIVE\_LEVEL. For more information about this flag bit, see [Interrupt-Related Callbacks](./interrupt-related-callbacks.md).

GpioClx automatically synchronizes calls to driver-implemented callback functions that run at PASSIVE\_LEVEL and are not called from the GpioClx ISR. Thus, only one of these functions can run at a time. However, GpioClx does not automatically synchronize these PASSIVE\_LEVEL callbacks with callbacks that GpioClx makes from its ISR. The GPIO controller driver must explicitly provide such synchronization, if it is required.

To avoid potential synchronization errors, GpioClx implements an *interrupt lock* that the GPIO controller driver can acquire and release. The interrupt lock is primarily used by the driver's [*CLIENT\_EnableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_enable_interrupt) and [*CLIENT\_DisableInterrupt*](/windows-hardware/drivers/ddi/gpioclx/nc-gpioclx-gpio_client_disable_interrupt) callback functions. The driver calls the [**GPIO\_CLX\_AcquireInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_acquireinterruptlock) method to acquire the lock, and calls the [**GPIO\_CLX\_ReleaseInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_releaseinterruptlock) method to release the lock. The driver calls these methods from a callback function that is called at PASSIVE\_LEVEL and is not called from the ISR in GpioClx. While the driver holds the lock, the GpioClx ISR cannot run. The driver should hold the lock only briefly and only during critical operations that must be synchronized with the ISR.

If the GpioClx ISR calls a driver-implemented callback function, this function does not need to acquire (or release) the interrupt lock because the ISR already holds the lock (and will release it). Calls to the [**GPIO\_CLX\_AcquireInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_acquireinterruptlock) and [**GPIO\_CLX\_ReleaseInterruptLock**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_releaseinterruptlock) methods by this function have no effect but are not treated as errors.

 

