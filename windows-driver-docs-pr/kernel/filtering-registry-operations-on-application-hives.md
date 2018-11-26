---
title: Filtering Registry Operations on Application Hives
description: Initial support for application hives was introduced in Windows Vista.
ms.assetid: A8D06E25-7CC6-476A-AB55-DAFE19954347
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Filtering Registry Operations on Application Hives


Initial support for application hives was introduced in Windows Vista. Starting with Windows 8, improved support for application hives is available, and wider use of application hives is expected. Thus, registry filter drivers developed for these versions of Windows, and particularly for Windows 8 and later, must be aware of registry operations on application hives. These drivers should handle such operations efficiently to avoid negatively impacting the user experience.

Application hives are registry hives loaded by user-mode applications to store application-specific state data. An application calls the [**RegLoadAppKey**](https://msdn.microsoft.com/library/windows/desktop/ms724886) function to load an application hive.

In contrast to other types of registry hives, application hives are loaded under the \\REGISTRY\\A registry path name instead of under \\REGISTRY\\MACHINE or \\REGISTRY\\USER. The \\REGISTRY\\A path name is special in that there is no way to traverse this path, and an attempt to open a key under \\REGISTRY\\A will fail with error status STATUS\_ACCESS\_DENIED. The only way an application can access a key in an application hive is to use the handle to the root key of the application hive. The application gets this handle from the **RegLoadAppKey** call that loads the hive.

An application does not need to explicitly unload an application hive. The operating system automatically unloads the application hive after all of the handles to the hive are closed.

An application hive does not support setting security descriptors on the keys in the hive. Instead, there is one security descriptor for the entire hive. An attempt to set a security descriptor on a key in an application hive will fail with error status STATUS\_ACCESS\_DENIED. In contrast to other types of registry hives, for which each key is secured with its own security descriptor, the security of an application hive is based on the hive file's security descriptor. Thus, an entity that is successful in loading the hive can modify the entire hive.

A registry filter driver receives calls to its [*RegistryCallback*](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine for registry operations on application hives. These calls do not distinguish between registry operations on application hives and operations on other types of registry hives. Registry filter drivers that handle create-key and open-key operations (which are indicated by the **RegNtPreOpenKey**, **RegNtPreOpenKeyEx**, **RegNtPreCreateKey**, and **RegNtPreCreateKeyEx** notification values) must correctly handle the following special situation. When an application hive is loaded, the last step in the loading process is the opening of the root key of the hive by the registry manager. The registry manager issues this open-key operation with an absolute path to the key, which means that the path name string in the **CompleteName** member of the [**REG\_CREATE\_KEY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff560920), [**REG\_CREATE\_KEY\_INFORMATION\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff560922), [**REG\_OPEN\_KEY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff560957), or [**REG\_OPEN\_KEY\_INFORMATION\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff560959) structure will start with "\\REGISTRY\\A\\". Only the registry manager can use an absolute path to open an application hive. If a registry filter driver tries to open an application hive in this way (for example, by calling the [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014) routine), the operation will fail with error status STATUS\_ACCESS\_DENIED.

 

 




