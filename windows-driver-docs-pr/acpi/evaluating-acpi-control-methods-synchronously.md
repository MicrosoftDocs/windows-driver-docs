---
title: Evaluating ACPI Control Methods Synchronously
description: Provides information about evaluating ACPI control methods synchronously
keywords:
- ACPI control methods WDK , evaluating synchronously
- ACPI control methods WDK , input buffer structures
- ACPI control methods WDK , SendDownStreamIrp code sample
ms.date: 08/17/2021
ms.localizationpriority: medium
---

# Evaluating ACPI Control Methods Synchronously

A device driver can use the following device control requests to synchronously evaluate control methods that are defined in the ACPI namespace of a device:

- [**IOCTL_ACPI_EVAL_METHOD**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method)

    This request evaluates a control method that is an immediate child object in the ACPI namespace of the device to which the request is sent.

- [**IOCTL_ACPI_EVAL_METHOD_EX**](/windows-hardware/drivers/ddi/acpiioct/ni-acpiioct-ioctl_acpi_eval_method_ex)

    This request synchronously evaluates a control method that is supported by the device or a descendant child object of the device to which the request is sent.

The [Windows ACPI driver](../kernel/acpi-driver.md), Acpi.sys, handles these requests on behalf of devices that are specified in the system description tables in the [ACPI BIOS](../kernel/acpi-bios.md). These requests can be used by kernel-mode device drivers that comply with the requirements of [Kernel-Mode Driver Framework (KMDF)](../wdf/index.md) or [Windows Driver Model (WDM)](../kernel/introduction-to-wdm.md). Starting with Windows 8, user-mode device drivers that comply with the requirements of [User-Mode Driver Framework (UMDF)](../wdf/overview-of-the-umdf.md) can use these requests.

For example, a WDM driver performs the following sequence of operations to use one of these IOCTLs:

1. Calls [**IoBuildDeviceIoControlRequest**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iobuilddeviceiocontrolrequest) to build the request.

1. Calls [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) to send the request down the device stack.

1. Waits for the I/O manager to signal the driver that the lower-level drivers have completed the request.

1. Checks the status of the request.

1. Checks the validity of the output arguments.

1. Processes the output arguments that are returned to the driver.

1. Completes the request.

To build a request, a driver calls **IoBuildDeviceIoControlRequest** and supplies the following parameters:

- *IoControlCode* is set to **IOCTL_ACPI_EVAL_METHOD** or **IOCTL_ACPI_EVAL_METHOD_EX**.

- *DeviceObject* is set to a pointer to the physical device object (PDO) of the device.

- *InputBuffer* is set to a pointer to an input buffer structure that depends on the type of input arguments to be passed to the control method. The ACPI driver supports methods that take no input arguments, that take a single integer, that take an ASCII string, or that take a custom array of input arguments. For more information about the supported input buffer structures, see [Control Method Input Buffer Structures](control-method-input-buffer-structures.md).

- *InputBufferLength* is set to the size, in bytes, of the input buffer that is supplied by *InputBuffer*.

- *OutputBufferLength* supplies the size, in bytes, of the output buffer that is supplied by *OutputBuffer*.

- *InternalDeviceIoControl* is set to **FALSE**.

- *Event* is set to a pointer to a caller-allocated and initialized event object. The driver waits until the I/O manager signals this event, which indicates that the lower-level drivers have completed the request.

- *OutputBuffer* supplies a pointer to an [**ACPI_EVAL_OUTPUT_BUFFER**](/windows-hardware/drivers/ddi/acpiioct/ns-acpiioct-_acpi_eval_output_buffer_v1) structure that contains the output arguments from the control method. Output arguments are specific to a given control method. For a driver to return any output, it must allocate a buffer that is large enough to hold all the output arguments.

- *IoStatusBlock* is set to an [**IO_STATUS_BLOCK**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_io_status_block) structure. This returns the status of the request that was set by the lower-level drivers.

For a code example of how to evaluate a control method that does not take input arguments, see [Evaluating a Control Method Without Input Arguments](evaluating-a-control-method-without-input-arguments.md).

For a code example of how to evaluate a control method that takes input arguments, see [Evaluating a Control Method that Takes Input Arguments](evaluating-a-control-method-that-takes-input-arguments.md).
