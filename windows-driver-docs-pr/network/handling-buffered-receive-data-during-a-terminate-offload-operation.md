---
title: Handling buffered receive data during terminate offload operation
description: Handling Buffered Receive Data During a Terminate Offload Operation
ms.assetid: 14746a36-0126-4924-85ad-ecca01779937
keywords:
- terminating offload state WDK TCP chimney offload , buffered receive data
- buffered receive data WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling Buffered Receive Data During a Terminate Offload Operation


\[The TCP chimney offload feature is deprecated and should not be used.\]




Outstanding receive data might exist on a TCP connection that is being uploaded. This data is data that the offload target has received off the wire, processed, and acknowledged. The offload target should use the [delivery algorithm](delivery-algorithm.md) to indicate this data to the host stack.

The offload target might include such receive data in the DELEGATED TCP state that it returns to the host stack during the terminate operation. In this situation, the offload target passes a pointer to the buffer that contains the data. This pointer is located in the **BufferedData** member of the [**TCP\_OFFLOAD\_STATE\_DELEGATED**](https://msdn.microsoft.com/library/windows/hardware/ff570939) structure for the connection. The buffer that is referenced by this pointer contains a linked list of [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures.

The host stack copies the buffered data into its own buffer and indicates the receive data to the client application. NDIS returns the NET\_BUFFER\_LIST structures to the offload target's [*MiniportTcpOffloadReceiveReturn*](https://msdn.microsoft.com/library/windows/hardware/ff559462) function.

Note that the offload target releases ownership of the NET\_BUFFER\_LIST structures that it passes up as buffered data. The offload target does not regain ownership of these NET\_BUFFER\_LIST structures until they are returned to its *MiniportTcpOffloadReceiveReturn* function.

 

 





