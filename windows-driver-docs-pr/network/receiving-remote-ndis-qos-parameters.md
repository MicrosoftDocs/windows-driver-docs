---
title: Receiving Remote NDIS QoS Parameters
description: Receiving Remote NDIS QoS Parameters
ms.assetid: 775FA8D7-ECF7-4F94-8958-C51D74243C3A
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Receiving Remote NDIS QoS Parameters


Remote NDIS Quality of Service (QoS) parameters are those that are received from a remote peer that the network adapter is connected to over the data link. The miniport driver discovers these parameters through the Data Center Bridging Exchange (DCBX) protocol that is specified by the IEEE 802.1Qaz draft standard.

The driver must follow these guidelines for managing remote QoS parameters:

-   The miniport driver must issue an [**NDIS\_STATUS\_QOS\_REMOTE\_PARAMETERS\_CHANGE**](https://msdn.microsoft.com/library/windows/hardware/hh439812) status indication when its remote NDIS QoS parameters are either received from a peer for the first time or change later. For more information on this procedure, see [Indicating Changes to the Remote NDIS QoS Parameters](indicating-changes-to-the-remote-ndis-qos-parameters.md).

-   The miniport driver can use the remote NDIS QoS parameters to resolve its operational NDIS QoS parameters only if the local Data Center Bridging Exchange (DCBX) Willing state is enabled on the network adapter. The miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the independent hardware vendor (IHV).

    For more information about this procedure, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

    For more information about the local DCBX Willing state, see [Managing the Local DCBX Willing State](managing-the-local-dcbx-willing-state.md).

For more information about NDIS QoS parameters, see [Overview of NDIS QoS Parameters](overview-of-ndis-qos-parameters.md).

 

 





