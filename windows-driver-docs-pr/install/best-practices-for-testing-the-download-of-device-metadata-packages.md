---
title: Best Practices for Testing Download of Device Metadata Packages
description: Best Practices for Testing the Download of Device Metadata Packages
ms.assetid: 4470fa63-527a-4e92-916f-a84421259f57
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Best Practices for Testing the Download of Device Metadata Packages


Because of how the device metadata retrieval client ([DMRC](device-metadata-retrieval-client.md)) caches metadata packages, a delay can occur between the time when a device metadata package is available on the Windows Metadata and Internet Services ([WMIS](windows-metadata-and-internet-services.md)) server and the time when the DMRC downloads the metadata package to a client system. To test the download of a device metadata package, you can force a download in one of the following ways:

-   Delete the folders in the [device metadata cache](device-metadata-cache.md). This cache is located in the following directory:

    Windows 7:

    ```cpp
    %LOCALAPPDATA%\Microsoft\Device Metadata\
    ```

    Windows 8:

    ```cpp
    %PROGRAMDATA%\Microsoft\Windows\DeviceMetadataCache\
    ```

    Deleting these folders resets the value of **LastCheckedDate** and forces the DMRC to query the WMIS server for all devices.

-   Set the **CheckBackMDRetrieved** and **CheckBackMDNotRetrieved** registry keys to 0. When these values are zero, the DMRC immediately queries the WMIS server for a target device.

    Be aware that the WMIS server overwrites these values every time that the DMRC receives a response from WMIS. Therefore, these parameters can change if the DMRC receives a response for any other device before it queries the WMIS server for your target device.

    **Note**  You must make these changes only when you test metadata packages. You must not provide end-users with any tools that change the registry values that are used by DMRC.

     

 

 





