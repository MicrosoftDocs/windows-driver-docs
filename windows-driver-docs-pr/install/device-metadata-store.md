---
title: Device Metadata Store
description: Device Metadata Store
keywords:
- device metadata store WDK
ms.date: 06/19/2025
---

# Device Metadata Store

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](windows-hardware/drivers/install/driver-package-container-metadata)**.

The device metadata store is the directory where device metadata packages are stored on the local computer. The device metadata store is accessed from the following directory:

```cpp
%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\<locale>
```

The \<locale> subdirectory represents the locale of the device metadata package. The name of this subdirectory can be in the following format:

```cpp
<Language>[-<Region>] 
```

For example, a value of EN-US specifies the subdirectory that contains device metadata package that are localized for the English language of the United States.

If only *\<Language>* is specified, the subdirectory that contains device metadata packages that are localized for the specified language in all locations where the language exists. For example, a value of 'EN' applies to 'EN-US and EN-BR.

A device metadata package is copied to the device metadata store in one of the following ways:

- The OEM or developer copies the device metadata package. For more information, see [Manually Adding Device Metadata Packages](manually-adding-device-metadata-packages.md).

- The device metadata package is copied by using an application that is provided by the OEM. For more information, see [Installing Device Metadata Packages through an Application](installing-device-metadata-packages-through-an-application.md).

> [!NOTE]
> We do not recommend that end-users copy device metadata packages to the device metadata store. Instead, end-users should install device metadata packages by using either the [Windows Metadata and Internet Services (WMIS)](installing-device-metadata-packages-from-wmis.md) or an application provided by the OEM.
