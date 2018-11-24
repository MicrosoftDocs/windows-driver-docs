---
title: Using an IViewHelper Clone-View COM Object
description: Using an IViewHelper Clone-View COM Object
ms.assetid: 2f264c5d-0e12-4116-9561-16dce99ce1fe
keywords:
- TMM WDK display , about IViewHelper
- monitor configurations WDK display , about IViewHelper
- monitor configurations WDK display , detecting new monitors
- monitor configurations WDK display , persisted
- video present networks WDK display , about IViewHelper
- VidPN WDK display , about IViewHelper
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using an IViewHelper Clone-View COM Object


TMM will use the methods of a hardware vendor's clone-view [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object in new monitor and persisted monitor configurations. In a persisted monitor configuration, TMM restores display data (that is, display modes and topology data) to monitors. TMM can pass this display data to the user-mode display driver through the [**IViewHelper::SetConfiguration**](https://msdn.microsoft.com/library/windows/hardware/ff568176) method so the driver can modify or fold in other display data (for example, gamma or TV settings).

Errors from a [Video Present Network (VidPN)](multiple-monitors-and-video-present-networks.md) are returned through the methods of [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164). Therefore, if TMM applies an improper topology, the VidPN fails and the failure result is passed back to the calling function. Mapping a target to two sources or using a target or source identifier that the VidPN cannot identify are examples of improper topology.

TMM determines the [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object through the **UserModeDriverGUID** string registry value. Hardware vendors should add this value under the registry keys that the **DeviceKey** member of the DISPLAY\_DEVICE structure specifies. A call to the Win32 **EnumDisplayDevices** function returns this registry key information in DISPLAY\_DEVICE that the *lpDisplayDevice* parameter points to. If multiple **DeviceKey** names exist, this value should appear under each of those keys. The following is an example of a device key and the **UserModeDriverGUID** string registry value:

```registry
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Video\{7661971C-A9BD-48B5-ACBC-298A8826535D}\0000]
"UserModeDriverGUID"="{YYYYYYYY-YYYY-YYYY-YYYY-YYYYYYYYYYYY}"
```

For COM to load the [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object, the COM object should be registered as an in-process (in-proc) handler, and the threading model should be Both. The GUID that is registered should match the GUID in **UserModeDriverGUID**. For information about the Both threading model attribute, see the Microsoft Windows SDK documentation.

You should only copy and register the correctly compiled versions of [IViewHelper](https://msdn.microsoft.com/library/windows/hardware/ff568164) COM interface object DLLs in the system directory. That is, you should only copy and register the 64-bit **IViewHelper** DLL for 64-bit operating systems and the 32-bit **IViewHelper** DLL for 32-bit operating systems. The two DLL binaries should not be concurrently present on the same computer. TMM will not operate properly if the two binaries are concurrently present on the same computer, even with Windows on Windows (WOW).

 

 





