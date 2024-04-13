---
title: "!dcr (WinDbg)"
description: "The !dcr extension displays the default control register (DCR) at the specified address."
keywords: ["DCR (default control register)", "!dcr Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dcr
api_type:
- NA
---

# !dcr


The **!dcr** extension displays the default control register (DCR) at the specified address.

```dbgcmd
!dcr Expression [DisplayLevel]
```

**Important**  This command has been deprecated in the Windows Debugger Version 10.0.14257 and later, and is no longer available.

 

## Parameters


<span id="_______Expression______"></span><span id="_______expression______"></span><span id="_______EXPRESSION______"></span> *Expression*   
Specifies the hexadecimal address of the DCR to display. The expression <strong>@dcr</strong> can also be used for this parameter. In that case, information about the current processor DCR is displayed.

<span id="_______DisplayLevel______"></span><span id="_______displaylevel______"></span><span id="_______DISPLAYLEVEL______"></span> *DisplayLevel*   
Can be any one of the following options:

<span id="0"></span>**0**  
Causes only the values of each DCR field to be displayed. This is the default value.

<span id="1"></span>**1**  
Causes the display to include more in-depth information about each of the DCR fields that is not reserved or ignored.

<span id="2"></span>**2**  
Causes the display to include more in-depth information about all of the DCR fields, including those that are ignored or reserved.

## DLL

Kdexts.dll

 

This extension command can only be used with an Itanium-based target computer.

## Remarks

The DCR specifies default parameters for the processor status register values on interruption. The DCR also specifies some additional global controls, as well as whether or not speculative load faults can be deferred.

Here are a couple of examples:

```dbgcmd
kd> !dcr @dcr
dcr:pp be lc dm dp dk dx dr da dd
1 0 1 1 1 1 1 1 1 1

kd> !dcr @dcr 2

  pp : 1 : Privileged Performance Monitor Default
  be : 0 : Big-Endian Default
  lc : 1 : IA-32 Lock check Enable
  rv : 0 : reserved1
  dm : 1 : Defer TLB Miss faults only
  dp : 1 : Defer Page Not Present faults only
  dk : 1 : Defer Key Miss faults only
  dx : 1 : Defer Key Permission faults only
  dr : 1 : Defer Access Rights faults only
  da : 1 : Defer Access Bit faults only
  dd : 0 : Defer Debug faults only
  rv : 0 : reserved2
```

