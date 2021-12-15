---
title: Registering and Deregistering an Operation Region Handler
description: Provides information about registering and deregistering an operation region handler
keywords:
- ACPI devices WDK , operation regions
- operation regions WDK ACPI
- function drivers WDK ACPI , operation regions
- WDM function drivers WDK ACPI , operation regions
- registering operation region handlers
- deregistering operation region handlers
ms.date: 08/17/2021
---

# Registering and Deregistering an Operation Region Handler

An ACPI device function driver registers an operation region handler by calling [**RegisterOpRegionHandler**](/windows-hardware/drivers/ddi/oprghdlr/nf-oprghdlr-registeropregionhandler) and supplying the following information:

- The physical device object (PDO) representing the ACPI device that defines the operation region.

- The type of access, which can be *raw* or *cooked.*

    For more information, see [Accessing an Operation Region](accessing-an-operation-region.md)

- The type of region space.

    The vendor should specify a vendor-defined value from 0x80 to 0xFF. (Values less than 0x80 are defined by the ACPI specification and are reserved for internal use.)

- A pointer to the driver's operation region handler.

    The ACPI driver accesses an operation region by calling the driver's operation region handler.

- A pointer to the *operation region context*.

    The operation region context is device-specific and is only used by the function driver. When the ACPI driver calls the operation region handler, it passes the operation region context back to the handler. Typically, it is the device extension of the functional device object (FDO).

**RegisterOpRegionHandler** returns an operation region object that the function driver uses to uniquely identify the operation region handler only when the driver deregisters the handler.

Typically, a driver registers an operation region handler in the driver's Plug and Play dispatch routine after it starts an FDO in response to an [**IRP_MN_START_DEVICE**](../kernel/irp-mn-start-device.md) request. The driver must register the handler after it allocates the handler's operation region context. If the driver creates a vendor-defined device interface, the driver should enable the device interface after it registers the handler.

An ACPI device function driver deregisters an operation region handler by calling [**DeRegisterOpRegionHandler**](/windows-hardware/drivers/ddi/oprghdlr/nf-oprghdlr-deregisteropregionhandler) and supplying the following information:

- The PDO that represents the ACPI device that defines the operation region.

- The operation region object that the ACPI driver returned when the driver registered the operation region handler. This object uniquely identifies the operation region handler.

Typically, a driver deregisters an operation region handler in the driver's Plug and Play dispatch routine before it stops an FDO in response to an [**IRP_MN_STOP_DEVICE**](../kernel/irp-mn-stop-device.md) request. The driver must deregister the handler before it frees the handler's operation region context. If the driver creates a vendor-defined device interface, the driver should disable the device interface before it deregisters the handler.
