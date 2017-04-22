---
title: Accelerated State Management
description: Accelerated State Management
ms.assetid: 276d3cdb-34bf-49e8-aae5-94315746c5ff
keywords:
- accelerated state management WDK Direct3D
- states WDK Direct3D
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Accelerated%20State%20Management%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




