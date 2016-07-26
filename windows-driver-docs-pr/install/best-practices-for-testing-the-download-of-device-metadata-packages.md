---
title: Best Practices for Testing the Download of Device Metadata Packages
description: Best Practices for Testing the Download of Device Metadata Packages
ms.assetid: 4470fa63-527a-4e92-916f-a84421259f57
---

# Best Practices for Testing the Download of Device Metadata Packages


Because of how the device metadata retrieval client ([DMRC](device-metadata-retrieval-client.md)) caches metadata packages, a delay can occur between the time when a device metadata package is available on the Windows Metadata and Internet Services ([WMIS](windows-metadata-and-internet-services.md)) server and the time when the DMRC downloads the metadata package to a client system. To test the download of a device metadata package, you can force a download in one of the following ways:

-   Delete the folders in the [device metadata cache](device-metadata-cache.md). This cache is located in the following directory:

    Windows 7:

    ``` syntax
    %LOCALAPPDATA%\Microsoft\Device Metadata\
    ```

    Windows 8:

    ``` syntax
    %PROGRAMDATA%\Microsoft\Windows\DeviceMetadataCache\
    ```

    Deleting these folders resets the value of **LastCheckedDate** and forces the DMRC to query the WMIS server for all devices.

-   Set the **CheckBackMDRetrieved** and **CheckBackMDNotRetrieved** registry keys to 0. When these values are zero, the DMRC immediately queries the WMIS server for a target device.

    Be aware that the WMIS server overwrites these values every time that the DMRC receives a response from WMIS. Therefore, these parameters can change if the DMRC receives a response for any other device before it queries the WMIS server for your target device.

    **Note**  You must make these changes only when you test metadata packages. You must not provide end-users with any tools that change the registry values that are used by DMRC.

     

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Best%20Practices%20for%20Testing%20the%20Download%20of%20Device%20Metadata%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




