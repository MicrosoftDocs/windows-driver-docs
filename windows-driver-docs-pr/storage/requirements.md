---
title: Requirements
description: Requirements
ms.assetid: d939a319-f321-455e-a34d-220a3faf6092
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 




