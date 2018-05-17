---
title: Access Permissions for WIA Drivers
author: windows-driver-content
description: Access Permissions for WIA Drivers
ms.assetid: 593e9367-5304-4b04-8597-4a7c498b9f47
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Access Permissions for WIA Drivers


## <a href="" id="ddk-access-permissions-for-wia-drivers-si"></a>


In order for a driver and another component to use the same named object, the correct permissions should be set for that object when it is created. Typically, this involves setting the appropriate DACL in that object's security descriptor.

An easy way to do this is to use the SDDL functions provided in Windows 2000 and later. SDDL stands for Security Descriptor Definition Language and is a simple string representation of a Windows security descriptor, or SD. An SDDL string can be converted to an SD, and SDs can be converted to SDDL strings, which can be useful for comparing two security descriptors.

For an example of using SDDL to set the access permissions on an event object, see [WIA Security and Security Descriptors](wia-security-and-security-descriptors.md).

 

 




