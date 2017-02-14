---
title: GDI Event Services in Windows 2000
description: GDI Event Services in Windows 2000
ms.assetid: bf7f2127-cd3e-430c-99fd-62c824394a57
keywords: ["DirectX 8.0 release notes WDK Windows 2000 display , GDI event services", "GDI WDK Windows 2000 display , events"]
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Event%20Services%20in%20Windows%202000%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




