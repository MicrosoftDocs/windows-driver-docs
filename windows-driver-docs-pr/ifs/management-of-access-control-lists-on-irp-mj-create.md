---
title: Management of Access Control Lists on IRP_MJ_CREATE
description: Management of Access Control Lists on IRP_MJ_CREATE
ms.assetid: 07b35931-8e20-4789-b2ef-14c6195b817f
keywords:
- IRP_MJ_CREATE
- access control list WDK file systems
- security checks WDK file systems , IRP_MJ_CREATE
- ACL WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Management of Access Control Lists on IRP\_MJ\_CREATE


## <span id="ddk_management_of_access_control_lists_on_irp_mj_create_if"></span><span id="DDK_MANAGEMENT_OF_ACCESS_CONTROL_LISTS_ON_IRP_MJ_CREATE_IF"></span>


There are numerous additional security-related issues that can be addressed within the file system. For example, the management of access control lists on disk is a major security issue. Given that security information might be identical on thousands of files, it is often useful for the file system to implement a sharing model for security descriptors. Thus, all files that use the same security descriptor share a single on-disk (and possibly in-memory) copy of the security descriptor. The NTFS file system uses this model.

An additional option would be for the file system to cache results. While not strictly related to security, it is important to realize that security operations can add substantial cost to ordinary operations, such as opening the file. Thus, caching security results from previous operations can allow the file system to rely upon previous decisions. For example, a new call that requests a subset of access previously granted to the same user on the same file could be summarily granted. Of course, the risk of adding any such mechanism is the potential for adding bugs, which allow improper access. It is important to ensure that any security implementation be thoroughly tested to ensure that it works in the manner expected.

 

 




