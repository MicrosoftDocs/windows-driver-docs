---
title: "!poolval (WinDbg)"
description: "The !poolval extension analyzes the headers for a pool page and diagnoses any possible corruption. "
keywords: ["!poolval Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- poolval
api_type:
- NA
---

# !poolval

The **!poolval** extension analyzes the headers for a pool page and diagnoses any possible corruption.

```dbgcmd
!poolval Address [DisplayLevel]
```

## Parameters

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the pool whose header is to be analyzed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Specifies the information to include in the display. This can be any of the following values (the default is zero):

<span id="0"></span>0  
Causes basic information to be displayed.

<span id="1"></span>1  
Causes basic information and linked header lists to be displayed.

<span id="2"></span>2  
Causes basic information, linked header lists, and basic header information to be displayed.

<span id="3"></span>3  
Causes basic information, linked header lists, and full header information to be displayed.

## DLL

Kdexts.dll

## Additional Information

For information about memory pools, see the Windows Driver Kit (WDK) documentation and *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.
