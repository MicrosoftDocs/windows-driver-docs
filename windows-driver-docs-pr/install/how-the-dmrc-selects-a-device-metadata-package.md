---
title: How the DMRC Selects a Device Metadata Package
description: How the DMRC Selects a Device Metadata Package
ms.assetid: dbedc995-520a-4b54-8613-d5a7810ab99c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the DMRC Selects a Device Metadata Package


When the Devices and Printers or Device Stage user interfaces are opened, the operating system starts the device metadata retrieval client ([DMRC](device-metadata-retrieval-client.md)) to search its cache for the most appropriate and current metadata package for a device. The DMRC also searches for a newer metadata package for the device on the Windows Metadata and Internet Services ([WMIS](windows-metadata-and-internet-services.md)) server. If one is found, the DMRC downloads the package and installs it on the computer.

**Note**  If the DMRC recently downloaded a metadata package for a device, it uses the cached metadata package for the device instead of searching the WMIS server for a newer package. For more information, see [How the DMRC Determines When to Search the WMIS Server](how-the-dmrc-determines-when-to-search-the-wmis-server.md).

 

The DMRC uses the following metadata XML elements, which are specified in the package, to select the appropriate package for a device. The order of these XML elements reflects the priority that the DMRC uses to select a metadata package:

-   [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) and [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303)

-   [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) and [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121)

-   [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647)

-   [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624)

The [DMRC](device-metadata-retrieval-client.md) follows these steps when it selects a metadata package for a device:

1.  If the device has a model ID, the DMRC searches device metadata packages for a match between a [**ModelID**](https://msdn.microsoft.com/library/windows/hardware/ff549295) entry in the package's [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303) XML element and the device's model ID value.

2.  If the device does not have a model ID, the DMRC searches device metadata packages for a match between the [**HardwareID**](https://msdn.microsoft.com/library/windows/hardware/ff546114) entries in the package's [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121) XML element and the device's hardware IDs.

3.  The DMRC creates a list of device metadata packages that meet the search criteria described in steps 1 and 2. From this list, the DMRC then searches the list entries for a match between the package's [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647) XML element and the list of preferred user locales on the computer.

    If no entries in the list match this search criterion, the DMRC searches the entries in the list for a device metadata package that contains a Locale XML element that has the **default** attribute set to **true**. If the DMRC finds a match, it selects that metadata package.

4.  If the DMRC finds more than one device metadata package during step 3, it selects the package that has a [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624) XML element that has the most recent time stamp.

The following points are relevant to the selection algorithm that is used by the [DMRC](device-metadata-retrieval-client.md):

-   If the DMRC selects a metadata package that is based on hardware IDs, it uses the same ranking of hardware IDs that the operating system uses during driver installation. The DMRC ranks more-specific hardware IDs larger than less-specific hardware IDs. For example, the following hardware IDs are listed in ranking order:

    ```cpp
    <HardwareID>DOID:USB\VID_XXXX&PID_YYYY&REV_0000</HardwareID>
    <HardwareID>DOID:USB\VID_XXXX&PID_YYYY</HardwareID>
    ```

    For the information about hardware IDs, see [Hardware IDs](hardware-ids.md).

-   Only one metadata package for a device should set the **default** attribute of the [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647) XML element to **true**. You should only set this attribute to true in the package that contains a hardware ID with the highest ranking value.

-   The [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624) XML element is used for versioning purposes and is used to select a newer version of a device metadata package for a device.

-   If two or more device metadata packages in the local metadata store contain the same values for the [**ModelIDList**](https://msdn.microsoft.com/library/windows/hardware/ff549303), [**HardwareIDList**](https://msdn.microsoft.com/library/windows/hardware/ff546121), [**Locale**](https://msdn.microsoft.com/library/windows/hardware/ff548647), or [**LastModifiedDate**](https://msdn.microsoft.com/library/windows/hardware/ff548624) XML elements, the DMRC selects only one of them for the device. In this case, the DMRC selects one of these packages in a nondeterministic manner.

For more information about the device metadata XML schema and elements, see [Device Metadata Schema Reference](https://msdn.microsoft.com/library/windows/hardware/ff541452).

 

 





