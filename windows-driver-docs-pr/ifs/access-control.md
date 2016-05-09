---
title: Access Control
description: Access Control
ms.assetid: 7f87276f-4014-4b37-b051-4bf02acbf575
keywords: ["security WDK file systems , minimizing threats", "access control WDK file systems", "access validation WDK file systems", "validating security WDK file systems", "checking security"]
---

# Access Control


## <span id="ddk_access_control_if"></span><span id="DDK_ACCESS_CONTROL_IF"></span>


To protect themselves from inappropriate access, most drivers rely upon the default access controls applied by the I/O manager against their device objects. Other mechanisms are available to drivers. Perhaps the simplest for normal drivers is to apply an explicit security descriptor when they install their driver. An example of applying security descriptors to the device object are discussed in a later section.

A driver that implements its own security policy could rely upon the standard Windows APIs for assistance managing security access. In this case, the driver manages the storage of security descriptors and is responsible for invoking the security reference monitor routines to validate security. These include numerous routines, such as the following:

-   [**SeAccessCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563674)--this routine compares the security descriptor against the security credentials of the caller.

-   [**SePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff556686)--this routine determines if the given privileges are enabled for the caller.

-   [**SeSinglePrivilegeCheck**](https://msdn.microsoft.com/library/windows/hardware/ff563740)--this routine determines if a specific privilege is enabled for the caller.

-   [**SeAuditingFileOrGlobalEvents**](https://msdn.microsoft.com/library/windows/hardware/ff554778)--this routine indicates if the system has enabled auditing.

-   [**SeOpenObjectAuditAlarm**](https://msdn.microsoft.com/library/windows/hardware/ff556682)--this routine audits open object events.

This list is incomplete, but it describes a number of the key functions that can be used within a driver to perform access validation.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Access%20Control%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




