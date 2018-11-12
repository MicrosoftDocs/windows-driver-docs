---
title: Accelerated State Management
description: Accelerated State Management
ms.assetid: 276d3cdb-34bf-49e8-aae5-94315746c5ff
keywords:
- accelerated state management WDK Direct3D
- states WDK Direct3D
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accelerated State Management


## <span id="ddk_accelerated_state_management_gg"></span><span id="DDK_ACCELERATED_STATE_MANAGEMENT_GG"></span>


Accelerated state management is a mechanism for communicating large state changes across the API and DDI in a single call. This scheme allows an application to define a collection of state-set calls as a state block defined by a single integer. Sending this integer as a render state executes all the state changes in one call.

This reduces API overhead by reducing the number of **IDirect3DDevice7::SetRenderState** method calls required, and can improve the efficiency of drivers by allowing them to "precompile" stage changes into their own hardware-specific format upon a state block define, instead of on execution of each state change. **IDirect3DDevice7::SetRenderState** is described in the Direct3D SDK documentation

Most applications render in only a handful of states, so having fine-grained state transitions is seldom important. What is more important is being able to define blocks of state that can be interchanged as the driver switches between common rendering scenarios. This is the whole point of accelerated state management.

State-set tokens are used to record the states in the driver. A handle refers to a collection of states. The [**D3DHAL\_DP2STATESET**](https://msdn.microsoft.com/library/windows/hardware/ff545844) structure informs the driver about what state-set operations to perform.

If the **dwOperation** member of the D3DHAL\_DP2STATESET structure is set to D3DHAL\_STATESETBEGIN, the driver begins recording the states for the handle contained in the **dwParam** member. When the driver receives a **dwOperation** of D3DHAL\_STATESETEND, it stops recording state.

If the **dwOperation** member is D3DHAL\_STATESETDELETE, the state-set referred to by the **dwParam** handle should be deleted.

If the **dwOperation** member is D3DHAL\_STATESETEXECUTE, the state block referred to by the **dwParam** handle should be applied in the device.

If the **dwOperation** member is D3DHAL\_STATESETCAPTURE, the current state in the driver should be captured in a specific way, giving a snapshot of the current states defined in the state block. That is, only states that are already in the state block are captured. Thus, the state block acts as a sort of mask, only recording states that are defined in it. For example, if there is a D3DRENDERSTATE\_ZENABLE render state in the state block, then the current state for D3DRENDERSTATE\_ZENABLE is captured and put in the state block. If there is no D3DRENDERSTATE\_ZENABLE in the state block, then that state is not captured.

Groupings of states are used to make generic state blocks that can be modified slightly for different rendering scenarios. These predefined groupings (enumerated in D3DSTATEBLOCKTYPE in the DirectX SDK documentation) define generic state blocks that can be subsequently modified with state changes to accommodate anticipated recurring rendering scenarios. For example, the driver might create 100 generic predefined state blocks and then modify each slightly to accommodate a different rendering scenario. The state block type is passed in the **sbType** member of the D3DHAL\_DP2STATESET structure.

The **sbType** member is only valid for D3DHAL\_STATESETBEGIN and D3DHAL\_STATESETEND and specifies the predefined state block type with one of the following D3DSTATEBLOCKTYPE enumerated types: **NULL** for no state, D3DSBT\_ALL for all state, D3DSBT\_PIXELSTATE for pixel state, and D3DSBT\_VERTEXSTATE for vertex state.

The driver should ignore the**sbType** member unless it implements render state extensions. If the driver implements extended render states, that is, render states beyond those the Direct3D runtime supplies, it can use **sbType**to determine what type of predefined render states are being used. From this information it can determine how to append the state block appropriately, to support its extensions.

 

 





