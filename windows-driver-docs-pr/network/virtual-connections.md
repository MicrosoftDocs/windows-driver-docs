---
title: Virtual Connections
description: Virtual Connections
ms.assetid: becb3acf-2a23-408a-8d1f-ff8a1e7ffe61
keywords:
- connection-oriented NDIS WDK , virtual connections
- CoNDIS WDK networking , virtual connections
- virtual connections WDK CoNDIS
- virtual connections WDK CoNDIS , about virtual connections
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Virtual Connections





On a local computer, a *virtual connection (VC)* is an endpoint (or association) that can host a single call between a client, call manager or MCM driver, and a miniport driver. On the network, a VC refers to a connection between two communicating endpoints, such as two connection-oriented clients.

Many VCs can be active on a NIC at the same time, enabling the NIC to simultaneously service many calls. Each connection can be to different endpoints on different computers.

VCs on a network vary in the type of service that they provide to clients. For example, a VC can provide unidirectional or bidirectional service. Quality of service (QoS) parameters for each direction can guarantee specific performance thresholds, such as bandwidth and latency. Depending on the signaling protocol, the QoS for a VC may be negotiable. For more information about NDIS support of QoS, see [Quality of Service](quality-of-service.md).

A VC on a network can be a switched VC (SVC) or a permanent VC (PVC):

-   An SVC is created as needed for a particular call. For example, a connection-oriented client initiates the creation of a VC for an outgoing call that it is going to make. Similarly, a call manager or MCM driver initiates the creation of a VC for an incoming call that it is going to indicate to a connection-oriented client. The call manager or MCM driver must communicate and sometimes negotiate the parameters for the VC with the remote party.

-   A permanent VC is manually created and eventually deleted by an operator using a configuration utility, which is not supplied in NDIS. A client that monitors such manual creation and deletion of PVCs can use the [OID\_CO\_ADD\_PVC](https://msdn.microsoft.com/library/windows/hardware/ff569087) and [OID\_CO\_DELETE\_PVC](https://msdn.microsoft.com/library/windows/hardware/ff569090) OIDs to request that a call manager or MCM driver add or delete a PVC to or from its list of configured PVCs. The QoS for a PVC is configured by the operator and is not negotiable over the network.

In NDIS, a VC consists of resources that are allocated by a miniport driver to maintain state information about a VC on a network. These resources could include, but are not limited to, memory buffers, events, and data structures. The miniport driver is requested to create such a context for a VC by a connection-oriented client for an outgoing call or a call manager for an incoming call. For more information about the creation of VCs, see [Creating a VC](creating-a-vc.md).

Before a created VC can be used for data transmission, it must be activated by a call manager or MCM driver. To activate a VC, a miniport driver or MCM driver sets up resources for the VC and communicates with a NIC as necessary to prepare the NIC to receive or transmit data on the VC. For more information about VC activation, see [Activating a VC](activating-a-vc.md).

When tearing down a call, a call manager or MCM driver [deactivates the VC](deactivating-a-vc.md) used for the call.

After a call is torn down, the creator of the VC (a connection-oriented client, call manager, or MCM driver) can either initiate the [deletion of the VC](deleting-a-vc.md) or use the VC for another call.

 

 





