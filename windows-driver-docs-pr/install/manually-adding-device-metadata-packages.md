---
title: Manually Adding Device Metadata Packages
description: Manually adding device metadata packages
ms.date: 06/19/2025
ms.topic: how-to
---

# Manually adding device metadata packages

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

Device metadata packages can be installed on a computer in the following ways:

- An OEM can use the Windows 7 OEM Preinstall Kit (OPK) to update an offline image of the operating system. The OEM copies the device metadata package to the image's [device metadata store](device-metadata-store.md) by using the OPK.

- Developers can copy their device metadata packages to the [device metadata store](device-metadata-store.md) to test and debug the installation of a package. For more information, see [Debugging Device Metadata Packages](debugging-device-metadata-packages-by-using-event-viewer.md).

    > [!NOTE]
    > We don't recommend that end-users copy device metadata packages to the device metadata store. Instead, end-users should install device metadata packages by using either the Windows Metadata and Internet Services (WMIS) or an installation application that is provided by the OEM.

The following path shows the location of the [device metadata store](device-metadata-store.md):

`%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore`

To copy device metadata packages to the [device metadata store](device-metadata-store.md), complete the following steps:

1. If a subdirectory doesn't exist in the device metadata store for the locale of your device metadata package, you must create the subdirectory by using the name of the target locale.

    For example, if the locale of the package is EN-US, you must first create the following directory if it doesn't currently exist:

    `%PROGRAMDATA%\Microsoft\Windows\DeviceMetadataStore\EN-US`

1. Copy your device metadata package to the appropriate *&lt;locale&gt;* subdirectory of the [device metadata store](device-metadata-store.md).

After the device metadata package is installed in the [device metadata store](device-metadata-store.md), the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) accesses the device metadata package and presents the device information to the Devices and Printers user interface.
