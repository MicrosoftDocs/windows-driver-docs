---
title: BDA Filter Category GUIDs
description: A BDA minidriver uses the BDA filter category GUIDs to specify the types of BDA filters to create.
ms.date: 10/07/2021
ms.localizationpriority: medium
---

# BDA Filter Category GUIDs

A BDA minidriver uses the BDA filter category GUIDs to specify the types of BDA filters to create. A BDA minidriver assigns these GUIDs in the array to which the **Categories** member of a [**KSFILTER_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-_ksfilter_descriptor) structure points. The *Bdamedia.h* header file defines these GUIDs.

The following filter category GUIDs are available in BDA:

**KSCATEGORY_BDA_RECEIVER_COMPONENT**  
A BDA minidriver assigns this GUID to specify to create a BDA receiver filter.

**KSCATEGORY_BDA_NETWORK_TUNER**  
A BDA minidriver assigns this GUID to specify to create a BDA network tuner filter.

**KSCATEGORY_BDA_NETWORK_EPG**  
A BDA minidriver assigns this GUID to specify to create a BDA electronic program guide (EPG) filter.

**KSCATEGORY_BDA_IP_SINK**  
A BDA minidriver assigns this GUID to specify to create a BDA IP sink filter.

KSCATEGORY_BDA_NETWORK_PROVIDER  
A BDA minidriver assigns this GUID to specify to create a BDA network provider filter.

**KSCATEGORY_BDA_TRANSPORT_INFORMATION**  
A BDA minidriver assigns this GUID to specify to create a BDA transport information filter (TIF).
