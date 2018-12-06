---
title: Registering Chimney Offload Functions
description: Registering Chimney Offload Functions
ms.assetid: 8169dc67-3ab1-4aeb-a513-7af4b01772c3
keywords:
- TCP chimney offload WDK networking , function registration
- chimney offload WDK networking , function registration
- registering chimney offload functions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Registering Chimney Offload Functions


\[The TCP chimney offload feature is deprecated and should not be used.\]

In the context of its [*MiniportSetOptions*](https://msdn.microsoft.com/library/windows/hardware/ff559443) function, an intermediate driver calls the [**NdisSetOptionalHandlers**](https://msdn.microsoft.com/library/windows/hardware/ff564550) function twice:

-   Once to register generic *MiniportXxx* chimney offload functions that apply to all chimney offload types.

-   Once to register TCP chimney-specific *MiniportXxx* functions.

To register its generic chimney offload functions, an offload target initializes an [**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566846) structure and passes a pointer to this structure to the **NdisSetOptionalHandlers** function. The NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_GENERIC\_CHARACTERISTICS structure contains entry points for the following functions:

-   [*MiniportInitiateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559393)

-   [*MiniportTerminateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559468)

-   [*MiniportUpdateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff560463)

-   [*MiniportInvalidateOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559406)

-   [*MiniportQueryOffload*](https://msdn.microsoft.com/library/windows/hardware/ff559423)

To register its TCP chimney-specific handlers, an offload target initializes an [**NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff566852) structure and passes a pointer to this structure to the **NdisSetOptionalHandlers** function. The NDIS\_PROVIDER\_CHIMNEY\_OFFLOAD\_TCP\_CHARACTERISTICS structure contains entry points for the following functions:

-   [*MiniportTcpOffloadSend*](https://msdn.microsoft.com/library/windows/hardware/ff559464)

-   [*MiniportTcpOffloadReceive*](https://msdn.microsoft.com/library/windows/hardware/ff559460)

-   [*MiniportTcpOffloadDisconnect*](https://msdn.microsoft.com/library/windows/hardware/ff559457)

-   [*MiniportTcpOffloadForward*](https://msdn.microsoft.com/library/windows/hardware/ff559458)

-   [*MiniportTcpOffloadReceiveReturn*](https://msdn.microsoft.com/library/windows/hardware/ff559462)

 

 





