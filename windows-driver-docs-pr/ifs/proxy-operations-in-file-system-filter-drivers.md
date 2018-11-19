---
title: Proxy Operations in File System Filter Drivers
description: Proxy Operations in File System Filter Drivers
ms.assetid: 01cc7a48-8b27-4de7-8968-8958e9512989
keywords:
- security WDK file systems , proxy operations
- proxy operations WDK file systems
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Proxy Operations in File System Filter Drivers


## <span id="ddk_proxy_operations_in_file_system_filter_drivers_if"></span><span id="DDK_PROXY_OPERATIONS_IN_FILE_SYSTEM_FILTER_DRIVERS_IF"></span>


File system filter drivers must frequently perform operations on behalf of the original (user-mode) caller. When doing so, it is imperative that the file system filter driver not perform an operation that might take an action that the original user could not. For example, suppose that a user attempts to open a file for FILE\_SUPERSEDE. A filter driver cannot then attempt to open the file specifying the same type of access using [**ZwCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff566424), for example, because even if the user did not have permission to supersede the file, the operation would succeed when performed by the file system filter driver.

The ways in which a file system filter driver might introduce such problems are many. They can occur any time a file system filter driver performs an operation on the underlying file system without knowing the results of the user's operation. A file system filter driver must thus identify such cases and ensure that it has either determined the outcome of the operation, or it has a mechanism for recovering from an error in the actual user operation. For example, in the case of a request to supersede the file, a filter driver might need to open the file on behalf of the original caller using [**IoCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff548418) indicating security rights on the file that would be sufficient for the supersede operation. If the filter driver were to use the IO\_FORCE\_ACCESS\_CHECK option, for example, a security check would be done with the credentials of the current thread, even though the call was from a kernel driver.

It is essential for a file system filter driver to identify instances where the driver is performing an operation on behalf of, or as a result of, some user level operation. In these cases, a clear strategy for how to ensure correct operation needs to be identified.

 

 




