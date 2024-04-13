---
title: Implementing an Operation Region Handler
description: Provides information about implementing an operation region handler
keywords:
- ACPI devices WDK , operation regions
- operation regions WDK ACPI
- function drivers WDK ACPI , operation regions
- WDM function drivers WDK ACPI , operation regions
ms.date: 03/17/2023
---

# Implementing an Operation Region Handler

The driver must provide an operation region handler, which is a [**PACPI_OP_REGION_HANDLER**](/windows-hardware/drivers/ddi/oprghdlr/nc-oprghdlr-acpi_op_region_handler)-typed callback. The ACPI driver calls the operation handler to access the data fields in the driver's operation region. The combined operation of the function driver and the ACPI BIOS is vendor-defined and device-specific. In general, the function driver and the ACPI BIOS access indexes in an operation region that result in device-specific operations and return whatever information is appropriate.

An operation region handler typically uses the following parameters that the ACPI driver passes to the handler:

- *AccessType* specifies whether the access is a read or write.

    If the access is a read, data is transferred from the operation region memory buffer to the *Data* buffer. If the access is a write, data is transferred from the *Data* buffer to the operation region memory buffer. See [Accessing an Operation Region](accessing-an-operation-region.md).

- *Address* specifies a byte offset in the operation region memory buffer.

- *Size* specifies the number of bytes to transfer.

- *Data* specifies a buffer supplied by the ACPI driver for the data transfer.

- *Context* specifies the operation region context that the driver registered for the operation region handler.

    The operation region context is only used by the function driver and is device-specific.

In addition to the previously described parameters, the ACPI driver also passes to an operation region handler pointers to the following: an operation region object, a completion handler, and a completion context. However, the function driver does not use the operation region object in a handler, and the completion handler and context are reserved for internal use.
