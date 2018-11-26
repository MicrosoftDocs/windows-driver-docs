---
title: SPB Framework Extension (SpbCx)
description: Starting with Windows 8, the SPB framework extension (SpbCx) is a system-supplied extension to the Kernel-Mode Driver Framework (KMDF).
ms.assetid: 84015f3c-ff55-4c1a-bb52-63b6f29b99d7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SPB Framework Extension (SpbCx)


Starting with Windows 8, the SPB framework extension (SpbCx) is a system-supplied extension to the [Kernel-Mode Driver Framework](https://msdn.microsoft.com/library/windows/hardware/ff544296) (KMDF). SpbCx works together with an [SPB controller driver](https://msdn.microsoft.com/library/windows/hardware/hh698221) to perform I/O operations on peripheral devices that are connected to a [simple peripheral bus](https://msdn.microsoft.com/library/windows/hardware/hh450903) (SPB), such as I²C or SPI.

The SPB controller driver performs all hardware-specific operations. These operations include accessing the hardware registers of the SPB controller to configure the controller and to initiate bus transfers to and from SPB-connected peripheral devices.

SpbCx performs processing tasks that are common to SPB controller devices. In particular, SpbCx manages the I/O request queues for an SPB controller. These queues contain I/O requests for peripheral devices that are attached to the bus. The hardware vendor for the SPB controller supplies an SPB controller driver to perform all hardware-specific operations that are required to handle these requests.

The division of responsibilities between SpbCx and the SPB controller driver is as follows:

-   SpbCx manages the generic functions that are common to all members of the SPB controller device class. SpbCx provides much of the default request handling and flow control for the controller driver. Starting with Windows 8, SpbCx is an inbox component of the Windows operating system.

-   The SPB controller driver manages the hardware-specific functions in the SPB controller device. Hardware vendors supply controller drivers for their SPB controller devices.

SpbCx and the SPB controller driver run in kernel mode. SpbCx is a framework extension, and the SPB controller driver is a KMDF driver. The SPB controller driver calls the methods in the SpbCx device-driver interface (DDI) to perform SPB-specific operations, and calls KMDF methods to perform other, more generic driver functions. For information about building a KMDF driver, see [Building and Loading a Framework-Based Driver](https://msdn.microsoft.com/library/windows/hardware/ff540730).

SPB controller drivers statically link to the DDI entry points in the SpbCx stub library, Spbcx.lib. At run time, this library performs the necessary driver-version negotiation to dynamically link to the framework extension module, Spbcx.sys, which implements the DDI. An SPB controller driver that requires a particular version of Spbcx.sys can safely link to a version of Spbcx.sys that has a higher version number. However, this driver cannot link to a version of Spbcx.sys that has a lower version number. The SpbCx I/O request interface is similarly backward compatible.

Although a hardware vendor has the option of writing a monolithic SPB controller driver that does not use SpbCx, a significant effort is required to do so. By comparison, a controller driver that uses SpbCx is easier to develop and is typically more reliable.

 

 




