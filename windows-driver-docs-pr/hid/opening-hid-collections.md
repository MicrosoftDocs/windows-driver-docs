---
title: Opening HID collections
author: windows-driver-content
description: This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.
ms.assetid: 97550D1D-2C37-4996-8522-DB18B1AA3C4A
---

# Opening HID collections


This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.

HID Clients can operate in the following modes:

-   Use- Mode Application/Driver
-   Kernel-Mode Driver

The following sections identify how the HID Client can communicate with HIDClass using either mode in the preceding list.

This section describes how user-mode applications and kernel-mode drivers operate [HID collections](hid-collections.md).

In general, a user-mode application does the following:

-   Calls [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) (**SetupDi***Xxx* functions) to find and identify a HID collection.

-   Calls CreateFile to open a file on a HID collection.

-   Calls **HidD\_***Xxx* HID support routines to obtain a HID collection's [preparsed data](preparsed-data.md) and information about the HID collection.

-   Calls ReadFile to read input reports and WriteFile to send output reports.

-   Calls **HidP\_***Xxx* HID support routines to interpret HID reports.

In general, a kernel-mode driver does the following:

-   Finds and identifies a HID collection

    If the driver is a function or filter driver, it is already attached to the collection's device stack. However, if the driver is not attached to the collection's device stack, the driver can [use Plug and Play notification](https://msdn.microsoft.com/library/windows/hardware/ff565480).

-   Uses an [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) request to open the HID collection

-   Uses IOCTL\_HID\_*Xxx* requests to obtain the HID collection's preparsed data and information about the HID collection

-   Uses [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) requests to read input reports and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests to send output reports

-   Calls **HidP\_***Xxx* HID support routines to interpret HID reports

For more information about operating a HID collection, see:

[Finding and Opening a HID Collection](finding-and-opening-a-hid-collection.md)

[Enforcing a Secure Read For a HID Collection](enforcing-a-secure-read-for-a-hid-collection.md)

[Obtaining Preparsed Data](obtaining-preparsed-data.md)

[Obtaining Collection Information](obtaining-collection-information.md)

[Handling HID Reports](handling-hid-reports.md)

[Freeing Resources](freeing-resources.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Opening%20HID%20collections%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


