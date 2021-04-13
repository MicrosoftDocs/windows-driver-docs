---
title: Advertising VMMQ capabilities
description: Miniport drivers register the VMMQ capability of a NIC during miniport adapter initialization.
ms.date: 02/28/2021
ms.localizationpriority: medium
---


# Advertising VMMQ capabilities

Miniport drivers register the [Virtual Machine Multiple Queues (VMMQ)](overview-of-virtual-machine-multiple-queues.md) capability of a NIC during miniport adapter initialization.

> [!NOTE]
> If the NIC supports VMMQ, the default VPort and at least one non-default VPort must support VMMQ.

During initialization, the miniport driver must examine the **\*RssOnHostVPorts** INF keyword in order to determine if it should enable the VMMQ feature on the NIC. For more information on handling RSS keywords for VMMQ, see [Standardized INF keywords for VMMQ](standardized-inf-keywords-for-vmmq.md). 

Additionally, the stack can only activate VMMQ on the NIC if the miniport adapter supports creating a NIC switch. NDIS can create a NIC switch on the miniport adapter when either the **\*SriovPreferred** INF keyword is set to **one** or **\*SriovPreferred** is set to **zero** and **\*RssOrVmqPreference** is set to **one**. For more information, see [Standardized INF Keywords for SR-IOV](standardized-inf-keywords-for-sr-iov.md) and [Standardized INF Keywords for VMQ](standardized-inf-keywords-for-vmq.md). 

When the miniport driver configures the parameters for the NIC switch, it must set the fields of the [**NDIS\_NIC\_SWITCH\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_parameters) structure as follows:

1. Set the **Revision** member of **Header** to   **NDIS\_NIC\_SWITCH\_PARAMETERS\_REVISION\_2**.

2. Set **NumQueuePairsForDefaultVPort** to the number of queue pairs assigned to a default VPort.

Miniport drivers advertise the NIC's VMMQ capability through the [**NDIS\_NIC\_SWITCH\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_capabilities) structure. The miniport driver must initialize **NDIS\_NIC\_SWITCH\_CAPABILITIES** as follows:

1. Set the **Revision** member of **Header** to **NDIS\_NIC\_SWITCH\_CAPABILITIES\_REVISION\_3**.

2. Set the **NicSwitchCapabilities** flags as follows:

   - Set NDIS\_NIC\_SWITCH\_CAPS\_SINGLE\_VPORT\_POOL to **one** to indicate that non-default VPorts can be created on the PF. This flag must be set. 

   - Set NDIS\_NIC\_SWITCH\_CAPS\_ASYMMETRIC\_QUEUE\_PAIRS\_FOR\_NONDEFAULT\_VPORT\_SUPPORTED to indicate that NDIS can allocate an arbitrary number of VMMQ queues on each VPort. Otherwise, all non-default VPorts have the same maximum number of VMMQ queues as the **MaxNumQueuePairsPerNonDefaultVPort** field defines. 

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_ON\_PF\_VPORTS\_SUPPORTED to **one** to indicate that the NIC supports VMMQ for PF VPorts.
    
    > [!NOTE]
    > If any of the following four per PF VPort flags are not set, higher level drivers will use the values that are specified when the RSS parameters of the PF VPorts are set (including the default VPort). For more information see [Enabling, disabling, and updating VMMQ on a VPort](updating-vmmq-on-a-vport.md).

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_INDIRECTION\_TABLE\_SUPPORTED to **one** to indicate that the NIC is able to maintain per PF VPort indirection tables. This flag must be set.
    
   > [!NOTE]
   > The following three flags NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_FUNCTION\_SUPPORTED, NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_TYPE\_SUPPORTED, and NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_KEY\_SUPPORTED must all be set to **zero** or all be set to **one**. If they're all set to **zero**, software will re-calculate the hash. 
    

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_FUNCTION\_SUPPORTED to **one** if the NIC supports setting a different hash function per PF VPort.

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_TYPE\_SUPPORTED to **one** if the NIC supports setting a different hash type per PF VPort. 

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_KEY\_SUPPORTED to **one** if the NIC supports setting a different hash secret key per PF VPort.

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_INDIRECTION\_TABLE\_SIZE\_RESTRICTED to **one** if the NIC has a limitation on indirection table size for PF VPorts. This flag forces the issuer of an RSS OID to use a per-PF VPort indirection table size equal to the number of VPort queues rounded up to the next power of two. This flag can be combined with the NDIS_NIC_SWITCH_CAPS_ASYMMETRIC_QUEUE_PAIRS_FOR_NONDEFAULT_VPORT_SUPPORTED flag (different PF VPorts can have different numbers of queues). This flag prevents VMMQ users from performing fine-grained queue steering.

1. Set **MaxNumVPorts** to specify the maximum number of VPorts.

1. Set  **MaxNumQueuePairs** to specify the maximum number of queue pairs that can be assigned to all VPorts. This includes the default VPort that is attached to the PF. This number should reflect the actual hardware capabilities. 

1. Set **MaxNumQueuePairsPerNonDefaultVPort** to specify the maximum number of queue pairs that can be assigned to a non-default VPort.

1. Set **MaxNumRssCapableNonDefaultPFVPorts** to specify the maximum number of non-default PF VPorts that can support VMMQ. 

1. Set **NumberOfIndirectionTableEntriesForDefaultVPort** to specify the number of indirection table entries for the default VPort.

1. Set **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** to specify the number of indirection table entries for each non-default PF VPort. The size of indirection table should be the same for all non-default PF VPorts.

1. Set **MaxNumQueuePairsForDefaultVPort** to specify the maximum number of queue pairs that can be assigned to a default VPort during NIC Switch creation.

After the VMMQ capabilities are advertised, NDIS is responsible for handling the [OID_GEN_RECEIVE_SCALE_CAPABILITIES](./oid-gen-receive-scale-capabilities.md) OID when it is called on either the default VPort or a non-default VPort. When the miniport driver returns the RSS capabilities in the [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities) structure, it should not constrain the **NumberOfInterruptMessages** fields  by any of the standard RSS keywords (such as **\*MaxRssProcessors**). The upper level driver will incorporate this number into the host CPU allocation algorithm.