---
title: Evaluating ACPI Control Methods
description: Provides information about evaluating ACPI control methods
keywords:
- ACPI control methods WDK , evaluating
- ACPI devices WDK , evaluating control methods
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Evaluating ACPI Control Methods

An Advanced Configuration and Power Interface (ACPI) control method is software that declares and defines operations to query and configure system hardware. An ACPI-compatible system provides a minimal set of control methods. Control methods are written in the ACPI Source Language (ASL), compiled by an ASL compiler into ACPI Machine Language (AML), loaded from the system firmware into the ACPI namespace, and interpreted by the ACPI driver.

Kernel-mode device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](../kernel/index.md) or [Windows Driver Model (WDM)](../kernel/writing-wdm-drivers.md) can evaluate ACPI control methods by using device control requests. Starting with Windows 8, user-mode drivers that comply with the requirements of [User-Mode Driver Framework (UMDF)](../wdf/getting-started-with-umdf-version-2.md) can use device control requests to evaluate ACPI control methods. Typically, a driver evaluates ACPI control methods to start or configure platform-specific functions. A driver can evaluate ACPI control methods within the namespace of the *physical device object (PDO)* for which it is loaded. For drivers loaded in the device stack of an ACPI-enumerated device, the ACPI driver is always the bus driver that created and operates the PDO in the device stack. This capability includes evaluating control methods that are supported by child objects that are descendants of a parent device.

A driver evaluates control methods by sending one of the following [**IRP_MJ_DEVICE_CONTROL**](../kernel/irp-mj-device-control.md) requests to a device.

- [**IOCTL_ACPI_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method)

    This request synchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an event object that waits for the request to complete. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

- [**IOCTL_ACPI_ASYNC_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_async_eval_method)

    This request asynchronously evaluates a control method that is supported by the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the name of a method, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request. The method must be an immediate child object in the ACPI namespace of the device to which the request is sent.

- [**IOCTL_ACPI_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex)

    This request synchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an event object that waits for the request to complete.

- [**IOCTL_ACPI_ASYNC_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_async_eval_method_ex)

    This request asynchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent. To use this IOCTL, a driver for the device supplies input and output method argument buffers, the path and name of the control method in the ACPI namespace of the device, and an *IoCompletion* routine that the I/O manager calls after all lower-level drivers have completed the request.

For more information about how to evaluate ACPI control methods synchronously, see [Evaluating ACPI Control Methods Synchronously](evaluating-acpi-control-methods-synchronously.md). For more information about how to evaluate ACPI control methods asynchronously, see [**IOCTL_ACPI_ASYNC_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_async_eval_method) and [**IOCTL_ACPI_ASYNC_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_async_eval_method_ex).

For a driver of a device to evaluate a control method that is not an immediate child object of the device, the driver must supply the path and name of the method in the ACPI namespace of the device. To help obtain the path and name of child objects of a device, Windows supports the [**IOCTL_ACPI_ENUM_CHILDREN**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_enum_children) request, which a driver for a device can use to enumerate the following:

- The device and its immediate child devices.

- The device and all its descendant child devices.

- Descendant child objects of a supplied name in the ACPI namespace of the device including, in particular, control methods.

For information about how to enumerate devices and methods in the namespace of a device, see [Enumerating Child Devices and Control Methods](enumerating-child-devices-and-control-methods.md).

For information about system-supplied macros that a driver can use to help evaluate control methods, see [Control Method Macros](control-method-macros.md).

For more information about ACPI devices, control methods, and namespaces, see the [Advanced Configuration and Power Interface Specification](https://uefi.org/specifications).
