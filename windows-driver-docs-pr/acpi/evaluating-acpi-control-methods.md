---
title: Evaluating ACPI Control Methods
description: Evaluating ACPI Control Methods
ms.assetid: 00cf7530-30e6-4ff2-8a26-1c5143413b56
keywords:
- ACPI control methods WDK , evaluating
- ACPI devices WDK , evaluating control methods
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Evaluating ACPI Control Methods


An Advanced Configuration and Power Interface (ACPI) control method is software that declares and defines operations to query and configure system hardware. An ACPI-compatible system provides a minimal set of control methods. Control methods are written in the ACPI Source Language (ASL), compiled by an ASL compiler into ACPI Machine Language (AML), loaded from the system firmware into the ACPI namespace, and interpreted by the ACPI driver.

Kernel-mode device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](https://docs.microsoft.com/windows-hardware/drivers/kernel) or [Windows Driver Model (WDM)](https://docs.microsoft.com/windows-hardware/drivers/kernel/windows-driver-model) can evaluate ACPI control methods by using device control requests. Starting with Windows 8, user-mode drivers that comply with the requirements of [User-Mode Driver Framework (UMDF)](https://docs.microsoft.com/windows-hardware/drivers/wdf/getting-started-with-umdf-version-2) can use device control requests to evaluate ACPI control methods. Typically, a driver evaluates ACPI control methods to start or configure platform-specific functions. A driver can evaluate ACPI control methods within the namespace of the [*physical device object (PDO)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-physical-device-object--pdo-) for which it is loaded. For drivers loaded in the device stack of an ACPI-enumerated device, the ACPI driver is always the bus driver that created and operates the PDO in the device stack. This capability includes evaluating control methods that are supported by child objects that are descendants of a parent device.

A driver evaluates control methods by sending one of the following [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests to a device.

-   [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148)

    This request synchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an event object that waits for the request to complete. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

-   [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536145)

    This request asynchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

-   [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149)

    This request synchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an event object that waits for the request to complete.

-   [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536146)

    This request asynchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request.

For more information about how to evaluate ACPI control methods synchronously, see [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md). For more information about how to evaluate ACPI control methods asynchronously, see [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536145) and [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536146).

For a driver of a device to evaluate a control method that is not an immediate child object of the device, the driver must supply the path and name of the method in the ACPI namespace of the device. To help obtain the path and name of child objects of a device, Windows supports the [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request, which a driver for a device can use to enumerate the following:

-   The device and its immediate child devices.

-   The device and all its descendant child devices.

-   Descendant child objects of a supplied name in the ACPI namespace of the device including, in particular, control methods.

For information about how to enumerate devices and methods in the namespace of a device, see [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).

For information about system-supplied macros that a driver can use to help evaluate control methods, see [Control Method Macros](control-method-macros.md).

For more information about ACPI devices, control methods, and namespaces, see the [Advanced Configuration and Power Interface Specification](https://go.microsoft.com/fwlink/p/?linkid=866846).
