---
title: Manually Adding Device Metadata Packages
description: Manually Adding Device Metadata Packages
ms.assetid: 1d0cee1f-8aa7-4fa9-b3c7-797cd09a07f4
---

# Manually Adding Device Metadata Packages


Device metadata packages can be installed on a computer in the following ways:

-   An OEM can use the Windows 7 OEM Preinstall Kit (OPK) to update an offline image of the operating system. By using the OPK, the OEM copies the device metadata package to the image's [device metadata store](device-metadata-store.md).

-   Developers can copy their device metadata packages to the [device metadata store](device-metadata-store.md) to test and debug the installation of a package. For more information, see [Debugging Device Metadata Packages](debugging-device-metadata-packages.md).

    **Note**  We do not recommend that end-users copy device metadata packages to the device metadata store. Instead, end-users should install device metadata packages by using either the Windows Metadata and Internet Services (WMIS) or an installation application that is provided by the OEM.

     

The following path shows the location of the [device metadata store](device-metadata-store.md):

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore
```

To copy device metadata packages to the [device metadata store](device-metadata-store.md), complete the following steps:

1.  If a subdirectory does not exist in the device metadata store for the locale of your device metadata package, you must create the subdirectory by using the name of the target locale.

    For example, if the locale of the package is EN-US, you must first create the following directory if it does not currently exist:

    ```
    %PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\EN-US
    ```

2.  Copy your device metadata package to the appropriate *&lt;locale&gt;* subdirectory of the [device metadata store](device-metadata-store.md).

After the device metadata package is installed in the [device metadata store](device-metadata-store.md), the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) accesses the device metadata package and presents the device information to the Devices and Printers user interface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Manually%20Adding%20Device%20Metadata%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




