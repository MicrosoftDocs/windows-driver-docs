---
title: bugdump
description: The bugdump extension formats and displays the information contained in the bug check callback buffers.
ms.assetid: cbea92de-e45b-416c-87f1-6faba95788d0
keywords: ["bugdump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- bugdump
api_type:
- NA
ms.localizationpriority: medium
---

# !bugdump


The **!bugdump** extension formats and displays the information contained in the bug check callback buffers.

```dbgsyntax
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

 

 





