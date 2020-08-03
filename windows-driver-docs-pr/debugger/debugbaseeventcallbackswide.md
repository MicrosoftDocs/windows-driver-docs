---
title: debugbaseeventcallbackswide
description: The DebugBaseEventCallbacksWide class provides a base implementation of the IDebugEventCallbacksWide interface. 
ms.assetid: 38AD8472-1BA3-42EA-99CE-E91098A5B334
keywords: [DebugBaseEventCallbacksWide]
ms.date: 01/10/2018
topic_type:
- apiref
api_name:
- debugbaseeventcallbackswide
api_type:
- NA
ms.localizationpriority: medium
---

# DebugBaseEventCallbacksWide class 

The DebugBaseEventCallbacksWide class provides a base implementation of the [IDebugEventCallbacksWide](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbackswide) interface. 

A program can derive an event callbacks class from DebugBaseEventCallbacksWide and implement only the methods needed. 

Be careful to implement GetInterestMask appropriately.
 
### Requirements

Header

Dbgeng.h (include Dbgeng.h)  


### See Also
[DebugBaseEventCallbacks](debugbaseeventcallbacks.md)

 

 





