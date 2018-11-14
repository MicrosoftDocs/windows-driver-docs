---
title: wdfkd.wdfdmaenablers
description: The wdfkd.wdfdmaenablers extension displays all WDF direct memory access (DMA) objects associated with a specified device object. 
ms.assetid: 31b185e7-74d3-4329-b389-37279e5aa75c
keywords: ["wdfkd.wdfdmaenablers Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfdmaenablers
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfdmaenablers


The **!wdfkd.wdfdmaenablers** extension displays all WDF direct memory access (DMA) objects associated with a specified device object. It also displays their associated transaction and common buffer objects.

```dbgcmd
!wdfkd.wdfdmaenablers Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object (WDFDEVICE).

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





