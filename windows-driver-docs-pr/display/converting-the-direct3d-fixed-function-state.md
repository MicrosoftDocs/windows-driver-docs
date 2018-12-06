---
title: Converting the Direct3D Fixed-Function State
description: Converting the Direct3D Fixed-Function State
ms.assetid: bc93d65e-ac16-470d-8c52-db8b1cc74456
keywords:
- user-mode display drivers WDK Windows Vista , convert Direct3D fixed-function state
- fixed-function state conversions WDK display
- converting Direct3D fixed-function state
- converters WDK Windows Vista Direct3D
- pixel shader converters WDK display
- vertex shader converters WDK display
- shader converters WDK display
- texture stage states WDK display
- render states WDK display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Converting the Direct3D Fixed-Function State


The Microsoft Direct3D runtime converts Direct3D fixed-function state to vertex or pixel shader version 2.0 if the user-mode display driver supports version 2.0 or later for each shader type. However, the runtime does not convert shader versions. For example, if an application uses vertex or pixel shader version 1.1, then version 1.1 is passed unconverted to the user-mode display driver regardless of whether the driver supports shader version 2.0 or later. Flexible vertex format (FVF) codes are used with fixed-function processing.

### <span id="converter_features_for_directx_versions"></span><span id="CONVERTER_FEATURES_FOR_DIRECTX_VERSIONS"></span>Converter Features for DirectX Versions

How the fixed-function vertex and pixel shader converters work depend on the version of Microsoft DirectX used:

-   DirectX 9.0

    Fixed-function vertex and pixel shader converters can work with the Windows Vista display driver model.

    The converters are enabled by default.

    When the fixed-function vertex or pixel shader converter is used, the pure device is disabled. When an application requests the pure device, the Direct3D runtime creates a HAL device.

    The runtime supports mixed vertex processing.

    Software vertex processing always uses the fixed-function vertex shader converter.

    Hardware vertex processing uses the fixed-function vertex shader converter when the driver supports vertex shader version 2.0 or later.

    Hardware vertex processing uses the fixed-function pixel shader converter when the driver supports pixel shader version 2.0 or later.

    In the mixed vertex processing mode when the fixed-function vertex shader converter is enabled for hardware, the number of float constants is set to what the hardware can support.

-   DirectX 8.0 and earlier

    Fixed-function vertex and pixel shader converters can work with the Windows Vista display driver model only.

    The converters are enabled by default.

    The fixed-function vertex shader converter is not supported with software vertex processing.

    Hardware vertex processing uses the fixed-function vertex shader converter when the driver supports vertex shader version 2.0 or later.

    Hardware vertex processing uses the fixed-function pixel shader converter when the driver supports pixel shader version 2.0 or later.

    **Note**   For versions of DirectX prior to DirectX 8.0, the fixed function to shader mapping code is implemented in *Ddraw.dll*.

     

### <span id="unused_user_mode_display_driver_functions"></span><span id="UNUSED_USER_MODE_DISPLAY_DRIVER_FUNCTIONS"></span>Unused User-Mode Display Driver Functions

The following [user-mode display driver functions](https://msdn.microsoft.com/library/windows/hardware/ff570118) are not called by the Direct3D runtime when the fixed-function vertex shader converter is enabled:

-   [**MultiplyTransform**](https://msdn.microsoft.com/library/windows/hardware/ff568516)

-   [**SetTransform**](https://msdn.microsoft.com/library/windows/hardware/ff569687)

-   [**SetMaterial**](https://msdn.microsoft.com/library/windows/hardware/ff569540)

-   [**SetLight**](https://msdn.microsoft.com/library/windows/hardware/ff569539)

-   [**CreateLight**](https://msdn.microsoft.com/library/windows/hardware/ff540658)

-   [**DestroyLight**](https://msdn.microsoft.com/library/windows/hardware/ff552778)

### <span id="unused_render_states"></span><span id="UNUSED_RENDER_STATES"></span>Unused Render States

The following render states are not passed by the Direct3D runtime (or, if passed by mistake, can be ignored by the driver) when the fixed-function vertex shader converter is enabled:

-   D3DRS\_VERTEXBLEND

-   D3DRS\_INDEXEDVERTEXBLENDENABLE

-   D3DRS\_TWEENFACTOR

-   D3DRS\_FOGVERTEXMODE

-   D3DRS\_LIGHTING

-   D3DRS\_AMBIENT

-   D3DRS\_COLORVERTEX

-   D3DRS\_LOCALVIEWER

-   D3DRS\_DIFFUSEMATERIALSOURCE

-   D3DRS\_SPECULARMATERIALSOURCE

-   D3DRS\_AMBIENTMATERIALSOURCE

-   D3DRS\_EMISSIVEMATERIALSOURCE

-   D3DRS\_POINTSCALEENABLE

-   D3DRS\_POINTSCALE\_A

-   D3DRS\_POINTSCALE\_B

-   D3DRS\_POINTSCALE\_C

-   D3DRS\_NORMALIZENORMALS

### <span id="ignored_texture_stage_states"></span><span id="IGNORED_TEXTURE_STAGE_STATES"></span>Ignored Texture Stage States

The Direct3D runtime passes all texture stage states to the driver. The driver should ignore the following texture stage states when the fixed-function pixel shader converter is enabled:

-   D3DTSS\_COLOROP

-   D3DTSS\_COLORARG1

-   D3DTSS\_COLORARG2

-   D3DTSS\_ALPHAOP

-   D3DTSS\_ALPHAARG1

-   D3DTSS\_ALPHAARG2

-   D3DTSS\_BUMPENVMAT00

-   D3DTSS\_BUMPENVMAT01

-   D3DTSS\_BUMPENVMAT10

-   D3DTSS\_BUMPENVMAT11

-   D3DTSS\_BUMPENVLSCALE

-   D3DTSS\_BUMPENVLOFFSET

-   D3DTSS\_COLORARG0

-   D3DTSS\_ALPHAARG0

-   D3DTSS\_RESULTARG

-   D3DTSS\_CONSTANT

 

 





