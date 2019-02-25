---
title: GpioClx I/O and Interrupt Interfaces
description: Typically, the clients of a GPIO controller are drivers for peripheral devices that connect to GPIO pins.
ms.assetid: F75E9B21-9DA4-4DD9-BB44-59E19EDFC099
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GpioClx I/O and Interrupt Interfaces


Typically, the clients of a GPIO controller are drivers for peripheral devices that connect to GPIO pins. These drivers use GPIO pins as low-bandwidth data channels, device-select outputs, and interrupt-request inputs. Peripheral device drivers open logical connections to GPIO pins that are configured as data inputs or outputs. They use these connections to send I/O requests to these pins. In addition, peripheral device drivers can logically connect their interrupt service routines to GPIO pins that are configured as interrupt request inputs.

GPIO pins are system-managed hardware resources. Before a peripheral device driver starts its device, the Plug and Play (PnP) manager assigns to this driver a list of hardware resources. This list of hardware resources might include the following:

-   A GPIO I/O resource. This resource is a set of one or more GPIO pins that are configured as data inputs or data outputs. GPIO I/O resources are a new Windows resource type starting with Windows 8.
-   An interrupt. This interrupt resource might be implemented as a GPIO pin that is configured as an interrupt input, but it might be implemented instead by a programmable interrupt controller or as a dedicated interrupt pin on a processor package. The hardware abstraction layer (HAL) interrupt abstraction hides these implementation details, which client drivers can safely ignore.

Before a peripheral device driver can use a set of GPIO pins as data inputs or outputs, the driver must open a logical connection to these pins. For example, a [kernel-mode driver interface](https://msdn.microsoft.com/library/windows/hardware/ff544296) (KMDF) driver obtains a WDFIOTARGET handle to identify the connection. The driver uses this handle to send I/O requests to the pins. Specifically, client drivers send [**IOCTL\_GPIO\_WRITE\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406487) and [**IOCTL\_GPIO\_READ\_PINS**](https://msdn.microsoft.com/library/windows/hardware/hh406483) I/O control requests to write data to output pins and read data from input pins. For code examples that show how to connect to a set of GPIO I/O pins, see the following topics:

[Connecting a KMDF Driver to GPIO I/O Pins](https://msdn.microsoft.com/library/windows/hardware/hh406474)

To use an interrupt resource to receive interrupts, a peripheral device driver must logically connect an interrupt service routine (ISR) to the interrupt. For example, a kernel-mode driver can make this connection by calling the [**WdfInterruptCreate**](https://msdn.microsoft.com/library/windows/hardware/ff547345) method or the [**IoConnectInterruptEx**](https://msdn.microsoft.com/library/windows/hardware/ff548378) routine. After being connected, the driver's ISR runs when the peripheral device signals an interrupt request to the GPIO pin or interrupt controller input. For more information about interrupts, see [Creating an Interrupt Object](https://msdn.microsoft.com/library/windows/hardware/ff540757).

The GPIO framework extension (GpioClx) manages both I/O connections and interrupt connections for the peripheral device drivers that are its clients. The PnP manager might assign different groups of GPIO pins on a GPIO controller device to different client drivers. Some of these pins are configured as data inputs or outputs, and some are configured as interrupt request inputs.

When client drivers receive interrupt requests or send I/O requests to GPIO pins, GpioClx calls event callback functions that are implemented by the GPIO controller driver. These callbacks access the hardware registers in the GPIO controller device. Through these function calls, GpioClx reads data inputs, writes to data outputs, and manages interrupt requests (by querying, enabling, masking, clearing, and so on, GPIO pins that are configured as interrupt inputs).

GpioClx does all the processing that is required to manage I/O and interrupt connections that are opened by clients. The GPIO controller driver—by delegating the management of these connections to GpioClx—is responsible only for the relatively simple task of accessing the hardware registers in the GPIO controller device. The GPIO controller driver does not need to know the client driver for which a particular access is made.

 

 




