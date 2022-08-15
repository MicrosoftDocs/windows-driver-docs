---
title: Adaptive refresh for playing 24 fps video content
description: When Windows Display Driver Model (WDDM) 1.3 and later drivers play 24 frame per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power.
ms.date: 10/19/2018
ms.topic: article
---

# Adaptive refresh for playing 24 fps video content


When Windows Display Driver Model (WDDM) 1.3 and later drivers play 24 frame per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power. In this scenario the monitor switches from 60 Hz to a 48-Hz refresh rate to play back 24-fps video content.



## Adaptive refresh reference

These are the device driver interfaces (DDIs) that WDDM 1.3 and later drivers must implement for 24-fps playback.

These reference topics describe how to implement this capability in your drivers:

-   [**D3DDDIARG\_CHECKPRESENTDURATIONSUPPORT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddiarg_checkpresentdurationsupport) 
-   [**DXGI\_DDI\_ARG\_CHECKPRESENTDURATIONSUPPORT**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_checkpresentdurationsupport) 
-   [**DXGKARG\_SETVIDPNSOURCEADDRESS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress) (**Duration** member)
-   [**DXGKARG\_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay) (**Duration** member)
-   [**D3DDDI\_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) (**pfnCheckPresentDurationSupport** function pointer)
-   [**DXGI1\_3\_DDI\_BASE\_FUNCTIONS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) (**pfnCheckPresentDurationSupport** function pointer)

The following are functions that a Windows Display Driver Model (WDDM) 1.3 and later user-mode display driver must implement in order to support a 48-Hz adaptive refresh rate:

-   [*CheckPresentDurationSupport*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_checkpresentdurationsupport)
-   [*pfnCheckPresentDurationSupport(DXGI)*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_checkpresentdurationsupport)




 

