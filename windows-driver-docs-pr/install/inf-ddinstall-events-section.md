---
title: INF DDInstall.Events section
description: Each per-Models DDInstall.Events section contains one or more INF AddEventProvider directives that reference additional INF-writer-defined sections in an INF file.
keywords:
- INF DDInstall.Events Section Device and Driver Installation
topic_type:
- apiref
api_name:
- INF DDInstall.Events Section
api_type:
- NA
ms.date: 06/08/2022
---

# INF DDInstall.Events section

Each per-Models _DDInstall_.**Events** section contains one or more [**INF AddEventProvider directives**](inf-addeventprovider-directive.md), [**AddAutoLogger**](inf-addupdateautologger-directive.md) or [**UpdateAutoLogger**](inf-addupdateautologger-directive.md) that reference additional INF-writer-defined sections in an INF file. This section is supported for Windows 10 version 1809 and later.

```inf
[install-section-name.Events] |
[install-section-name.nt.Events] |
[install-section-name.ntx86.Events] |
[install-section-name.ntia64.Events] |
[install-section-name.ntamd64.Events] |
[install-section-name.ntarm.Events] |
[install-section-name.ntarm64.Events]

AddEventProvider={ProviderGUID},event-provider-install-section
AddAutoLogger=session-name,{SessionGUID},add-autologger-install-section 
UpdateAutoLogger=session-name,update-autologger-install-section  
[Include=filename.inf[,filename2.inf]...]
[Needs=inf-section-name[,inf-section-name]...] 
```

You can provide a _DDInstall_.**Events** section with at least one **AddEventProvider** directive to register [Event Tracing for Windows](/windows/desktop/ETW/about-event-tracing) (ETW) providers. You can also provide one or more **AddAutoLogger** directives to [Configure and Start an AutoLogger Session](/windows/win32/etw/configuring-and-starting-an-autologger-session) and  **UpdateAutoLogger** directives to add AutoLogger providers to an existing AutoLogger session.

## Entries

**AddEventProvider=**{_ProviderGUID_},_event-provider-install-section_  
This directive references an INF-writer-defined _event-provider-install-section_ elsewhere in the INF file for the drivers of the devices covered by this _DDInstall_ section. For more information, see [**INF AddEventProvider Directive**](inf-addeventprovider-directive.md).

**AddAutoLogger=**_session-name_,{_SessionGUID_},_add-autologger-install-section_  
This directive references an INF-writer-defined _add-autologger-install-section_ elsewhere in the INF file for the drivers of the devices covered by this _DDInstall_ section. For more information, see [**INF AddAutoLogger and UpdateAutoLogger Directives**](inf-addupdateautologger-directive.md).

**UpdateAutoLogger=**_session-name_,_update-autologger-install-section_  
This directive references an INF-writer-defined _update-autologger-install-section_ elsewhere in the INF file for the drivers of the devices covered by this _DDInstall_ section. For more information, see [**INF AddAutoLogger and UpdateAutoLogger Directives**](inf-addupdateautologger-directive.md).

**Include=**_filename_.**inf**[,_filename2_.**inf**]...  
This optional entry specifies one or more additional system-supplied INF files that contain sections needed to install this device. If this entry is specified, a **Needs** entry is also usually required.

**Needs=**_inf-section-name_[,_inf-section-name_]...  
This optional entry specifies the section that must be processed during the installation of this device. Typically, the section is a _DDInstall_.**Events** section within a system-supplied INF file that is listed in an **Include** entry. However, it can be any section that is referenced within a _DDInstall_.**Events** section.

## Remarks

_DDInstall_.**Events** sections should have the same platform and operating system decorations as their related [**_DDInstall_**](inf-ddinstall-section.md) sections. For example, an _install-section-name_.**ntx86** section would have a corresponding _install-section-name_.**ntx86.Events** section.

The specified _DDInstall_ section must be referenced in a device/models-specific entry under the per-manufacturer _Models_ section of the INF file. The case-insensitive extensions to the _install-section-name_ shown in the formal syntax statement can be inserted into such a _DDInstall_.**Events** section name in cross-platform INF files.

For more information about how to use the system-defined **.nt**, **.ntx86**, **.ntia64**, **.ntamd64**, **.ntarm**, and **.ntarm64** extensions, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

## Examples

This example shows the _install-section-name_.**Events** section and its event-provider-install-sections, add-autologger-install-sections, and update-autologger-install-sections in the INF file.

```inf
[Device_Inst.NT.Events]
AddEventProvider={071acb53-ccfb-42e0-9a68-5336b7301507},Contoso_Event_Provider_1_Inst 
AddEventProvider={6d3fd9ef-bcbb-42d7-9fbd-1bf2d926b394},Contoso_Event_Provider_2_Inst 
AddAutoLogger=ContosoAddSession,{d9ff08ce-a7a6-4c44-91e9-bc1e3692301b},Contoso_Add_AutoLogger_Inst 
UpdateAutoLogger=ContosoUpdateSession,Contoso_Update_AutoLogger_Inst 

; entries in the following xxx_Inst sections omitted here for brevity,
; but fully specified as the example for the AddEventProvider,  
; AddAutoLogger, and UpdateAutoLogger directives 
; 

[Contoso_Event_Provider_1_Inst] 
; ...  

[Contoso_Event_Provider_2_Inst]  
; ... 

[Contoso_Add_AutoLogger_Inst] 
; ...

[Contoso_Update_AutoLogger_Inst] 
; ... 
```

## See also

[**AddEventProvider**](inf-addeventprovider-directive.md)

[**AddAutoLogger and UpdateAutoLogger**](inf-addupdateautologger-directive.md)

[**_DDInstall_**](inf-ddinstall-section.md)
