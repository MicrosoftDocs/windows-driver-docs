---
title: Maintaining State Within a Context
description: Maintaining State Within a Context
ms.assetid: dabf6aa7-f127-419c-9245-5270768fef5b
keywords: ["context WDK Direct3D , maintaining state", "states WDK Direct3D", "internal states WDK Direct3D", "public states WDK Direct3D"]
---

# Maintaining State Within a Context


## <span id="ddk_maintaining_state_within_a_context_gg"></span><span id="DDK_MAINTAINING_STATE_WITHIN_A_CONTEXT_GG"></span>


A driver updates its internal state associated with a context when its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback is called. This callback must also return the updated context's public state to Direct3D.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Maintaining%20State%20Within%20a%20Context%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




