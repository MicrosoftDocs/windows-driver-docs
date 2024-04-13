---
title: Windows Kernel-Mode Security Reference Monitor
description: Windows Kernel-Mode Security Reference Monitor
ms.date: 10/17/2018
---

# Windows Kernel-Mode Security Reference Monitor


An increasingly important aspect of operating systems is security. Before an action can take place, the operating system must be sure that the action is not a violation of system policy. For example, a device may or may not be accessible to all requests. When creating a driver, you may want to allow some requests to succeed or fail, depending on the permission of the entity making the request.

Windows uses an access control list (ACL) to determine which objects have what security. The Windows kernel-mode security reference monitor provides routines for your driver to work with access control. For more information about the ACL, see [Access Control List](../ifs/access-control-list.md).

Routines that provide a direct interface to the security reference monitor are prefixed with the letters "**Se**"; for example, **SeAccessCheck**. For a list of security reference monitor routines, see [Security Reference Monitor Routines](/previous-versions/windows/hardware/drivers/ff563711(v=vs.85)).

 

