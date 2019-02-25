---
title: User-Mode Library
description: User-Mode Library
ms.assetid: a471ae15-bbdd-47c8-ad77-9b82281dd430
keywords:
- filter manager WDK file system minifilter , user-mode library
- user-mode library WDK file system minifilter
- Fltlib.dll
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# User-Mode Library


The filter manager user mode interfaces provide common functionality for products that include filter drivers. The user-mode library is *Fltlib.dll*. Applications include the header files *FltUser.h* and *FltUserStructures.h*, and link to *FltLib.lib*.

These user-mode interfaces enable general control of the minifilter driver and communication between the user-mode service or control program and the filter driver. User-mode interfaces also provide interfaces for management tools that allow enumeration of filters, volumes, and instances.

For minifilters, user-mode communication APIs do not require administrator privileges. Instead, a minifilter defines the necessary privilege using an [**ACL**](https://msdn.microsoft.com/library/windows/hardware/ff538866) defined on a port.

### <span id="Filter_Manager_User-Mode_Library_Routines"></span><span id="filter_manager_user-mode_library_routines"></span><span id="FILTER_MANAGER_USER-MODE_LIBRARY_ROUTINES"></span>Filter Manager User-Mode Library Routines

The filter manager provides the following support routines for user-mode applications to use for loading and unloading minifilter drivers:

[**FilterLoad**](https://msdn.microsoft.com/library/windows/hardware/ff541504)

[**FilterUnload**](https://msdn.microsoft.com/library/windows/hardware/ff541516)

The following support routines are provided for creating and closing minifilter driver and instance handles:

[**FilterClose**](https://msdn.microsoft.com/library/windows/hardware/ff540453)

[**FilterCreate**](https://msdn.microsoft.com/library/windows/hardware/ff540467)

[**FilterInstanceClose**](https://msdn.microsoft.com/library/windows/hardware/ff540524)

[**FilterInstanceCreate**](https://msdn.microsoft.com/library/windows/hardware/ff540528)

The following support routines are provided for attaching and detaching minifilter driver instances:

[**FilterAttach**](https://msdn.microsoft.com/library/windows/hardware/ff540442)

[**FilterAttachAtAltitude**](https://msdn.microsoft.com/library/windows/hardware/ff540448)

[**FilterDetach**](https://msdn.microsoft.com/library/windows/hardware/ff540475)

The following support routines are provided for enumerating filters, volumes, and instances:

[**FilterFindFirst**](https://msdn.microsoft.com/library/windows/hardware/ff540485)

[**FilterFindNext**](https://msdn.microsoft.com/library/windows/hardware/ff540488)

[**FilterInstanceFindFirst**](https://msdn.microsoft.com/library/windows/hardware/ff540541)

[**FilterInstanceFindNext**](https://msdn.microsoft.com/library/windows/hardware/ff541493)

[**FilterVolumeFindFirst**](https://msdn.microsoft.com/library/windows/hardware/ff541525)

[**FilterVolumeFindNext**](https://msdn.microsoft.com/library/windows/hardware/ff541530)

[**FilterVolumeInstanceFindFirst**](https://msdn.microsoft.com/library/windows/hardware/ff541541)

[**FilterVolumeInstanceFindNext**](https://msdn.microsoft.com/library/windows/hardware/ff541551)

The following support routines are provided for querying for information:

[**FilterGetDosName**](https://msdn.microsoft.com/library/windows/hardware/ff540492)

[**FilterGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff540500)

[**FilterInstanceGetInformation**](https://msdn.microsoft.com/library/windows/hardware/ff541499)

The following support routines are provided for communication initiated by a user operation:

[**FilterConnectCommunicationPort**](https://msdn.microsoft.com/library/windows/hardware/ff540460)

[**FilterSendMessage**](https://msdn.microsoft.com/library/windows/hardware/ff541513)

The following support routines are provided for responding to communication initiated by a minifilter driver:

[**FilterGetMessage**](https://msdn.microsoft.com/library/windows/hardware/ff540506)

[**FilterReplyMessage**](https://msdn.microsoft.com/library/windows/hardware/ff541508)

 

 




