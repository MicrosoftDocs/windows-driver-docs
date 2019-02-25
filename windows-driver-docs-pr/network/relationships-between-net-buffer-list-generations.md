---
title: Relationships Between NET_BUFFER_LIST Generations
description: Relationships Between NET_BUFFER_LIST Generations
ms.assetid: 37b3b08d-4656-47bc-b656-a03f208e4311
keywords:
- NET_BUFFER_LIST
- parent/child NET_BUFFER_LIST relationships WDK networking
- child/parent NET_BUFFER_LIST relationships WDK networking
- relationships WDK NET_BUFFER_LIST
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Relationships Between NET\_BUFFER\_LIST Generations





Driver writers should understand and maintain the relationship between the parent (original) [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structures and the child (derived) structures that result from clone, fragment, and reassemble operations.

The caller of a clone/fragment/reassemble function maintains the parent/child relationship, including the parent pointer in the child NET\_BUFFER\_LIST structure and a child count. The child count ensures that the caller frees the parent after all the children have been freed. The following rules apply:

-   After a driver creates child structures from a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/library/windows/hardware/ff568388) structure, it should retain the ownership of the parent structure and should pass the child structures to other drivers. The driver should never pass the parent NET\_BUFFER\_LIST structure to another driver.

-   A driver should only update the child count in the parent NET\_BUFFER\_LIST structure. Because the parent structure is never passed to another driver, there is no risk that the value of the child count could be overwritten. The driver should set the parent pointer in the child structures to point to the parent structure.

-   When a driver receives a NET\_BUFFER\_LIST from another driver, the driver must not overwrite the parent pointer. If the received NET\_BUFFER\_LIST structure is a child, its parent pointer should be set already. The driver can use the NET\_BUFFER\_LIST received from another driver as a parent structure.

-   NDIS does not enforce the preceding rules. The current owner of a NET\_BUFFER\_LIST structure must manage the child count and parent pointer. For example, if the current owner will both clone and fragment a NET\_BUFFER\_LIST structure, it must manage the parent pointer and child counter.

-   NDIS sets the child count to zero and the parent pointer to **NULL** when it allocates a NET\_BUFFER\_LIST structure. NDIS does not change these fields each time a driver passes a NET\_BUFFER\_LIST structure to another driver.

## Related topics


[Derived NET\_BUFFER\_LIST Structures](derived-net-buffer-list-structures.md)

 

 






