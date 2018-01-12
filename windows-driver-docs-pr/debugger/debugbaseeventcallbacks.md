---
title: debugbaseeventcallbacks
description: The DebugBaseEventCallbacks class provides a base implementation of the IDebugEventCallbacks interface. 
ms.assetid: B0422248-2F5F-4AE6-93C9-D96B5E4A1B5A
keywords: [DebugBaseEventCallbacks]
ms.author: windowsdriverdev
ms.date: 01/10/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- debugbaseeventcallbacks
api_type:
- NA
---

# DebugBaseEventCallbacks class 

The DebugBaseEventCallbacks class provides a base implementation of the [IDebugEventCallbacks](https://msdn.microsoft.com/library/windows/hardware/ff550550.aspx) interface. 

A program can derive an event callbacks class from DebugBaseEventCallbacks and implement only the methods needed. 

Be careful to implement GetInterestMask appropriately.
 
### Requirements

Header

Dbgeng.h (include Dbgeng.h)  


### See Also
[DebugBaseEventCallbacksWide](debugbaseeventcallbackswide.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!debugbaseeventcallbacks%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




