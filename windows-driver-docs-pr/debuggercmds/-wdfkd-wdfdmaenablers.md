---
title: wdfkd.wdfdmaenablers
description: The wdfkd.wdfdmaenablers extension displays all WDF direct memory access (DMA) objects associated with a specified device object. 
keywords: ["wdfkd.wdfdmaenablers Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wdfkd.wdfdmaenablers
api_type:
- NA
---

# !wdfkd.wdfdmaenablers


The **!wdfkd.wdfdmaenablers** extension displays all WDF direct memory access (DMA) objects associated with a specified device object. It also displays their associated transaction and common buffer objects.

```dbgcmd
!wdfkd.wdfdmaenablers Handle
```

## Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object (WDFDEVICE).

## DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](../debugger/kernel-mode-driver-framework-debugging.md).

 

 





