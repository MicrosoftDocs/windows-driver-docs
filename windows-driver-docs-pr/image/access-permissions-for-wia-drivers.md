---
title: Access Permissions for WIA Drivers
author: windows-driver-content
description: Access Permissions for WIA Drivers
ms.assetid: 593e9367-5304-4b04-8597-4a7c498b9f47
ms.author: windows-driver-content
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Access%20Permissions%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


