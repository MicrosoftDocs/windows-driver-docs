---
title: findfilelockowner
description: The findfilelockowner extension attempts to find the owner of a file object lock by examining all threads for a thread that is blocked.
ms.assetid: 0d6eabf4-e7ac-4536-beab-d3027720efa8
keywords: ["findfilelockowner Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- findfilelockowner
api_type:
- NA
ms.localizationpriority: medium
---

# !findfilelockowner


The **!findfilelockowner** extension attempts to find the owner of a file object lock by examining all threads for a thread that is blocked in an IopSynchronousServiceTail assert and that has the file object as a parameter.

```dbgcmd
!findfilelockowner [FileObject]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______FileObject______"></span><span id="_______fileobject______"></span><span id="_______FILEOBJECT______"></span> *FileObject*   
Specifies the address of a file object. If *FileObject* is omitted, the extension searches for any thread in the current process that is stuck in **IopAcquireFileObjectLock** and retrieves the file object address from the stack trace.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Unavailable</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about file objects, see the Microsoft Windows SDK documentation, the Windows Driver Kit (WDK) documentation, and *Microsoft Windows Internals* by Mark Russinovich and David Solomon. (These resources may not be available in some languages and countries.)

Remarks
-------

This extension is most useful after a critical section timeout in which the thread that times out was waiting for the file inside **IopAcquireFileObjectLock**. After the offending thread is found, the extension attempts to recover the IRP that was used for the request and to display the driver that was processing the IRP.

The extension takes some time to complete because it walks the stack of all threads in the system until it finds the offending thread.You can stop \` at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 





