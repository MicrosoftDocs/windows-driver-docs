---
title: dskheap (WinDbg)
description: The dskheap extension displays desktop heap information for a specified session.
keywords: ["desktops", "dskheap Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- dskheap
api_type:
- NA
---

# !dskheap


The **!dskheap** extension displays desktop heap information for a specified session.

```dbgcmd
!dskheap [-v] [-s SessionID]
```

## Parameters


<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Causes the display to include more detailed output.

<span id="_______-s_SessionID"></span><span id="_______-s_sessionid"></span><span id="_______-S_SESSIONID"></span> **-s** **** *SessionID*  
Specifies a session. If this parameter is omitted, then the desktop heap information for session 0 is displayed.

## DLL

Windows XP and later - Kdexts.dll



### Additional Information

For information about desktops or desktop heaps, see the Microsoft Windows SDK documentation and *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

## Remarks

The desktop heap information for the session is arranged by window station.

Here are a couple of examples:

```dbgcmd
kd> !dskheap -s 3
##   Winstation\Desktop            Heap Size(KB)   Used Rate(%)

  WinSta0\Screen-saver              3072                 0%
  WinSta0\Default                   3072                 0%
  WinSta0\Disconnect                  64                 4%
##   WinSta0\Winlogon                   128                 5%

                Total Desktop: (    6336 KB -   4 desktops)
#                 Session ID:  3

kd> !dskheap
##   Winstation\Desktop            Heap Size(KB)   Used Rate(%)

  WinSta0\Default                   3072                 0%
  WinSta0\Disconnect                  64                 4%
  WinSta0\Winlogon                   128                 9%
  Service-0x0-3e7$\Default           512                 4%
  Service-0x0-3e5$\Default           512                 0%
  Service-0x0-3e4$\Default           512                 1%
##   SAWinSta\SADesktop                 512                 0%

                Total Desktop: (    5312 KB -   7 desktops)
#                 Session ID:  0
```









