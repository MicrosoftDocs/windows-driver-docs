---
title: Maintaining State Within a Context
description: Maintaining State Within a Context
keywords:
- context WDK Direct3D , maintaining state
- states WDK Direct3D
- internal states WDK Direct3D
- public states WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Maintaining State Within a Context


## <span id="ddk_maintaining_state_within_a_context_gg"></span><span id="DDK_MAINTAINING_STATE_WITHIN_A_CONTEXT_GG"></span>


A driver updates its internal state associated with a context when its [**D3dDrawPrimitives2**](/windows-hardware/drivers/ddi/d3dhal/nc-d3dhal-lpd3dhal_drawprimitives2cb) callback is called. This callback must also return the updated context's public state to Direct3D.

 

