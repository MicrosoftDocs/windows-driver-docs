---
title: .scriptlist (List Loaded Scripts)
description: The .scriptlist command lists the loaded scripts.
ms.assetid: 98F24BE6-3F34-44E7-9546-3D5AB6D521DD
keywords: [".scriptlist (List Loaded Scripts) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .scriptlist (List Loaded Scripts)
api_type:
- NA
ms.localizationpriority: medium
---

# .scriptlist (List Loaded Scripts)


The **.scriptlist** command lists the loaded scripts.

```dbgcmd
.scriptlist 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______________"></span>    
None

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

The .scriptlist command will list any scripts which have been loaded via the .scriptload command.

If the TestScript was successfully loaded using .scriptload, the .scriptlist command would display the name of the loaded script.

```dbgcmd
0:000> .scriptlist
Command Loaded Scripts:
    JavaScript script from 'C:\WinDbg\Scripts\TestScript.js'
```

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```dbgcmd
0:000> .load jsprovider.dll
```

## <span id="see_also"></span>See also


[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[**.scriptload (Load Script)**](-scriptload--load-script-.md)

 

 






