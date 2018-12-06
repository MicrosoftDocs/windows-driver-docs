---
title: Porting CoNDIS Miniport Driver Registration
description: Porting CoNDIS Miniport Driver Registration
ms.assetid: dcbde406-6498-4bb0-a80e-f2d0f0962051
keywords:
- registering CoNDIS drivers
- entry points WDK networking
- registration porting WDK CoNDIS
- porting CoNDIS drivers WDK networking , registration
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting CoNDIS Miniport Driver Registration





In NDIS 5.*x*, miniport drivers specify CoNDIS *MiniportXxx* functions when they call the [**NdisMRegisterMiniport**](https://msdn.microsoft.com/library/windows/hardware/ff553602) function during driver registration.

In NDIS 6.0, miniport drivers register CoNDIS *MiniportXxx* functions by calling the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function from the [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function. In *MiniportSetOptions*, a miniport driver initializes an [**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948) structure and passes it at the *OptionalHandlers* parameter of **NdisSetOptionalHandlers**.

For more information about CoNDIS miniport driver registration, see [CoNDIS Miniport Driver Registration](condis-miniport-driver-registration.md).

 

 





