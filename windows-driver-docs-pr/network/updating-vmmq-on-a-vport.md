---
title: Enabling, disabling, and updating VMMQ on a VPort
description: After creating a VPort, an upper layer driver can enable, disable, or update the RSS parameters of the VPort. 
ms.date: 02/28/2021
ms.localizationpriority: medium
---



# Enabling, disabling, and updating VMMQ on a VPort

After creating a VPort, an upper layer driver can enable, disable, or update the RSS parameters of the VPort. 

The upper layer driver enables, disables, or changes the RSS parameters of a VPort by issuing an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID request. The upper layer driver sets the **VPortId** field in the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) structure to the ID of the target VPort of the new configuration. 

The upper layer driver also sets the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure used in the OID request as follows. Please note that based on the VMMQ capabilities advertised by the underlying miniport adapter, some of the fields may be set to the same value for all PF VPorts.


- Set the **Revision** member of **Header** to **NDIS\_RECEIVE\_SCALE\_PARAMETERS\_REVISION\_3**.

- Set the NDIS\_RSS\_PARAM\_FLAG\_DEFAULT\_PROCESSOR\_UNCHANGED flag to specify that the **DefaultProcessorNumber** member has not changed.

- Set **BaseCpuNumber** to **zero**.

- Set **DefaultProcessorNumber** to specify the default RSS processor for this VPort. The miniport can assume that default processor is part of RSS processor list, but it cannot assume that the default RSS processor is in the current indirection table. 

- Set **HashInformation** to indicate the hash type and hash function that the NIC should use to calculate the hash value of the packets received for this VPort. The upper layer driver may set this field to a different value for each VPort.

- Set **IndirectionTableSize** to specify the size of the indirection table in bytes. Set this field to the same value for all PF VPorts. The upper layer driver must ensure that the number of entries in the indirection table is a power of two.

- Set **IndirectionTableOffset** to specify the offset of the indirection table from the beginning of the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure.

- Set **HashSecretKeySize** to specify the size of the hash secret key in bytes. The upper layer driver may set a different secret key for each VPort if the miniport adapter supports this. For more information, see [Advertising VMMQ capabilities](advertising-vmmq-capabilities.md).

- Set **HashSecretKeyOffset** to specify the offset of the hash secret key from the beginning of the [**NDIS\_RECEIVE\_SCALE\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_receive_scale_parameters) structure. The upper layer driver may set a different secret key for each VPort if the miniport adapter supports this. For more information, see [Advertising VMMQ capabilities](advertising-vmmq-capabilities.md).

- Set **ProcessorMaskOffset**, **NumberOfProcessorMasks**, and **ProcessorMasksEntrySize** appropriately.

When a miniport driver receives an OID request to disable VMMQ for a VPort, it should revert to indicating all packets received for that VPort on the processor specified by the **ProcessorAffinity** field in the [NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure that was used in the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport) OID request.

## Changing the number queues for a VPort

An upper layer driver must follow these steps to decrease the number of queues for a PF VPort:

1. Send an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID with the original (may be bigger) indirection table size. However, indirection table references the number of distinct processors only up to the new number of queues. If new indirection table needs to be smaller than old one (due to RESTRICTED flag), the issuer will guarantee that the indirection table at this step will contain new indirection table replicated as many times as needed to satisfy RESTRICTED requirement for the old number of queues.

2. Send an [OID_NIC_SWITCH_VPORT_PARAMETERS](oid-nic-switch-vport-parameters.md) OID with new number of queues.

3. Send an RSS OID with new (possible smaller) indirection table size.

An upper layer driver must follow these steps to increase the number of queues for a PF VPort:

1. The old indirection table is already established and only references the number of distinct processors only up to the old number of queues.

2. Send an [OID_NIC_SWITCH_VPORT_PARAMETERS](oid-nic-switch-vport-parameters.md) OID with new number of queues. If needed, miniport should internally replicate the original indirection table as many times as it needed too to match RESTRICTED requirement for the new (bigger) number of queues.

3. Send an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID with new (possible bigger) indirection table size.

## Updating the RSS parameters of a PF VPort

At runtime, the upper layer driver can update of RSS parameters of a PF VPort by issuing an [OID\_GEN\_RECEIVE\_SCALE\_PARAMETERS](oid-gen-receive-scale-parameters.md) OID request. The upper layer driver may use this OID to enable VMMQ, disable VMMQ, or update the RSS indirection table of the VPort. The RSS hash type, hash function, and hash secret key of a VPort are considered static parameters and are not changed by the overlying drivers during the lifetime of a VPort. If an upper layer driver wishes to change any of the RSS static parameters, it will delete and recreate the VPort.

The number of unique processors used in the indirection table of a VPort will not exceed the value of NumQueuePairs field of the [**NDIS\_NIC\_SWITCH\_VPORT\_PARAMETERS**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_nic_switch_vport_parameters) structure used in the [OID\_NIC\_SWITCH\_CREATE\_VPORT](oid-nic-switch-create-vport.md) OID request. Furthermore, these processors will be a subset of the RSS processor set returned by a call to [**NdisGetRssProcessorInformation**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisgetrssprocessorinformation). However, the miniport driver must not assume that the processors in the indirection tables for different VPorts are disjoint sets. In other words, the indirection tables on different VPorts could contain the same processor.



