---
title: .srcpath, .lsrcpath (Set Source Path)
description: The .srcpath and .lsrcpath commands set or display the source file search path.
ms.assetid: 416c062f-cbf9-4134-aa2c-306147a466b5
keywords: [".srcpath, .lsrcpath (Set Source Path) Windows Debugging"]
topic_type:
- apiref
api_name:
- .srcpath, .lsrcpath (Set Source Path)
api_type:
- NA
---

# .srcpath, .lsrcpath (Set Source Path)


The **.srcpath** and **.lsrcpath** commands set or display the source file search path.

``` syntax
.srcpath[+] [Directory [; ...]] 
.lsrcpath[+] [Directory [; ...]] 
```

## <span id="ddk_meta_set_source_path_dbg"></span><span id="DDK_META_SET_SOURCE_PATH_DBG"></span>Parameters


<span id="______________"></span> **+**   
Specifies that the new directories will be appended to (rather than replacing) the previous source file search path.

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If *Directory* is not specified, the current path is displayed. Separate multiple directories with semicolons.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

The **.srcpath** command is available on all debuggers. The **.lsrcpath** command is available only in WinDbg and cannot be used in script files.

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

For details and other ways to change this path, see [Source Path](source-path.md). For more information about commands that can be used while performing remote debugging through the debugger, see [Controlling a Remote Debugging Session](controlling-a-remote-debugging-session.md).

Remarks
-------

If you include `srv*` in your source path, the debugger uses [SrcSrv](srcsrv.md) to retrieve source files from locations specified in the target modules' symbol files. For more information about using srv\* in a source path, see [Using a Source Server](using-a-source-server.md) and [**.srcfix**](-srcfix---lsrcfix--use-source-server-.md).

When this command is issued from a debugging client, **.srcpath** sets the source path on the debugging server, while **.lsrcpath** sets the source path on the local machine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.srcpath,%20.lsrcpath%20%28Set%20Source%20Path%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




