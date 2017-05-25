---
title: bugdump
description: The bugdump extension formats and displays the information contained in the bug check callback buffers.
ms.assetid: cbea92de-e45b-416c-87f1-6faba95788d0
keywords: ["bugdump Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- bugdump
api_type:
- NA
---

# !bugdump


The **!bugdump** extension formats and displays the information contained in the bug check callback buffers.

``` syntax
    !bugdump [Component] 
```

## <span id="ddk__bugdump_dbg"></span><span id="DDK__BUGDUMP_DBG"></span>Parameters


<span id="_______Component______"></span><span id="_______component______"></span><span id="_______COMPONENT______"></span> *Component*   
Specifies the component whose callback data is to be examined. If omitted, all bug check callback data is displayed.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Reading Bug Check Callback Data](reading-bug-check-callback-data.md).

Remarks
-------

This extension can only be used after a bug check has occurred, or when you are debugging a kernel-mode crash dump file.

The *Component* parameter corresponds to the final parameter used in [**KeRegisterBugCheckCallback**](https://msdn.microsoft.com/library/windows/hardware/ff553105).

The buffers that hold callback data are not available in a Small Memory Dump. These buffers are present in Kernel Memory Dumps and Full Memory Dumps. However, in Windows XP SP1, Windows Server 2003, and later versions of Windows, the dump file is created before the drivers' **BugCheckCallback** routines are called, and therefore these buffers will not contain the data written by these routines.

If you are performing live debugging of a crashed system, all callback data will be present.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!bugdump%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




