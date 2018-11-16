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





A *Medium* defines a type of communication bus. The minidriver indicates which mediums a pin supports by providing a pointer to an array of [**KSPIN\_MEDIUM**](https://msdn.microsoft.com/library/windows/hardware/ff563538) structures in the relevant [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure. A KSPIN\_MEDIUM identifies a specific connection on a communication bus.

Clients specify the medium to use for a connection by setting the **Medium** member in the [**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531) structure that they provide in a call to [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652).

Clients request a list of mediums supported by a filter or pin by using the [**KSPROPERTY\_PIN\_MEDIUMS**](https://msdn.microsoft.com/library/windows/hardware/ff565202) property.

 

 




