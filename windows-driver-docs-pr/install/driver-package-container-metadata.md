---
title: Driver Package Container Metadata
description: Driver package container metadata provides OEMs and IHVs with a driver package-based solution to customize and enhance user facing information about their physical device.
ms.date: 03/21/2025
---

# Driver Package Container Metadata

Driver package container metadata provides OEMs and IHVs with a [driver package](driver-packages.md)-based solution to customize and enhance user-facing information about their physical device. For example, it can enhance information about a [device container](container-ids.md). The physical device can be a peripheral connected to the computer, or the computer itself. The following list shows the type of information that driver package container metadata can supply:

- The name of the OEM/IHV.
- The model name of the device container.
- One or more functional categories that the device container supports.
- A photo-realistic icon that represents the device container in the "Devices and Printers" user interface.

Without container metadata, the operating system generates the information in the previous list by looking at all device nodes (devnodes) that belong to the device container, then running heuristics based on the information of the devnodes. This process might not satisfy the needs of OEMs or IHVs for how their physical device is displayed. Using container metadata can fulfill this gap.

<!-- TODO: use KB article -->
Driver package container metadata is supported starting in Windows 11 24H2 2D release

## Using Base INF or Extension INF

The [INF AddProperty directive](inf-addproperty-directive.md) within the driver package [INF file](overview-of-inf-files.md) specifies the driver package container metadata. Our recommendations for which INF file to use for container metadata are:

1. If OEMs/IHVs already have a driver package with the base INF for their physical device, update the base INF to include the container metadata.
1. If OEMs/IHVs don't have a driver package with the base INF for their physical device, creating a driver package with extension INF is recommended. Compared to a base INF, extension INF is the lighter weight way of including the container metadata.

For more information about base INF and extension INF, see [Using an Extension INF File](using-an-extension-inf-file.md).

## Device Container Targeting

Driver packages are targeted on individual devnodes using device-specific information. This information includes [hardware ID](hardware-ids.md) and [compatible IDs](compatible-ids.md). To supply container metadata to the correct device container, the driver package must target one of the devnodes that belong to the device container. There are several ways to view all devnodes that belong to a device container:

<!-- TODO: screenshots -->
1. [PnPUtil /enum-containers](..\devtest\pnputil-command-syntax.md###/enum-containers) (Command available starting in Windows 11, version 23H2)
1. Device Manager: View Devices by Container
1. Devices and Printers: View Properties on Container

For computer container, it's represented by a special devnode called **OEM computer device**, which needs to be used for driver package targeting for container metadata. **OEM computer device** is available starting in Windows 11, version 23H2.

> [!NOTE]
> Hardware Dev Center only allows extension INF for OEM computer device.

A **OEM computer device** can be identified by device description and hardware IDs such as in the following example:

<!-- TODO: use a generic example -->
```console
Friendly name: HP HP Z2 Tower G9 Workstation Desktop PC
Device description: Computer Device
Hardware IDs:
    COMPUTER\{137BF115-E0A3-5E03-9CF3-1A8F2303884A}
    COMPUTER\{B9FCB14E-BB0F-5B37-B27F-183103877144}
    COMPUTER\{A6C3EC7B-6F22-5700-A17C-D9409F22D793}
    COMPUTER\{9059F30D-53DA-5CF6-8A6C-BBA78D4852C3}
    COMPUTER\{E9743E0A-2B5A-593B-9C98-336532EA6A9D}
    COMPUTER\{753B339A-28CE-51F7-8E34-88ADD9928BF0}
    COMPUTER\{B4693619-89DB-5E2E-82BD-12FB6B2756DF}
    COMPUTER\{49088BAF-FD52-5BFA-B836-442C16C0F41F}
    COMPUTER\{BE346E1C-6EC2-50F5-A3FA-D02B82CA91C7}
    COMPUTER\{3BA15CFC-E9C2-56FD-AC5C-E671A539A8CE}
    COMPUTER\{29EEE337-A41E-50B1-B87D-8085A10A5352}
    COMPUTER\{3412CC8D-7338-5131-A04E-79B87B6B2FCB}
```

<!-- TODO: remove for the first publish -->
## Device Ranking for Resolving Conflicts

**[Not ready for publish since the logic is internal only for now]**

Ideally only one devnode within a device container is configured with a driver package with container metadata. However, it's possible that several devnodes within the device container are all configured with driver packages that provide a full set or subset of container metadata. So device ranking is needed to resolve the conflicts to ensure consistent and optimal display information of the device container. The following list shows the categories of devnodes with container metadata:

1. **Full-Property Devnode**: highest ranked devnode with a full set of container metadata.
1. **Identity-Property Devnode**: highest ranked devnode with at least ContainerManufacturer and ContainerModelName but not a full set of container metadata.
1. **Class-Property Devnode**: highest ranked devnode with at least ContainerCategories and ContainerIcon but not a full set of container metadata.
1. **Discrete-Property Devnode**: highest ranked devnode with other combinations of container metadata.

The rankings of devnodes for each container metadata are as follows:

| Rank | ContainerModelName | ContainerManufacturer | ContainerCategories | ContainerIcon |
|--|--|--|--|--|
| 1 | Full-Property Devnode | Full-Property Devnode | Full-Property Devnode | Full-Property Devnode |
| 2 | Identity-Property Devnode | Identity-Property Devnode | Class-Property Devnode | Class-Property Devnode |
| 3 | Class-Property Devnode | Class-Property Devnode | Identity-Property Devnode | Identity-Property Devnode |
| 4 | Discrete-Property Devnode | Discrete-Property Devnode | Discrete-Property Devnode | Discrete-Property Devnode |

> [!NOTE]
> For ContainerCategories, the value is an aggregation of property values from all devnodes according to the rankings listed in the table. For other container metadata, values are sourced from a single devnode.

## Examples

The following example shows how container metadata is supplied to the computer container by targeting to the OEM computer device:

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
Device.ExtensionDesc = "Custom Computer Metadata Extension"
ModelName = "自定义电脑型号"
Manufacturer = "自定义制造商"
```

The following example shows how container metadata is supplied to a multi-function printer, along with Print Support App association:

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
