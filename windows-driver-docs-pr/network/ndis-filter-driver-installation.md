---
title: NDIS Filter Driver Installation
description: NDIS Filter Driver Installation
ms.assetid: 8e0c47bf-6b63-4be5-98b7-7a99e9efe283
keywords:
- filter drivers WDK networking , installation
- NDIS filter drivers WDK , installation
- installing NDIS filter drivers WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NDIS Filter Driver Installation





This section provides information about installing NDIS filter drivers. Filter drivers are different from filter intermediate drivers. The configuration manager installs filter drivers as autostart services, similar to protocol drivers. The configuration manager supplies NDIS with a list of filter modules for each miniport adapter. There is no virtual device (or virtual miniport) that is associated with a filter driver as there is with an NDIS filter intermediate driver.

To install a filter driver, you must provide a single INF file. The configuration manager reads configuration information about the filter driver from the INF file and copies it to the registry. In contrast, filter intermediate drivers require two INF files: one of the INF files defines the installation parameters for the protocol lower edge, and the other INF file defines the installation parameters for the virtual miniport upper edge.

The filter driver INF file defines a network service that is similar to the filter intermediate driver's protocol INF file. Filter drivers do not have a miniport INF file.

This section includes:

[Specifying Filter Driver Binding Relationships](specifying-filter-driver-binding-relationships.md)

[INF File Settings for Filter Drivers](inf-file-settings-for-filter-drivers.md)

[Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md)

 

 





