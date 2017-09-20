---
title: dp ( ntsdexts.dp)
description: The dp extension in Ntsdexts.dll displays a CSR process.
ms.assetid: 9e489cfc-2105-4605-b94d-88eea7883420
keywords: ["dp ( ntsdexts.dp) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- dp ( ntsdexts.dp)
api_type:
- NA
---

# !dp (!ntsdexts.dp)


The **!dp** extension in Ntsdexts.dll displays a CSR process.

This extension command should not be confused with the [**dp (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command, or with the [**!kdext\*.dp**](-db---dc---dd---dp---dq---du---dw.md) extension command.

```
!dp [v] [ PID | CSR-Process ]
```

## <span id="ddk__ntsdexts_dp_dbg"></span><span id="DDK__NTSDEXTS_DP_DBG"></span>Parameters


<span id="_______v______"></span><span id="_______V______"></span> **v**   
Verbose mode. Causes the display to include structure and thread list.

<span id="_______PID______"></span><span id="_______pid______"></span> *PID*   
Specifies the process ID of the CSR process.

<span id="_______CSR-Process______"></span><span id="_______csr-process______"></span><span id="_______CSR-PROCESS______"></span> *CSR-Process*   
Specifies the hexadecimal address of the CSR process.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ntsdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension displays the process address, process ID, sequence number, flags, and reference count. If verbose mode is selected, additional details are displayed, and thread information is shown for each process.

If no process is specified, all processes are displayed.

## <span id="see_also"></span>See also


[**!dt**](-dt.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dp%20%28!ntsdexts.dp%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





