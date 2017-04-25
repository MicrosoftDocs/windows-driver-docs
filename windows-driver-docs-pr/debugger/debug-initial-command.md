---
title: Debug initial command
description: Debug initial command
ms.assetid: 0af0b53d-455f-4cdb-b956-9d7e49601733
keywords: ["Debug initial command (global flag)"]
---

# Debug initial command


## <span id="ddk_debug_initial_command_dtools"></span><span id="DDK_DEBUG_INITIAL_COMMAND_DTOOLS"></span>


The **Debug initial command** flag debugs the Client Server Run-time Subsystem (CSRSS) and the WinLogon process.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Abbreviation</strong></p></td>
<td align="left"><p>dic</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Hexadecimal value</strong></p></td>
<td align="left"><p>0x4</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Symbolic Name</strong></p></td>
<td align="left"><p>FLG_DEBUG_INITIAL_COMMAND</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Destination</strong></p></td>
<td align="left"><p>System-wide registry entry, kernel flag</p></td>
</tr>
</tbody>
</table>

 

### <span id="comments"></span><span id="COMMENTS"></span>Comments

NTSD debugs the processes (using the command **ntsd -d**), but control is redirected to the kernel debugger.

For details on NTSD, see [Debugging Using CDB and NTSD](debugging-using-cdb-and-ntsd.md).

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[Enable debugging of Win32 subsystem](enable-debugging-of-win32-subsystem.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20initial%20command%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




