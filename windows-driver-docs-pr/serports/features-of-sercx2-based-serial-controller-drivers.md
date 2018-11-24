---
title: Features of SerCx2-Based Serial Controller Drivers
description: A SerCx2-based serial controller driver is a KMDF driver that uses the methods and callbacks in KMDF to perform generic driver operations, and that communicates with SerCx2 to perform operations that are specific to serial controller drivers.
ms.assetid: 4A9B80F1-4DE1-4D35-ADDF-90058A4F8388
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Features of SerCx2-Based Serial Controller Drivers


SerCx2 is an extension to the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff544296) (KMDF) that has special features to support serial controller drivers. A SerCx2-based serial controller driver is a KMDF driver that uses the methods and callbacks in KMDF to perform generic driver operations, and that communicates with SerCx2 to perform operations that are specific to serial controller drivers.

Typically, serial controllers are compatible at the hardware level with 16550 universal asynchronous receiver/transmitter (UART) devices. UARTs have been used since the early days of personal computing to control the serial ports located on the cases of desktop PCs. More recently, serial controllers are contained in System on a Chip (SoC) integrated circuits to provide low-pin-count communication with other integrated circuits. In a SoC-based hardware platform, the "serial port" to which a client sends I/O requests is simply a set of serial interface pins on the SoC chip. For more information, see [Serial Controller Drivers Overview](serial-drivers-overview.md).

Microsoft might supply the serial controller driver for a family of serial controllers that have similar hardware features. Or, the hardware vendor for a serial controller that has special features might supply a custom serial controller driver to support these features.

A serial controller driver communicates with SerCx2 through a device driver interface (DDI). The SerCx2 DDI has two parts:

-   A set of driver-support methods that are implemented by SerCx2 and that are called by the serial controller driver.
-   A set of event callback functions that are implemented by the serial controller driver and are called by SerCx2.

For detailed descriptions of the methods and callbacks in the SerCx2 DDI, see [Version 2 Serial Framework Extension (SerCx2) Reference](https://msdn.microsoft.com/library/windows/hardware/dn265349).

Although a hardware vendor has the option of writing a stand-alone serial controller driver, a significant effort is required to do so. By comparison, developing a serial controller driver that uses SerCx2 is easier and typically results in a driver that is much smaller and more reliable.

SerCx2 manages the following tasks on behalf of the controller driver:

-   Read and write operations
-   Serial I/O time-out detection
-   Hardware events
-   System DMA transfers (if system DMA transactions are supported)
-   Transitions to and from low-power device states
-   Cancellations of I/O requests (except during custom I/O transactions)

To manage read and write operations, SerCx2 transforms [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff546883) and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff546904) requests from clients into relatively simple I/O transactions for the serial controller driver to process. For more information, see [SerCx2 I/O Transactions](sercx2-i-o-transactions.md).

SerCx2 is included in Windows as a component named Sercx2.sys. The serial controller driver statically links to the SerCx2 library, Sercxstubs.lib (version 2.0), and, at run time, communicates with Sercx2.sys. The SerCx2 DDI is defined in the 2.0\\Sercx.h header file. Sercxstubs.lib and Sercx.h are available in the Windows Driver Kit for Windows 8.1.

 

 




