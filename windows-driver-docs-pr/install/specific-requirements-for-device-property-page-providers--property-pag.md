---
title: Requirements for Property Page Extension DLLs
description: Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)
ms.assetid: bc48d848-a216-442e-97ca-f990f8d243ac
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)


This topic how to create and install a property page extension DLL.

### Creating a property page extension dll

A property page extension DLL that provides custom property pages must handle the request to add a property page. This request is made through the **AddPropSheetPageProc** callback function.

In response to this request, the DLL provides information about each of its custom property pages, creates the pages, and adds the created pages to the list of dynamic property pages for the device.

For information about how to create a custom device property page by a property page extension DLL, see [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

### Installing a device property page

A property page extension DLL is installed by using the following directives in the [INF file](inf-files.md) of a [driver package](driver-packages.md):

1.  Use the *add-registry-section*, which is specified by an [**INF AddReg directive**](inf-addreg-directive.md) in the [**INF *DDInstall* section**](inf-ddinstall-section.md), to add an **EnumPropPages32** entry for the device. The **EnumPropPages32** entry specifies the following [REG_SZ](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) values:

    -   The name of the DLL that exports the **ExtensionPropSheetPageProc** callback function.
    -   The name of the **ExtensionPropSheetPageProc** callback function as implemented by the DLL.

    The following code example shows an *add-registry-section* that adds the **EnumPropPages32** entry that specifies the name of the DLL (*MyPropProvider.dll*) and callback function (*MyCallbackFunction*):

    ```cpp
    HKR, , EnumPropPages32, 0, "MyPropProvider.dll, MyCallbackFunction"
    ```

    **Important**  Both the name of the DLL and callback function must be enclosed together within quotation marks (" ").

     

2.  Include an [**INF CopyFiles directive**](inf-copyfiles-directive.md) that copies the property page extension DLL to the *%SystemRoot%\\System32* directory.

3.  If the device is a network adapter, you must specify NCF_HAS_UI as one of the **Characteristics** values in the [**INF DDInstall section**](inf-ddinstall-section.md). This value indicates that the adapter supports a user interface.

    For more information, see [Specifying Custom Property Pages for Network Adapters](https://msdn.microsoft.com/library/windows/hardware/ff570843).

 

 





