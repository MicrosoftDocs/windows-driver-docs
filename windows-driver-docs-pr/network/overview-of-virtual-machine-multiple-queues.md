# Overview of Virtual Machine Multiple Queues

Figure 1.  VMMQ architecture.

Virtual Machine Multiple Queues (VMMQ), formerly known as Hardware vRSS, is a NIC offload technology that provides scalability for processing network traffic of a VPort in the host (root partition) of a virtualized node. In essence, VMMQ extends the native RSS feature to the VPorts that are associated with the physical function (PF) of a NIC including the default VPort.

VMMQ is available for the VPorts exposed in the host (root partition) regardless of whether the NIC is operating in SR-IOV or VMQ mode. VMMQ is a feature available to NDIS 6.60 drivers.

# Advertising VMMQ capabilities

Miniport drivers register the [Virtual Machine Multiple Queues (VMMQ)](ADD LINK) capability of a NIC during miniport adapter initialization.

> [!NOTE]
> If the NIC supports VMMQ, the default VPort and at least one non-default VPort must support VMMQ.

During initialization, the miniport driver must examine the **\*RssOnHostVPorts** INF keyword in order to determine if it should enable the VMMQ feature on the NIC. For more information on handling RSS keywords for VMMQ, see [Standardized INF keywords for VMMQ](ADD LINK). 

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
    > If any of the following five per PF VPort flags are not set, higher level drivers will use the values that the miniport driver set when it specified the RSS parameters of the PF VPorts (including the default VPort).

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_INDIRECTION\_TABLE\_SUPPORTED to **one** to indicate that the NIC is able to maintain per PF VPort indirection tables. This flag must be set.
    
   > [!NOTE]
   > The following three flags NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_FUNCTION\_SUPPORTED, NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_TYPE\_SUPPORTED, and NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_KEY\_SUPPORTED must all be set to **zero** or all be set to **one**. If they're all set to **zero**, software will re-calculate the hash. 
    

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_FUNCTION\_SUPPORTED to **one** if the NIC supports setting a different hash function per PF VPort.

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_TYPE\_SUPPORTED to **one** if the NIC supports setting a different hash type per PF VPort. 

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_HASH\_KEY\_SUPPORTED to **one** if the NIC supports setting a different hash secret key per PF VPort.

    - Set NDIS\_NIC\_SWITCH\_CAPS\_RSS\_PER\_PF\_VPORT\_INDIRECTION\_TABLE\_SIZE\_RESTRICTED to **one** if the NIC has a limitation on indirection table size for PF VPorts. This flag prevents VMMQ users from performing fine-grained queue steering.

1. Set **MaxNumVPorts** to specify the maximum number of VPorts.

1. Set  **MaxNumQueuePairs** to specify the maximum number of queue pairs that can be assigned to all VPorts. This includes the default VPort that is attached to the PF. This number should reflect the actual hardware capabilities. 

1. Set **MaxNumQueuePairsPerNonDefaultVPort** to specify the maximum number of queue pairs that can be assigned to a non-default VPort.

1. Set **MaxNumRssCapableNonDefaultPFVPorts** to specify the maximum number of non-default PF VPorts that can support VMMQ. 

1. Set **NumberOfIndirectionTableEntriesForDefaultVPort** to specify the number of indirection table entries for the default VPort.

1. Set **NumberOfIndirectionTableEntriesPerNonDefaultPFVPort** to specify the number of indirection table entries for each non-default PF VPort. The size of indirection table should be the same for all non-default PF VPorts.

1. Set **MaxNumQueuePairsForDefaultVPort** to specify the maximum number of queue pairs that can be assigned to a default VPort during NIC Switch creation.

After the VMMQ capabilities are advertised, NDIS is responsible for handling the [OID_GEN_RECEIVE_SCALE_CAPABILITIES](/windows-hardware/drivers/network/oid-gen-receive-scale-capabilities) OID when it is called on either the default VPort or a non-default VPort. When the miniport driver returns the RSS capabilities in the [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities) structure, it should not constrain the **NumberOfInterruptMessages** fields  by any of the standard RSS keywords (such as **\*MaxRssProcessors**). The upper level driver will incorporate this number into the host CPU allocation algorithm.

# Standardized INF keywords for VMMQ

The **\*RssOnHostVPorts** standardized INF keyword is defined to enable or disable support for the network adapter [Virtual Machine Multiple Queues (VMMQ)](ADD LINK) feature.

The **\*RssOnHostVPorts** INF keyword is an enumeration keyword. Enumeration standardized INF keywords have the following attributes:

SubkeyName: The name of the keyword that you must specify in the INF file.

ParamDesc: The display text that is associated with the SubkeyName. 

Value: The enumeration integer value that is associated with each SubkeyName in the list. 

EnumDesc: The display text that is associated with each value that appears in the menu.

Default: The default value for the menu.

The following table describes the possible INF entries for the **\*RssOnHostVPorts** INF keyword.

| SubkeyName       | ParamDesc          | Value       | EnumDesc |
|-------------------|--------------------|-------------|----------|
| \*RssOnHostVPorts | Virtual Switch RSS | 0 (Default) | Disabled |
|                   |                    | 1           | Enabled  |

During miniport adapter initialization, the miniport driver must examine the **\*RssOnHostVPorts** keyword to determine if it should enable the VMMQ feature on the NIC.

## Handling RSS INF keywords for VMMQ

If a NIC supports VMMQ, all [Standardized INF Keywords for RSS](standardized-inf-keywords-for-rss.md) should also be supported to provide future compatibility even if the OS doesn't not currently use them all.
You should use the keywords as normal for RSS functionality except for:

-   **\*RSSProfile**: The “ClosestProcessor” profile should be supported and used as a policy for VMMQ.

-   **\*MaxRssProcessors**: When VMMQ is active, this keyword should not restrict the number of MSIx interrupt messages reported in [**NDIS\_RECEIVE\_SCALE\_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_capabilities).

# Allocating VPorts (For VMMQ?)

NDIS allocates VPorts when the [Virtual Machine Multiple Queues (VMMQ)](ADD LINK) capability is present in the following way.

NDIS creates a non-default VPort on the miniport adapter by issuing the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) OID request. When creating an RSS Physical Function (PF) VPort, NDIS will initialize the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure as follows:

- NDIS sets the **AttachedFunctionId** field to **NDIS\_PF\_FUNCTION\_ID**.

- If VMMQ is enabled, NDIS sets the **NumQueuePairs** field to the number of VMMQ queue pairs that should be used for this VPort. This number includes the default RSS processor for this VPort. It is guaranteed that total number of processors will not exceed this number. If VMMQ is disabled, NDIS sets this value to **one**.

- If VMMQ is enabled, the **ProcessorAffinity** field defines a bitmask of the potential RSS processors that the miniport adapter must use for this VPort. The processors that the network stack used to populate the indirection table entries for the VPort are a subset of the processors that this bitmask identifies. The mask will be a subset of the RSS processors returned from the call to [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation) and the number of set bits might exceed the number of RSS queues requested for the VPort. If VMMQ is disabled, the miniport adapter must use the lowest processor number specified in this bitmask when setting the affinity of the VPort queue.

- NDIS sets the NDIS\_NIC\_SWITCH\_VPORT\_PARAMS\_NUM\_QUEUE\_PAIRS\_CHANGED flag to indicate that the **NumQueuePairs** member has been updated after the VPort has been created. When VMMQ is enabled, the number of queues for default and non-default Vports can be updated. 

# Enabling and Disabling VMMQ on a Particular VPort

After creating a VPort, an upper layer driver can enable or disable [Virtual Machine Multiple Queues (VMMQ)](ADD LINK) on the VPort. 

The upper layer driver enables, disables, or changes the RSS parameters of a VPort by issuing an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID request. The upper layer driver sets the **VPortId** field in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the ID of the target VPort of the new configuration. 

The upper layer driver also sets the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure used in the OID request as follows. Please note that based on the VMMQ capabilities advertised by the underlying miniport adapter, some of the fields may be set to the same value for all PF VPorts.


- Set the **Revision** member of **Header** to **NDIS\_RECEIVE\_SCALE\_PARAMETERS\_REVISION\_3**.

- Set the NDIS\_RSS\_PARAM\_FLAG\_DEFAULT\_PROCESSOR\_UNCHANGED flag to specify that the **DefaultProcessorNumber** member has not changed.

- Set **BaseCpuNumber** to **zero**.

- Set **DefaultProcessorNumber** to specify the default RSS processor for this VPort. The miniport can assume that default processor is part of RSS processor list, but it cannot assume that the default RSS processor is in the current indirection table. 

- Set **HashInformation** to indicate the hash type and hash function that the NIC should use to calculate the hash value of the packets received for this VPort. The upper layer driver may set this field to a different value for each VPort.

- Set **IndirectionTableSize** to specify the size of the indirection table in bytes. Set this field to the same value for all PF VPorts. The upper layer driver must ensure that the number of entries in the indirection table is a power of two.

- Set **IndirectionTableOffset** to specify the offset of the indirection table from the beginning of the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure.

- Set **HashSecretKeySize** to specify the size of the hash secret key in bytes. The upper layer driver may set a different secret key for each VPort if the miniport adapter supports this. For more information, see [Advertising VMMQ capabilities](ADD LINK).

- Set **HashSecretKeyOffset** to specify the offset of the hash secret key from the beginning of the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure. The upper layer driver may set a different secret key for each VPort if the miniport adapter supports this. For more information, see [Advertising VMMQ capabilities](ADD LINK).

- Set **ProcessorMaskOffset**, **NumberOfProcessorMasks**, and **ProcessorMasksEntrySize** appropriately.

When a miniport driver receives an OID request to disable VMMQ for a VPort, it should revert to indicating all packets received for that VPort on the processor specified by the **ProcessorAffinity** field in the [NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure that was used in the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport) OID request.

# Changing number queues of VPorts

Process of changing the number of queues for PF VPort:

1.  When decreasing:

    1.  Send an RSS OID with the original (may be bigger) indirection table size. However, indirection table references the number of distinct processors only up to the new number of queues. If new indirection table needs to be smaller than old one (due to RESTRICTED flag), the issuer will guarantee that the indirection table at this step will contain new indirection table replicated as many times as needed to satisfy RESTRICTED requirement for the old number of queues.

    2.  Send UPDATE\_VPORT oid with new number of queues.

    3.  Send an RSS OID with new (possible smaller) indirection table size.

2.  When increasing:

    1.  Old Indirection table is already established and only references the number of distinct processors only up to the old number of queues.

    2.  Send UPDATE\_VPORT oid with new number of queues. If needed, miniport should internally replicate the original indirection table as many times as it needed too to match RESTRICTED requirement for the new (bigger) number of queues.

    3.  Send an RSS OID with new (possible bigger) indirection table size.

# Runtime Operation

On the receive path, when a packet arrives at a VMMQ supported NIC, the NIC matches the destination MAC address to find the target VPort. The NIC then uses the RSS parameters of the VPort (i.e. secret key, hash type, etc.) to calculate the RSS hash value of the packet, which is then used with the indirection table associated with the VPort to interrupt a specific processor for indicating the received packet to the host network stack. When indicating a received NBL, the miniport adapter sets the VPort ID and RSS related OOB fields to the appropriate values.

On transmit, the NIC must use the RSS hash value in the packet (if present) as an index into the RSS indirection table for the VPort in order to determine the processor that would handle the transmit-complete interrupts and DPCs for the transmitted packet.

If the NIC cannot calculate the RSS hash value of a received packet or the RSS hash value is not present in a transmit packet, it should use the default RSS processor of the VPort as the target RSS processor for the purpose of receive indication or transmit-completion. The default RSS processor for a VPort will be specified in the RSS parameters for the VPort.

The host networking stack can update the RSS parameters of a VPort dynamically at runtime. The NIC should respond to the changes in the RSS parameters of a VPort with minimal interruption in traffic to and from the VPort.

The APIs that are used for setting or querying the VMMQ parameters of a PF VPort use the existing RSS and VPort OIDs and relevant structures. The new SwitchId and VPortId fields of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) introduced in NDIS 6.50 are used to specify the VPort that is the target of the VMMQ API.

# Updating the RSS parameters of a PF VPort

At runtime, the upper layer driver can update of RSS parameters of a PF VPort by issuing an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID request. The upper layer driver may use this OID to enable VMMQ, disable VMMQ, or update the RSS indirection table of the VPort. The RSS hash type, hash function, and hash secret key of a VPort are considered static parameters and are not changed by the overlying drivers during the lifetime of a VPort. If an upper layer driver wishes to change any of the RSS static parameters, it will delete and recreate the VPort.

The number of unique processors used in the indirection table of a VPort will not exceed the value of NumQueuePairs field of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure used in the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) OID request. Furthermore, these processors will be a subset of the RSS processor set returned by a call to [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation). However, the miniport driver must not assume that the processors in the indirection tables for different VPorts are disjoint sets. In other words, the indirection tables on different VPorts could contain the same processor.

# Expected Feature Interactions

-   NVGRE/VXLAN: The NIC will calculate the hash for spreading based on the inner headers of the packets.

-   PacketDirect (PD): In this release, the NIC will only be in one mode, PD or NBL. During NBL-&gt;PD transition (when PDPI AcquireReceiveQueues() call is made for a VPort) it’s current VMMQ configuration is returned. In PD Mode, per-VPort RSS OID can be received and should be handled. Further details can be fouind in “PacketDirect note for IHVs”.

-   SR-IOV: The NIC will be able to support both VMMQ and SR-IOV simultaneously

