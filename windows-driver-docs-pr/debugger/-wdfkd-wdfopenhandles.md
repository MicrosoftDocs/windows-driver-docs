---
title: wdfkd.wdfopenhandles
description: The wdfkd.wdfopenhandles extension displays information about all the handles that are open on the specified WDF device.
ms.assetid: 9b62a80a-6f53-4581-98b7-8eb5f9f146c2
keywords: ["wdfkd.wdfopenhandles Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfopenhandles
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfopenhandles


The **!wdfkd.wdfopenhandles** extension displays information about all the handles that are open on the specified WDF device.

```dbgcmd
!wdfkd.wdfopenhandles Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object (WDFDEVICE).

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays file object context information.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





