---
title: Installing Device Metadata Packages through an Application
description: Installing Device Metadata Packages through an Application
ms.assetid: 3fec5938-b81b-4efe-8bcd-b2ef4b1c4b8b
---

# Installing Device Metadata Packages through an Application


To install device metadata packages in the [device metadata store](device-metadata-store.md) by using an application, such as a device installation application, follow these steps:

1.  The application first queries the path of the [device metadata store](device-metadata-store.md) by calling the [SHGetKnownFolderPath](http://go.microsoft.com/fwlink/p/?linkid=145428) function. The [KNOWNFOLDERID](http://go.microsoft.com/fwlink/p/?linkid=145429) GUID for the device metadata store is {5CE4A5E9-E4EB-479D-B89F-130C02886155}.

2.  The application then copies the device metadata package to the device metadata store by calling the [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) function.

    **Note**  The application must be running with administrator privileges or started from an elevated command prompt window.

     

When your application copies the device metadata package to the [device metadata store](device-metadata-store.md), it must complete the following steps:

1.  If a subdirectory does not exist in the device metadata store for the locale of your device metadata package, the application must create the subdirectory by using the name of the target locale.

    For example, if the locale of the package is EN-US, the application must create the *EN-US* subdirectory under the path of the device metadata store if the subdirectory does not currently exist.

2.  Copy the device metadata package to the appropriate *&lt;locale&gt;* subdirectory within the [device metadata store](device-metadata-store.md).

    **Note**  If you use the [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) function to copy the device metadata package, specify the full path name, which includes the appropriate *&lt;locale&gt;* subdirectory. By doing this, [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) creates the associated subdirectories for your package if they do not exist on the local computer.

     

    After the device metadata package is installed in the [device metadata store](device-metadata-store.md), the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) accesses the device metadata package and presents the device information to the Devices and Printers user interface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Device%20Metadata%20Packages%20through%20an%20Application%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




