---
title: GPIO Device Contexts
description: A general-purpose I/O (GPIO) controller device is represented by a framework device object.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GPIO Device Contexts


A general-purpose I/O (GPIO) controller device is represented by a framework device object. The GPIO controller driver can associate a device context with this device object. The driver uses this device context to persistently store information about the state of the GPIO controller device.

When the GPIO framework extension (GpioClx) calls an event callback function that is implemented by the driver, GpioClx passes the device context to this function as a parameter. The callback function examines the device context to determine the current state of the device. If the function alters this state, it updates the device context accordingly.

GpioClx allocates the storage for a device object. If a GPIO controller driver has more than one device object, the device context for each of these objects is the same size. During the [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, the driver calls the [**GPIO\_CLX\_RegisterClient**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_registerclient) method to register its callback functions and to specify the device context size that it requires. Later, during the [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback routine, the driver calls the [**GPIO\_CLX\_ProcessAddDevicePostDeviceCreate**](/windows-hardware/drivers/ddi/gpioclx/nf-gpioclx-gpio_clx_processadddevicepostdevicecreate) method to pass the new device object to GpioClx, and GpioClx allocates the device context for this object. Thereafter, when GpioClx calls a driver-implemented callback function, this device context is passed to the function as a parameter.

 

