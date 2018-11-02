---
title: wdfkd.wdfwmi
description: The wdfkd.wdfwmi extension displays the Microsoft Windows Management Instrumentation (WMI) information for a specified framework device object. 
ms.assetid: fd521be8-3c7a-415b-8044-c9fb25188cbc
keywords: ["wdfkd.wdfwmi Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfwmi
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfwmi


The **!wdfkd.wdfwmi** extension displays the Microsoft Windows Management Instrumentation (WMI) information for a specified framework device object. This information includes all WMI provider objects and their associated WMI instance objects.

```dbgcmd
!wdfkd.wdfwmi Handle
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a framework device object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The output of the **!wdfkd.wdfwmi** extension includes information about the WMI registration, provider, and instances.

 

 





