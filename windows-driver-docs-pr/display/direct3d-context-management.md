---
title: Direct3D Context Management
description: Direct3D Context Management
ms.assetid: 143f5150-9ac4-43f7-985f-0baa32871af2
keywords:
- context WDK Direct3D
- Direct3D WDK Windows 2000 display , context management
- context WDK Direct3D , about context management
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Direct3D Context Management


## <span id="ddk_direct3d_context_management_gg"></span><span id="DDK_DIRECT3D_CONTEXT_MANAGEMENT_GG"></span>


A context encapsulates the state information for an application-created Microsoft Direct3D hardware abstraction layer (HAL) device; that is, a context describes how the driver should draw. State includes information such as the surface being rendered to, the depth surface, shading information, and texture information.

A Direct3D driver is responsible for creating and managing its own rendering contexts.

 

 





