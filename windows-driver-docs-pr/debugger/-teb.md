---
title: teb
description: The teb extension displays a formatted view of the information in the thread environment block (TEB).
ms.assetid: 4137b54b-f784-412d-bffd-e8a71a54155e
keywords: ["teb Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- teb
api_type:
- NA
---

# !teb


The **!teb** extension displays a formatted view of the information in the thread environment block (TEB).

``` syntax
!teb [TEB-Address] 
```

## <span id="ddk__teb_dbg"></span><span id="DDK__TEB_DBG"></span>Parameters


<span id="_______TEB-Address______"></span><span id="_______teb-address______"></span><span id="_______TEB-ADDRESS______"></span> *TEB-Address*   
The hexadecimal address of the thread whose TEB you want to examine. (This is not the address of the TEB as derived from the kernel thread block for the thread.) If *TEB-Address* is omitted in user mode, the TEB for the current thread is used. If it is omitted in kernel mode, the TEB corresponding to the current [register context](changing-contexts.md#register-context) is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

Exts.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about thread environment blocks, see *Microsoft Windows Internals* by Mark Russinovich and David Solomon.

Remarks
-------

The TEB is the user-mode portion of Microsoft Windows thread control structures.

If the **!teb** extension with no argument gives you an error in kernel mode, you should use the [**!process**](-process.md) extension to determine the TEB address for the desired thread. Make sure your [register context](changing-contexts.md#register-context) is set to the desired thread, and then use the TEB address as the argument for **!teb**.

Here is an example of this command's output in user mode:

```
0:001> ~
   0  id: 324.458   Suspend: 1 Teb 7ffde000 Unfrozen
.  1  id: 324.48c   Suspend: 1 Teb 7ffdd000 Unfrozen

0:001> !teb 
TEB at 7FFDD000
    ExceptionList:    76ffdc
    Stack Base:       770000
    Stack Limit:      76f000
    SubSystemTib:     0
 FiberData:        1e00
    ArbitraryUser:    0
    Self:             7ffdd000
    EnvironmentPtr:   0
 ClientId:         324.48c
    Real ClientId:    324.48c
    RpcHandle:        0
    Tls Storage:      0
    PEB Address:      7ffdf000
    LastErrorValue:   0
    LastStatusValue:  0
    Count Owned Locks:0
    HardErrorsMode:   0
```

The similar [**!peb**](-peb.md) extension displays the process environment block.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!teb%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




