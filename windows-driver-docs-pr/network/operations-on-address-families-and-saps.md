---
title: Operations on Address Families and SAPs
description: Operations on Address Families and SAPs
ms.assetid: 0fc821bb-49a2-4631-8735-ef5217073ba9
keywords:
- connection-oriented NDIS WDK , address families
- CoNDIS WDK networking , address families
- connection-oriented NDIS WDK , service access points
- CoNDIS WDK networking , service access points
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Operations on Address Families and SAPs





A call manager or MCM driver must register its call manager entry points with NDIS and advertise its call manager services to connection-oriented clients. For more information about registering enttry points with NDIS, see [CoNDIS Registration](condis-registration.md).

To use the call manager services of a call manager or MCM driver, a connection-oriented client must open an address family with that call manager or MCM driver. To receive incoming calls, the client must also register one or more SAPs with the call manager or MCM driver.

The following connection-oriented operations pertain to address families and SAPs:

[Registering and Opening an Address Family](registering-and-opening-an-address-family.md)

[Registering a SAP](registering-a-sap.md)

[Deregistering a SAP](deregistering-a-sap.md)

[Closing an Address Family](closing-an-address-family.md)

 

 





