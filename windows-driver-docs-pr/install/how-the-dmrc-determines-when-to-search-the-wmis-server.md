---
title: How the DMRC Determines When to Search the WMIS Server
description: How the DMRC Determines When to Search the WMIS Server
ms.assetid: dc68045e-85c2-443d-9e4d-099bbd21590d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How the DMRC Determines When to Search the WMIS Server


The device metadata retrieval client ([DMRC](device-metadata-retrieval-client.md)) maintains a cache of device metadata packages. This cache is populated with metadata packages that the DMRC downloaded from the Windows Metadata and Internet Services ([WMIS](windows-metadata-and-internet-services.md)) server.

When the Devices and Printers or Device Stage user interfaces (UIs) are opened, the DMRC searches its cache for the most appropriate and current metadata package of every device that is displayed in the UI.

Periodically, before it selects a metadata package from its cache, the DMRC searches for a newer metadata package for a device on the [WMIS](windows-metadata-and-internet-services.md) server. If one is found, the DMRC downloads the package and installs it in its cache on the computer. Then, the DMRC selects the newer version of the metadata package from its cache.

Based on the following values, the DMRC determines when to search the [WMIS](windows-metadata-and-internet-services.md) server for a newer metadata package for a device:

<a href="" id="lastcheckeddate"></a>**LastCheckedDate**  
This value indicates the most recent date when the DMRC queried the WMIS server for metadata for a device. This date does not reflect whether the DMRC successfully downloaded a metadata package.

The DMRC manages an index table that contains the properties for the device metadata package of each [device ID](device-ids.md) in the system. The **LastCheckedDate** value is a field of each row in this index table.

<a href="" id="checkbackmdnotretrieved"></a>**CheckBackMDNotRetrieved**  
This registry value indicates the number of days that the DMRC waits before it repeats a query of the WMIS server for a device metadata package. This value applies to devices for which the DMRC has not yet downloaded metadata from WMIS.

The **CheckBackMDNotRetrieved** value is located under the following registry key:

```cpp
HKLM\Software\Microsoft\Windows\CurrentVersion\Device Metadata
```

The following table describes the format and value range for the **CheckBackMDNotRetrieved** value.

| Data type  | Value range         | Default value |
|------------|---------------------|---------------|
| [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) | 0 to 256, inclusive | 5             |

 

<a href="" id="checkbackmdretrieved"></a>**CheckBackMDRetrieved**  
This registry value indicates the number of days that the DMRC waits before it queries for updated device metadata packages. This value applies to devices for which the DMRC previously downloaded metadata packages.

The **CheckBackMDRetrieved** value is located under the following registry key:

```cpp
HKLM\Software\Microsoft\Windows\CurrentVersion\Device Metadata
```

The following table describes the format and value range for the **CheckBackMDRetrieved** value.

| Data type  | Value range         | Default value |
|------------|---------------------|---------------|
| [REG_DWORD](https://docs.microsoft.com/windows/desktop/SysInfo/registry-value-types) | 0 to 256, inclusive | 8             |

 

**Note**  The WMIS server, in cooperation with the DMRC, sets the values for the **CheckBackMDRetrieved** and **CheckBackMDNotRetrieved** registry values on the client system. These values are set based on network conditions and load balancing. Every response from the WMIS server contains the client configuration data and controls the DMRC behavior.

 

The DMRC follows these steps to determine whether it has to search the WMIS server for a newer metadata package for a device:

1.  If the target device's [device ID](device-ids.md) is not listed in the DMRC index table, the DMRC is searching for the device's metadata package for the first time. In this case, the DMRC queries the WMIS server.

2.  If the target device's [device ID](device-ids.md) is listed in the DMRC index table, the DMRC calculates whether it is time to query the WMIS server again for a metadata package for the device. In this case, the DMRC queries the WMIS server in the following way:

    1.  If the DMRC has previously downloaded a device metadata package for the device, the DMRC compares the value of the **CheckBackMDRetrieved** registry key to the value of today's date minus the **LastCheckedDate** value. If the **CheckBackMDRetrieved** value is smaller, the DMRC queries the WMIS server.

    2.  If the DMRC has not previously downloaded a device metadata package for the device, the DMRC compares the value of the **CheckBackMDNotRetrieved** registry key to the value of today's date minus the **LastCheckedDate** value. If the **CheckBackMDNotRetrieved** value is smaller, the DMRC queries the WMIS server.

 

 





