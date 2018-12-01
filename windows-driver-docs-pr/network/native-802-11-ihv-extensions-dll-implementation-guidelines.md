---
title: Native 802.11 IHV Extensions DLL Implementation Guidelines
description: Native 802.11 IHV Extensions DLL Implementation Guidelines
ms.assetid: ef13de2a-3510-46c5-afb6-0bf1002af5ca
keywords:
- IHV Extensions DLL WDK Native 802.11 , implementation guidelines
- Native 802.11 IHV Extensions DLL WDK , implementation guidelines
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Native 802.11 IHV Extensions DLL Implementation Guidelines




 

The IHV Extensions DLL is implemented as a run-time dynamic-link library (DLL). For more information about DLLs, refer to the topic "About Dynamic-Link Libraries" within the Microsoft Windows SDK documentation.

Refer to the following guidelines when implementing an IHV Extensions DLL.

-   The structures and function prototypes referenced by the IHV Extensions DLL are declared in Wlanihv.h.

-   The IHV Extensions DLL must implement the [*Dot11ExtIhvGetVersionInfo*](https://msdn.microsoft.com/library/windows/hardware/ff547464) and [*Dot11ExtIhvInitService*](https://msdn.microsoft.com/library/windows/hardware/ff547470) functions. Also, these functions must be exported through the module-definition (.def) file used to build the DLL. The operating system resolves the address for these functions through the **GetProcAddress** function. For more information about **GetProcAddress**, refer to the Windows SDK documentation.

-   The IHV Extensions DLL must implement all of the IHV Handler functions. The DLL returns a list of function pointers to these functions when the operating system calls the [*Dot11ExtIhvInitService*](https://msdn.microsoft.com/library/windows/hardware/ff547470) function.

    For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](https://msdn.microsoft.com/library/windows/hardware/ff560627).

-   For Windows Vista, the IHV Extensions DLL must support the interface version of zero. When [*Dot11ExtIhvGetVersionInfo*](https://msdn.microsoft.com/library/windows/hardware/ff547464) is called, the DLL must define the minimum and maximum supported interface versions to be zero.

 

 





