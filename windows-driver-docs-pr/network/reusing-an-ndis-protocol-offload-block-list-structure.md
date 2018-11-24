---
title: Reusing an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST Structure
description: Reusing an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST Structure
ms.assetid: da8c1d8e-87cc-46b0-a322-759abb162808
keywords:
- propagating TCP chimney state-manipulation operations, block list types
- state-manipulation operations WDK TCP chimney offload , block list types
- block list types WDK TCP chimney offload
- NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reusing an NDIS\_PROTOCOL\_OFFLOAD\_BLOCK\_LIST Structure


\[The TCP chimney offload feature is deprecated and should not be used.\]

When [propagating the completion of a state-manipulation operation](propagating-the-completion-of-a-state-manipulation-operation.md), an intermediate driver overlays most of the members of an incoming [**NDIS\_PROTOCOL\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566833) structure onto an [**NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff566469) structure. (For a comparison of these structures, see [Comparison of Offload Block List Types](comparison-of-offload-block-list-types.md).)

The intermediate driver uses the pointer in the **ImReserved** member of the incoming NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure to locate its IM call entry for the state-manipulation operation. The intermediate driver supplied this pointer when constructing the NDIS\_PROTOCOL\_OFFLOAD\_BLOCK\_LIST structure that it passed to the **Ndis*Xxx*Offload** function when propagating the state-manipulation operation.

The intermediate driver copies the **ImReserved** and **SourceHandle** members that it stored in its IM call entry to the **ImReserved** and **SourceHandle** members of the NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure.

When calling the **NdisM*Xxx*Complete** function, the intermediate driver passes a pointer to the newly constructed NDIS\_MINIPORT\_OFFLOAD\_BLOCK\_LIST structure.

 

 





