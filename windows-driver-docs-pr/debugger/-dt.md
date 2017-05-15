---
title: dt
description: The dt extension displays information about a CSR thread.This extension command should not be confused with the dt (Display Type) command.
ms.assetid: 7fbca028-8d11-42b5-b64e-41eb3edc56cc
keywords: ["dt Windows Debugging"]
topic_type:
- apiref
api_name:
- dt
api_type:
- NA
---

# !dt


The **!dt** extension displays information about a CSR thread.

This extension command should not be confused with the [**dt (Display Type)**](dt--display-type-.md) command.

``` syntax
    !dt [v] CSR-Thread 
```

## <span id="ddk__dt_dbg"></span><span id="DDK__DT_DBG"></span>Parameters


<span id="_______v______"></span><span id="_______V______"></span> **v**   
Verbose mode.

<span id="_______CSR-Thread______"></span><span id="_______csr-thread______"></span><span id="_______CSR-THREAD______"></span> *CSR-Thread*   
Specifies the hexadecimal address of the CSR thread.

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

This extension displays the thread, process, client ID, flags, and reference count associated with the CSR thread. If verbose mode is selected, the display will also include list pointers, thread handle, and the wait block.

## <span id="see_also"></span>See also


[**!dp (!ntsdexts.dp)**](-dp---ntsdexts-dp-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!dt%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





