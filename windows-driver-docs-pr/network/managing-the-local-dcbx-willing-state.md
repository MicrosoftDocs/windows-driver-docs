---
title: Managing the Local DCBX Willing State
description: Managing the Local DCBX Willing State
ms.assetid: B37CA18B-FCCD-414D-95AB-0C54B9F1F421
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Managing the Local DCBX Willing State


The IEEE 802.1Qaz draft standard defines the Data Center Bridging Exchange (DCBX) protocol. This protocol allows DCB configuration parameters to be exchanged between the network adapter (local peer) and a directly connected remote peer. This allows these peers to adapt and tune Quality of Service (QoS) parameters to optimize data transfer over the connection.

Based on the local and remote QoS parameter settings, the miniport driver resolves the conflicts and derives a set of operational QoS parameters. The network adapter uses these operational parameters for the prioritized transmission of packets to the remote peer. For more information about how the driver resolves its operational NDIS QoS parameter settings, see [Resolving Operational NDIS QoS Parameters](resolving-operational-ndis-qos-parameters.md).

DCBX consists of DCB type-length-value (TLV) settings that are carried over Link Layer Discovery Protocol (LLDP) packets. A separate TLV is defined for the following types of QoS parameters:

-   [Enhanced Transmission Selection (ETS)](enhanced-transmission-selection--ets--algorithm.md)

-   [Priority-based Flow Control (PFC)](priority-based-flow-control--pfc.md)

The TLVs for ETS and PFC define a bit known as the *Willing* bit. If the network adapter sends its TLV settings to the remote peer with the Willing bit set to one, it indicates that the adapter is willing to accept QoS parameters from the remote peer.

The ability to set individual Willing bits in these TLVs depends on the local DCBX Willing state that is managed by the miniport driver. The miniport driver must follow these guidelines for managing the local DCBX Willing state:

-   If the local DCBX Willing state is disabled, the local Willing bit must be set to zero in the DCBX TLVs. In this case, the operational QoS parameters are always resolved from the local QoS parameters. For more information on these parameters, see [Setting Local NDIS QoS Parameters](setting-local-ndis-qos-parameters.md).

-   If the local DCBX Willing state is enabled, the local Willing bit must be set to one in the DCBX TLVs. In this case, the operational QoS parameters must be resolved from the remote QoS parameters. For more information on these parameters, see [Receiving Remote NDIS QoS Parameters](receiving-remote-ndis-qos-parameters.md).

    **Note**  If local DCBX Willing state is enabled, the miniport driver can also resolve its operational QoS parameters based on any proprietary QoS settings that are defined by the independent hardware vendor (IHV). The driver can only do this for QoS parameters that are not configured remotely by the peer or locally by the operating system.

     

The miniport driver manages the local DCBX Willing state in the following way:

-   When the miniport driver is initialized through a call to its [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) function, it should enable the local DCBX Willing state based on proprietary QoS settings that are defined by the IHV.

-   The DCB component (Msdcb.sys) issues an object identifier (OID) method request of [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) to configure the local QoS parameters on a network adapter. The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](https://msdn.microsoft.com/library/windows/hardware/ff566710) structure for this OID request contains a pointer to an [**NDIS\_QOS\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451640) structure.

    If the **NDIS\_QOS\_PARAMETERS\_WILLING** flag is set in the **Flags** member of this structure, the miniport driver enables the DCBX Willing state. If this bit is not set, the miniport driver disabled the DCBX Willing state.

For more information about LLDP, refer to the IEEE 802.1AB-2005 standard.

For more information about the local DCBX Willing bits and TLVs, refer to the IEEE 802.1Qaz draft standard.

**Note**  Starting with Windows Server 2012, the DCB component can be configured through a PowerShell cmdlet to set or clear the **NDIS\_QOS\_PARAMETERS\_WILLING** flag when it issues an [OID\_QOS\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451835) request. This causes the miniport driver to respectively enable or disable the local DCBX Willing state.

 

 

 





