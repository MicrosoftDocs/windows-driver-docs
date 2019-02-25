---
title: GDI Event Services in Windows 2000
description: GDI Event Services in Windows 2000
ms.assetid: bf7f2127-cd3e-430c-99fd-62c824394a57
keywords:
- DirectX 8.0 release notes WDK Windows 2000 display , GDI event services
- GDI WDK Windows 2000 display , events
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDI Event Services in Windows 2000


## <span id="ddk_gdi_event_services_in_windows_2000_gg"></span><span id="DDK_GDI_EVENT_SERVICES_IN_WINDOWS_2000_GG"></span>


[GDI Event Services](gdi-event-services.md) describes a group of GDI event-related functions that a display driver can use for synchronization. While these event-related functions are documented as only available in Microsoft Windows XP and later, most of them are also available in Microsoft Windows 2000. Although most of these event-related functions are available in Windows 2000, using them in a driver implemented for Windows 2000 is discouraged because such a driver could make Windows 2000 unreliable.

The event-related functions that are available in Windows 2000 behave similarly in Windows 2000 as they do in Windows XP except for the [**EngWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff565461) function. The **EngWaitForSingleObject** implementation in Windows 2000 returns a DWORD value rather than the BOOL value that the Windows XP implementation returns. This DWORD value can be one of the following values:

<span id="Zero"></span><span id="zero"></span><span id="ZERO"></span>Zero  
Indicates that one of the following operations occurred:

-   The wait succeeded. That is, the specified event object was set to the signaled state. The thread that called **EngWaitForSingleObject** can resume processing.

-   The calling thread passed an invalid event-object pointer to the *pEvent* parameter of **EngWaitForSingleObject**.

<span id="Any_nonzero_value"></span><span id="any_nonzero_value"></span><span id="ANY_NONZERO_VALUE"></span>Any nonzero value  
This value is an NTSTATUS status value that indicates the specific error condition. For example, STATUS\_TIMEOUT indicates that a time-out occurred.

**Note**   The [**EngClearEvent**](https://msdn.microsoft.com/library/windows/hardware/ff564190) and [**EngReadStateEvent**](https://msdn.microsoft.com/library/windows/hardware/ff565001) functions are not available in Windows 2000.

 

 

 





