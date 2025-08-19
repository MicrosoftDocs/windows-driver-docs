---
title: Driver Package Container Metadata
description: Driver package container metadata provides OEMs and IHVs with a driver package-based solution to customize and enhance user facing information about their physical device.
ms.date: 03/21/2025
ms.topic: concept-article
---

# Driver Package Container Metadata

Driver package container metadata provides OEMs and IHVs with a [driver package](driver-packages.md)-based solution to customize and enhance user-facing information about their physical device as represented by a [device container](container-ids.md). The physical device can be a peripheral connected to the computer or the computer itself. The following list shows the type of information that driver package container metadata can supply:

- The name of the OEM/IHV.
- The model name of the device container.
- One or more functional categories that the device container supports.
- A photo-realistic icon that represents the device container.

Without container metadata, the operating system generates the information in the previous list by looking at all [device nodes](../gettingstarted/device-nodes-and-device-stacks.md) (devnodes) that belong to the device container, then running heuristics based on the information of the devnodes. This process may not result in the values desired by the OEMs or IHVs for the display of their physical devices. Container metadata can be used by the OEMs or IHVs to directly control these values.

Driver package container metadata is supported starting in Windows 11 24H2 KB5052093 (OS Build 26100.3323). If the driver package that includes the container metadata is installed on an older Windows system, the installation will be successful but the container metadata will not be processed and applied.

## Using Base INF or Extension INF

The [INF AddProperty directive](inf-addproperty-directive.md) within the driver package [INF file](overview-of-inf-files.md) specifies the driver package container metadata. Our recommendations for which INF file to use for container metadata are:

1. If OEMs/IHVs already have a driver package that is the base INF for a devnode that is part of the device container, that driver package should be updated to include the container metadata.
1. If OEMs/IHVs don't have a driver package that is the base INF for a devnode that is part of the device container, creating an extension INF driver package is recommended. Compared to a base INF, an extension INF is the lighter weight way of including the container metadata.

For more information about base INFs and extension INFs, see [Using an Extension INF File](using-an-extension-inf-file.md).

To certify an INF file that specifies the container metadata, an updated [InfVerif](../devtest/infverif.md) is required, which is available starting in [Windows Driver Kit, Version 10.0.26100.3323](../wdk-release-notes.md) and [Windows HLK 24H2 (updated January 2025)](/windows-hardware/test/hlk/windows-hardware-lab-kit).

## Device Container Targeting

Driver packages are targeted on individual devnodes using device-specific information. This information includes [hardware IDs](hardware-ids.md) and [compatible IDs](compatible-ids.md). To supply container metadata to the correct device container, the driver package must target one of the devnodes that belong to the device container. There are several ways to view all devnodes that belong to a device container:

1. [PnPUtil /enum-containers /devices](..\devtest\pnputil-command-syntax.md#enum-containers) (Command available starting in Windows 11, version 24H2)
1. Device Manager: View -> Devices by container (View option available starting in Windows 10, version 1703)

To supply container metadata for the computer container, you must target an extension INF at a special devnode called the **OEM computer device**. The **OEM computer device** is available starting in Windows 11, version 22H2.

The **OEM computer device** can be identified by device class and hardware IDs such as in the following example:

1. Enumerate all devnodes belonging to the Computer class:

    ```console
    PnPUtil /enum-devices /class Computer /deviceids
    ```
1. The OEM computer device appears as follows:
    ```console
    Instance ID: SWD\COMPUTER\...
    Status: Started
    Driver Name: compdev.inf
    Hardware IDs:
        COMPUTER\{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
        COMPUTER\{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
        COMPUTER\{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
        COMPUTER\{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
        ...
    ```

Windows Hardware Dev Center only allows driver packages matching on IDs exposed by the **OEM computer device** to be extension INFs. During submission, it is important to specify the inbox Windows driver for the device in the **Business Justification** box of the shipping label page: `ExtendsInboxDriver=compdev.inf`. For more information about submitting and publishing extension INFs, see [Working with extension INF files in the Partner Center](../dashboard/submit-dashboard-extension-inf-files.md) and [Extension INF targeting rules](../dashboard/extension-inf-targeting-rules.md).

## Examples

The following example shows how container metadata is supplied to the computer container by targeting the OEM computer device on specific model systems:

```inf
[Standard.NTamd64]
%Device.ExtensionDesc% = DeviceInstall, Computer\{417c41d7-1d11-5b78-ab26-00b745dfac94}
%Device.ExtensionDesc% = DeviceInstall, Computer\{70127e8f-991f-505a-b966-fc08b6f74f94}
%Device.ExtensionDesc% = DeviceInstall, Computer\{ff26d547-8d7f-5069-bbcb-0c50756b691a}
%Device.ExtensionDesc% = DeviceInstall, Computer\{770bbdbb-bbf5-5d39-ae1a-25f41b7bbcfd}

[DeviceInstall]
AddProperty = ComputerMetadata_Properties

[ComputerMetadata_Properties]
ContainerModelName,,,, %ModelName%
ContainerManufacturer,,,, %Manufacturer%
ContainerCategories,,,, Computer.Tablet
ContainerIcon,,,, %13%\CustomComputer.ico

[Strings]
Device.ExtensionDesc = "Custom Computer Metadata Extension"
ModelName = "Custom Computer"
Manufacturer = "Custom Manufacturer"

; en-us
[Strings.0409]
Device.ExtensionDesc = "Custom Computer Metadata Extension"
ModelName = "Custom Computer"
Manufacturer = "Custom Manufacturer"

; zh-cn
[Strings.0804]
Device.ExtensionDesc = "自定义电脑元数据拓展"
ModelName = "自定义电脑型号"
Manufacturer = "自定义制造商"
```

The following example shows how container metadata, including a [Print Support App association](../devapps/print-support-app-association.md) is supplied for a container that represents a multi-function printer:

```inf
[Standard.NTamd64]
%Device.ExtensionDesc% = DeviceInstall, MF\CustomPrinter&WSD&IP_PRINT
%Device.ExtensionDesc% = DeviceInstall, WSDPRINT\CustomPrinter
%Device.ExtensionDesc% = DeviceInstall, USBPRINT\CustomPrinter
%Device.ExtensionDesc% = DeviceInstall, CustomPrinter

[DeviceInstall]
AddProperty = Container_Metadata_Properties
AddProperty = PSA_Association_Property

[Container_Metadata_Properties]
ContainerModelName,,,, %ModelName%
ContainerManufacturer,,,, %Manufacturer%
ContainerCategories,,,, PrintFax.Printer, Imaging.Scanner
ContainerIcon,,,, %13%\CustomPrinter.ico

[PSA_Association_Property]
{A925764B-88E0-426D-AFC5-B39768BE59EB}, 1, 0x12,, CustomPrinterAUMID

[DeviceInstall.Software]
AddSoftware = Printer Control App,, Print_SoftwareInstall

[Print_SoftwareInstall]
SoftwareType = 2
SoftwareID = pfn://CustomPrinterControlAppId

[Strings]
Device.ExtensionDesc = "Container Property Extension"
ModelName = "Custom Printer"
Manufacturer = "Custom Manufacturer"
```

For those transitioning from [Device Metadata Packages](overview-of-device-metadata-packages.md), the following shows what a Device Metadata Package might look like for the example above of the multi-function printer:

- PackageInfo.xml

    ```xml
    <?xml version="1.0" encoding="utf-8"?> 
    <PackageInfo xmlns="http://schemas.microsoft.com/windows/DeviceMetadata/PackageInfo/2007/11/">
      <MetadataKey>
        <HardwareIDList> 
          <HardwareID>DOID:MF\CustomPrinter&WSD&IP_PRINT</HardwareID>
          <HardwareID>DOID:WSDPRINT\CustomPrinter</HardwareID>
          <HardwareID>DOID:USBPRINT\CustomPrinter</HardwareID>
          <HardwareID>DOID:CustomPrinter</HardwareID>
        </HardwareIDList>
        <Locale default="true">en-US</Locale>
      <LastModifiedDate>2014-04-08T07:19:14Z</LastModifiedDate> 
      </MetadataKey> 
      ...
    </PackageInfo>
    ```

- DeviceInfo.xml

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <DeviceInfo xmlns="http://schemas.microsoft.com/windows/DeviceMetadata/DeviceInfo/2007/11/">
      <DeviceCategoryList>
        <DeviceCategory>PrintFax.Printer</DeviceCategory>
        <DeviceCategory>Imaging.Scanner</DeviceCategory>
      </DeviceCategoryList>
      <ModelName>Custom Printer</ModelName>
      <Manufacturer>Custom Manufacturer</Manufacturer> 
      <DeviceIconFile>CustomPrinter.ico</DeviceIconFile>
    </DeviceInfo>
    ```

- SoftwareInfo.xml

    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <SoftwareInfo xmlns="http://schemas.microsoft.com/windows/2010/08/DeviceMetadata/SoftwareInfo">
      <DeviceCompanionApplications>
        <Package>
          <Identity Name="CustomPrinterControlAppName" Publisher="CustomPrinterControlAppPublisher" />
          ...
        </Package>
      </DeviceCompanionApplications>
      ...
    </SoftwareInfo>
    ```
