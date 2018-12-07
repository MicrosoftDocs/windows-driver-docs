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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing Shader Codes


The user-mode display driver uses vertex declarations, and the tokens within each individual pixel and vertex shader code, to program shader assemblers.

The user-mode display driver receives vertex and pixel shader code when the Microsoft Direct3D runtime calls the driver's [**CreateVertexShaderFunc**](https://msdn.microsoft.com/library/windows/hardware/ff540717) and [**CreatePixelShader**](https://msdn.microsoft.com/library/windows/hardware/ff540668) functions, respectively. The user-mode display driver receives vertex declarations when the runtime calls the driver's [**CreateVertexShaderDecl**](https://msdn.microsoft.com/library/windows/hardware/ff540714) function. The vertex declarations consist of arrays of [**D3DDDIVERTEXELEMENT**](https://msdn.microsoft.com/library/windows/hardware/ff544344) structures. The user-mode display driver converts shader code and vertex shader declarations into a hardware-specific format and associates the shader code and declarations with shader and declaration handles. The runtime uses the created handles in calls to the [**SetVertexShaderDecl**](https://msdn.microsoft.com/library/windows/hardware/ff569692), [**SetVertexShaderFunc**](https://msdn.microsoft.com/library/windows/hardware/ff569693), and [**SetPixelShader**](https://msdn.microsoft.com/library/windows/hardware/ff569543) functions to set the vertex shader declaration and the vertex and pixel shaders so that all subsequent drawing operations use them.

For more information about the format of an individual shader code and the tokens that comprise each shader code, see [Direct3D Shader Codes](https://msdn.microsoft.com/library/windows/hardware/ff552891).

**Note**   When an application creates vertex shaders, pixel shaders, and vertex declarations, the shader code and declaration for each ends with an [end token](https://msdn.microsoft.com/library/windows/hardware/ff564170). When the Direct3D runtime, in turn, passes vertex and pixel shader creation requests to the user-mode display driver, the vertex and pixel shader code that accompanies the requests ends with end tokens. However, when the runtime passes vertex declaration creation requests, the vertex declarations that accompany the requests do not end with end tokens.

 

 

 





