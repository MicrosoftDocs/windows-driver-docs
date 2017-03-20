---
title: Setting the Current Index Buffer
description: Setting the Current Index Buffer
ms.assetid: 4d190ce1-56a0-4445-9a68-6a24f3a9aee4
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , index buffers", "index buffers WDK Directx 8.0"]
---

# Setting the Current Index Buffer


## <span id="ddk_setting_the_current_index_buffer_gg"></span><span id="DDK_SETTING_THE_CURRENT_INDEX_BUFFER_GG"></span>


As with vertex data, the index buffer to be used by drawing primitives is no longer part of the data passed to the driver with the primitive, but rather is driver state. The current index buffer is set by a new DP2 token, D3DDP2OP\_SETINDICES. This token established the index buffer with the given handle as the current index buffer to use when drawing indexed primitives until a new index buffer is set or the current index buffer is cleared (an index buffer handle of zero is specified in the DP2 token data).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Setting%20the%20Current%20Index%20Buffer%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




