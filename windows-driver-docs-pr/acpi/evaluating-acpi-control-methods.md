---
title: Evaluating ACPI Control Methods
author: windows-driver-content
description: Evaluating ACPI Control Methods
MS-HAID:
- 'acpi-meth-eval-dg\_87baa061-4626-4822-bde0-7835cc11225f.xml'
- 'acpi.evaluating\_acpi\_control\_methods'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 00cf7530-30e6-4ff2-8a26-1c5143413b56
keywords: ["ACPI control methods WDK , evaluating", "ACPI devices WDK , evaluating control methods"]
---

# Evaluating ACPI Control Methods


An Advanced Configuration and Power Interface (ACPI) control method is software that declares and defines operations to query and configure system hardware. An ACPI-compatible system provides a minimal set of control methods. Control methods are written in the ACPI Machine Language (AML), loaded from the system firmware into the ACPI namespace, and interpreted by the ACPI driver.

Kernel-mode device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](https://msdn.microsoft.com/library/windows/hardware/dn265580) or [Windows Driver Model (WDM)](https://msdn.microsoft.com/library/windows/hardware/ff565698) can evaluate ACPI control methods by using device control requests. Starting with Windows 8, user-mode drivers that comply with the requirements of [User-Mode Driver Framework (UMDF)](https://msdn.microsoft.com/library/windows/hardware/ff560442) can use device control requests to evaluate ACPI control methods. Typically, a driver evaluates ACPI control methods to start or configure platform-specific functions. A driver can evaluate ACPI control methods within the namespace of the [*physical device object (PDO)*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-physical-device-object--pdo-) for which it is loaded. For drivers loaded in the device stack of an ACPI-enumerated device, the ACPI driver is always the bus driver that created and operates the PDO in the device stack. This capability includes evaluating control methods that are supported by child objects that are descendants of a parent device.

A driver evaluates control methods by sending one of the following [**IRP\_MJ\_DEVICE\_CONTROL**](https://msdn.microsoft.com/library/windows/hardware/ff550744) requests to a device.

-   [**IOCTL\_ACPI\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536148)

    This request synchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an event object that waits for the request to complete. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

-   [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536145) (Windows Server 2008, Windows Vista and later versions of Windows)

    This request asynchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

-   [**IOCTL\_ACPI\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536149) (Windows Server 2008, Windows Vista and later versions of Windows)

    This request synchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an event object that waits for the request to complete.

-   [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536146) (Windows Server 2008, Windows Vista and later versions of Windows)

    This request asynchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request.

For more information about how to evaluate ACPI control methods synchronously, see [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md). For more information about how to evaluate ACPI control methods asynchronously, see [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD**](https://msdn.microsoft.com/library/windows/hardware/ff536145) and [**IOCTL\_ACPI\_ASYNC\_EVAL\_METHOD\_EX**](https://msdn.microsoft.com/library/windows/hardware/ff536146).

For a driver of a device to evaluate a control method that is not an immediate child object of the device, the driver must supply the path and name of the method in the ACPI namespace of the device. To help obtain the path and name of child objects of a device, Windows Server 2008, Windows Vista and later versions of Windows support the [**IOCTL\_ACPI\_ENUM\_CHILDREN**](https://msdn.microsoft.com/library/windows/hardware/ff536147) request, which a driver for a device can use to enumerate the following:

-   The device and its immediate child devices.

-   The device and all its descendant child devices.

-   Descendant child objects of a supplied name in the ACPI namespace of the device including, in particular, control methods.

For information about how to enumerate devices and methods in the namespace of a device, see [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).

For information about system-supplied macros that a driver can use to help evaluate control methods, see [Control Method Macros](control-method-macros.md).

For more information about ACPI devices, control methods, and namespaces, see the [Advanced Configuration and Power Interface Specification](http://go.microsoft.com/fwlink/p/?linkid=57185).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bacpi\acpi%5D:%20Evaluating%20ACPI%20Control%20Methods%20%20RELEASE:%20%284/27/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


