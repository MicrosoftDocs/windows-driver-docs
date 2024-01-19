---
title: Adaptive Refresh for Playing 24 fps Video Content
description: When Windows Display Driver Model (WDDM) 1.3 and later drivers play 24 frame per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power.
ms.date: 01/12/2024
ms.topic: article
---

# Adaptive refresh for playing 24-fps video content

When WDDM 1.3 and later drivers play 24 frames per second (fps) video content on 60-Hz monitors, they must implement 48-Hz adaptive refresh to conserve power. In this scenario, the monitor switches from 60 Hz to a 48-Hz refresh rate to play back 24-fps video content.

## Adaptive refresh reference

WDDM 1.3 and later drivers must implement the following DDIs for 24-fps playback:

* [**D3DDDIARG_CHECKPRESENTDURATIONSUPPORT**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-d3dddiarg_checkpresentdurationsupport)
* [**DXGI_DDI_ARG_CHECKPRESENTDURATIONSUPPORT**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_checkpresentdurationsupport)
* [**DXGKARG_SETVIDPNSOURCEADDRESS**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddress) (**Duration** member)
* [**DXGKARG_SETVIDPNSOURCEADDRESSWITHMULTIPLANEOVERLAY**](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgkarg_setvidpnsourceaddresswithmultiplaneoverlay) (**Duration** member)
* [**D3DDDI_DEVICEFUNCS**](/windows-hardware/drivers/ddi/d3dumddi/ns-d3dumddi-_d3dddi_devicefuncs) (**pfnCheckPresentDurationSupport** function pointer)
* [**DXGI1_3_DDI_BASE_FUNCTIONS**](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-dxgi1_3_ddi_base_functions) (**pfnCheckPresentDurationSupport** function pointer)

A WDDM 1.3 and later user-mode display driver must implement the following functions in order to support a 48-Hz adaptive refresh rate:

* [*CheckPresentDurationSupport*](/windows-hardware/drivers/ddi/d3dumddi/nc-d3dumddi-pfnd3dddi_checkpresentdurationsupport)
* [*pfnCheckPresentDurationSupport(DXGI)*](/windows-hardware/drivers/ddi/dxgiddi/ns-dxgiddi-_dxgi_ddi_arg_checkpresentdurationsupport)
