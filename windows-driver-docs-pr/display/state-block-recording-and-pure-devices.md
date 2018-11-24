---
title: State Block Recording and Pure Devices
description: State Block Recording and Pure Devices
ms.assetid: 9959d361-aa92-4209-8f81-deba96498941
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , pure devices, state block handling
- pure devices WDK DirectX 8.0 , state block handling
- state block handling WDK DirectX 8.0
- state block handling WDK DirectX 8.0 , pure devices
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# State Block Recording and Pure Devices


## <span id="ddk_state_block_recording_and_pure_devices_gg"></span><span id="DDK_STATE_BLOCK_RECORDING_AND_PURE_DEVICES_GG"></span>


State block handling is different for a device operating in pure device mode. In this mode, the state block control DP2 token (D3DDP2OP\_STATESET) is sent to the driver with a new operation type (in the **dwOperations** field). This new operation type is D3DHAL\_STATESETCREATE.

 

 





