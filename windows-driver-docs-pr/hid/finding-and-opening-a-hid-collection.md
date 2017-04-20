---
title: Finding and Opening a HID Collection
author: windows-driver-content
description: Finding and Opening a HID Collection
ms.assetid: b46fdb06-e6ae-4376-994f-69bf6539f2ce
keywords:
- collections WDK HID , finding
- HID collections WDK , finding
- finding HID collections
- collections WDK HID , opening
- HID collections WDK , opening
- opening HID collections
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Finding and Opening a HID Collection


## <a href="" id="ddk-finding-and-opening-a-hid-collection-kg"></a>


This section describes how user-mode applications and kernel-mode drivers find and open a top-level [HID collection](hid-collections.md).

### User-Mode Application

Microsoft Windows provides device installation routines (**SetupDi***Xxx* functions) to find and identify the HIDClass devices. Windows provides other Win32 functions to initialize and connect to a HID collection.

After a user-mode application is loaded, it does the following sequence of operations:

-   Calls [**HidD\_GetHidGuid**](https://msdn.microsoft.com/library/windows/hardware/ff538924) to obtain the system-defined GUID for HIDClass devices.

-   Calls [**SetupDiGetClassDevs**](https://msdn.microsoft.com/library/windows/hardware/ff551069) to obtain a handle to an opaque device information set that describes the device interfaces supported by all the [HID collections](hid-collections.md) currently installed in the system. The application should specify DIGCF\_PRESENT and DIGCF\_DEVICEINTERFACE in the *Flags* parameter that is passed to **SetupDiGetClassDevs**.

-   Calls [**SetupDiEnumDeviceInterfaces**](https://msdn.microsoft.com/library/windows/hardware/ff551015) repeatedly to retrieve all the available interface information.

-   Calls [**SetupDiGetDeviceInterfaceDetail**](https://msdn.microsoft.com/library/windows/hardware/ff551120) to format interface information for each collection as a SP\_INTERFACE\_DEVICE\_DETAIL\_DATA structure. The **DevicePath** member of this structure contains the user-mode name that the application uses with the Win32 function [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) to obtain a file handle to a HID collection.

-   Calls [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) to obtain a file handle to a HID collection.

### Kernel-Mode Driver

If a kernel-mode driver is a function or filter driver, it has attached a device object to the HID collection's device stack. The driver has to only use a create request to open the device.

If the driver is not a function or filter driver, it typically uses [Plug and Play notification](https://msdn.microsoft.com/library/windows/hardware/ff559640) to find a collection. After finding a collection, the driver uses a create request to open the collection.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Finding%20and%20Opening%20a%20HID%20Collection%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


