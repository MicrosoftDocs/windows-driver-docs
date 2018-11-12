---
title: Managing Physical Network Adapters
description: Managing Physical Network Adapters
ms.assetid: 564841F2-997C-44F5-8EC9-264FC9128483
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing Physical Network Adapters


This section describes the operations that a Hyper-V extensible switch extension can perform on underlying physical adapters that are bound to the extensible switch external network adapter.

These operations allow an extension to forward or originate object identifier (OID) requests to an underlying physical network adapter. The extension can also forward or originate NDIS status indications from a physical network adapter up the extensible switch driver stack.

**Note**  Operations of this sort can only be performed by an extensible switch forwarding extension. For more information about this type of extension, see [Forwarding Extensions](forwarding-extensions.md).

 

This section includes the following topics:

[Managing Physical Network Adapter Connection Status](forwarding-packets-to-physical-network-adapters.md)

[Forwarding Packets to Physical Network Adapters](forwarding-packets-to-physical-network-adapters.md)

[Managing OID Requests to Physical Network Adapters](managing-oid-requests-to-physical-network-adapters.md)

[Managing NDIS Status Indications from Physical Network Adapters](managing-ndis-status-indications-from-physical-network-adapters.md)

 

 





