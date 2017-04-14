---
title: Input Buffer Order Rules
description: Input Buffer Order Rules
ms.assetid: 2c588276-88c3-42e4-9f73-50a05e31c451
keywords: ["input buffers WDK DirectX VA", "deinterlacing WDK DirectX VA , input buffer order"]
---

# Input Buffer Order Rules


## <span id="ddk_input_buffer_order_rules_gg"></span><span id="DDK_INPUT_BUFFER_ORDER_RULES_GG"></span>


**This section applies only to Windows Server 2003 with SP1 and later, and Windows XP with SP2 and later.**

The order of the surfaces within the **lpBufferInfo** array conforms to the following rules:

-   The first surface in the array is the destination surface. The driver only writes to the destination surface.

-   The next sequence of surfaces in the array is the group of any previous destination surfaces, in reverse temporal order, that the deinterlacing device requested for its deinterlace algorithm.

-   The next sequence of surfaces in the array is the collection of input interlaced or progressive surfaces that the device requires in order to perform its deinterlace operation.

-   The next sequence of surfaces in the array is the collection of video substream surfaces, which are in Z order.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Input%20Buffer%20Order%20Rules%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




