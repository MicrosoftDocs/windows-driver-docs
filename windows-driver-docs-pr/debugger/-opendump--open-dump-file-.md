---
title: .opendump (Open Dump File)
description: The .opendump command opens a dump file for debugging.
ms.assetid: 751af9ea-be7e-4aef-a6f6-fc99e3b3a56e
keywords: [".opendump (Open Dump File) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .opendump (Open Dump File)
api_type:
- NA
ms.localizationpriority: medium
---

# .opendump (Open Dump File)


The **.opendump** command opens a dump file for debugging.

```dbgcmd
.opendump DumpFile 
.opendump /c "DumpFileInArchive" [CabFile] 
```

## <span id="ddk_meta_open_dump_file_dbg"></span><span id="DDK_META_OPEN_DUMP_FILE_DBG"></span>Parameters


<span id="_______DumpFile______"></span><span id="_______dumpfile______"></span><span id="_______DUMPFILE______"></span> *DumpFile*   
Specifies the name of the dump file to open. *DumpFile* should include the file name extension (typically .dmp or .mdmp) and can include an absolute or relative path. Relative paths are relative to the directory that you started the debugger in.

<span id="________c__DumpFileInArchive_"></span><span id="________c__dumpfileinarchive_"></span><span id="________C__DUMPFILEINARCHIVE_"></span> **/c** **"**<em>DumpFileInArchive</em>**"**  
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

 
**Note**   There are complications, when you debug live targets and dump targets together, because commands behave differently for each type of debugging. For example, if you use the **g (Go)** command when the current system is a dump file, the debugger begins executing, but you cannot break back into the debugger, because the break command is not recognized as valid for dump file debugging.
 





