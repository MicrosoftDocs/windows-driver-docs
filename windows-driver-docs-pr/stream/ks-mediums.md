---
title: KS Mediums
description: KS Mediums
ms.assetid: c94c738c-66c6-491b-9157-28cccf95af4d
keywords:
- mediums WDK kernel streaming
- KSPIN_MEDIUM
- kernel streaming WDK , mediums
- KS WDK , mediums
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Mediums





A *Medium* defines a type of communication bus. The minidriver indicates which mediums a pin supports by providing a pointer to an array of [**KSPIN\_MEDIUM**](https://docs.microsoft.com/previous-versions/ff563538(v=vs.85)) structures in the relevant [**KSPIN\_DESCRIPTOR**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure. A KSPIN\_MEDIUM identifies a specific connection on a communication bus.

Clients specify the medium to use for a connection by setting the **Medium** member in the [**KSPIN\_CONNECT**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect) structure that they provide in a call to [**KsCreatePin**](https://docs.microsoft.com/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin).

Clients request a list of mediums supported by a filter or pin by using the [**KSPROPERTY\_PIN\_MEDIUMS**](https://docs.microsoft.com/windows-hardware/drivers/stream/ksproperty-pin-mediums) property.

 

 




