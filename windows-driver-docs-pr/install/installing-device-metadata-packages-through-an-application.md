---
title: Installing Device Metadata Packages through an Application
description: Installing Device Metadata Packages through an Application
ms.assetid: 3fec5938-b81b-4efe-8bcd-b2ef4b1c4b8b
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Device Metadata Packages through an Application


To install device metadata packages in the [device metadata store](device-metadata-store.md) by using an application, such as a device installation application, follow these steps:

1.  The application first queries the path of the [device metadata store](device-metadata-store.md) by calling the [SHGetKnownFolderPath](http://go.microsoft.com/fwlink/p/?linkid=145428) function. The [KNOWNFOLDERID](http://go.microsoft.com/fwlink/p/?linkid=145429) GUID for the device metadata store is {5CE4A5E9-E4EB-479D-B89F-130C02886155}.

2.  The application then copies the device metadata package to the device metadata store by calling the [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) function.

    **Note**  The application must be running with administrator privileges or started from an elevated command prompt window.



When your application copies the device metadata package to the [device metadata store](device-metadata-store.md), it must complete the following steps:

1.  If a subdirectory does not exist in the device metadata store for the locale of your device metadata package, the application must create the subdirectory by using the name of the target locale.

    For example, if the locale of the package is EN-US, the application must create the *EN-US* subdirectory under the path of the device metadata store if the subdirectory does not currently exist.

2.  Copy the device metadata package to the appropriate *&lt;locale&gt;* subdirectory within the [device metadata store](device-metadata-store.md).

    **Note**  If you use the [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) function to copy the device metadata package, specify the full path name, which includes the appropriate *&lt;locale&gt;* subdirectory. By doing this, [CopyFile]( http://go.microsoft.com/fwlink/p/?linkid=189596) creates the associated subdirectories for your package if they do not exist on the local computer.




After the device metadata package is installed in the [device metadata store](device-metadata-store.md), the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) accesses the device metadata package and presents the device information to the Devices and Printers user interface.










