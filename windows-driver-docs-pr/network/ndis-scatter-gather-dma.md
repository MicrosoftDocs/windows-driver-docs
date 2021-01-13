---
title: NDIS Scatter/Gather DMA
description: NDIS Scatter/Gather DMA
keywords:
- miniport drivers WDK networking , scatter/gather DMA
- NDIS miniport drivers WDK , scatter/gather DMA
- scatter/gather DMA WDK networking
- SGDMA WDK networking
- NICs WDK networking , system memory transfers
- network interface cards WDK networking , s
ms.date: 06/11/2018
ms.localizationpriority: medium
---

# NDIS Scatter/Gather DMA

[!include[NDIS DMA ARM note](../includes/ndis-dma-arm-note.md)]

NDIS miniport drivers can use the Scatter/Gather DMA (SGDMA) method to transfer data between a NIC and system memory. A successful DMA transfer requires the physical address of the data to be in an address range that the NIC supports. HAL provides a mechanism for drivers to obtain the physical address list for an MDL chain and, if necessary, will double-buffer the data to a physical address range.

In NDIS versions prior to NDIS 6.0, SGDMA support in miniport drivers and NDIS is limited in some respects, and in particular does not work well in a multipacket send scenario. The NDIS 6.0 SGDMA support overcomes these limitations while providing a simple interface for miniport drivers.

## History of NDIS SGDMA

In NDIS versions prior to NDIS 6.0, NDIS obtains a scatter gather (SG) list for each packet before sending the packet to the miniport driver. NDIS also handles the case where the original attempt to get the SG list fails due to excessive fragmentation. In this case, NDIS double-buffers the packet to a contiguous buffer and tries again. HAL can also double-buffer the data to a physical address that the NIC supports if, for example, the physical address of the data is above the 32-bit maximum and the NIC does not support 64-bit DMA.

To avoid a deadlock situation, NDIS obtains a SG list for a packet, and sends one packet at a time. If NDIS attempts to map all the packets before sending them to the miniport driver, the system could run out resources. In this case, NDIS would be waiting for map registers to become available while some map registers are locked down for the packets that have not been sent. Locked down packets cannot be reused.

This approach to SGDMA support has the following limitations:

-   Because the packet is mapped before it gets to the miniport driver, the driver cannot optimize for small packets or packets that are too fragmented. The miniport driver cannot double buffer the packet to a known physical address.

-   There is no guarantee that the physical address array that NDIS passed to the miniport driver maps to the virtual address of the original data. Therefore, if the driver changes the data at the virtual address in the MDL chain before sending it, the modifications made to the data are not reflected in the data in the physical addresses. In this case, the NIC sends the unmodified data.

-   NDIS is limited to sending one packet at a time to avoid a deadlock due to resource issues. This is not as efficient as sending multiple packets.

-   Because NDIS cannot determine the transmit capabilities of miniport drivers, it cannot preallocate the storage for an SG list buffer. Therefore, NDIS must allocate the necessary storage at run time. This is not as efficient as preallocating the storage.

-   HAL functions that allocate an SG list should be called at IRQL = DISPATCH\_LEVEL. NDIS does not have the current IRQL information, so it has to set the IRQL to DISPATCH\_LEVEL even if it is already at DISPATCH\_LEVEL. This is not efficient if the IRQL is already at DISPATCH\_LEVEL.

## Benefits of NDIS SGDMA Support

In the NDIS 6.0 and later SGDMA interface, NDIS does not map the data buffer before sending it down to the miniport driver. Instead, NDIS provides an interface for the driver to map the network data.

This approach yields the following benefits:

-   Since NDIS provides the interface to HAL for mapping the network data, NDIS shields miniport drivers from the complexity and details of the mapping process.

-   Miniport drivers have access to the data before it is mapped. Therefore, any changes made to the original data are reflected in the data represented by the SG list even if NDIS or HAL double-buffers the data.

-   Miniport drivers can optimize the transmission of small or highly fragmented packets by copying them to a preallocated buffer with a known physical address. This approach avoids mapping that is not required and therefore improves system performance.

-   NDIS can send multiple buffers to the miniport driver safely. This results in fewer calls to miniport drivers and therefore improves system performance.

-   Miniport drivers can preallocate the memory for an SG list as part of the transmit descriptor blocks. Therefore, NDIS or miniport drivers are not required to allocate memory for SG lists at run time.

-   Because miniport drivers can be running at IRQL = DISPATCH\_LEVEL, miniport drivers can avoid unnecessary calls to raise the IRQL to DISPATCH\_LEVEL. For example, because completing a send happens in the context of an interrupt DPC, miniport drivers can free the SG list without raising the IRQL.


## Registering and Deregistering DMA Channels

An NDIS miniport driver calls the [**NdisMRegisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterscattergatherdma) function from its [*MiniportInitializeEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_initialize) function to register a DMA channel with NDIS.

The miniport driver passes a DMA description to [**NdisMRegisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterscattergatherdma) in the *DmaDescription* parameter. **NdisMRegisterScatterGatherDma** returns a size for the buffer that should be large enough to hold the scatter/gather list. Miniport drivers should use this size to preallocate the storage for scatter/gather lists.

The miniport driver also passes [**NdisMRegisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismregisterscattergatherdma) the entry points for the *MiniportXxx* functions that NDIS calls to process the scatter/gather list. NDIS calls the miniport driver's [*MiniportProcessSGList*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_process_sg_list) function after HAL has built the scatter/gather list for a buffer. **NdisMRegisterScatterGatherDma** supplies a handle in the *pNdisMiniportDmaHandle* parameter, which the miniport driver must use in subsequent calls to NDIS scatter/gather DMA functions.

An NDIS miniport driver calls the [**NdisMDeregisterScatterGatherDma**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismderegisterscattergatherdma) function from its [*MiniportHaltEx*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_halt) function to release scatter/gather DMA resources.

## Allocating and Freeing Scatter/Gather Lists

An NDIS miniport driver calls the [**NdisMAllocateNetBufferSGList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismallocatenetbuffersglist) function in its [*MiniportSendNetBufferLists*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_send_net_buffer_lists) function. The miniport driver calls **NdisMAllocateNetBufferSGList** once for each [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure that it must map. After the resources become available and HAL has the SG list ready, NDIS calls the driver's [*MiniportProcessSGList*](/windows-hardware/drivers/ddi/ndis/nc-ndis-miniport_process_sg_list) function. NDIS can call *MiniportProcessSGList* before or after the miniport driver's call to **NdisMAllocateNetBufferSGList** returns.

To improve system performance, the scatter/gather list is generated from the network data starting at the beginning of the MDL that is specified at the **CurrentMdl** member of the associated [**NET\_BUFFER\_DATA**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer_data) structure. The start of the network data in the SG list is offset from the beginning of the SG list by the value specified in the **CurrentMdlOffset** member of the associated **NET\_BUFFER\_DATA** structure.

While handling a DPC for a send-complete interrupt, and after the miniport driver does not need the SG list any more, the miniport driver should call the [**NdisMFreeNetBufferSGList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreenetbuffersglist) function to free the SG list.

**Note**  Do not call [**NdisMFreeNetBufferSGList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreenetbuffersglist) while the driver or hardware is still accessing the memory that is described by the [**NET\_BUFFER**](/windows-hardware/drivers/ddi/nbl/ns-nbl-net_buffer) structure that is associated with the scatter/gather list. 

Before accessing received data, miniport drivers must call [**NdisMFreeNetBufferSGList**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismfreenetbuffersglist) to flush the memory cache.
