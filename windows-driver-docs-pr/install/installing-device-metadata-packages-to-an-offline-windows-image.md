---
title: Installing Device Metadata Packages to an Offline Windows Image
description: Installing Device Metadata Packages to an Offline Windows Image
ms.assetid: 53480324-951f-4c51-9b5b-051ce1a3b709
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Device Metadata Packages to an Offline Windows Image


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

 

 





