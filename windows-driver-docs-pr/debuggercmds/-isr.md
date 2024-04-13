---
title: "!isr (WinDbg)"
description: "The !isr extension displays the Itanium Interruption Status Register (ISR) at the specified address."
keywords: ["ISR (Interruption Status Register)", "Interruption Status Register (ISR)", "!isr Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- isr
api_type:
- NA
---

# !isr

The !isr extension displays the Itanium Interruption Status Register (ISR) at the specified address.

```dbgcmd
!isr Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.
 
## Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of the ISR register to display. The expression <strong>@isr</strong> can also be used for this parameter. In that case, information about the current processor ISR register is displayed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Displays only the values of each ISR field. This is the default.

<span id="1"></span>**1**  
Displays detailed information about ISR fields that are not reserved or ignored.

<span id="2"></span>**2**  
Displays details about all ISR fields, including those that are ignored or reserved.

## DLL

Kdexts.dll

This extension command can only be used with an Itanium target computer.

## Remarks

Here are a couple of examples of output from this extension:

```dbgcmd
kd> !isr @isr
isr:ed ei so ni ir rs sp na r w x vector code
  0  0  0  0  0  0  0  0 0 0 0      0   0

kd> !isr @isr 2

 cod : 0 : interruption Code
 vec : 0 : IA32 exception vector number
  rv : 0 : reserved0
   x : 0 : eXecute exception
   w : 0 : Write exception
   r : 0 : Read exception
  na : 0 : Non-Access exception
  sp : 0 : Speculative load exception
  rs : 0 : Register Stack
  ir : 0 : Invalid Register frame
  ni : 0 : Nested Interruption
  so : 0 : IA32 Supervisor Override
  ei : 0 : Exception IA64 Instruction
  ed : 0 : Exception Deferral
  rv : 0 : reserved1
```

