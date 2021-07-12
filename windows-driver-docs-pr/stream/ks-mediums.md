---
title: KS Mediums
description: KS Mediums
keywords:
- mediums WDK kernel streaming
- KSPIN_MEDIUM
- kernel streaming WDK , mediums
- KS WDK , mediums
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Mediums





A *Medium* defines a type of communication bus. The minidriver indicates which mediums a pin supports by providing a pointer to an array of [**KSPIN\_MEDIUM**](/windows-hardware/drivers/stream/kspin-medium-structure) structures in the relevant [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure. A KSPIN\_MEDIUM identifies a specific connection on a communication bus.

Clients specify the medium to use for a connection by setting the **Medium** member in the [**KSPIN\_CONNECT**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect) structure that they provide in a call to [**KsCreatePin**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin).

Clients request a list of mediums supported by a filter or pin by using the [**KSPROPERTY\_PIN\_MEDIUMS**](./ksproperty-pin-mediums.md) property.

 

