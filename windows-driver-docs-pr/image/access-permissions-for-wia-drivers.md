---
title: Access Permissions for WIA Drivers
description: Access Permissions for WIA Drivers
ms.date: 03/27/2023
---

# Access Permissions for WIA Drivers

In order for a driver and another component to use the same named object, the correct permissions should be set for that object when it is created. Typically, this involves setting the appropriate DACL in that object's security descriptor.

An easy way to do this is to use Security Descriptor Definition Language (SDDL) functions. SDDL stands is a simple string representation of a Windows security descriptor, or SD. An SDDL string can be converted to an SD, and SDs can be converted to SDDL strings, which can be useful for comparing two security descriptors.

For an example of using SDDL to set the access permissions on an event object, see [WIA Security and Security Descriptors](wia-security-and-security-descriptors.md).
