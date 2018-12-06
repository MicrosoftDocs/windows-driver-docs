---
title: Access Permissions for WIA Drivers
description: Access Permissions for WIA Drivers
ms.assetid: 593e9367-5304-4b04-8597-4a7c498b9f47
ms.date: 07/18/2018
ms.localizationpriority: medium
---

# Access Permissions for WIA Drivers

In order for a driver and another component to use the same named object, the correct permissions should be set for that object when it is created. Typically, this involves setting the appropriate DACL in that object's security descriptor.

An easy way to do this is to use Security Descriptor Definition Language (SDDL) functions. SDDL stands is a simple string representation of a Windows security descriptor, or SD. An SDDL string can be converted to an SD, and SDs can be converted to SDDL strings, which can be useful for comparing two security descriptors.

For an example of using SDDL to set the access permissions on an event object, see [WIA Security and Security Descriptors](wia-security-and-security-descriptors.md).

