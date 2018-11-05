---
title: Registering intermediate driver ProtocolXxx chimney functions
description: Registering an Intermediate Driver's ProtocolXxx Chimney Functions
ms.assetid: 3fbdff0a-caf7-46bd-9893-d81ceb0e8c93
keywords:
- intermediate drivers WDK TCP chimney offload , function registration
- registering TCP chimney-specific functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering an Intermediate Driver's ProtocolXxx Chimney Functions


\[The TCP chimney offload feature is deprecated and should not be used.\]

In the context of its [*ProtocolSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff570269) function, an intermediate driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function twice:

-   Once to register generic *ProtocolXxx* chimney offload functions that apply to all chimney offload types.

-   Once to register TCP chimney-specific *ProtocolXxx* functions.

To register its generic *ProtocolXxx* chimney offload functions, an offload target initializes an [**NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff564840) structure and passes a pointer to this structure to the **NdisSetOptionalHandlers** function. The NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS structure contains entry points for the following functions:

-   [*ProtocolInitiateOffloadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570261)

-   [*ProtocolTerminateOffloadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570277)

-   [*ProtocolUpdateOffloadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570280)

-   [*ProtocolInvalidateOffloadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570262)

-   [*ProtocolQueryOffloadComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570266)

-   [*ProtocolIndicateOffloadEvent*](https://msdn.microsoft.com/library/windows/hardware/ff570260)

To register its TCP chimney-specific *ProtocolXxx* functions, an offload target initializes an [**NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff564846) structure and passes a pointer to this structure to the **NdisSetOptionalHandlers** function. The NDIS\_CLIENT\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS structure contains entry points for the following functions:

-   [*ProtocolTcpOffloadSendComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570276)

-   [*ProtocolTcpOffloadReceiveComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570274)

-   [*ProtocolTcpOffloadDisconnectComplete*](https://msdn.microsoft.com/library/windows/hardware/ff570271)

-   [**ProtocolTcpOffloadEvent**](https://msdn.microsoft.com/library/windows/hardware/ff570272)

-   [*ProtocolTcpOffloadReceiveIndicate*](https://msdn.microsoft.com/library/windows/hardware/ff570275)

 

 





