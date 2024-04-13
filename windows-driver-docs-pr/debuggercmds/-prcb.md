---
title: "!prcb (WinDbg)"
description: "The !prcb extension displays the processor control block (PRCB)."
keywords: ["processor control block", "!prcb Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- prcb
api_type:
- NA
---

# !prcb

The **!prcb** extension displays the processor control block (PRCB).

```dbgcmd
!prcb [Processor]
```

## <span id="ddk__prcb_dbg"></span><span id="DDK__PRCB_DBG"></span>Parameters


<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor to retrieve the PRCB information from. If *Processor* is omitted, processor zero will be used.

## DLL

Kdexts.dll

## Additional Information

For information about the PCR and the PRCB, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

The PRCB is an extension of the processor control region (PCR). To display the PCR, use the [**!pcr**](-pcr.md) extension.

Here is an example:

```dbgcmd
kd> !prcb
PRCB for Processor 0 at e0000000818ba000:
Threads--  Current e0000000818bbe10 Next 0000000000000000 Idle e0000000818bbe10
Number 0 SetMember 00000001
Interrupt Count -- 0000b81f
Times -- Dpc    00000028 Interrupt 000003ff 
         Kernel 00005ef4 User      00000385 
```
