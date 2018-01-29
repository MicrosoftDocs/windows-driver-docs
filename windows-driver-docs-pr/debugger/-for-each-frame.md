---
title: for_each_frame
description: The for_each_frame extension executes a debugger command one time for each frame in the stack of the current thread.
ms.assetid: 7294dc5e-190f-486f-9079-1fb28d6d484b
keywords: ["for_each_frame Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- for_each_frame
api_type:
- NA
---

# !for\_each\_frame


The **!for\_each\_frame** extension executes a debugger command one time for each frame in the stack of the current thread.

```
!for_each_frame ["CommandString"] 
!for_each_frame -?
```

## <span id="ddk__for_each_frame_dbg"></span><span id="DDK__FOR_EACH_FRAME_DBG"></span>Parameters


<span id="_______CommandString______"></span><span id="_______commandstring______"></span><span id="_______COMMANDSTRING______"></span> *CommandString*   
Specifies the debugger commands to execute one time for each frame. If *CommandString* includes multiple commands, you must separate them with semicolons and enclose *CommandString* in quotation marks. If you include multiple commands, the individual commands within *CommandString* cannot contain quotation marks. If you want to refer to the index of the current frame within *CommandString*, use the @$frame pseudoregister.

<span id="_______-_______"></span> **-?**   
Displays some Help text for this extension in the [Debugger Command window](debugger-command-window.md).

### <span id="DLL"></span><span id="dll"></span>DLL

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

For more information about the local context, see [Changing Contexts](changing-contexts.md).

Remarks
-------

If you do not specify any arguments, the **!for\_each\_frame** extension displays a list of all frames and their frame indexes. For a more detailed list of all frames, use the [**k (Display Stack Backtrace)**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command.

The [**k**](k--kb--kc--kd--kp--kp--kv--display-stack-backtrace-.md) command walks up to 256 frames. For each enumerated frame, that frame temporarily becomes the current local context (similar to the [**.frame (Set Local Context)**](-frame--set-local-context-.md) command). After the context has been set, *CommandString* is executed. After all frames have been used, the local context is reset to the value that it had before you used the **!for\_each\_frame** extension.

If you include *CommandString*, the debugger displays the frame and its index before the command is executed for that frame.

The following command displays all local variables for the current stack.

```
!for_each_frame !for_each_local dt @#Local
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!for_each_frame%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




