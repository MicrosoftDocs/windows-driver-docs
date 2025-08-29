---
title: Installing Device Metadata Packages through a Driver Package
description: Installing Device Metadata Packages through a Driver Package
ms.date: 06/19/2025
ms.topic: concept-article
---

# Installing Device Metadata Packages through a Driver Package

> [!IMPORTANT]
> Device metadata is deprecated and will be removed in a future release of Windows. For information about the replacement for this functionality, see **[Driver Package Container Metadata](driver-package-container-metadata.md)**.

A [driver package](driver-packages.md) can install device metadata packages by copying them to the [device metadata store](device-metadata-store.md). This installation is accomplished by using setup information (INF) **[CopyFiles directives](inf-copyfiles-directive.md)** within the **[DestinationDirs](inf-destinationdirs-section.md)** and **[DDInstall](inf-ddinstall-section.md)** sections of the [INF file](overview-of-inf-files.md) for the driver package.

> [!NOTE]
> We highly recommend that you install device metadata packages from the Windows Metadata and Internet Services (WMIS) server instead of through driver packages. For more information, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).

To install device metadata packages through a [driver package](driver-packages.md), you must follow these guidelines:

- The device metadata packages must be copied to the [device metadata store](device-metadata-store.md) by using INF directives. A [co-installer](writing-a-co-installer.md)  must not copy the metadata packages.

- If your driver package is used to install devices on versions of Windows earlier than Windows 7, you must use a separate **[INF *DDInstall* section](inf-ddinstall-section.md)** that contains your metadata-related INF directives. You must specify this section name in the **[INF *Models* section](inf-models-section.md)** by using a *TargetOSversion* decoration that specifies an *OSMajorVersion* and *OSMinorVersion* value for Windows 7 or later versions of Windows.

    > [!NOTE]
    > If you don't use a separate INF *DDInstall* section that is decorated for Windows 7 or later versions of Windows, the installation of your digitally signed [driver package](driver-packages.md) results in a signature alert when installed on versions of Windows earlier than Windows 7.

For more information, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).

- To support dynamic changes to locale, all metadata packages in the driver package must be copied to the correct locale-specific folder in the [device metadata store](device-metadata-store.md).

- The COPYFLG_NODECOMP flag (0x00000800) is required in the **[INF CopyFiles directives](inf-copyfiles-directive.md)** that specify the device metadata packages. This flag guarantees that the binary integrity of the device metadata package is retained, and avoids a decompression of the device metadata package when the driver package is installed.

- You must first digitally sign the device metadata package before you digitally sign the driver package. For more information about digital signing, see [Driver Signing](driver-signing.md).

- Any failure during the installation of the metadata package installation causes the driver installation to fail.

The following example shows how to copy device metadata packages to locale-specific directory paths by using an INF file for the device metadata store within the **[DestinationDirs Section](inf-destinationdirs-section.md)** and **[DDInstall](inf-ddinstall-section.md)** INF sections:

```inf
[SourceDisksNames]
1 = %Media_Description%,,,\MetadataPackage ;

[SourceDisksFiles.NTx86]
GUID1.devicemetadata-ms= 1,, ;A metadata package file for EN-US
GUID2.devicemetadata-ms= 1,, ;A metadata package file for AR-SA
GUID3.devicemetadata-ms= 1,, ;A metadata package file for JA-JP

[DestinationDirs]
COPYMETADATA_EN-US = 24, \ProgramData\Microsoft\Windows\DeviceMetadataStore\EN-US ;
COPYMETADATA_AR-SA = 24, \ProgramData\Microsoft\Windows\DeviceMetadataStore\AR-SA ;
COPYMETADATA_JA-JP = 24, \ProgramData\Microsoft\Windows\DeviceMetadataStore\JA-JP ;
. . .

[DeviceInstall.ntx86]
CopyFiles=COPYMETADATA_EN-US
CopyFiles=COPYMETADATA_AR-SA
CopyFiles=COPYMETADATA_JA-JP

[COPYMETADATA_EN-US]
GUID1.devicemetadata-ms,,,0x00000800 ;COPYFLG_NODECOMP
[COPYMETADATA_AR-SA]
GUID2.devicemetadata-ms,,,0x00000800 ;COPYFLG_NODECOMP
[COPYMETADATA_JA-JP]
GUID3.devicemetadata-ms,,,0x00000800 ;COPYFLG_NODECOMP
```
