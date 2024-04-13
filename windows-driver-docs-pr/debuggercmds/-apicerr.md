---
title: "!apicerr (WinDbg)"
description: "The !apicerr extension displays the local Advanced Programmable Interrupt Controller (APIC) error log."
keywords: ["APIC (Advanced Programmable Interrupt Controller)", "!apicerr Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- apicerr
api_type:
- NA
---

# !apicerr

The **!apicerr** extension displays the local Advanced Programmable Interrupt Controller (APIC) error log.

```dbgcmd
     !apicerr [Format] 
```

## Parameters


<span id="_______Format______"></span><span id="_______format______"></span><span id="_______FORMAT______"></span> *Format*   
Specifies the order in which to display the error log contents. This can be any one of the following values:

<span id="0x0"></span><span id="0X0"></span>0x0  
Displays the error log according to order of occurrence.

<span id="0x1"></span><span id="0X1"></span>0x1  
Displays the error log according to processor.

## DLL

Kdexts.dll

This extension command can only be used with an x86-based or an x64-based target computer.

## Additional Information

For information about APICs, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon. 
