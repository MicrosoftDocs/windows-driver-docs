---
title: Maintaining State Within a Context
description: Maintaining State Within a Context
ms.assetid: dabf6aa7-f127-419c-9245-5270768fef5b
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


A driver updates its internal state associated with a context when its [**D3dDrawPrimitives2**](https://msdn.microsoft.com/library/windows/hardware/ff544704) callback is called. This callback must also return the updated context's public state to Direct3D.

 

 





