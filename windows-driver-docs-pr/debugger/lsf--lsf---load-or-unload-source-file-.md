---
title: lsf, lsf- (Load or Unload Source File)
description: The lsf and lsf- commands load or unload a source file.
ms.assetid: e788a778-e331-4b7b-8aad-072b3d08442b
keywords: ["lsf, lsf- (Load or Unload Source File) Windows Debugging"]
topic_type:
- apiref
api_name:
- lsf, lsf- (Load or Unload Source File)
api_type:
- NA
---

# lsf, lsf- (Load or Unload Source File)


The **lsf** and **lsf-** commands load or unload a source file.

``` syntax
lsf Filename 
lsf- Filename
```

## <span id="ddk_cmd_load_or_unload_source_file_dbg"></span><span id="DDK_CMD_LOAD_OR_UNLOAD_SOURCE_FILE_DBG"></span>Parameters


<span id="_______Filename______"></span><span id="_______filename______"></span><span id="_______FILENAME______"></span> *Filename*   
Specifies the file to load or unload. If this file is not located in the directory where the debugger was opened from, you must include an absolute or relative path. The file name must follow Microsoft Windows file name conventions.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Modes</strong></p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The **lsf** command loads a source file.

The **lsf-** command unloads a source file. You can use this command to unload files that you previously loaded with **lsf** or automatically loaded source files. You cannot use **lsf-** to unload files that were loaded through WinDbg's [File | Open Source File](file---open-source-file.md) command or files that a WinDbg workspace loaded.

In CDB or KD, you can view source files in the [Debugger Command window](debugger-command-window.md). In WinDbg, source files are loaded as new [Source windows](source-window.md).

For more information about source files, source paths, and other ways to load source files, see [Source Path](source-path.md).

## <span id="see_also"></span>See also


[**ls, lsa (List Source Lines)**](ls--lsa--list-source-lines-.md)

[**lsc (List Current Source)**](lsc--list-current-source-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20lsf,%20lsf-%20%28Load%20or%20Unload%20Source%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





