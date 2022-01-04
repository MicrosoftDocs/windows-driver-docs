---
title: Native 802.11 IHV Extensions DLL Implementation Guidelines
description: Native 802.11 IHV Extensions DLL Implementation Guidelines
keywords:
- IHV Extensions DLL WDK Native 802.11 , implementation guidelines
- Native 802.11 IHV Extensions DLL WDK , implementation guidelines
ms.date: 04/20/2017
---

# Native 802.11 IHV Extensions DLL Implementation Guidelines




 

The IHV Extensions DLL is implemented as a run-time dynamic-link library (DLL). For more information about DLLs, refer to the topic "About Dynamic-Link Libraries" within the Microsoft Windows SDK documentation.

Refer to the following guidelines when implementing an IHV Extensions DLL.

-   The structures and function prototypes referenced by the IHV Extensions DLL are declared in Wlanihv.h.

-   The IHV Extensions DLL must implement the [*Dot11ExtIhvGetVersionInfo*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_get_version_info) and [*Dot11ExtIhvInitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) functions. Also, these functions must be exported through the module-definition (.def) file used to build the DLL. The operating system resolves the address for these functions through the **GetProcAddress** function. For more information about **GetProcAddress**, refer to the Windows SDK documentation.

-   The IHV Extensions DLL must implement all of the IHV Handler functions. The DLL returns a list of function pointers to these functions when the operating system calls the [*Dot11ExtIhvInitService*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_init_service) function.

    For more information about the IHV Handler functions, see [Native 802.11 IHV Handler Functions](./native-802-11-ihv-handler-functions.md).

-   For Windows Vista, the IHV Extensions DLL must support the interface version of zero. When [*Dot11ExtIhvGetVersionInfo*](/windows-hardware/drivers/ddi/wlanihv/nc-wlanihv-dot11extihv_get_version_info) is called, the DLL must define the minimum and maximum supported interface versions to be zero.

 

 
