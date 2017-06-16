---
title: Filtering Registry Operations on Application Hives
author: windows-driver-content
description: Initial support for application hives was introduced in Windows Vista.
ms.assetid: A8D06E25-7CC6-476A-AB55-DAFE19954347
---

# Filtering Registry Operations on Application Hives


Initial support for application hives was introduced in Windows Vista. Starting with Windows 8, improved support for application hives is available, and wider use of application hives is expected. Thus, registry filter drivers developed for these versions of Windows, and particularly for Windows 8 and later, must be aware of registry operations on application hives. These drivers should handle such operations efficiently to avoid negatively impacting the user experience.

Application hives are registry hives loaded by user-mode applications to store application-specific state data. An application calls the [**RegLoadAppKey**](https://msdn.microsoft.com/library/windows/desktop/ms724886) function to load an application hive.

In contrast to other types of registry hives, application hives are loaded under the \\REGISTRY\\A registry path name instead of under \\REGISTRY\\MACHINE or \\REGISTRY\\USER. The \\REGISTRY\\A path name is special in that there is no way to traverse this path, and an attempt to open a key under \\REGISTRY\\A will fail with error status STATUS\_ACCESS\_DENIED. The only way an application can access a key in an application hive is to use the handle to the root key of the application hive. The application gets this handle from the **RegLoadAppKey** call that loads the hive.

An application does not need to explicitly unload an application hive. The operating system automatically unloads the application hive after all of the handles to the hive are closed.

An application hive does not support setting security descriptors on the keys in the hive. Instead, there is one security descriptor for the entire hive. An attempt to set a security descriptor on a key in an application hive will fail with error status STATUS\_ACCESS\_DENIED. In contrast to other types of registry hives, for which each key is secured with its own security descriptor, the security of an application hive is based on the hive file's security descriptor. Thus, an entity that is successful in loading the hive can modify the entire hive.

A registry filter driver receives calls to its [*RegistryCallback*](https://msdn.microsoft.com/library/windows/hardware/ff560903) routine for registry operations on application hives. These calls do not distinguish between registry operations on application hives and operations on other types of registry hives. Registry filter drivers that handle create-key and open-key operations (which are indicated by the **RegNtPreOpenKey**, **RegNtPreOpenKeyEx**, **RegNtPreCreateKey**, and **RegNtPreCreateKeyEx** notification values) must correctly handle the following special situation. When an application hive is loaded, the last step in the loading process is the opening of the root key of the hive by the registry manager. The registry manager issues this open-key operation with an absolute path to the key, which means that the path name string in the **CompleteName** member of the [**REG\_CREATE\_KEY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff560920), [**REG\_CREATE\_KEY\_INFORMATION\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff560922), [**REG\_OPEN\_KEY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff560957), or [**REG\_OPEN\_KEY\_INFORMATION\_V1**](https://msdn.microsoft.com/library/windows/hardware/ff560959) structure will start with "\\REGISTRY\\A\\". Only the registry manager can use an absolute path to open an application hive. If a registry filter driver tries to open an application hive in this way (for example, by calling the [**ZwOpenKey**](https://msdn.microsoft.com/library/windows/hardware/ff567014) routine), the operation will fail with error status STATUS\_ACCESS\_DENIED.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Filtering%20Registry%20Operations%20on%20Application%20Hives%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


