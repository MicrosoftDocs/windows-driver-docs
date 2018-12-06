---
title: Extension Driver MSI Packaging Requirements
description: Switch extensions must be packaged in a silently installable MSI file.
ms.assetid: 300118F9-D9C7-4AFA-B54A-59666BC680F1
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Extension Driver MSI Packaging Requirements


Switch extensions must be packaged in a silently installable MSI file. This file can then be deployed to the computer where the extensions are used by management applications automatically.

The MSI file must meet the following requirements:

-   Drivers must be packaged and distributed in the standard MSI package format.
-   The MSI package must be silently uninstallable.
-   The MSI package can contain only one extension.
-   The MSI package must contain the required table fields described in the MSI table fields listed below. In addition, the MSI file must be able to silently install the driver .sys, .inf and any supplemental files required for the driver to operate using the parameters described in the *DriverInstallParams* field of the MSI Properties table fields list below.

| Field                           | Required | Type       | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------|----------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description**                 | Required | **String** | Description for the extension that is displayed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Manufacturer**                | Required | **String** | Name of the company publishing the extension driver. Localized strings can be stored.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **ProductVersion**              | Required | **String** | The version of the this MSI package. Example: 1.0.0.0                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **ProductName**                 | Required | **String** | Name of the driver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **DriverID**                    | Required | **String** | Must match the Msvm\_InstalledEthernetSwitchExtension.Name field that is available after the driver is installed and the driver ID in the driver’s INF file.                                                                                                                                                                                                                                                                                                                                                    |
| **DriverVersion**               | Required | **String** | The version of the driver contained in this package. Example: 1.0.0.0                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **ExtensionType**               | Required | **String** | Type of the extension. Values: Forwarding, Capture, Monitoring, Filter                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **DriverInstallParams**         | Required | **String** | Parameters used to install this driver silently. Example: /q                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **IsManagedByExtensionManager** | Optional | **String** | Present and non-zero = Yes, 0 or not present = No                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **MinApplicableOSVersion**      | Required | **String** | The minimum version of the Windows operating system that this extension will run on. See Operating System Version for operating system version numbers. Note that the Hyper-V Extensible Switch feature was added in Windows Server 2012, so the lowest valid value for this field is "6.2".                                                                                                                                                                                                                    |
| **MaxApplicableOSVersion**      | Optional | **String** | The maximum version of the Windows operating system that this extension will run on. See [Operating System Version](https://msdn.microsoft.com/library/windows/desktop/ms724832) for operating system version numbers. Note that the Hyper-V Extensible Switch feature was added in Windows Server 2012, so the lowest valid value for this field is "6.2" or the value of **MinApplicableOSVersion**, whichever is higher. This field is optional. If no value is specified, the extension will run on **MinApplicableOSVersion** and later. |

 

 

 





