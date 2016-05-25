---
title: IRP\_MJ\_FILE\_SYSTEM\_CONTROL
author: windows-driver-content
description: IRP\_MJ\_FILE\_SYSTEM\_CONTROL
ms.assetid: 38b88379-c007-4e88-a6d9-5aacd6bdefd3
keywords: ["IRP_MJ_FILE_SYSTEM_CONTROL", "security WDK file systems , adding security checks", "security checks WDK file systems , IRP_MJ_FILE_SYSTEM_CONTROL", "file system controls WDK security", "set file information processing WDK file systems"]
---

# IRP\_MJ\_FILE\_SYSTEM\_CONTROL


A file system control allows the file system to perform essentially any specialized operation. The existing Windows file systems have a number of specialized controls and for them, as well as any third-party file systems developed for Windows, it is imperative to aggressively check all parameters. In addition, FSCTL operations often have restricted security rights. These can be seen in the FASTFAT sample code that the WDK contains (see the **FatInvalidateVolumes** function in fsctrl.c, for example). This is an example of a privilege check. The policy of the FASTFAT file system in this case is to require that the given privilege be enabled on the system.

The I/O manager will enforce FILE\_READ\_DATA and FILE\_WRITE\_DATA permissions on specific FSCTL operations, if the file system has set these bits in the file system operation definition using the CTL\_CODE macro. All other permissions required must be checked by the file system (FILE\_READ\_ATTRIBUTES permissions, for example) if this is the policy of the file system.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_FILE_SYSTEM_CONTROL%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


