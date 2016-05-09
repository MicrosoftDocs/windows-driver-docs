---
title: Reparse Points in a File System Filter Driver
description: Reparse Points in a File System Filter Driver
ms.assetid: 6aae70d9-c934-4759-bb26-728b0ac025d1
keywords: ["security WDK file systems , reparse points", "reparse points WDK file systems"]
---

# Reparse Points in a File System Filter Driver


## <span id="ddk_reparse_points_in_a_file_system_filter_driver_if"></span><span id="DDK_REPARSE_POINTS_IN_A_FILE_SYSTEM_FILTER_DRIVER_IF"></span>


A filter driver that processes reparse points must be aware of the risk that an application program might create invalid reparse points. To ensure the strictest security, a driver that handles reparse points must ensure that the data contents of the reparse point itself are verifiable, whether through a secure checksum, encrypted contents, or some other mechanism that ensures invalid reparse points cannot be created by unprivileged applications. For example, a filter driver might require that its reparse points be encrypted using a password shared between an application (or the local security authority, for example), and the driver, in order to ensure that the data contents of the reparse point are valid.

Otherwise, it is possible that a malicious application could create reparse points that have invalid reparse point information. In this case, the file system filter driver must be prepared to handle invalid reparse point data, including self-referential data (data that creates reference loops that might cause some sort of overflow, for example), data overflow issues, and invalid data contents.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Reparse%20Points%20in%20a%20File%20System%20Filter%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




