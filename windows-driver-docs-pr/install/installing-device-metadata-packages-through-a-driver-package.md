---
title: Installing Device Metadata Packages through a Driver Package
description: Installing Device Metadata Packages through a Driver Package
ms.assetid: fd140583-d4f9-4817-8edc-5bc3c6a2a1d7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Device Metadata Packages through a Driver Package


A [driver package](driver-packages.md) can install device metadata packages by copying them to the [device metadata store](device-metadata-store.md). This is accomplished by using [**INF CopyFiles directives**](inf-copyfiles-directive.md) within the [**DestinationDirs**](inf-destinationdirs-section.md) and [**DDInstall**](inf-ddinstall-section.md) sections of the [INF file](inf-files.md) for the driver package.

**Note**  We highly recommend that you install device metadata packages from the WMIS server instead of through driver packages. For more information, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).



To install device metadata packages through a [driver package](driver-packages.md), you must follow these guidelines:

-   The device metadata packages must be copied to the [device metadata store](device-metadata-store.md) by using INF directives. The metadata packages must not be copied by a [co-installer](writing-a-co-installer.md).

-   If your driver package is used to install devices on versions of Windows earlier than Windows 7, you must use a separate [**INF *DDInstall* section**](inf-ddinstall-section.md) that contains your metadata-related INF directives. You must specify this section name in the [**INF *Models* section**](inf-models-section.md) by using a *TargetOSversion* decoration that specifies an *OSMajorVersion* and *OSMinorVersion* value for Windows 7 or later versions of Windows.

    **Note**  If you do not use a separate INF *DDInstall* section that is decorated for Windows 7 or later versions of Windows, the installation of your digitally signed [driver package](driver-packages.md) will result in a signature alert when installed on versions of Windows earlier than Windows 7.




For more information, see [Combining Platform Extensions with Operating System Versions](combining-platform-extensions-with-operating-system-versions.md).


-   All metadata packages in the driver package must be copied to the correct locale-specific folder in the [device metadata store](device-metadata-store.md). This is needed in order to support dynamic changes to locale.

-   The COPYFLG_NODECOMP flag (0x00000800) is required in the [**INF CopyFiles directives**](inf-copyfiles-directive.md) that specify the device metadata packages. This flag guarantees that the binary integrity of the device metadata package is retained and avoids a decompression of the device metadata package when the driver package is installed.

-   You must first digitally sign the device metadata package before you digitally sign the driver package. For more information about digital signing, see [Driver Signing](driver-signing.md).

-   Any failure during the installation of the metadata package installation causes the driver installation to fail.

The following example shows how to copy device metadata packages to locale-specific directory paths by using an INF file for the device metadata store within the [**DestinationDirs Section**](inf-destinationdirs-section.md) and [**DDInstall**](inf-ddinstall-section.md) INF sections:

```cpp
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









