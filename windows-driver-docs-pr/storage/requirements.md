---
title: Requirements
description: Requirements
ms.assetid: d939a319-f321-455e-a34d-220a3faf6092
---

# Requirements


The storage silo driver system meets the following requirements:

-   Targeted systems include Windows XP, Windows Vista, and Windows 7.

-   End-user experience for 1667 UFD devices must remain consistent with experience for legacy UFD devices.

-   Previous versions of Windows XP and Vista do not rely on modification of any existing system binaries other than USBStor.sys.

-   The storage silo driver system enables 1667 authentication class solutions while remaining flexible, serving as a platform for hardware vendor innovation. All third-party extension points are made available to vendors via user mode code.

-   Third-party applications granted non-exclusive access to silos which have not been claimed by a silo driver shall be supported.

-   Third-party UMDF drivers that claim exclusive ownership of a silo are supported. Applications or other drivers may only access the silo through this driver.

-   Third-party authentication silo drivers allow participation in the authorization workflow for an ACT. The vendor creates a UMDF driver that implements the published authentication DDI.

-   Backward compatibility allows legacy non-1667 devices to participate in platform experience that is otherwise reserved for 1667 devices.

-   The storage silo driver system manages device access on the host in accordance with Windows Group Policy. Policy may be applied at either the device or individual-silo level of granularity.

-   A dynamically changing ACL on the host grants exclusive ACT access rights to a single authorized user at a time in order to provide a secure solution that protects access to user data in a multi-user or fast user switch environment.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Requirements%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




