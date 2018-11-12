---
title: wdfkd.wdfextendwatchdog
description: The wdfkd.wdfextendwatchdog extension extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.
ms.assetid: 6feb922f-0016-468c-8dd2-963db6874977
keywords: ["wdfkd.wdfextendwatchdog Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfextendwatchdog
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfextendwatchdog


The **!wdfkd.wdfextendwatchdog** extension extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.

```dbgcmd
!wdfkd.wdfextendwatchdog Handle [Extend]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFDEVICE-typed object.

<span id="_______Extend______"></span><span id="_______extend______"></span><span id="_______EXTEND______"></span> *Extend*   
Optional. A value that indicates whether to enable or disable extension of the time-out period. If *Extend* is 0, extension is disabled, and the time-out period is 10 minutes. If *Extend* is 1, extension is enabled and the time-out period is 24 hours. The default value is 1.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The framework starts an internal watchdog timer every time it calls a power policy or power event callback function for a driver that is not power pageable (that is, the DO\_POWER\_PAGABLE bit is clear). If the callback function causes paging I/O and therefore blocks, the operating system hangs because no paging device is available to service the request.

If the time-out period elapses, the framework issues bug check 0x10D (WDF\_VIOLATION). For details, see [**Bug Check 0x10D**](bug-check-0x10d---wdf-violation.md).

 

 





