---
title: sid
description: The sid extension displays the security identifier (SID) at the specified address.
ms.assetid: 7b93eb0e-7c0f-4c30-851b-6f40c7df8e1b
keywords: ["sid Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- sid
api_type:
- NA
---

# !sid


The **!sid** extension displays the security identifier (SID) at the specified address.

Syntax

```
!sid Address [Flags] 
```

## <span id="ddk__sid_dbg"></span><span id="DDK__SID_DBG"></span>Parameters


<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the SID structure.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
If this is set to 1, the SID type, domain, and user name for the SID is displayed.

If this is set to 1, the friendly name is displayed. This includes the SID type, as well as the domain and user name for the SID.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about SIDs, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, or *Microsoft Windows Internals* by Mark Russinovich and David Solomon. Also see [**!sd**](-sd.md) and [**!acl**](-acl.md).

Remarks
-------

Here are two examples, one without the friendly name shown, and one with:

```
kd> !sid 0xe1bf35b8
SID is: S-1-5-21-518066528-515770016-299552555-513

kd> !sid 0xe1bf35b8 1
SID is: S-1-5-21-518066528-515770016-299552555-513 (Group: MYGROUP\Domain Users)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!sid%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




