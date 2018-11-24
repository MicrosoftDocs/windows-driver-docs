---
title: Supporting Standard WMI Blocks
description: Supporting Standard WMI Blocks
ms.assetid: ddec3afb-8274-4eff-93ef-b0a07fd7c13a
keywords: ["WMI WDK kernel , event blocks", "event blocks WDK WMI", "data blocks WDK WMI", "WMI WDK kernel , data blocks", "blocks WDK WMI", "standard blocks WDK WMI"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Supporting Standard WMI Blocks





Each driver should support any *standard blocks* defined for drivers of its type. Standard blocks provide WMI clients with consistent data for all devices of a given type, regardless of vendor.

To support a standard block, a driver:

-   Registers the block with WMI, along with the other standard and custom blocks supported by the driver, as described in [Registering as a WMI Data Provider](registering-as-a-wmi-data-provider.md).

-   Handles all WMI requests that specify the driver's device object pointer at **Parameters.WMI.ProviderId** and the GUID of the standard block at **Parameters.WMI.DataPath**, as described in [Handling WMI Requests](handling-wmi-requests.md).

MOF classes for standard blocks are published in system-supplied MOF files. A driver must not redefine a standard block in its own MOF file, because doing so would duplicate the block in the WMI database.

Currently, class definitions of standard blocks are published in the file wmicore.mof, which is included in the Windows Driver Kit (WDK).

 

 




