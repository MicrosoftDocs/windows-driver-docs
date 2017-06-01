---
title: wdfkd.wdfextendwatchdog
description: The wdfkd.wdfextendwatchdog extension extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.
ms.assetid: 6feb922f-0016-468c-8dd2-963db6874977
keywords: ["wdfkd.wdfextendwatchdog Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- wdfkd.wdfextendwatchdog
api_type:
- NA
---

# !wdfkd.wdfextendwatchdog


The **!wdfkd.wdfextendwatchdog** extension extends the time-out period (from 10 minutes to 24 hours) of the framework's watchdog timer during power transitions.

```
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!wdfkd.wdfextendwatchdog%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




