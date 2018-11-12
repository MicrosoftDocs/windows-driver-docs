---
title: Symmetric and Asymmetric Assignment of Queue Pairs
description: Symmetric and Asymmetric Assignment of Queue Pairs
ms.assetid: B4BA1567-D536-4E7D-924C-7476FB82DAEB
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Symmetric and Asymmetric Assignment of Queue Pairs


A queue pair consists of a separate transmit and receive queue on the network adapter. Queue pairs are configured on a virtual port (VPort) when the VPort is created. Queue pairs associated with the default VPort are configured at the time of switch creation through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_SWITCH](https://msdn.microsoft.com/library/windows/hardware/hh451815). One or more queue pairs are configured on a nondefault VPort through an OID method request of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816).

Each nondefault VPort can be configured to have a different number of queue pairs. This is known as *asymmetric allocation* of queue pairs. If the miniport driver does not support asymmetric allocations, each nondefault VPort is configured to have an equal number of queue pairs. This is known as *symmetric allocation* of queue pairs.

The miniport driver advertises its VPort and queue pair capabilities during [*MiniportInitializeEx*](https://msdn.microsoft.com/library/windows/hardware/ff559389) by using an [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure. The driver advertises its support for asymmetric allocation of queue pairs by setting the NDIS\_NIC\_SWITCH\_CAPS\_ASYMMETRIC\_QUEUE\_PAIRS\_FOR\_NONDEFAULT\_VPORT\_SUPPORTED flag in the **NicSwitchCapabilities** member of this structure.

If the miniport driver supports asymmetric queue pair allocation, the virtualization stack configures each nondefault VPort with a different number of queue pairs. If the miniport driver supports symmetric queue pair allocation, the virtualization stack configures each VPort with the same number of queue pairs.

**Note**  A miniport driver that supports either symmetric or asymmetric queue pair allocation on nondefault VPorts must support a different number of queue pairs to be allocated on the default VPort. The default VPort is always attached to the network adapter's PF.

 

The queue pair configuration is specified when the nondefault VPort is created or updated through OID requests of [OID\_NIC\_SWITCH\_CREATE\_VPORT](https://msdn.microsoft.com/library/windows/hardware/hh451816) and [OID\_NIC\_SWITCH\_VPORT\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/hh451825). The configuration parameters are specified in an [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/hh451597) structure that is associated with both OID requests.

For example, assume that the miniport driver advertises the configuration for VPorts and queue pairs on the NIC switch by setting the following members of the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](https://msdn.microsoft.com/library/windows/hardware/ff566583) structure:

-   **MaxNumQueuePairs** is set to 128.

-   **MaxNumVPorts** is set to 64.

-   **MaxNumQueuePairsPerNonDefaultPort** is set to 4.

If the miniport driver does not support asymmetric configuration of queue pairs on nondefault VPorts, the virtualization stack can specify the following queue pair configuration when VPorts are created:

-   63 nondefault VF VPorts with two queue pairs each, together with the default PF VPort with one queue pair.
-   31 nondefault VF VPorts with four queue pairs each, together with the default PF VPort with one queue pair.

**Note**  Starting with Windows Server 2012, only one default VPort is supported and is always attached to the network adapter's PF.

 

 

 





