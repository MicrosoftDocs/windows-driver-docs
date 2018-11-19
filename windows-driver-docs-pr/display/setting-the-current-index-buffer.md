---
title: Setting the Current Index Buffer
description: Setting the Current Index Buffer
ms.assetid: 4d190ce1-56a0-4445-9a68-6a24f3a9aee4
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , index buffers
- index buffers WDK Directx 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting the Current Index Buffer


## <span id="ddk_setting_the_current_index_buffer_gg"></span><span id="DDK_SETTING_THE_CURRENT_INDEX_BUFFER_GG"></span>


As with vertex data, the index buffer to be used by drawing primitives is no longer part of the data passed to the driver with the primitive, but rather is driver state. The current index buffer is set by a new DP2 token, D3DDP2OP\_SETINDICES. This token established the index buffer with the given handle as the current index buffer to use when drawing indexed primitives until a new index buffer is set or the current index buffer is cleared (an index buffer handle of zero is specified in the DP2 token data).

 

 





