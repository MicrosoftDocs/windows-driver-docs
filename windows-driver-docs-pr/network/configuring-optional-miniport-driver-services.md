---
title: Configuring Optional Miniport Driver Services
description: Configuring Optional Miniport Driver Services
ms.assetid: 42fe3863-ded0-4a02-9216-86fa4c167a49
keywords:
- miniport drivers WDK networking , optional services
- NDIS miniport drivers WDK , optional services
- MiniportSetOptions
- characteristics structure WDK networking
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Optional Miniport Driver Services





NDIS calls a miniport driver's [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function to allow the driver to configure optional services. NDIS calls *MiniportSetOptions* within the context of the miniport driver's call to the [**NdisMRegisterMiniportDriver**](https://msdn.microsoft.com/library/windows/hardware/ff563654) function.

*MiniportSetOptions* registers the default entry points for optional *MiniportXxx* functions and can allocate other driver resources. To register optional *MiniportXxx* functions, the miniport driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function and passes a characteristics structure at the *OptionalHandlers* parameter.

Starting with NDIS 6.0, the valid characteristics structures include the following:

[**NDIS\_MINIPORT\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff565948)

[**NDIS\_MINIPORT\_PNP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566475)

[**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883)

[**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566846) (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

[**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566852) (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

Starting with NDIS 6.30, the valid characteristics structures also include the following:

[**NDIS\_MINIPORT\_SS\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/hh451559)

[**NDIS\_NDK\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/hh451566)

 

 





