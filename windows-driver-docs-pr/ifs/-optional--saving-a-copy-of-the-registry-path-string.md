---
title: \ Optional\ Saving a Copy of the Registry Path String
description: \ Optional\ Saving a Copy of the Registry Path String
ms.assetid: cf3b8649-6fb0-4ada-816c-5c7783918b2f
keywords: ["RegistryPath string copies", "saving RegistryPath string copies", "copying RegistryPath strings"]
---

# \[Optional\] Saving a Copy of the Registry Path String


## <span id="ddk_saving_a_copy_of_the_registry_path_string_if"></span><span id="DDK_SAVING_A_COPY_OF_THE_REGISTRY_PATH_STRING_IF"></span>


**Note**   This step is necessary only if the filter driver needs to use the registry path after the **DriverEntry** routine returns.

 

Save a copy of the *RegistryPath* string that was passed as input to **DriverEntry**. This parameter points to a counted Unicode string that specifies a path to the driver's registry key, **\\Registry\\Machine\\System\\CurrentControlSet\\Services\\***DriverName*, where *DriverName* is the name of the driver. If the *RegistryPath* string will be needed later, **DriverEntry** must save a copy of it, not just a pointer to it, because the pointer is no longer valid after the **DriverEntry** routine returns. You can use the [**RtlCopyUnicodeString**](https://msdn.microsoft.com/library/windows/hardware/ff561817) routine to copy the *RegistryPath* source string to a destination string.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20[Optional]%20Saving%20a%20Copy%20of%20the%20Registry%20Path%20String%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




