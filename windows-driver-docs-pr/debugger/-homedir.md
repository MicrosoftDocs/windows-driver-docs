---
title: homedir
description: The homedir extension sets the default directory used by the symbol server and the source server.
ms.assetid: 6bebd7df-03d8-4413-8a0c-a0d5ad913173
keywords: ["homedir Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- homedir
api_type:
- NA
ms.localizationpriority: medium
---

# !homedir


The **!homedir** extension sets the default directory used by the symbol server and the source server.

```dbgcmd
!homedir Directory
!homedir
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies the new directory to use as the home directory.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Windows 2000</p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p>Windows XP and later</p></td>
<td align="left"><p>Dbghelp.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If the **!homedir** extension is used with no argument, the current home directory is displayed.

The cache for a source server is located in the src subdirectory of the home directory. The downstream store for a symbol server defaults to the sym subdirectory of the home directory, unless a different location is specified.

When WinDbg is started, the home directory is the directory where Debugging Tools for Windows was installed. The **!homedir** extension can be used to change this value.

 

 





