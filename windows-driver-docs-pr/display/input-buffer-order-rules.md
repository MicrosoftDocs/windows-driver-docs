---
title: Input Buffer Order Rules
description: Input Buffer Order Rules
ms.assetid: 2c588276-88c3-42e4-9f73-50a05e31c451
keywords:
- input buffers WDK DirectX VA
- deinterlacing WDK DirectX VA , input buffer order
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Buffer Order Rules


## <span id="ddk_input_buffer_order_rules_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_RULES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The order of the surfaces within the **lpBufferInfo** array conforms to the following rules:

-   The first surface in the array is the destination surface. The driver only writes to the destination surface.

-   The next sequence of surfaces in the array is the group of any previous destination surfaces, in reverse temporal order, that the deinterlacing device requested for its deinterlace algorithm.

-   The next sequence of surfaces in the array is the collection of input interlaced or progressive surfaces that the device requires in order to perform its deinterlace operation.

-   The next sequence of surfaces in the array is the collection of video substream surfaces, which are in Z order.

 

 





