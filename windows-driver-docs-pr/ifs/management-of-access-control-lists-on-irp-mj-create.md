---
title: Management of Access Control Lists on IRP\_MJ\_CREATE
author: windows-driver-content
description: Management of Access Control Lists on IRP\_MJ\_CREATE
ms.assetid: 07b35931-8e20-4789-b2ef-14c6195b817f
keywords: ["IRP_MJ_CREATE", "access control list WDK file systems", "security checks WDK file systems , IRP_MJ_CREATE", "ACL WDK file systems"]
---

# Management of Access Control Lists on IRP\_MJ\_CREATE


## <span id="ddk_management_of_access_control_lists_on_irp_mj_create_if"></span><span id="DDK_MANAGEMENT_OF_ACCESS_CONTROL_LISTS_ON_IRP_MJ_CREATE_IF"></span>


There are numerous additional security-related issues that can be addressed within the file system. For example, the management of access control lists on disk is a major security issue. Given that security information might be identical on thousands of files, it is often useful for the file system to implement a sharing model for security descriptors. Thus, all files that use the same security descriptor share a single on-disk (and possibly in-memory) copy of the security descriptor. The NTFS file system uses this model.

An additional option would be for the file system to cache results. While not strictly related to security, it is important to realize that security operations can add substantial cost to ordinary operations, such as opening the file. Thus, caching security results from previous operations can allow the file system to rely upon previous decisions. For example, a new call that requests a subset of access previously granted to the same user on the same file could be summarily granted. Of course, the risk of adding any such mechanism is the potential for adding bugs, which allow improper access. It is important to ensure that any security implementation be thoroughly tested to ensure that it works in the manner expected.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Management%20of%20Access%20Control%20Lists%20on%20IRP_MJ_CREATE%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


