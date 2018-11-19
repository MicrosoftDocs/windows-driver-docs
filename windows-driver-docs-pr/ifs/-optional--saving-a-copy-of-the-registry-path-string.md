---
title: '[Optional] Saving a Copy of the Registry Path String'
description: '[Optional] Saving a Copy of the Registry Path String'
ms.assetid: cf3b8649-6fb0-4ada-816c-5c7783918b2f
keywords:
- RegistryPath string copies
- saving RegistryPath string copies
- copying RegistryPath strings
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# \[Optional\] Saving a Copy of the Registry Path String


## <span id="ddk_saving_a_copy_of_the_registry_path_string_if"></span><span id="DDK_SAVING_A_COPY_OF_THE_REGISTRY_PATH_STRING_IF"></span>


**Note**   This step is necessary only if the filter driver needs to use the registry path after the **DriverEntry** routine returns.

 

Save a copy of the *RegistryPath* string that was passed as input to **DriverEntry**. This parameter points to a counted Unicode string that specifies a path to the driver's registry key, **\\Registry\\Machine\\System\\CurrentControlSet\\Services\\**<em>DriverName</em>, where *DriverName* is the name of the driver. If the *RegistryPath* string will be needed later, **DriverEntry** must save a copy of it, not just a pointer to it, because the pointer is no longer valid after the **DriverEntry** routine returns. You can use the [**RtlCopyUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561817) routine to copy the *RegistryPath* source string to a destination string.

 

 




