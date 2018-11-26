---
title: SPB Device Stacks
description: Acpi.sys creates the PDO for a peripheral device on an SPB.
ms.assetid: 21AB67A2-AA3C-4998-A532-78D6F6F76244
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SPB Device Stacks


The Windows Driver Model cleanly separates the driver components that control a peripheral device (for example, a temperature sensor) on a bus from the driver components that manage the bus controller, which transfers data and control information to and from the peripheral device. This separation enables the hardware vendor for a peripheral device that connects to a [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB) to write a driver that controls the device a variety of bus controllers, bus types, and hardware platforms. Similarly, the hardware vendor for an SPB controller can write a driver for this controller that can enable connections to a variety of peripheral devices.

In Windows, a peripheral device that is attached to a Plug and Play (PnP) bus is represented by two, and possibly more, [*device objects*](https://msdn.microsoft.com/library/windows/hardware/ff548014). The device objects for this device are organized hierarchically to form a [*device stack*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-stack). A *functional* device object (FDO) represents the internal state of the device, and is created and owned by the function driver that controls the peripheral device's internal functions. Below the FDO in the stack is a *physical* device object (PDO) that represents the device's connection to the bus. The PDO is created and owned by the bus controller driver that detects and enumerates the device for the PnP manager. This PDO contains the information (for example, bus address) that the bus controller needs to access the device over the bus. If the function driver requires assistance from the bus controller to perform an I/O operation on the device, the function driver sends an I/O request packet (IRP) down the device stack to the PDO, and the bus controller driver receives the IRP. For more information, see [Device Objects and Device Stacks](https://msdn.microsoft.com/library/windows/hardware/ff543153).

In contrast, an SPB (for example, an I²C or SPI bus) does not support PnP, and the SPB controller driver does not detect and enumerate the peripheral devices on the SPB. Instead, the hardware platform's ACPI firmware describes these devices and their bus connections, and the ACPI driver, Acpi.sys, enumerates these devices for the PnP manager.

Additionally, Acpi.sys creates the PDO for a peripheral device on an SPB. To perform an I/O operation on this device, the device's function driver does not send an IRP down the stack to the PDO because the PDO is owned by Acpi.sys, which cannot perform I/O operations. Instead, the function driver must send the IRP to the SPB controller driver. The SPB controller driver owns the FDO for the SPB controller, which is not in the same device stack as the FDO for the peripheral device. To send this IRP, the device's function driver must first open a logical connection to the SPB controller and receive a WDFFILEOBJECT object handle to this connection. The driver then specifies this handle as the target for the IRPs that it sends to the device. The SPB controller driver receives these IRPs and (in conjunction with the [SPB framework extension](https://msdn.microsoft.com/library/windows/hardware/hh406203), SpbCx) performs the requested I/O operations on the device. For more information about opening logical connections to SPB controllers, see [Connection IDs for SPB Peripheral Devices](https://msdn.microsoft.com/library/windows/hardware/hh698216).

Some IRPs can be handled entirely by drivers that are above the SPB controller driver in the I/O-request chain, including the function driver for the peripheral device. However, IRPs that require transfers of data or control information to and from the peripheral device over the bus must be processed by the SPB controller driver.

A filter driver that is designed to operate with the function driver for an SPB peripheral device can be inserted above the function driver's FDO. However, inserting such a filter between the FDO and PDO has no effect because it cannot intercept the IRPs that are exchanged between the function driver and the SPB controller driver.

If necessary, a filter driver can be inserted above the SPB controller driver (and SpbCx, which manages the queues for IRPs sent to the SPB controller driver). However, the [SPB I/O request interface](https://msdn.microsoft.com/library/windows/hardware/hh698227) is a top-level driver interface, and drivers in the I/O-request chain must ensure that I/O requests are delivered in the context of the calling thread so that SpbCx and the SPB controller driver can access user-mode buffers during I/O transfers.

 

 




