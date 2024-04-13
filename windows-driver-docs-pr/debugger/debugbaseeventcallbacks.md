---
title: DebugBaseEventCallbacks class
description: The DebugBaseEventCallbacks class provides a base implementation of the IDebugEventCallbacks interface. 
keywords: [DebugBaseEventCallbacks]
ms.date: 01/10/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- debugbaseeventcallbacks
api_type:
- NA
---

# DebugBaseEventCallbacks class 

The DebugBaseEventCallbacks class provides a base implementation of the [IDebugEventCallbacks](/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) interface. 

A program can derive an event callbacks class from DebugBaseEventCallbacks and implement only the methods needed. 

Be careful to implement GetInterestMask appropriately.
 
### Requirements

Header

Dbgeng.h (include Dbgeng.h)  


### See Also
[DebugBaseEventCallbacksWide](debugbaseeventcallbackswide.md)

 

