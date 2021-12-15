---
title: BDA Pin Name GUIDs
description: A BDA minidriver uses BDA pin name GUIDs to specify the names and categories of pins it supports.
ms.date: 10/07/2021
---

# BDA Pin Name GUIDs

A BDA minidriver uses BDA pin name GUIDs to specify the names and categories of pins it supports. A BDA minidriver assigns these GUIDs to the **Name** and **Category** members of a [**KSPIN_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure. The *Bdamedia.h* header file defines these GUIDs. Pins of filters specify their names and categories to connect to pins of other filters that also specify those names and categories.

The following pin name GUIDs are available in BDA:

**PINNAME_BDA_TRANSPORT**  
Pin name for a BDA transport pin.

**PINNAME_BDA_ANALOG_VIDEO**  
Pin name for a BDA analog video pin.

**PINNAME_BDA_ANALOG_AUDIO**  
Pin name for a BDA analog audio pin.

**PINNAME_BDA_FM_RADIO**  
Pin name for a BDA FM radio pin.

**PINNAME_BDA_IF_PIN**  
Pin name for a BDA intermediate frequency pin.

**PINNAME_BDA_OPENCABLE_PSIP_PIN**  
Pin name for a BDA Open Cable PSIP pin.

**PINNAME_IPSINK_INPUT**  
Pin name for an input pin to a BDA IP sink node (KSNODE_BDA_IP_SINK).

**PINNAME_MPE**  
Pin name for a multiprotocol encapsulation (MPE) pin.
