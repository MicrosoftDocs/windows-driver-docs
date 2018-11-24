---
title: Configuring Optional Protocol Driver Services
description: Configuring Optional Protocol Driver Services
ms.assetid: 3bb6d0ed-bc44-48c6-8f28-d861c4ff7a87
keywords:
- protocol drivers WDK networking , optional services
- NDIS protocol drivers WDK , optional services
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Optional Protocol Driver Services





NDIS calls a protocol driver's [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function to allow a protocol driver to configure optional services. NDIS calls *ProtocolSetOptions* within the context of the protocol driver's call to the [**NdisRegisterProtocolDriver**](https://msdn.microsoft.com/library/windows/hardware/ff564520) function

*ProtocolSetOptions* registers default entry points for optional *ProtocolXxx* functions and can allocate other driver resources. To register optional *ProtocolXxx* functions, the protocol driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function and passes a characteristics structure at the *OptionalHandlers* parameter. In this case, the protocol driver passes the handle from the *NdisDriverHandle* parameter of *ProtocolSetOptions* at the *NdisHandle* parameter of **NdisSetOptionalHandlers**.

A protocol driver can also call **NdisSetOptionalHandlers** from the [*ProtocolBindAdapterEx*](https://msdn.microsoft.com/library/windows/hardware/ff570220) function or the [*ProtocolOpenAdapterCompleteEx*](https://msdn.microsoft.com/library/windows/hardware/ff570265) function after the protocol driver has a valid handle from the [**NdisOpenAdapterEx**](https://msdn.microsoft.com/library/windows/hardware/ff563715) function. In this case, the protocol driver passes the handle from the *NdisBindingHandle* parameter of **NdisOpenAdapterEx** at the *NdisHandle* parameter of **NdisSetOptionalHandlers**.

In this case, the valid characteristics structures are:

[**NDIS\_PROTOCOL\_CO\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566817)

[**NDIS\_CO\_CLIENT\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564884)

[**NDIS\_CO\_CALL\_MANAGER\_OPTIONAL\_HANDLERS**](https://msdn.microsoft.com/library/windows/hardware/ff564883)

NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS (see [NDIS 6.0 TCP chimney offload documentation](full-tcp-offload.md))

 

 





