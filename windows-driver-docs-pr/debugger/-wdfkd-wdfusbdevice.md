---
title: wdfkd.wdfusbdevice
description: The wdfkd.wdfusbdevice extension displays information about a specified KMDF USB device object, incuding all USB interfaces and the pipes that are configured.
ms.assetid: 94e0a4ef-36a6-4a37-ac4a-5a2ee2678b9a
keywords: ["wdfkd.wdfusbdevice Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfusbdevice
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfusbdevice


The !wdfkd.wdfusbdevice extension displays information about a specified Kernel-Mode Driver Framework (KMDF) USB device object. This information includes all USB interfaces and the pipes that are configured for each interface.

```dbgcmd
!wdfkd.wdfusbdevice Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFUSBDEVICE-typed USB device object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. A hexadecimal value that modifies the kind of information to return. The default value is 0x0. Flags can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include the properties of the I/O target.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
The display will include the properties of the I/O target for each USB pipe object.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

 

 





