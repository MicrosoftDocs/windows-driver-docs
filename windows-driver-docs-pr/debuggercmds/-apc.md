---
title: apc (WinDbg)
description: The apc extension formats and displays the contents of one or more asynchronous procedure calls (APCs).
keywords: ["apc Windows Debugging"]
ms.date: 09/17/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- apc
api_type:
- NA
---

# !apc


The **!apc** extension formats and displays the contents of one or more asynchronous procedure calls (APCs).

```dbgcmd
    !apc
    !apc proc Process
    !apc thre Thread
    !apc KAPC
```

## Parameters


<span id="Process"></span><span id="process"></span><span id="PROCESS"></span>*Process*  
Specifies the address of the process whose APCs are to be displayed.

<span id="Thread"></span><span id="thread"></span><span id="THREAD"></span>*Thread*  
Specifies the address of the thread whose APCs are to be displayed.

<span id="_______KAPC______"></span><span id="_______kapc______"></span> *KAPC*   
Specifies the address of the kernel APC to be displayed.

## <span id="DLL"></span><span id="dll"></span>DLL


Windows XP and later - Kdexts.dll

 

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For information about APCs, see the Windows Driver Kit (WDK) documentation and Microsoft Windows Internals by Mark Russinovich and David Solomon.

## Remarks

Without any parameters, **!apc** displays all APCs.

Here is an example:

```console
kd> !apc
*** Enumerating APCs in all processes
Process e0000000858ba8b0 System
Process e0000165fff86040 smss.exe
Process e0000165fff8c040 csrss.exe
Process e0000165fff4e1d0 winlogon.exe
Process e0000165fff101d0 services.exe
Process e0000165fffa81d0 lsass.exe
Process e0000165fff201d0 svchost.exe
Process e0000165fff8e040 svchost.exe
Process e0000165fff3e040 svchost.exe
Process e0000165fff6e040 svchost.exe
Process e0000165fff24040 spoolsv.exe
Process e000000085666640 wmiprvse.exe
Process e00000008501e520 wmiprvse.exe
Process e0000000856db480 explorer.exe
Process e0000165fff206a0 ctfmon.exe
Process e0000000850009d0 ctfmon.exe
Process e0000165fff51600 conime.exe
Process e000000085496340 taskmgr.exe
Process e000000085489c30 userinit.exe
```

 

 





