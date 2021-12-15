---
title: Finding and Opening a HID Collection
description: Finding and Opening a HID Collection
keywords:
- collections WDK HID , finding
- HID collections WDK , finding
- finding HID collections
- collections WDK HID , opening
- HID collections WDK , opening
- opening HID collections
ms.date: 04/20/2017
---

# Finding and Opening a HID Collection





This section describes how user-mode applications and kernel-mode drivers find and open a top-level [HID collection](hid-collections.md).

### User-Mode Application

Microsoft Windows provides device installation routines (**SetupDi***Xxx* functions) to find and identify the HIDClass devices. Windows provides other Win32 functions to initialize and connect to a HID collection.

After a user-mode application is loaded, it does the following sequence of operations:

-   Calls [**HidD\_GetHidGuid**](/windows-hardware/drivers/ddi/hidsdi/nf-hidsdi-hidd_gethidguid) to obtain the system-defined GUID for HIDClass devices.

-   Calls [**SetupDiGetClassDevs**](/windows/win32/api/setupapi/nf-setupapi-setupdigetclassdevsw) to obtain a handle to an opaque device information set that describes the device interfaces supported by all the [HID collections](hid-collections.md) currently installed in the system. The application should specify DIGCF\_PRESENT and DIGCF\_DEVICEINTERFACE in the *Flags* parameter that is passed to **SetupDiGetClassDevs**.

-   Calls [**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) repeatedly to retrieve all the available interface information.

-   Calls [**SetupDiGetDeviceInterfaceDetail**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetaila) to format interface information for each collection as a SP\_INTERFACE\_DEVICE\_DETAIL\_DATA structure. The **DevicePath** member of this structure contains the user-mode name that the application uses with the Win32 function [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to obtain a file handle to a HID collection.

-   Calls [**CreateFile**](/windows/win32/api/fileapi/nf-fileapi-createfilea) to obtain a file handle to a HID collection.

### Kernel-Mode Driver

If a kernel-mode driver is a function or filter driver, it has attached a device object to the HID collection's device stack. The driver has to only use a create request to open the device.

If the driver is not a function or filter driver, it typically uses [Plug and Play notification](../kernel/pnp-notification-overview.md) to find a collection. After finding a collection, the driver uses a create request to open the collection.

 

