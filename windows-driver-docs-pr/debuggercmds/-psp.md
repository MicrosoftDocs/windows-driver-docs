---
title: psp (WinDbg)
description: The psp extension displays the processor state parameter (PSP) register at the specified address.
keywords: ["processor state parameter (PSP)", "PSP register", "psp Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- psp
api_type:
- NA
---

# !psp


The **!psp** extension displays the processor state parameter (PSP) register at the specified address.

This extension is supported only on Itanium-based target computers.

```dbgcmd
!psp Address [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the PSP register to display.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Displays only the values of each PSP field. This is the default.

<span id="1"></span>**1**  
Displays more in-depth information on each of the PSP fields that is not reserved or ignored.

<span id="2"></span>**2**  
Displays more in-depth information on all of the PSP fields, including those that are ignored or reserved.

## DLL

Windows XP and later - Kdexts.dll

 

 

 





