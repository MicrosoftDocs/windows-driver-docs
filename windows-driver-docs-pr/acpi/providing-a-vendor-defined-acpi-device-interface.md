---
title: Providing a Vendor-Defined ACPI Device Interface
description: Describes providing a vendor-defined ACPI device interface
keywords:
- ACPI devices WDK , device interfaces
- vendor-defined device interfaces WDK ACPI
- device interfaces WDK ACPI
- function drivers WDK ACPI , vendor-defined device interfaces
- WDM function drivers WDK ACPI , vendor-defined device interfaces
ms.date: 03/17/2023
---

# Providing a Vendor-Defined ACPI Device Interface

A vendor can provide an optional *device interface* and support for custom IOCTLs to operate an ACPI device's functional device object (*FDO*).

The function driver typically calls [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioregisterdeviceinterface) in its [**AddDevice**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine to register a device interface. The driver calls [**IoSetDeviceInterfaceState**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacestate) to enable the interface after Plug and Play starts the FDO. The driver should disable the interface if a device is removed by Plug and Play.

The device interface class GUID is vendor-defined.
