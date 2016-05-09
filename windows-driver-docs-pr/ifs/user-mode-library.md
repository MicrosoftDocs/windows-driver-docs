---
title: User-Mode Library
author: windows-driver-content
description: User-Mode Library
ms.assetid: a471ae15-bbdd-47c8-ad77-9b82281dd430
keywords: ["filter manager WDK file system minifilter , user-mode library", "user-mode library WDK file system minifilter", "Fltlib.dll"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20User-Mode%20Library%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


