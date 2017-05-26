---
title: sd
description: The sd extension displays the security descriptor at the specified address.
ms.assetid: 67c72bdb-7bfc-42d6-9b65-31a07dc67729
keywords: ["sd Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- sd
api_type:
- NA
---

# !sd


The **!sd** extension displays the security descriptor at the specified address.

Syntax

```
    !sd Address [Flags] 
```

## <span id="ddk__sd_dbg"></span><span id="DDK__SD_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the hexadecimal address of the SECURITY\_DESCRIPTOR structure.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
If this is set to 1, the friendly name is displayed. This includes the security identifier (SID) type, as well as the domain and user name for the SID.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an application and an example of this command, see [Determining the ACL of an Object](determining-the-acl-of-an-object.md). For information about security descriptors, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Also see [**!sid**](-sid.md) and [**!acl**](-acl.md).

Remarks
-------

Here is an example:

```
kd> !sd e1a96a80 1
->Revision: 0x1
->Sbz1    : 0x0
->Control : 0x8004
            SE_DACL_PRESENT
            SE_SELF_RELATIVE
->Owner   : S-1-5-21-518066528-515770016-299552555-2981724 (User: MYDOMAIN\myuser)
->Group   : S-1-5-21-518066528-515770016-299552555-513 (Group: MYDOMAIN\Domain Users)
->Dacl    :
->Dacl    : ->AclRevision: 0x2
->Dacl    : ->Sbz1       : 0x0
->Dacl    : ->AclSize    : 0x40
->Dacl    : ->AceCount   : 0x2
->Dacl    : ->Sbz2       : 0x0
->Dacl    : ->Ace[0]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
->Dacl    : ->Ace[0]: ->AceFlags: 0x0
->Dacl    : ->Ace[0]: ->AceSize: 0x24
->Dacl    : ->Ace[0]: ->Mask : 0x001f0003
->Dacl    : ->Ace[0]: ->SID: S-1-5-21-518066528-515770016-299552555-2981724 (User: MYDOMAIN\myuser)

->Dacl    : ->Ace[1]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
->Dacl    : ->Ace[1]: ->AceFlags: 0x0
->Dacl    : ->Ace[1]: ->AceSize: 0x14
->Dacl    : ->Ace[1]: ->Mask : 0x001f0003
->Dacl    : ->Ace[1]: ->SID: S-1-5-18 (Well Known Group: NT AUTHORITY\SYSTEM)

->Sacl    :  is NULL
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!sd%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




