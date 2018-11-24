---
title: Specifying Custom Property Pages for Network Adapters
description: Specifying Custom Property Pages for Network Adapters
ms.assetid: c9d54e9b-3d11-46d1-9c24-86a802c64a7a
keywords:
- add-registry-sections WDK networking , custom property pages
- custom property pages WDK networking
- property pages WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specifying Custom Property Pages for Network Adapters





If the **Advanced** property page is not suitable for displaying the configuration choices for a Net component (adapter), you can create one or more custom property pages.

**To create a custom property page**

1.  Create a Microsoft Win32 property page. Then create a property sheet extension DLL that provides *AddPropSheetPageProc* and *ExtensionPropSheetPageProc* callback functions. For more information, see the Windows 2000 Platform SDK.

2.  Use the *add-registry-section* that is referenced by the **DDInstall** section for the adapter to add the **EnumPropPages32** key to the instance key for the adapter. The **EnumPropPages32** key has two REG\_SZ values: the name of the DLL that exports the *ExtensionPropSheetPageProc* function and the name of the *ExtensionPropSheetPageProc* function. The following is an example of an *add-registry-section* that adds the **EnumPropPages32** key:

    ```INF
    HKR, EnumPropPages32, 0, "DLL name, ExtensionPropSheetPageProc function name"
    ```

3.  In the INF file for the adapter, include a **CopyFiles** section that copies the property sheet extension DLL to the Windows\\System32 directory. For more information about the **CopyFiles** section, see [INF File Sections and Directives](https://msdn.microsoft.com/library/windows/hardware/ff547433).

4.  In the **DDInstall** section for the adapter, specify NCF\_HAS\_UI as one of the **Characteristics** values to indicate that the adapter supports a user interface. For more information, see [DDInstall Section](ddinstall-section-in-a-network-inf-file.md).

5.  After the user applies changes to a property page, the property sheet extension DLL must:
    -   Call **SetupDiGetDeviceInstallParams**
    -   Set the DI\_FLAGSEX\_PROPCHANGE\_PENDING flag in the SP\_DEVINSTALL\_PARAMS structure supplied by **SetupDiGetDeviceInstallParams**
    -   Pass the updated SP\_DEVINSTALL\_PARAMS structure to **SetupDiSetDeviceInstallParams**.

        This reloads the driver so that it can read the changed parameter values.

 

 





