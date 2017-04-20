---
title: Processing Shader Codes
description: Processing Shader Codes
ms.assetid: c858766c-b414-4971-b4d9-23ec94aca8ea
keywords:
- user-mode display drivers WDK Windows Vista , shader codes
- shader codes WDK display
- pixel shader codes WDK display
- vertex shader codes WDK display
- vertex declarations WDK display
- tokens WDK display
- end tokens WDK display
- declarations WDK display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Processing Shader Codes


The user-mode display driver uses vertex declarations, and the tokens within each individual pixel and vertex shader code, to program shader assemblers.

The user-mode display driver receives vertex and pixel shader code when the Microsoft Direct3D runtime calls the driver's [**CreateVertexShaderFunc**](https://msdn.microsoft.com/library/windows/hardware/ff540717) and [**CreatePixelShader**](https://msdn.microsoft.com/library/windows/hardware/ff540668) functions, respectively. The user-mode display driver receives vertex declarations when the runtime calls the driver's [**CreateVertexShaderDecl**](https://msdn.microsoft.com/library/windows/hardware/ff540714) function. The vertex declarations consist of arrays of [**D3DDDIVERTEXELEMENT**](https://msdn.microsoft.com/library/windows/hardware/ff544344) structures. The user-mode display driver converts shader code and vertex shader declarations into a hardware-specific format and associates the shader code and declarations with shader and declaration handles. The runtime uses the created handles in calls to the [**SetVertexShaderDecl**](https://msdn.microsoft.com/library/windows/hardware/ff569692), [**SetVertexShaderFunc**](https://msdn.microsoft.com/library/windows/hardware/ff569693), and [**SetPixelShader**](https://msdn.microsoft.com/library/windows/hardware/ff569543) functions to set the vertex shader declaration and the vertex and pixel shaders so that all subsequent drawing operations use them.

For more information about the format of an individual shader code and the tokens that comprise each shader code, see [Direct3D Shader Codes](https://msdn.microsoft.com/library/windows/hardware/ff552891).

**Note**   When an application creates vertex shaders, pixel shaders, and vertex declarations, the shader code and declaration for each ends with an [end token](https://msdn.microsoft.com/library/windows/hardware/ff564170). When the Direct3D runtime, in turn, passes vertex and pixel shader creation requests to the user-mode display driver, the vertex and pixel shader code that accompanies the requests ends with end tokens. However, when the runtime passes vertex declaration creation requests, the vertex declarations that accompany the requests do not end with end tokens.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Processing%20Shader%20Codes%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




