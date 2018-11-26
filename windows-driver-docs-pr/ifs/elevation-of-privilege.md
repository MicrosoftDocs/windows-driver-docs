---
title: Elevation of Privilege
description: Elevation of Privilege
ms.assetid: 08e20c51-fbc1-4e38-b12d-f123e4a2ba10
keywords:
- threat models WDK file systems , elevation-of-privilege
- security threat models WDK file systems , elevation-of-privilege
- elevation-of-privilege WDK file systems
- buffers WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Elevation of Privilege


## <span id="ddk_elevation_of_privilege_if"></span><span id="DDK_ELEVATION_OF_PRIVILEGE_IF"></span>


An elevation-of-privilege occurs when an application gains rights or privileges that should not be available to them. Many of the elevation-of-privilege exploits are similar to exploits for other threats. For example, buffer overrun attacks that cleverly attempt to write executable code. This works on the x86-based architecture when a buffer is allocated from the stack as a local variable. The stack also contains the return address of the current procedure call. If a malicious developer ascertains that there is a buffer overflow potential, data can be placed in the buffer so that it overwrites the return address. When the CPU executes the "ret" instruction to return back to the previous caller, it will return control to the location specified by the malicious developer and not the real caller.

For file systems and file system filter drivers, the possibility of an elevation--of-privilege attack is quite high due to a combination of the following reasons:

-   File systems and file system filter drivers are actively involved in managing access to data, including privileges.

-   File systems and file system filter drivers exploit special privileges and access rights to implement their features.

-   Many of the operating system privileges directly relate to file systems (**SeChangeNotifyPrivilege**, which controls the ability to traverse directories, for example).

This type of exploit is most important for those implementing file systems. This exploit can be an issue to file system filter drivers that are actively managing data storage (encryption filters, for example) that might circumvent or bypass normal file system security operations.

 

 




