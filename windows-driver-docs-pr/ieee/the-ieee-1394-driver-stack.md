---
title: The IEEE 1394 Driver Stack
description: The IEEE 1394 Driver Stack
ms.assetid: 3c8c218e-d814-451c-9a39-fe7fe5fb7aaf
keywords:
- IEEE 1394 WDK buses , driver stacks
- 1394 WDK buses , driver stacks
- driver stacks WDK IEEE 1394 bus
- stacks WDK IEEE 1394 bus
- device stacks WDK IEEE 1394 bus
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# The IEEE 1394 Driver Stack





The following diagram illustrates the IEEE 1394 driver stack with the new 1394 bus driver and the Microsoft-supported 1394 client drivers.

![diagram illustrating the ieee 1394 driver stack](images/1394driverstack.png)

A client driver for a device that connects to the IEEE 1394 bus driver sits on top of the IEEE 1394 driver stack. The bus driver provides a hardware-independent interface to the IEEE 1394 bus. The device driver communicates with the device by sending IRPs, which are processed by the IEEE 1394 bus driver. Before Windows 7, the bus driver was a combination of a port driver (1394bus.sys) and a primary miniport driver for the motherboard's host controller (ochi1394.sys). In Windows 7 and later versions, the legacy port/miniport bus drivers are replaced by 1394ohci.sys, a monolithic IEEE 1394 bus driver that is implemented by using the kernel-mode driver framework (KMDF). The 1394ohci.sys bus driver is fully backward compatible with the legacy 1394 bus drivers. For more information about some known differences in behavior between the new bus driver and the legacy 1394 bus drivers, see [IEEE 1394 Bus Driver in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266402).

The following illustration shows the relationship between the legacy and the new 1394 bus drivers.

![Diagram showing the relationship between the legacy and the new 1394 bus drivers.](images/1394busdriver.png)

To issue commands to devices connected to the bus, drivers issue the [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) IRP, with control code [**IOCTL\_1394\_CLASS**](https://msdn.microsoft.com/library/windows/hardware/ff537232). The driver packages the parameters in an IEEE 1394 I/O request block ([**IRB**](https://msdn.microsoft.com/library/windows/hardware/ff537350)), and passes a pointer to it in the **Parameters.Others.Argument1** member of the IRP. The **FunctionNumber** member of the IRB determines the type of operation, and the **u** member describes the operation. The bus driver uses the IOCTL\_1394\_CLASS IRP to present an interface to both the bus and the host controller.

The IRB structure contains parameters that apply to each bus request and request-specific parameters. The **u** member of the IRB contains the request-specific parameters, in a union of data structures, one per request type.

During normal operation, drivers receive ordinary I/O requests (such as [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794)), convert them to the appropriate IEEE 1394 operation, and dispatch that operation to the device through IOCTL\_1394\_CLASS.

## Related topics
[IEEE 1394 Bus Driver in Windows 7](https://msdn.microsoft.com/library/windows/hardware/gg266402)  



