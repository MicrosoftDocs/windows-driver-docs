---
title: debugbaseeventcallbacks
description: The DebugBaseEventCallbacks class provides a base implementation of the IDebugEventCallbacks interface. 
ms.assetid: B0422248-2F5F-4AE6-93C9-D96B5E4A1B5A
keywords: [DebugBaseEventCallbacks]
ms.date: 01/10/2018
topic_type:
- apiref
api_name:
- debugbaseeventcallbacks
api_type:
- NA
ms.localizationpriority: medium
---

# DebugBaseEventCallbacks class 

The DebugBaseEventCallbacks class provides a base implementation of the [IDebugEventCallbacks](https://docs.microsoft.com/windows-hardware/drivers/ddi/dbgeng/nn-dbgeng-idebugeventcallbacks) interface. 

A program can derive an event callbacks class from DebugBaseEventCallbacks and implement only the methods needed. 

Be careful to implement GetInterestMask appropriately.
 
### Requirements

Header

Dbgeng.h (include Dbgeng.h)  


### See Also
[DebugBaseEventCallbacksWide](debugbaseeventcallbackswide.md)

 

 





