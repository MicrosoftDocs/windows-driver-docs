---
title: Determining the ACL of an Object
description: Determining the ACL of an Object
ms.assetid: 8dcd4f5a-1415-4a58-bfb1-fd3cbd58cc56
keywords: ["access control list (ACL)", "ACL (access control list)"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Determining the ACL of an Object


## <span id="ddk_determining_the_acl_of_an_object_dbg"></span><span id="DDK_DETERMINING_THE_ACL_OF_AN_OBJECT_DBG"></span>


You can use the debugger to examine the access control list (ACL) of an object.

The following method can be used if you are performing kernel debugging. To use it while you are performing user-mode debugging, you need to redirect control to a kernel debugger. See [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md) for details.

First, use the [**!object**](-object.md) debugger extension with the name of the object in question:

``` syntax
kd> !object \BaseNamedObjects\AgentToWkssvcEvent
Object: ffbb8a98  Type: (80e30e70) Event
    ObjectHeader: ffbb8a80
    HandleCount: 2  PointerCount: 3
    Directory Object: e14824a0  Name: AgentToWkssvcEvent
```

This shows that the object header has address 0xFFBB8A80. Use the [**dt (Display Type)**](dt--display-type-.md) command with this address and the **nt!\_OBJECT\_HEADER** structure name:

``` syntax
kd> dt nt!_OBJECT_HEADER ffbb8a80
   +0x000 PointerCount     : 3
   +0x004 HandleCount      : 2
   +0x004 NextToFree       : 0x00000002
 +0x008 Type             : 0x80e30e70
   +0x00c NameInfoOffset   : 0x10 '
 +0x00d HandleInfoOffset : 0 '
   +0x00e QuotaInfoOffset  : 0 '
   +0x00f Flags            : 0x20 ' '
   +0x010 ObjectCreateInfo : 0x8016b460
   +0x010 QuotaBlockCharged : 0x8016b460
   +0x014 SecurityDescriptor : 0xe11f08b6
   +0x018 Body             : _QUAD
```

The security descriptor pointer value is shown as 0xE11F08B6. The lowest 3 bits of this value represent an offset past the beginning of this structure, so you should ignore them. In other words, the SECURITY\_DESCRIPTOR structure actually begins at 0xE11F08B6 & ~0x7. Use the [**!sd**](-sd.md) extension on this address:

``` syntax
kd> !sd e11f08b0
->Revision: 0x1
->Sbz1    : 0x0
->Control : 0x8004
            SE_DACL_PRESENT
 SE_SELF_RELATIVE
->Owner   : S-1-5-32-544
->Group   : S-1-5-18
->Dacl    : 
->Dacl    : ->AclRevision: 0x2
->Dacl    : ->Sbz1       : 0x0
->Dacl    : ->AclSize    : 0x44
->Dacl    : ->AceCount   : 0x2
->Dacl    : ->Sbz2       : 0x0
->Dacl    : ->Ace[0]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
->Dacl    : ->Ace[0]: ->AceFlags: 0x0
->Dacl    : ->Ace[0]: ->AceSize: 0x14
->Dacl    : ->Ace[0]: ->Mask : 0x001f0003
->Dacl    : ->Ace[0]: ->SID: S-1-5-18

->Dacl    : ->Ace[1]: ->AceType: ACCESS_ALLOWED_ACE_TYPE
->Dacl    : ->Ace[1]: ->AceFlags: 0x0
->Dacl    : ->Ace[1]: ->AceSize: 0x18
->Dacl    : ->Ace[1]: ->Mask : 0x00120001
->Dacl    : ->Ace[1]: ->SID: S-1-5-32-544

->Sacl    :  is NULL
```

This displays the security information for this object.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Determining%20the%20ACL%20of%20an%20Object%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




