---
title: Security Descriptors
author: windows-driver-content
description: Security Descriptors
ms.assetid: a5edd5e8-6fc7-4ab0-aebc-f0cd8e9299b6
keywords: ["security descriptors WDK objects", "system ACL WDK objects", "SACL WDK objects", "discretionary ACL WDK objects", "DACL WDK objects", "access control lists WDK objects", "ACL WDK objects"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Security Descriptors


Every object has a *security descriptor*, which contains the security settings for an object. In kernel-mode, the opaque [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563689) data type represents a security descriptor.

Information in a security descriptor is stored in *access control lists* (ACLs). An access control list is made up of a series of *access control entries* (ACEs).

A security descriptor has two separate ACLs:

-   A *system ACL* (SACL), which determines which operations on an object are logged.

-   A *discretionary ACL* (DACL), which determines which users can perform particular operations on the object.

Typically, a driver developer is only concerned with discretionary ACLs. For more information about system ACLs, see the Microsoft Windows SDK.

For a discretionary ACL, each ACE contains three pieces of information:

-   A *security identifier* (SID). The security identifier determines who the ACE applies to. A SID can represent a single user, or a group of users. For example, the World SID represents the set of all users.

-   A set of access rights. For a description of access rights, see [Access Rights](access-rights.md).

-   Whether the set of access rights is granted, or denied.

For a driver, the most important security descriptors are those for the driver's device objects. For more information, see [Securing Device Objects](securing-device-objects.md).

For more information about security descriptors in general, see the Windows SDK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Security%20Descriptors%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


