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

For minifilters, user-mode communication APIs do not require administrator privileges. Instead, a minifilter defines the necessary privilege using an [**ACL**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/ns-wdm-_acl) defined on a port.

### <span id="Filter_Manager_User-Mode_Library_Routines"></span><span id="filter_manager_user-mode_library_routines"></span><span id="FILTER_MANAGER_USER-MODE_LIBRARY_ROUTINES"></span>Filter Manager User-Mode Library Routines

The filter manager provides the following support routines for user-mode applications to use for loading and unloading minifilter drivers:

[**FilterLoad**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterload)

[**FilterUnload**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterunload)

The following support routines are provided for creating and closing minifilter driver and instance handles:

[**FilterClose**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterclose)

[**FilterCreate**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtercreate)

[**FilterInstanceClose**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterinstanceclose)

[**FilterInstanceCreate**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterinstancecreate)

The following support routines are provided for attaching and detaching minifilter driver instances:

[**FilterAttach**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterattach)

[**FilterAttachAtAltitude**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterattachataltitude)

[**FilterDetach**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterdetach)

The following support routines are provided for enumerating filters, volumes, and instances:

[**FilterFindFirst**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterfindfirst)

[**FilterFindNext**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterfindnext)

[**FilterInstanceFindFirst**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterinstancefindfirst)

[**FilterInstanceFindNext**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterinstancefindnext)

[**FilterVolumeFindFirst**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtervolumefindfirst)

[**FilterVolumeFindNext**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtervolumefindnext)

[**FilterVolumeInstanceFindFirst**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtervolumeinstancefindfirst)

[**FilterVolumeInstanceFindNext**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtervolumeinstancefindnext)

The following support routines are provided for querying for information:

[**FilterGetDosName**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtergetdosname)

[**FilterGetInformation**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtergetinformation)

[**FilterInstanceGetInformation**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterinstancegetinformation)

The following support routines are provided for communication initiated by a user operation:

[**FilterConnectCommunicationPort**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterconnectcommunicationport)

[**FilterSendMessage**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtersendmessage)

The following support routines are provided for responding to communication initiated by a minifilter driver:

[**FilterGetMessage**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filtergetmessage)

[**FilterReplyMessage**](https://docs.microsoft.com/windows/desktop/api/fltuser/nf-fltuser-filterreplymessage)

 

 




