---
title: "!pcr (WinDbg)"
description: "The !pcr extension displays the current status of the Processor Control Region (PCR) on a specific processor."
keywords: ["processor control region (PCR)", "!pcr Windows Debugging"]
ms.date: 10/07/2019
topic_type:
- apiref
ms.topic: reference
api_name:
- pcr
api_type:
- NA
---

# !pcr

The **!pcr** extension displays the current status of the Processor Control Region (PCR) on a specific processor.

```dbgcmd
!pcr [Processor]
```

## Parameters

<span id="_______Processor______"></span><span id="_______processor______"></span><span id="_______PROCESSOR______"></span> *Processor*   
Specifies the processor to retrieve the PCR information from. If *Processor* is omitted, the current processor is used.

> [!NOTE]
> This command is not currently supported and may display incorrect output.
>

### DLL

Kdexts.dll

## Additional Information

For information about the PCR and the PRCB, see *Microsoft Windows Internals*, by Mark Russinovich and David Solomon.

## Remarks

The processor control block (PRCB) is an extension of the PCR. It can be displayed with the [**!prcb**](-prcb.md) extension.

Here is an example of the **!pcr** extension on an x86 target computer:

```dbgcmd
kd> !pcr 0
KPCR for Processor 0 at ffdff000:
    Major 1 Minor 1
      NtTib.ExceptionList: 801626e0
          NtTib.StackBase: 801628f0
         NtTib.StackLimit: 8015fb00
       NtTib.SubSystemTib: 00000000
            NtTib.Version: 00000000
        NtTib.UserPointer: 00000000
            NtTib.SelfTib: 00000000

                  SelfPcr: ffdff000
                     Prcb: ffdff120
                     Irql: 00000000
                      IRR: 00000000
                      IDR: ffffffff
            InterruptMode: 00000000
                      IDT: 80043400
                      GDT: 80043000
                      TSS: 803cc000

            CurrentThread: 8015e8a0
               NextThread: 00000000
               IdleThread: 8015e8a0

                DpcQueue:  0x80168ee0 0x80100d04 ntoskrnl!KiTimerExpiration
```

One of the entries in this display shows the interrupt request level (IRQL). The **!pcr** extension shows the current IRQL, but the current IRQL is usually not of much interest. The IRQL that existed just before the bug check or debugger connection is more interesting. This is displayed by [**!irql**](-irql.md), which is only available on computers running Windows Server 2003 or later versions of Windows.
