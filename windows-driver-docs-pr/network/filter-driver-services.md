---
title: Filter Driver Services
description: Filter Driver Services
ms.assetid: 72ee00c6-0887-46bd-a329-ee7bf0dd2c06
keywords:
- filter drivers WDK networking , services
- NDIS filter drivers WDK , services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Filter Driver Services





Filter drivers can provide the following services:

-   Originate send requests and receive indications.

-   Modify data buffer ordering or timing in the send and receive data paths.

-   Add, modify, delete network data buffers in both the send and receive data paths of a driver stack. For more information about filtering send and receive data, see [Filter Module Send and Receive Operations](filter-module-send-and-receive-operations.md).

-   Originate query and set OID requests to the underlying drivers.

-   Filter query and set OID requests to the underlying drivers.

-   Filter responses of OID requests from the underlying drivers. For more information about OID requests, see [Filter Module OID Requests](filter-module-oid-requests.md).

-   Originate status indications to the overlying drivers.

-   Filter status indications from the underlying drivers. For more information, see [Filter Module Status Indications](filter-module-status-indications.md).

-   Manage configuration parameters in the registry for each miniport adapter with which it interfaces. For more information, see [Accessing Configuration Information for a Filter Driver](accessing-configuration-information-for-a-filter-driver.md).

 

 





