---
title: BDA Node Category GUIDs
description: A BDA minidriver uses the BDA node category GUIDs to specify the types of BDA nodes that are available to create.
ms.date: 10/07/2021
ms.localizationpriority: medium
---

# BDA Node Category GUIDs

A BDA minidriver uses the BDA node category GUIDs to specify the types of BDA nodes that are available to create. A BDA minidriver assigns one of these GUIDs in the variable to which the **Type** member of a [**KSNODE_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksnode_descriptor) structure points. The *Bdamedia.h* header file defines these GUIDs.

The network provider uses the KSPROPERTY_BDA_NODE_TYPES property of the [KSPROPSETID_BdaTopology](kspropsetid-bdatopology.md) property set to retrieve a list of nodes types available from the BDA minidriver. This list of node types is an array of KSNODE_DESCRIPTOR structures.

The following node category GUIDs are available in BDA:

**KSNODE_BDA_RF_TUNER**  
A BDA minidriver assigns this GUID to specify a BDA radio frequency tuner node for cable, satellite, or terrestrial broadcast.

**KSNODE_BDA_ANALOG_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA analog-type demodulator node.

**KSNODE_BDA_QAM_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA QAM-type demodulator node for Digital Video Broadcast (DVB)-cable demodulators.

**KSNODE_BDA_QPSK_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA QPSK-type demodulator node for DVB-satellite demodulators.

**KSNODE_BDA_8VSB_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA 8VSB-type demodulator node for Advanced Television Systems Committee (ATSC)-terrestrial demodulators.

**KSNODE_BDA_COFDM_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA COFDM-type demodulator node for DVB-terrestrial demodulators.

**KSNODE_BDA_OPENCABLE_POD**  
A BDA minidriver assigns this GUID to specify a BDA open-cable POD node.

**KSNODE_BDA_COMMON_CA_POD**  
A BDA minidriver assigns this GUID to specify a BDA common conditional access POD node.

**KSNODE_BDA_PID_FILTER**  
A BDA minidriver assigns this GUID to specify a BDA packet identifier (PID) filter node.

**KSNODE_BDA_IP_SINK**  
A BDA minidriver assigns this GUID to specify a BDA IP sink node.

**KSNODE_BDA_ISDB_T_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA ISDB-type demodulator node for DVB-terrestrial demodulators.

**KSNODE_BDA_ISDB_S_DEMODULATOR**  
A BDA minidriver assigns this GUID to specify a BDA ISDB-type demodulator node for DVB-satellite demodulators.
