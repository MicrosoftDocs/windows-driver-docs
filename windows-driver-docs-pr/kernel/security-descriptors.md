---
title: Security Descriptors
description: Security Descriptors
ms.assetid: a5edd5e8-6fc7-4ab0-aebc-f0cd8e9299b6
keywords: ["security descriptors WDK objects", "system ACL WDK objects", "SACL WDK objects", "discretionary ACL WDK objects", "DACL WDK objects", "access control lists WDK objects", "ACL WDK objects"]
ms.date: 06/16/2017
ms.localizationpriority: medium
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

 

 




