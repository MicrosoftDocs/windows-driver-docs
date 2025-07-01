---
title: Device Metadata Cache
description: Device Metadata Cache
keywords:
- device metadata cache WDK
ms.date: 06/19/2025
---

# Device Metadata Cache

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

The device metadata cache is the directory where device metadata packages are stored on the local computer.

On Windows 7, the device metadata cache is accessed from the following directory:

```cpp
%LOCALAPPDATA%\Local\Microsoft\Device Metadata\
```

On Windows 8 and later, the device metadata cache is accessed from the following directory:

```cpp
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataCache\
```

When the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) downloads device metadata packages from the Windows Metadata and Services (WMIS) website, it saves them within the device metadata cache. For more information about this process, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).

> [!NOTE]
> The device metadata cache is reserved for only the operating system to use. Device metadata packages that are not installed by DMRC, such as through an application that is provided by an OEM, must be copied to the [device metadata store](device-metadata-store.md) instead.
