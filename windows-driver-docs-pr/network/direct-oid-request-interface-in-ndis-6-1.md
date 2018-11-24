---
title: Direct OID Request Interface in NDIS 6.1
description: Direct OID Request Interface in NDIS 6.1
ms.assetid: 1a24dec6-f16a-45f5-857b-c6e0df4ce261
keywords:
- direct OID request interface WDK networking
- direct OID request path WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct OID Request Interface in NDIS 6.1





NDIS provides a direct OID request interface for NDIS 6.1 and later drivers. The *direct OID request path* supports OID requests that are queried or set frequently. For example, the IPsec offload version 2 (IPsecOV2) interface provides the [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812) OID for direct OID requests.

The direct OID request interface is optional for NDIS drivers. To support the direct OID path, drivers provide entry points and NDIS provides **Ndis*Xxx*** functions for protocol, filter, and miniport drivers.

**Note**  NDIS supports specific OIDs for use with the direct OID request interface. To determine whether your driver can use an OID in the direct OIDs interface, see the notes in the OID reference page.

 

For NDIS 6.1, the only interface that uses the direct OID request interface is IPsecOV2. For more information about IPsecOV2, see [IPsec Task Offload Version 2 in NDIS 6.1](ipsec-task-offload-version-2-in-ndis-6-1.md).

For NDIS 6.1 drivers in the Windows Server 2008 and Windows Vista with Service Pack 1 (SP1) operating systems, you can use only the following OIDs with the direct OID request interface:

-   [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_ADD\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569812)

-   [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_DELETE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569813)

-   [OID\_TCP\_TASK\_IPSEC\_OFFLOAD\_V2\_UPDATE\_SA](https://msdn.microsoft.com/library/windows/hardware/ff569814)

Miniport drivers and filter drivers must be able to handle direct OID requests that are not serialized. Unlike the standard OID request interface, NDIS does not serialize direct OID requests with other requests that are sent with the direct OID interface or with the standard OID request interface. Also, miniport drivers and filter drivers must be able to handle direct OID requests at IRQL &lt;= DISPATCH\_LEVEL.

For more information about how to implement the direct OID interface in drivers, see the following topics:

-   [Miniport Adapter OID Requests](miniport-adapter-oid-requests.md)

-   [Protocol Driver OID Requests](protocol-driver-oid-requests.md)

-   [Filter Module OID Requests](filter-module-oid-requests.md)

 

 





