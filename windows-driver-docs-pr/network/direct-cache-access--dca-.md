---
title: Direct Cache Access (DCA)
description: Direct Cache Access (DCA)
ms.assetid: d2f46f5f-e9be-4ed8-9107-39cf178ead6a
keywords:
- direct cache access WDK NetDMA
- DCA WDK NetDMA
- memory-to-memory data transfers WDK NetDMA , direct cache access
- data transfers WDK NetDMA , direct cache access
- transferring data WDK NetDMA , direct cache access
- DMA transfers WDK NetDMA , direct cache access
- NetDMA WDK networking , direct cache access
- CPU affinities WDK NetDMA
- NetDMA 2.0 WDK networking , direct cache access
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct Cache Access (DCA)


**Note**  The NetDMA interface is not supported in Windows 8 and later.

 




*Direct cache access (DCA)* provides a mechanism for NetDMA clients to indicate that destination data is targeted for a CPU cache. DCA support is not present for NetDMA providers before version 2.0 and it is optional for NetDMA 2.0 and later providers. A NetDMA provider that supports DCA sets the NET\_DMA\_PROVIDER\_CHARACTERISTICS\_DCA\_SUPPORTED bit in the **Flags** member of the [**NET\_DMA\_PROVIDER\_CHARACTERISTICS**](https://msdn.microsoft.com/library/windows/hardware/ff568738) structure at the *ProviderCharacteristics* parameter of the [**NetDmaRegisterProvider**](https://msdn.microsoft.com/library/windows/hardware/ff568336) function.

During NetDMA channel allocation, a NetDMA provider that supports DCA sets the CPU affinity of the Status Completion Write register (that is, the memory location that is specified in the **CompletionVirtualAddress** and **CompletionPhysicalAddress** members in the [**NET\_DMA\_CHANNEL\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff568732) structure) to the target processor that it specifies in the **CpuNumber** member of NET\_DMA\_CHANNEL\_PARAMETERS structure. When the DMA engine completes a DMA transfer, if the NetDMA interface requests a status update (by setting the NET\_DMA\_STATUS\_UPDATE\_ON\_COMPLETION bit), the DMA engine sends a DCA hint to the target processor that is associated with the NetDMA channel.

If a NetDMA provider supports DCA, the NetDMA interface sets the processor affinity of the destination data of DMA transfers on a particular channel by submitting a "Context Change" descriptor to the NetDMA provider on that channel right after allocating the channel and in other cases where the hardware context might have been lost.

A DCA-capable NetDMA engine provides an interface to control sending the DCA hint on a per-transfer basis. A DCA-capable NetDMA provider checks the NET\_DMA\_DESTINATION\_DCA\_ENABLE bit in the **ControlFlags** member of each submitted [**NET\_DMA\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff568734) structure to determine if it should send a DCA hint for the destination address to the target processor. Drivers that are not DCA-capable should ignore the NET\_DMA\_DESTINATION\_DCA\_ENABLE bit.

When the NET\_DMA\_OP\_TYPE\_CONTEXT\_CHANGE bit in the **ControlFlags** member is set, the DMA engine should identify the descriptor as a "Context Change" descriptor. The NetDMA interface submits a "Context Change" descriptor to a DCA-capable NetDMA provider to set the DCA target processor of the destination data for all the DMA transfers on a NetDMA channel. The NetDMA interface uses the **DCAContext8** member in a "Context Change" descriptor to specify the 8-bit advanced programmable interrupt controller (APIC) identifier of the target processor for the channel. A DCA-capable NetDMA provider must keep the DCA affinity of a DMA channel with a processor as long as it has not received a new "Context Change" descriptor. The NetDMA interface submits a "Context Change" descriptor one time after the channel is allocated and again when it detects that the DMA provider might have lost the hardware context (for example, after a suspend and resume operation).

 

 





