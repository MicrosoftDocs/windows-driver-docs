---
title: Enforcing a Secure Read For a HID Collection
author: windows-driver-content
description: Enforcing a Secure Read For a HID Collection
ms.assetid: be3c7d1b-195c-4b7f-a404-070b3b265333
keywords:
- collections WDK HID , secure reads
- HID collections WDK , secure reads
- secure reads WDK HID
- trusted secure reads WDK HID
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Enforcing a Secure Read For a HID Collection


## <a href="" id="ddk-enforcing-a-secure-read-for-a-hid-collection-kg"></a>


This section describes how a user-mode application or kernel-mode driver can enforce a *secure read* for a top-level [HID collection](hid-collections.md).

If a secure read is enabled for a collection, only "trusted" clients (those with SeTcbPrivilege privileges) can obtain input from an open file of a collection. Kernel-mode drivers have SeTcbPrivilege privileges by default, but user-mode applications do not. For information about how to obtain system privileges in user mode, see the information about authorization in the Microsoft Windows SDK documentation.

This mechanism is provided primarily so that "trusted" user-mode system components can prevent user-mode applications without SeTcbPrivilege privileges from obtaining input from a collection during critical system operations. For example, a "trusted" user-mode system component can prevent a user-mode application without SeTcbPrivilege privileges from obtaining confidential information that a user supplies during a logon operation.

"Trusted" clients use [**IOCTL\_HID\_ENABLE\_SECURE\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff541081) and [**IOCTL\_HID\_DISABLE\_SECURE\_READ**](https://msdn.microsoft.com/library/windows/hardware/ff541077) requests to enable and disable a secure read for a collection. If a client without SeTcbPrivilege privileges uses these requests, the request does not change the secure read state of a collection, and the HID class driver returns a status value of STATUS\_PRIVILEGE\_NOT\_HELD.

Enabling and disabling a secure read for a collection works in the following way:

-   The HID class driver maintains a file-specific secure read count for each open file of a collection. The HID class driver also maintains a secure read count for the collection, which is the sum of the file-specific secure read counts. The secure read count for the collection is initialized to zero when the collection is created, and a secure read count for a file is initialized to zero when a file is opened.

-   When the HID class driver receives an enable request for a file, it increments by 1 the secure read count for the file (and increments by 1 the secure read count for the collection).

-   When the HID class driver receives a disable request for a file:
    -   If the secure read count for the file is greater than zero, the driver decrements by 1 the secure read count for the file (and decrements by 1 the secure read count for the collection).
    -   If the secure read count for the file is equal to zero, the driver does not change the secure read counts.
-   If the secure read count for a collection is greater than zero, the HID class driver enforces a secure read for the collection. Otherwise, the driver does not enforce a secure read for the collection.

-   A client should use a disable request to cancel a corresponding enable request. However, if the client does not do this, the HID class driver appropriately decrements the secure read count for a collection when it processes an [**IRP\_MJ\_CLOSE**](https://msdn.microsoft.com/library/windows/hardware/ff550720) request for a file. When the driver processes the close request, it decrements the secure read count for the collection by the secure read count for the file being closed.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhid\hid%5D:%20Enforcing%20a%20Secure%20Read%20For%20a%20HID%20Collection%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


