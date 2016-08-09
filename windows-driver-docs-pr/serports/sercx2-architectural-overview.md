---
title: SerCx2 Architectural Overview
author: windows-driver-content
description: SerCx2 works together with a serial controller driver to enable communication between a peripheral driver and a serially connected peripheral device.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: BA5D8966-ACC5-44ED-8CB8-61D1BCF39522
---

# SerCx2 Architectural Overview


SerCx2 works together with a serial controller driver to enable communication between a peripheral driver and a serially connected peripheral device. Typically, the serial controller is integrated into a System on a Chip (SoC) chip to provide low-pin-count communication with a peripheral device that is external to the SoC chip but is soldered to the same printed circuit board.

The following diagram shown the communication path between a serially connected peripheral device and the driver for this device. This peripheral driver runs in either kernel mode or user mode, and sends I/O requests to the serial port to which the peripheral device is connected.

![block diagram of sercx2 and associated components](images/sercx2modules.png)

SerCx2 and the serial controller driver both run in kernel mode, and communicate with each other through the SerCx2 device-driver interface (DDI). The serial controller driver calls driver-support methods that are implemented by SerCx2. SerCx2 calls event callback functions that are implemented by the serial controller driver.

Typically, the hardware registers of the serial controller are memory-mapped. The serial controller driver directly accesses these registers to configure the serial port, and to transfer data to and from the peripheral device that is connected to the serial port. For longer data transfers, SerCx2 typically uses DMA transfers (not shown in the preceding diagram).

The information that the peripheral driver needs to open a logical connection to the peripheral device is encapsulated in a special type of hardware resource that is called a *connection ID*. For more information, see [Connection IDs for Serially Connected Peripheral Devices](connection-ids-for-serially-connected-peripheral-devices.md).

Typically, only drivers send I/O requests directly to a serial controller. When a user-mode application needs to communicate with a serially connected peripheral device, the peripheral driver for the device acts as intermediary between the application and the device. If the application needs to transfer data to or from the peripheral device, the application sends a write ([**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904)) request or read ([**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883)) request to the peripheral driver, and the peripheral driver responds by sending a corresponding write or read request to the serial controller. In addition, the peripheral driver can send device I/O control requests (IOCTLs) to configure the serial port. For a list of IOCTLs supported by SerCx2, see [Serial I/O Request Interface](serial-i-o-request-interface.md).

The peripheral driver that sends I/O requests to the serial controller is either a kernel-mode driver that uses the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff544296) (KMDF), or a user-mode driver that uses the [User-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff560442) (UMDF). SerCx2 manages the queues of I/O requests sent to the serial controller by the peripheral driver.

In response to a read or write request, SerCx2 initiates one or more I/O transactions to move data between the serial controller and the data buffer in the request. Each I/O transaction uses either programmed I/O (PIO) or DMA to transfer data between the serial controller and the data buffer in the request. The types of I/O transactions supported by a serial controller driver depend on the hardware capabilities of the serial controller. For more information, see [Overview of SerCx2 I/O Transactions](overview-of-sercx2-i-o-transactions.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20SerCx2%20Architectural%20Overview%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


