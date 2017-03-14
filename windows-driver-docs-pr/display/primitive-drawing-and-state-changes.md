---
title: Primitive Drawing and State Changes
description: Primitive Drawing and State Changes
ms.assetid: 01eba14d-234e-48f5-9116-47760dfdae0e
keywords: ["Direct3D WDK Windows 2000 display , primitive drawing", "Direct3D WDK Windows 2000 display , state changes", "states WDK Direct3D", "primitive drawing WDK Direct3D", "D3dDrawPrimitives2"]
---

# Primitive Drawing and State Changes


## <span id="ddk_primitive_drawing_and_state_changes_gg"></span><span id="DDK_PRIMITIVE_DRAWING_AND_STATE_CHANGES_GG"></span>


All Microsoft Direct3D graphics primitives and state changes are passed to the [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback in command and vertex buffers. The driver must parse these buffers and process all drawing and state change requests.

The following sections discuss the layout of command and vertex buffers and describe how the driver should process them:

[Command and Vertex Buffers](command-and-vertex-buffers.md)

[Direct3D Command Buffers](direct3d-command-buffers.md)

[Direct3D Vertex Buffers](direct3d-vertex-buffers.md)

[Accelerated State Management](accelerated-state-management.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Primitive%20Drawing%20and%20State%20Changes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




