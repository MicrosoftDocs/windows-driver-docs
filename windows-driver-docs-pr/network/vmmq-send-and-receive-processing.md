---
title: VMMQ send and receive processing
description: VMMQ send and receive processing 
ms.date: 02/28/2021
ms.localizationpriority: medium
---


# VMMQ send and receive processing

The following figure shows the network packet receive path within the VMMQ interface.

![diagram illustrating network packet data paths with vmmq](images/vmmq-architecture.png)

For more information on the SR-IOV interface and its components see [SR-IOV Architecture](sr-iov-architecture.md).

On the receive path, when a packet arrives at a VMMQ supported NIC, the NIC matches the destination MAC address to find the target VPort. The NIC then uses the RSS parameters of the VPort (i.e. secret key, hash type, etc.) to calculate the RSS hash value of the packet, which is then used with the indirection table associated with the VPort to interrupt a specific processor for indicating the received packet to the host network stack. When indicating a received NBL, the miniport adapter sets the VPort ID and RSS related OOB fields to the appropriate values.

On transmit, the NIC must use the RSS hash value in the packet (if present) as an index into the RSS indirection table for the VPort in order to determine the processor that would handle the transmit-complete interrupts and DPCs for the transmitted packet.

If the NIC cannot calculate the RSS hash value of a received packet or the RSS hash value is not present in a transmit packet, it should use the default RSS processor of the VPort as the target RSS processor for the purpose of receive indication or transmit-completion. The default RSS processor for a VPort will be specified in the RSS parameters for the VPort.

The host networking stack can update the RSS parameters of a VPort dynamically at runtime. The NIC should respond to the changes in the RSS parameters of a VPort with minimal interruption in traffic to and from the VPort.

The APIs that are used for setting or querying the VMMQ parameters of a PF VPort use the existing RSS and VPort OIDs and relevant structures. The new SwitchId and VPortId fields of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_oid_request) introduced in NDIS 6.50 are used to specify the VPort that is the target of the VMMQ API.
