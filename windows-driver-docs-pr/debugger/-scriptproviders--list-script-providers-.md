---
title: .scriptproviders (List Script Providers)
description: The .scriptproviders command lists the active script providers.
ms.assetid: DF2FAA60-422F-4600-9E31-0F8EF127E5A9
keywords: [".scriptproviders (List Script Providers) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .scriptproviders (List Script Providers)
api_type:
- NA
---

# .scriptproviders (List Script Providers)


The **.scriptproviders** command lists the active script providers.

```
    .scriptproviders 
   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______________"></span> ****   
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

```
0:000> .scriptproviders
Available Script Providers:
    NatVis (extension &#39;.NatVis&#39;)
    JavaScript (extension &#39;.js&#39;)
```

**Requirements**

Before using any of the .script commands, a scripting provider needs to be loaded. Use the [**.load (Load Extension DLL)**](-load---loadby--load-extension-dll-.md) command to load the JavaScript provider.

```
0:000> .load jsprovider.dll
```

## <span id="see_also"></span>See also


[JavaScript Debugger Scripting](javascript-debugger-scripting.md)

[**.scriptload (Load Script)**](-scriptload--load-script-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.scriptproviders%20%28List%20Script%20Providers%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





