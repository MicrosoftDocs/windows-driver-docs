---
title: Installing Device Metadata Packages to an Offline Windows Image
description: Installing Device Metadata Packages to an Offline Windows Image
ms.date: 06/19/2025
ms.topic: concept-article
---

# Installing Device Metadata Packages to an Offline Windows Image

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

Computer OEMs can add device metadata packages to an offline image of Windows by copying the packages to the local device metadata store. This store is in the following location:

```cpp
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\<locale>
```

You must first create the *&lt;locale&gt;* subdirectory based on the target locale of the device metadata package. Then you must copy the metadata package to the appropriate *&lt;locale&gt;* subdirectory.

For example, a device metadata package that is localized for the English language of Great Britain must be copied to the following location:

```cpp
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\EN-GB
```

A device metadata package that is localized for the Japanese language must be copied to the following location:

```cpp
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\JA
```

For more information, see [Device Metadata Store](device-metadata-store.md).
