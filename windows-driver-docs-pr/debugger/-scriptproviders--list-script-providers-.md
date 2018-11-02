---
title: .scriptproviders (List Script Providers)
description: The .scriptproviders command lists the active script providers.
ms.assetid: DF2FAA60-422F-4600-9E31-0F8EF127E5A9
keywords: [".scriptproviders (List Script Providers) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- .scriptproviders (List Script Providers)
api_type:
- NA
ms.localizationpriority: medium
---

# .scriptproviders (List Script Providers)


The **.scriptproviders** command lists the active script providers.

```dbgcmd
.scriptproviders 
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

The .scriptproviders command will list all the script languages which are presently understood by the debugger and the extension under which they are registered. Any file ending in ".NatVis" is understood as a NatVis script and any file ending in ".js" is understood as a JavaScript script. Either type of script can be loaded with the .scriptload command.

In the example below, the JavaScript and NatVis providers are loaded.

```dbgcmd
0:000> .scriptproviders
Available Script Providers:
    NatVis (extension '.NatVis')
    JavaScript (extension '.js')
```

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```dbgcmd
0:000> .load jsprovider.dll
```

## <span id="see_also"></span>See also


[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[**.scriptload (Load Script)**](-scriptload--load-script-.md)

 

 






