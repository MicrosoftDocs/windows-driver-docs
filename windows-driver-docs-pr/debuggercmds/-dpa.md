---
title: dpa (WinDbg)
description: The dpa extension displays pool allocation information.
keywords: ["pool allocation", "dpa Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dpa
api_type:
- NA
---

# !dpa


The **!dpa** extension displays pool allocation information.

```dbgcmd
!dpa Options 
!dpa -?
```

## Parameters


*Options*
Must be exactly one of the following options:

<span id="-c"></span><span id="-C"></span>**-c**  
Displays current pool allocation statistics.

<span id="-v"></span><span id="-V"></span>**-v**  
Displays all current pool allocations.

<span id="-vs"></span><span id="-VS"></span>**-vs**  
Causes the display to include stack traces.

<span id="-f"></span><span id="-F"></span>**-f**  
Displays failed pool allocations.

<span id="-r"></span><span id="-R"></span>**-r**  
Displays free pool allocations.

<span id="-p_Ptr"></span><span id="-p_ptr"></span><span id="-P_PTR"></span>**-p** **** *Ptr*  
Displays all pool allocations that contain the pointer *Ptr*.

<span id="_______-_______"></span> **-?**   
Displays some brief Help text for this extension in the Debugger Command window.

## DLL

Windows XP and later - Kdexts.dll

 

## Remarks

Pool instrumentation must be enabled in Win32k.sys in order for this extension to work.

 

 





