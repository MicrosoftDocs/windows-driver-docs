---
title: wdfkd.wdffindobjects
description: The wdfkd.wdffindobjects extension searches memory for WDF objects.
ms.assetid: 8c0a4881-9417-481b-82f8-f3510af768a1
keywords: ["wdfkd.wdffindobjects Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdffindobjects
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdffindobjects


The **!wdfkd.wdffindobjects** extension searches memory for WDF objects.

```dbgcmd
!wdfkd.wdffindobjects [StartAddress [Flags]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______StartAddress______"></span><span id="_______startaddress______"></span><span id="_______STARTADDRESS______"></span> *StartAddress*   
Optional. Specifies the address at which the search must begin. If this is omitted, the search will begin from where the most recent **!wdfkd.wdffindobjects** search ended.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to display. *Flags* can be any combination of the following bits. The default value is 0x0. *Flags* cannot be used unless *StartAddress* is specified.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Displays verbose output.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Displays internal type information for each handle.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The following examples show the output of the **!wdfkd.wdffindobjects** extension. The 0x1 flag is set in the second example.

```dbgcmd
1: kd> !wdffindobjects 0xfffffa600211b668 
  Address             Value               Object
  ------------------  ------------------  ------------------
  0xfffffa600211b668  0x0000000000000008  
  0xfffffa600211b670  0xfffffa8002e7b1f0  !WDFREQUEST 0x0000057ffd184e08
  0xfffffa600211b678  0x0000000000000004  
  0xfffffa600211b680  0x0000000000000001  
  0xfffffa600211b688  0xfffffa8006aa3640  !WDFUSBPIPE 0x0000057ff955c9b8
  0xfffffa600211b690  0x0000000000000000  
  0xfffffa600211b698  0xfffff80001e61f78  
  0xfffffa600211b6a0  0x0000000000000010  
  0xfffffa600211b6a8  0x0000000000010286  
  0xfffffa600211b6b0  0xfffffa600211b6c0  
  0xfffffa600211b6b8  0x0000000000000000  
  0xfffffa600211b6c0  0xfffffa8006aa3640  !WDFUSBPIPE 0x0000057ff955c9b8
  0xfffffa600211b6c8  0x0000057ffd184e08  !WDFREQUEST 0x0000057ffd184e08
  0xfffffa600211b6d0  0x0000000000000000  
  0xfffffa600211b6d8  0x0000057ffc51ea18  !WDFMEMORY 0x0000057ffc51ea18
  0xfffffa600211b6e0  0x0000000000000000  

1: kd> !wdffindobjects 0xfffffa600211b668 1 
  Address             Value               Type    Object
  ------------------  ------------------  ------  ------------------
  0xfffffa600211b668  0x0000000000000008  
  0xfffffa600211b670  0xfffffa8002e7b1f0  Object  !WDFREQUEST 0x0000057ffd184e08
  0xfffffa600211b678  0x0000000000000004  
  0xfffffa600211b680  0x0000000000000001  
  0xfffffa600211b688  0xfffffa8006aa3640  Object  !WDFUSBPIPE 0x0000057ff955c9b8
  0xfffffa600211b690  0x0000000000000000  
  0xfffffa600211b698  0xfffff80001e61f78  
  0xfffffa600211b6a0  0x0000000000000010  
  0xfffffa600211b6a8  0x0000000000010286  
  0xfffffa600211b6b0  0xfffffa600211b6c0  
  0xfffffa600211b6b8  0x0000000000000000  
  0xfffffa600211b6c0  0xfffffa8006aa3640  Object  !WDFUSBPIPE 0x0000057ff955c9b8
  0xfffffa600211b6c8  0x0000057ffd184e08  Handle  !WDFREQUEST 0x0000057ffd184e08
  0xfffffa600211b6d0  0x0000000000000000  
  0xfffffa600211b6d8  0x0000057ffc51ea18  Handle  !WDFMEMORY 0x0000057ffc51ea18
  0xfffffa600211b6e0  0x0000000000000000  
```

 

 





