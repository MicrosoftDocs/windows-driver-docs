---
title: .createdir (Set Created Process Directory)
description: The .createdir command controls the starting directory and handle inheritance for any processes created by the debugger.
ms.assetid: 797f5398-f0b4-48e9-bc5f-eac5a53cad67
keywords: [".createdir (Set Created Process Directory) Windows Debugging"]
topic_type:
- apiref
api_name:
- .createdir (Set Created Process Directory)
api_type:
- NA
---

# .createdir (Set Created Process Directory)


The **.createdir** command controls the starting directory and handle inheritance for any processes created by the debugger.

``` syntax
    .createdir [-i | -I] [Path] 
```

## <span id="ddk_meta_set_created_process_directory_dbg"></span><span id="DDK_META_SET_CREATED_PROCESS_DIRECTORY_DBG"></span>Parameters


<span id="_______-i______"></span><span id="_______-I______"></span> **-i**   
Causes processes created by the debugger to inherit handles from the debugger. This is the default.

<span id="_______-I______"></span><span id="_______-i______"></span> **-I**   
Prevents processes created by the debugger from inheriting handles from the debugger.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
Specifies the starting directory for all child processes created by any target process. If *Path* contains spaces, it must be enclosed in quotation marks.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode only</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If **.createdir** is used with no parameters, the current starting directory and handle inheritance status are displayed.

If **.createdir** has never been used, any created process will use its usual default directory as its starting directory. If you have already set a path with **.createdir** and want to return to the default status, use **.createdir ""** with nothing inside the quotation marks.

The **.createdir** setting affects all processes created by [**.create (Create Process)**](-create--create-process-.md). It also affects processes created by WinDbg's [File | Open Executable](file---open-executable.md) menu command, unless the **Start directory** text box is used to override this setting.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.createdir%20%28Set%20Created%20Process%20Directory%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




