---
title: Porting Miniport Driver DMA Operations to NDIS 6.0
description: Porting Miniport Driver DMA Operations to NDIS 6.0
ms.assetid: cc0e5e1d-9e7a-4725-9db7-beb9fa1c1895
keywords:
- SGDMA WDK networking , porting DMA operations
- DMA operations WDK networking , porting DMA operations
- scatter/gather DMA WDK networking , porting DMA operations
- porting miniport drivers WDK networking , DMA operations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Porting Miniport Driver DMA Operations to NDIS 6.0





When compared with NDIS 5.*x*, NDIS 6.0 provides a much different interface for handling DMA. For information about the benefits of the NDIS 6.0 approach, see [NDIS 6.0 SGDMA Support](benefits-of-ndis-sgdma-support.md).

NDIS 6.0 provides services to register for DMA support. It also provides a runtime interface that a miniport driver uses when it handles send requests.

To register for NDIS 6.0 scatter gather DMA (SGDMA) support, initialize an NDIS\_SG\_DMA\_DESCRIPTION structure and then pass this structure to the [**NdisMRegisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563659) function. **NdisMRegisterScatterGatherDma** returns a handle and the miniport driver subsequently passes the handle to NDIS SGDMA runtime functions.

To release SGDMA resources that it allocated, a miniport driver calls the [**NdisMDeregisterScatterGatherDma**](https://msdn.microsoft.com/library/windows/hardware/ff563581) function and passes it the handle returned by **NdisMRegisterScatterGatherDma**. The driver should call **NdisMDeregisterScatterGatherDma** in the context of its [*MiniportHaltEx*](https://msdn.microsoft.com/library/windows/hardware/ff559388) function.

NDIS 6.0 scatter gather lists are associated with [**NET\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff568376) structures.

For miniport drivers that call the [**NdisMAllocateSharedMemoryAsyncEx**](https://msdn.microsoft.com/library/windows/hardware/ff562784) function (formerly [**NdisMAllocateSharedMemoryAsync**](https://msdn.microsoft.com/library/windows/hardware/ff552304)), define the [*MiniportSharedMemoryAllocateComplete*](https://msdn.microsoft.com/library/windows/hardware/ff559446) function (formerly [**MiniportAllocateComplete**](https://msdn.microsoft.com/library/windows/hardware/ff549352)). The entry point for *MiniportSharedMemoryAllocateComplete* is in the NDIS\_SG\_DMA\_DESCRIPTION structure.

**Note**  In NDIS 6.0, you must call the [**NdisMRegisterDmaChannel**](https://msdn.microsoft.com/library/windows/hardware/ff563646) function before calling [**NdisMAllocateSharedMemoryAsyncEx**](https://msdn.microsoft.com/library/windows/hardware/ff562784).

 

While processing send requests, a miniport driver can call the [**NdisMAllocateNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff562776) function to obtain a scatter gather DMA list (SGL) for a NET\_BUFFER structure.

When a miniport driver calls **NdisMAllocateNetBufferSGList**, NDIS calls the HAL to build the SGL. After the HAL builds the SGL, NDIS calls the [*MiniportProcessSGList*](https://msdn.microsoft.com/library/windows/hardware/ff559420) function. When NDIS calls *MiniportProcessSGList*, the driver can send the NET\_BUFFER structure to the hardware.

Miniport drivers must call the [**NdisMFreeNetBufferSGList**](https://msdn.microsoft.com/library/windows/hardware/ff563586) function to free an SGL.

For more information about scatter gather DMA, see [Scatter/Gather DMA](https://msdn.microsoft.com/library/windows/hardware/ff570739). For more information about porting send request handling, see [Porting NDIS Miniport Driver Send Data Handling](porting-ndis-miniport-driver-send-data-handling.md).

 

 





