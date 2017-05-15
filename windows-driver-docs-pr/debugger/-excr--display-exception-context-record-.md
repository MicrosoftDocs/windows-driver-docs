---
title: .excr (Display Exception Context Record)
description: The .excr command displays the context record that is associated with the current exception.
ms.assetid: 18FD32B9-93DE-4E23-A73C-18CC3665417A
keywords: [".excr (Display Exception Context Record) Windows Debugging"]
topic_type:
- apiref
api_name:
- .excr (Display Exception Context Record)
api_type:
- NA
---

# .excr (Display Exception Context Record)


The **.excr** command displays the context record that is associated with the current exception.

``` syntax
.excr
```

## <span id="ddk_meta_display_exception_context_record_dbg"></span><span id="DDK_META_DISPLAY_EXCEPTION_CONTEXT_RECORD_DBG"></span>


### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Crash dump only (minidumps only)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the register context and other context settings, see [Changing Contexts](changing-contexts.md).

Remarks
-------

The **.excr** command locates the current exception's context information and displays the important registers for the specified context record.

This command also instructs the debugger to use the context record that is associated with the current exception as the register context. After you run **.excr**, the debugger can access the most important registers and the stack trace for this thread. This register context persists until you enable the target to execute, change the current process or thread, or use another register context command ([**.cxr**](-cxr--display-context-record-.md) or **.excr**). For more information about register contexts, see [Register Context](changing-contexts.md#register-context).

The [**.ecxr**](-ecxr--display-exception-context-record-.md) command is a synonym command and has identical functionality.

## <span id="see_also"></span>See also


[**.ecxr**](-ecxr--display-exception-context-record-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.excr%20%28Display%20Exception%20Context%20Record%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





