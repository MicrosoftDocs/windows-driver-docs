---
title: wdfkd.wdfusbinterface
description: The wdfkd.wdfusbinterface extension displays information about a specified Kernel-Mode Driver Framework (KMDF) USB interface object, including its possible and current settings.
ms.assetid: 2c0788aa-adb0-4a51-9937-32c8d9e0c240
keywords: ["wdfkd.wdfusbinterface Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfusbinterface
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfusbinterface


The **!wdfkd.wdfusbinterface** extension displays information about a specified Kernel-Mode Driver Framework (KMDF) USB interface object, including its possible and current settings.

```dbgcmd
!wdfkd.wdfusbinterface Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFUSBINTERFACE-typed USB interface object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. A hexadecimal value that modifies the kind of information to return. The default value is 0x0. Flags can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include the properties of the I/O target for each KMDF USB pipe object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





