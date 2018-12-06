---
title: Simplified Reset Handling
description: Simplified Reset Handling
ms.assetid: ac07bfe3-9144-422a-96ca-d2ca2cc6861d
keywords:
- NDIS miniport drivers WDK , resetting miniport adapters
- resetting miniport adapters
- adapters WDK networking , reset operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Simplified Reset Handling





NDIS 6.0 and later drivers do not reset miniport adapters to cancel send or OID requests. Instead, NDIS provides send cancellation and OID request cancellation functions.

An NDIS miniport driver can complete or cancel a pending send operation or pending OID request at any time -- either before or after completing a reset. The miniport driver does not have to keep track of when it received a request with respect to a reset. Also, the driver does not have to synchronize a canceled request with the completion of a reset.

For more information, see [Canceling a Send Operation](canceling-a-send-operation.md), [OID Requests for an Adapter](miniport-adapter-oid-requests.md), [Protocol Driver OID Requests](protocol-driver-oid-requests.md), and [Filter Module OID Requests](filter-module-oid-requests.md).

 

 





