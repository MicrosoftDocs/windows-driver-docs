---
title: Device Metadata Cache
description: Device Metadata Cache
ms.assetid: 0b20e1e0-9137-4572-8a5b-6bde63c34ce4
keywords: ["device metadata cache WDK"]
---

# Device Metadata Cache


The device metadata cache is the directory where device metadata packages are stored on the local computer.

On Windows 7, the device metadata cache is accessed from the following directory:

```
%LOCALAPPDATA%\Local\Microsoft\Device Metadata\
```

On Windows 8 and later, the device metadata cache is accessed from the following directory:

```
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataCache\
```

When the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) downloads device metadata packages from the Windows Metadata and Services (WMIS) website, it saves them within the device metadata cache. For more information about this process, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).

**Note**   The device metadata cache is reserved for only the operating system to use. Device metadata packages that are not installed by DMRC, such as through an application that is provided by an OEM, must be copied to the [device metadata store](device-metadata-store.md) instead.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Metadata%20Cache%20%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




