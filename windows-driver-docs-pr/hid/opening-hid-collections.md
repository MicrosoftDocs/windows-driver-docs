---
title: Opening HID Collections
description: This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device's HID collections.
ms.date: 01/11/2024
---

# Opening HID collections

This section describes how a HID Client can communicate with the HID Class driver (HIDClass) to operate the device's HID collections.

HID Clients can operate in the following modes:

- Use- Mode Application/Driver
- Kernel-Mode Driver

The following sections identify how the HID Client can communicate with HIDClass using either mode in the preceding list.

This section describes how user-mode applications and kernel-mode drivers operate [HID collections](hid-collections.md).

In general, a user-mode application does the following:

- Calls [device installation functions](/previous-versions/ff541299(v=vs.85)) (**SetupDi***Xxx* functions) to find and identify a HID collection.

- Calls CreateFile to open a file on a HID collection.

- Calls **HidD_***Xxx* HID support routines to obtain a HID collection's [preparsed data](preparsed-data.md) and information about the HID collection.

- Calls ReadFile to read input reports and WriteFile to send output reports.

- Calls **HidP_***Xxx* HID support routines to interpret HID reports.

In general, a kernel-mode driver does the following:

- Finds and identifies a HID collection

  If the driver is a function or filter driver, it is already attached to the collection's device stack. However, if the driver is not attached to the collection's device stack, the driver can [use Plug and Play notification](../kernel/using-pnp-notification.md).

- Uses an [**IRP_MJ_CREATE**](../kernel/irp-mj-create.md) request to open the HID collection

- Uses IOCTL_HID_*Xxx* requests to obtain the HID collection's preparsed data and information about the HID collection

- Uses [**IRP_MJ_READ**](../kernel/irp-mj-read.md) requests to read input reports and [**IRP_MJ_WRITE**](../kernel/irp-mj-write.md) requests to send output reports

- Calls **HidP_***Xxx* HID support routines to interpret HID reports

## See also

- [Finding and Opening a HID Collection](finding-and-opening-a-hid-collection.md)
- [Enforcing a Secure Read For a HID Collection](enforcing-a-secure-read-for-a-hid-collection.md)
- [Obtaining Preparsed Data](obtaining-preparsed-data.md)
- [Obtaining Collection Information](obtaining-collection-information.md)
- [Handling HID Reports](handling-hid-reports.md)
- [Freeing Resources](freeing-resources.md)
