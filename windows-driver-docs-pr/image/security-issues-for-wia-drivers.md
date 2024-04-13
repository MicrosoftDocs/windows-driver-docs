---
title: Security Issues for WIA Drivers
description: Security Issues for WIA Drivers
ms.date: 08/25/2020
---

# Security Issues for WIA Drivers

Running services under a **LocalSystem** account can be dangerous, because **LocalSystem** is essentially Administrator and, therefore, has access to virtually any resource on the machine. Design flaws or buggy code in a service running under **LocalSystem** might result in an escalation of privilege for a destructive user. Windows XP introduced two new built-in service accounts, **LocalService** and **NetworkService**, specifically designed to mitigate the consequences of a service compromise. These two new accounts are restricted user accounts without any special privileges, except "Login as service".

In keeping with this security initiative, the WIA service runs under the **LocalService** account in Microsoft Windows Server 2003 and later operating system versions.

Prior to Windows Server 2003, the WIA service and WIA drivers were developed on the assumption that they would run under **LocalSystem**. This changed with Windows Server 2003 and has several ramifications that driver developers need to be aware of. This section contains a list of common problems that a WIA driver developer might experience, including possible ways to resolve them.

Following the practices outlined in this document ensures that the WIA drivers developed will function correctly whether running on Windows XP, Windows Server 2003, or later operating system versions.

[Common WIA Security Problems](common-wia-security-problems.md)

[WIA Security Best Practices](wia-security-best-practices.md)

For additional information about device driver security, see [Creating Secure Device Installations](../install/creating-secure-device-installations.md).
