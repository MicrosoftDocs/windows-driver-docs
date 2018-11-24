---
title: Processing the D3DDP2OP_CLEAR DP2 Token
description: Processing the D3DDP2OP_CLEAR DP2 Token
ms.assetid: ec027f44-bdd5-4d5a-8c47-1ac6a0c1cb6e
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , pure devices, D3DDP2OP_CLEAR DP2 token processing
- pure devices WDK DirectX 8.0 , D3DDP2OP_CLEAR DP2 token processing
- D3DDP2OP_CLEAR WDK DirectX 8.0
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Processing the D3DDP2OP\_CLEAR DP2 Token


## <span id="ddk_processing_the_d3ddp2op_clear_dp2_token_gg"></span><span id="DDK_PROCESSING_THE_D3DDP2OP_CLEAR_DP2_TOKEN_GG"></span>


DirectX 8.0 introduces some changes to the required processing of the D3DDP2OP\_CLEAR token. Specifically a new flag D3DCLEAR\_COMPUTERECTS has been added to the **dwFlags** field of the [**D3DHAL\_DP2CLEAR**](https://msdn.microsoft.com/library/windows/hardware/ff545441) data structure. This new flag is only passed to the driver when a pure device type is being used (that is, D3DCREATE\_PUREDEVICE was specified when creating the device and the driver exports the D3DDEVCAPS\_PUREDEVICE device cap). Furthermore, this flag is never passed to non-DirectX 8.0 drivers and it is not specified by using the legacy **Clear** or **Clear2** driver callbacks.

 

 





