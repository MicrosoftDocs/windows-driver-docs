---
title: User-Mode Library
description: User-Mode Library
keywords:
- filter manager WDK file system minifilter , user-mode library
- user-mode library WDK file system minifilter
- Fltlib.dll
ms.date: 04/20/2017
---

# User-Mode Library


The filter manager user mode interfaces provide common functionality for products that include filter drivers. The user-mode library is *Fltlib.dll*. Applications include the header files *FltUser.h* and *FltUserStructures.h*, and link to *FltLib.lib*.

These user-mode interfaces enable general control of the minifilter driver and communication between the user-mode service or control program and the filter driver. User-mode interfaces also provide interfaces for management tools that allow enumeration of filters, volumes, and instances.

For minifilters, user-mode communication APIs do not require administrator privileges. Instead, a minifilter defines the necessary privilege using an [**ACL**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_acl) defined on a port.

### <span id="Filter_Manager_User-Mode_Library_Routines"></span><span id="filter_manager_user-mode_library_routines"></span><span id="FILTER_MANAGER_USER-MODE_LIBRARY_ROUTINES"></span>Filter Manager User-Mode Library Routines

The filter manager provides the following support routines for user-mode applications to use for loading and unloading minifilter drivers:

[**FilterLoad**](/windows/win32/api/fltuser/nf-fltuser-filterload)

[**FilterUnload**](/windows/win32/api/fltuser/nf-fltuser-filterunload)

The following support routines are provided for creating and closing minifilter driver and instance handles:

[**FilterClose**](/windows/win32/api/fltuser/nf-fltuser-filterclose)

[**FilterCreate**](/windows/win32/api/fltuser/nf-fltuser-filtercreate)

[**FilterInstanceClose**](/windows/win32/api/fltuser/nf-fltuser-filterinstanceclose)

[**FilterInstanceCreate**](/windows/win32/api/fltuser/nf-fltuser-filterinstancecreate)

The following support routines are provided for attaching and detaching minifilter driver instances:

[**FilterAttach**](/windows/win32/api/fltuser/nf-fltuser-filterattach)

[**FilterAttachAtAltitude**](/windows/win32/api/fltuser/nf-fltuser-filterattachataltitude)

[**FilterDetach**](/windows/win32/api/fltuser/nf-fltuser-filterdetach)

The following support routines are provided for enumerating filters, volumes, and instances:

[**FilterFindFirst**](/windows/win32/api/fltuser/nf-fltuser-filterfindfirst)

[**FilterFindNext**](/windows/win32/api/fltuser/nf-fltuser-filterfindnext)

[**FilterInstanceFindFirst**](/windows/win32/api/fltuser/nf-fltuser-filterinstancefindfirst)

[**FilterInstanceFindNext**](/windows/win32/api/fltuser/nf-fltuser-filterinstancefindnext)

[**FilterVolumeFindFirst**](/windows/win32/api/fltuser/nf-fltuser-filtervolumefindfirst)

[**FilterVolumeFindNext**](/windows/win32/api/fltuser/nf-fltuser-filtervolumefindnext)

[**FilterVolumeInstanceFindFirst**](/windows/win32/api/fltuser/nf-fltuser-filtervolumeinstancefindfirst)

[**FilterVolumeInstanceFindNext**](/windows/win32/api/fltuser/nf-fltuser-filtervolumeinstancefindnext)

The following support routines are provided for querying for information:

[**FilterGetDosName**](/windows/win32/api/fltuser/nf-fltuser-filtergetdosname)

[**FilterGetInformation**](/windows/win32/api/fltuser/nf-fltuser-filtergetinformation)

[**FilterInstanceGetInformation**](/windows/win32/api/fltuser/nf-fltuser-filterinstancegetinformation)

The following support routines are provided for communication initiated by a user operation:

[**FilterConnectCommunicationPort**](/windows/win32/api/fltuser/nf-fltuser-filterconnectcommunicationport)

[**FilterSendMessage**](/windows/win32/api/fltuser/nf-fltuser-filtersendmessage)

The following support routines are provided for responding to communication initiated by a minifilter driver:

[**FilterGetMessage**](/windows/win32/api/fltuser/nf-fltuser-filtergetmessage)

[**FilterReplyMessage**](/windows/win32/api/fltuser/nf-fltuser-filterreplymessage)

 

