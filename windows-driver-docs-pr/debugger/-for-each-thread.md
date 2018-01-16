---
title: for_each_thread
description: The for_each_thread extension executes the specified debugger command once for each thread in the target.
ms.assetid: 4ca8e1bd-1a1b-4fef-a2d9-42c26f9b746b
keywords: ["for_each_thread Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- for_each_thread
api_type:
- NA
---

# !for\_each\_thread


The **!for\_each\_thread** extension executes the specified debugger command once for each thread in the target.

```
!for_each_thread ["CommandString"] 
!for_each_thread -? 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to be executed for each thread. If *CommandString* includes multiple commands, separate them with semicolons (;) and enclose *CommandString* in quotation marks ("). If *CommandString* is enclosed in quotations marks, the individual commands within *CommandString* cannot contain quotation marks. Within *CommandString*, **@\#Thread** is replaced by the thread address.

<span id="_______-_______"></span> **-?**   
Displays help for this extension in the Debugger Command window.

### <span id="DLL"></span><span id="dll"></span>DLL

This extension works only in kernel mode, even though it resides in Ext.dll.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ext.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more general information about threads, see [Threads and Processes](controlling-threads-and-processes.md). For more information about manipulating or obtaining information about threads, see [Controlling Processes and Threads](controlling-processes-and-threads.md).

Remarks
-------

If no arguments are supplied, the debugger displays a list of all threads, along with thread wait states. This is equivalent to entering [**!thread @\#Thread 2**](-process.md) as the *CommandString* value.

You can terminate execution at any point by pressing CTRL+BREAK (in WinDbg) or CTRL+C (in KD).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!for_each_thread%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




