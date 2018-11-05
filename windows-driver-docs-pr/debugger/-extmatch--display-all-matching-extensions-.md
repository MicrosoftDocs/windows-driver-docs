---
title: .extmatch (Display All Matching Extensions)
description: The .extmatch command displays extension commands exported by the currently loaded extension DLLs that match the specified pattern.
ms.assetid: 068a32ce-c5ac-4fee-9e9d-e47393097675
keywords: [".extmatch (Display All Matching Extensions) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .extmatch (Display All Matching Extensions)
api_type:
- NA
ms.localizationpriority: medium
---

# .extmatch (Display All Matching Extensions)


The **.extmatch** command displays extension commands exported by the currently loaded extension DLLs that match the specified pattern.

```dbgcmd
.extmatch [Options] Pattern 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Specifies the searching options. You can use one or more of the following options:

<span id="_e_ExtDLLPattern"></span><span id="_e_extdllpattern"></span><span id="_E_EXTDLLPATTERN"></span>**/e** **** *ExtDLLPattern*  
Limits the enumeration to extension commands exported by extension DLLs that match the specified pattern string. *ExtDLLPattern* is matched against the extension DLL filename.

<span id="_n"></span><span id="_N"></span>**/n**  
Excludes the extension name when the extensions are displayed. Thus, if this option is specified, then only the extension name itself will be displayed.

<span id="________D______"></span><span id="________d______"></span> **/D**   
Displays the output using [Debugger Markup Language (DML)](debugger-markup-language-commands.md). In the output, each listed extension is a link that you can click to get more information about the extension. Not all extension modules support DML.

<span id="_______Pattern______"></span><span id="_______pattern______"></span><span id="_______PATTERN______"></span> *Pattern*   
Specifies a pattern that the extension must contain. *Pattern*can contain a variety of wildcard characters and specifiers. For more information about the syntax, see [String Wildcard Syntax](string-wildcard-syntax.md).

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

To display a list of loaded extension DLLs, use the [**.chain**](-chain--list-debugger-extensions-.md) command.

Here is an example of this command, showing all the loaded extension DLLs that have an export named !help:

```dbgcmd
0:000> .extmatch help 
!ext.help
!exts.help
!uext.help
!ntsdexts.help
```

The following example lists all extension commands beginning with the string "he" that are exported by extension DLLs whose names begin with the string "ex":

```dbgcmd
0:000> .extmatch /e ext* he* 
!ext.heap
!ext.help
!exts.heap
!exts.help
```

The following example lists all extension commands, so we can see which ones support DML.

![screen shot of .extmatch /d output](images/extmatch01.png)

 

 





