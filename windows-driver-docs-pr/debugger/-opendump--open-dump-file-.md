---
title: .opendump (Open Dump File)
description: The .opendump command opens a dump file for debugging.
ms.assetid: 751af9ea-be7e-4aef-a6f6-fc99e3b3a56e
keywords: [".opendump (Open Dump File) Windows Debugging"]
topic_type:
- apiref
api_name:
- .opendump (Open Dump File)
api_type:
- NA
---

# .opendump (Open Dump File)


The **.opendump** command opens a dump file for debugging.

``` syntax
.opendump DumpFile 
.opendump /c "DumpFileInArchive" [CabFile] 
```

## <span id="ddk_meta_open_dump_file_dbg"></span><span id="DDK_META_OPEN_DUMP_FILE_DBG"></span>Parameters


<span id="_______DumpFile______"></span><span id="_______dumpfile______"></span><span id="_______DUMPFILE______"></span> *DumpFile*   
Specifies the name of the dump file to open. *DumpFile* should include the file name extension (typically .dmp or .mdmp) and can include an absolute or relative path. Relative paths are relative to the directory that you started the debugger in.

<span id="________c__DumpFileInArchive_"></span><span id="________c__dumpfileinarchive_"></span><span id="________C__DUMPFILEINARCHIVE_"></span> **/c** **"***DumpFileInArchive***"**  
Specifies the name of a dump file to debug. This dump file must be contained in the archive file that *CabFile* specifies. You must enclose the *DumpFileInArchive* file in quotation marks.

<span id="_______CabFile______"></span><span id="_______cabfile______"></span><span id="_______CABFILE______"></span> *CabFile*   
Specifies the name of an archive file to open. *CabFile*should include the file name extension (typically .cab) and can include an absolute or relative path. Relative paths are relative to the directory that you started the debugger in. If you use the **/c** switch to specify a dump file in an archive but you omit *CabFile*, the debugger reuses the archive file that you most recently opened.

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
<td align="left"><p>Crash dump only (but you can use this command if other sessions are running)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

After you use the **.opendump** command, you must use the [**g (Go)**](g--go-.md) command to finish loading the dump file.

When you are opening an archive file (such as a CAB file), you should use the **/c** switch. If you do not use this switch and you specify an archive for *DumpFile*, the debugger opens the first file that has an .mdmp or .dmp file name extension within this archive.

You can use **.opendump** even if a debugging session is already in progress. This feature enables you to debug more than one crash dump at the same time. For more information about how to control a multiple-target session, see [Debugging Multiple Targets](debugging-multiple-targets.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.opendump%20%28Open%20Dump%20File%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




