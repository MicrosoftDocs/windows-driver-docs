---
title: .copysym (Copy Symbol Files)
description: The .copysym command copies the current symbol files to the specified directory.
ms.assetid: f90d1402-4bf3-4cd0-993e-a42c220beb7a
keywords: [".copysym (Copy Symbol Files) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .copysym (Copy Symbol Files)
api_type:
- NA
ms.localizationpriority: medium
---

# .copysym (Copy Symbol Files)


The **.copysym** command copies the current symbol files to the specified directory.

```dbgsyntax
    .copysym [/l] Path
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________l______"></span><span id="________L______"></span> **/l**   
Causes each symbol file to be loaded as it is copied.

<span id="_______Path______"></span><span id="_______path______"></span><span id="_______PATH______"></span> *Path*   
Specifies the directory to which the symbol files should be copied. Copies do not overwrite existing files.

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

 

Remarks
-------

Many times, symbols are stored on a network. The symbol access can often be slow, or you may need to transport your debugging session to another computer where you no longer have network access. In such scenarios, the **.copysym** command can be used to copy the symbols you need for your session to a local directory.

 

 





