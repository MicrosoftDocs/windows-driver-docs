---
title: USB-Specific UMDF 1.x Interfaces
description: USB-Specific UMDF 1.x Interfaces
ms.assetid: b458d96d-e15e-4a9b-a26e-490620cec38e
keywords:
- UMDF WDK , UMDF-USB object model
- User-Mode Driver Framework WDK , UMDF-USB object model
- user-mode drivers WDK UMDF , UMDF-USB object model
- UMDF-USB object model WDK UMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# USB-Specific UMDF 1.x Interfaces


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

A USB device can have one or more configurations. Each configuration can have one or more interfaces. Each interface is associated with one or more alternate settings, and each alternate setting defines one or more endpoints. An endpoint represents a buffer on the device hardware.

A pipe is a software abstraction of a connection between the host controller and an endpoint in the current alternate setting. A pipe can be a target for I/O, and is exposed in UMDF by the [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391) interface.

The USB-specific UMDF interfaces are built on top of the [WinUSB](https://msdn.microsoft.com/library/windows/hardware/ff540196) architecture. By design, WinUSB allows access only to the first configuration of a multiple configuration device. Therefore, the WinUSB interface does not expose the ability to submit a select-configuration request. Consequently, the I/O target functionality in UMDF does not support selecting any device configuration other than the first.

The USB-specific UMDF interfaces have an object hierarchy that is similar to that of the general USB model. A UMDF driver creates a target device object, which is exposed by the [IWDFUsbTargetDevice](https://msdn.microsoft.com/library/windows/hardware/ff560362) interface. The driver can then use methods of IWDFUsbTargetDevice to access USB interfaces, which are exposed by instances of [IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312). The driver can call IWDFUsbInterface methods to manipulate settings and endpoints.

The following table shows the USB-specific UMDF interface hierarchy:

| USB-specific UMDF interface                    | Derived from                     |
|------------------------------------------------|----------------------------------|
| [IWDFUsbTargetDevice](https://msdn.microsoft.com/library/windows/hardware/ff560362) | [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) |
| [IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312)       | [IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200)     |
| [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391)     | [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) |

 

The [IWDFUsbTargetDevice](https://msdn.microsoft.com/library/windows/hardware/ff560362) and [IWDFUsbTargetPipe](https://msdn.microsoft.com/library/windows/hardware/ff560391) interfaces derive from the [IWDFIoTarget](https://msdn.microsoft.com/library/windows/hardware/ff559170) interface and, therefore, expose I/O target objects. The [IWDFUsbInterface](https://msdn.microsoft.com/library/windows/hardware/ff560312) interface does not derive from IWDFIoTarget (IWDFUsbInterface derives from the [IWDFObject](https://msdn.microsoft.com/library/windows/hardware/ff560200) interface) and, therefore, does not expose an I/O target object. Any I/O sent to discover and manipulate interface details is sent to the target device.

For step-by-step directions on writing a simple UMDF-based USB client driver, see [How to write your first USB client driver (UMDF)](https://msdn.microsoft.com/library/windows/hardware/hh706184).

To learn about the source code required for a UMDF-based USB client driver, see [Understanding the USB client driver code structure (UMDF)](https://msdn.microsoft.com/library/windows/hardware/hh770893).

 

 





