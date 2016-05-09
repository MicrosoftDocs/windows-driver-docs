---
title: Elevation of Privilege
description: Elevation of Privilege
ms.assetid: 08e20c51-fbc1-4e38-b12d-f123e4a2ba10
keywords: ["threat models WDK file systems , elevation-of-privilege", "security threat models WDK file systems , elevation-of-privilege", "elevation-of-privilege WDK file systems", "buffers WDK file systems"]
---

# Elevation of Privilege


## <span id="ddk_elevation_of_privilege_if"></span><span id="DDK_ELEVATION_OF_PRIVILEGE_IF"></span>


An elevation-of-privilege occurs when an application gains rights or privileges that should not be available to them. Many of the elevation-of-privilege exploits are similar to exploits for other threats. For example, buffer overrun attacks that cleverly attempt to write executable code. This works on the x86-based architecture when a buffer is allocated from the stack as a local variable. The stack also contains the return address of the current procedure call. If a malicious developer ascertains that there is a buffer overflow potential, data can be placed in the buffer so that it overwrites the return address. When the CPU executes the "ret" instruction to return back to the previous caller, it will return control to the location specified by the malicious developer and not the real caller.

For file systems and file system filter drivers, the possibility of an elevation--of-privilege attack is quite high due to a combination of the following reasons:

-   File systems and file system filter drivers are actively involved in managing access to data, including privileges.

-   File systems and file system filter drivers exploit special privileges and access rights to implement their features.

-   Many of the operating system privileges directly relate to file systems (**SeChangeNotifyPrivilege**, which controls the ability to traverse directories, for example).

This type of exploit is most important for those implementing file systems. This exploit can be an issue to file system filter drivers that are actively managing data storage (encryption filters, for example) that might circumvent or bypass normal file system security operations.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Elevation%20of%20Privilege%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




