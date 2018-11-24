---
title: Opening HID collections
description: This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.
ms.assetid: 97550D1D-2C37-4996-8522-DB18B1AA3C4A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Opening HID collections


This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device’s HID collections.

HID Clients can operate in the following modes:

-   Use- Mode Application/Driver
-   Kernel-Mode Driver

The following sections identify how the HID Client can communicate with HIDClass using either mode in the preceding list.

This section describes how user-mode applications and kernel-mode drivers operate [HID collections](hid-collections.md).

In general, a user-mode application does the following:

- Calls [device installation functions](https://msdn.microsoft.com/library/windows/hardware/ff541299) (**SetupDi***Xxx* functions) to find and identify a HID collection.

- Calls CreateFile to open a file on a HID collection.

- Calls **HidD\_**<em>Xxx</em> HID support routines to obtain a HID collection's [preparsed data](preparsed-data.md) and information about the HID collection.

- Calls ReadFile to read input reports and WriteFile to send output reports.

- Calls **HidP\_**<em>Xxx</em> HID support routines to interpret HID reports.

In general, a kernel-mode driver does the following:

- Finds and identifies a HID collection

  If the driver is a function or filter driver, it is already attached to the collection's device stack. However, if the driver is not attached to the collection's device stack, the driver can [use Plug and Play notification](https://msdn.microsoft.com/library/windows/hardware/ff565480).

- Uses an [**IRP\_MJ\_CREATE**](https://msdn.microsoft.com/library/windows/hardware/ff550729) request to open the HID collection

- Uses IOCTL\_HID\_*Xxx* requests to obtain the HID collection's preparsed data and information about the HID collection

- Uses [**IRP\_MJ\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff550794) requests to read input reports and [**IRP\_MJ\_WRITE**](https://msdn.microsoft.com/library/windows/hardware/ff550819) requests to send output reports

- Calls **HidP\_**<em>Xxx</em> HID support routines to interpret HID reports

For more information about operating a HID collection, see:

[Finding and Opening a HID Collection](finding-and-opening-a-hid-collection.md)

[Enforcing a Secure Read For a HID Collection](enforcing-a-secure-read-for-a-hid-collection.md)

[Obtaining Preparsed Data](obtaining-preparsed-data.md)

[Obtaining Collection Information](obtaining-collection-information.md)

[Handling HID Reports](handling-hid-reports.md)

[Freeing Resources](freeing-resources.md)

 

 




