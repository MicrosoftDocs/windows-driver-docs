---
title: Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)
description: Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)
ms.assetid: bc48d848-a216-442e-97ca-f990f8d243ac
---

# Specific Requirements for Device Property Page Providers (Property Page Extension DLLs)


This topic how to create and install a property page extension DLL.

### Creating a property page extension dll

A property page extension DLL that provides custom property pages must handle the request to add a property page. This request is made through the **AddPropSheetPageProc** callback function.

In response to this request, the DLL provides information about each of its custom property pages, creates the pages, and adds the created pages to the list of dynamic property pages for the device.

For information about how to create a custom device property page by a property page extension DLL, see [General Requirements for Device Property Page Providers](general-requirements-for-device-property-page-providers.md).

### Installing a device property page

A property page extension DLL is installed by using the following directives in the [INF file](inf-files.md) of a [driver package](driver-packages.md):

1.  Use the *add-registry-section*, which is specified by an [**INF AddReg directive**](inf-addreg-directive.md) in the [**INF *DDInstall* section**](inf-ddinstall-section.md), to add an **EnumPropPages32** entry for the device. The **EnumPropPages32** entry specifies the following REG\_SZ values:

    -   The name of the DLL that exports the **ExtensionPropSheetPageProc** callback function.
    -   The name of the **ExtensionPropSheetPageProc** callback function as implemented by the DLL.

    The following code example shows an *add-registry-section* that adds the **EnumPropPages32** entry that specifies the name of the DLL (*MyPropProvider.dll*) and callback function (*MyCallbackFunction*):

    ```
    HKR, EnumPropPages32, 0, "MyPropProvider.dll, MyCallbackFunction"
    ```

    **Important**  Both the name of the DLL and callback function must be enclosed together within quotation marks (" ").

     

2.  Include an [**INF CopyFiles directive**](inf-copyfiles-directive.md) that copies the property page extension DLL to the *%SystemRoot%\\System32* directory.

3.  If the device is a network adapter, you must specify NCF\_HAS\_UI as one of the **Characteristics** values in the [**INF DDInstall section**](inf-ddinstall-section.md). This value indicates that the adapter supports a user interface.

    For more information, see [Specifying Custom Property Pages for Network Adapters](https://msdn.microsoft.com/library/windows/hardware/ff570843).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Specific%20Requirements%20for%20Device%20Property%20Page%20Providers%20%28Property%20Page%20Extension%20DLLs%29%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




