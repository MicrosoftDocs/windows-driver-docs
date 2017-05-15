---
title: .dumpcab (Create Dump File CAB)
description: The .dumpcab command creates a CAB file containing the current dump file.
ms.assetid: 65ed766f-b049-47b0-90d7-e21d510a35ba
keywords: [".dumpcab (Create Dump File CAB) Windows Debugging"]
topic_type:
- apiref
api_name:
- .dumpcab (Create Dump File CAB)
api_type:
- NA
---

# .dumpcab (Create Dump File CAB)


The **.dumpcab** command creates a CAB file containing the current dump file.

``` syntax
    .dumpcab [-a] CabName 
```

## <span id="ddk_meta_create_dump_file_cab_dbg"></span><span id="DDK_META_CREATE_DUMP_FILE_CAB_DBG"></span>Parameters


<span id="_______-a______"></span><span id="_______-A______"></span> **-a**   
Causes all currently loaded symbols to be included in the CAB file. For minidumps, all loaded images will be included as well. Use [**lml**](lm--list-loaded-modules-.md) to determine which symbols and images are loaded.

<span id="_______CabName______"></span><span id="_______cabname______"></span><span id="_______CABNAME______"></span> *CabName*   
The CAB file name, including extension. *CabName* can include an absolute or relative path; relative paths are relative to the directory in which the debugger was started. It is recommended that you choose the extension .cab.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>user mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more details on crash dumps, see [Crash Dump Files](crash-dump-files.md).

Remarks
-------

This command can only be used if you are already debugging a dump file.

If you are debugging a live target and want to create a dump file and place it in a CAB, you should use the [**.dump (Create Dump File)**](-dump--create-dump-file-.md) command. Next, start a new debugging session with the dump file as its target, and use **.dumpcab**.

The **.dumpcab** command cannot be used to place multiple dump files into one CAB file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.dumpcab%20%28Create%20Dump%20File%20CAB%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




