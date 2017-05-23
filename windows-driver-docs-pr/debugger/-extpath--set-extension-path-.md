---
title: .extpath (Set Extension Path)
description: The .extpath command sets or displays the extension DLL search path.
ms.assetid: 957028ff-d8f4-41ab-bdaa-ff1bbe886bec
keywords: [".extpath (Set Extension Path) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .extpath (Set Extension Path)
api_type:
- NA
---

# .extpath (Set Extension Path)


The **.extpath** command sets or displays the extension DLL search path.

``` syntax
.extpath[+] [Directory[;...]]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="______________"></span> +   
Signifies that the debugger should append new directories to the previous extension DLL search path (instead of replacing the path).

<span id="_______Directory______"></span><span id="_______directory______"></span><span id="_______DIRECTORY______"></span> *Directory*   
Specifies one or more directories to put in the search path. If you do not specify *Directory*, the current path is displayed. You can separate multiple directories with semicolons.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Modes</p></td>
<td align="left"><p>User mode, kernel mode</p></td>
</tr>
<tr class="even">
<td align="left"><p>Targets</p></td>
<td align="left"><p>Live, crash dump</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Platforms</p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the extension search path and loading extension DLLs, see [Loading Debugger Extension DLLs](loading-debugger-extension-dlls.md).

Remarks
-------

The extension DLL search path is reset to its default value at the start of each debugging session.

During live kernel-mode debugging, a reboot of the target computer results in the start of a new debugging session. So any changes that you make to the extension DLL search path during kernel-mode debugging will not persist across a reboot of the target computer.

The default value of the extension DLL search path contains all the extension paths known to the debugger and all the paths in the %PATH% environment variable. For example, suppose your %PATH% environment variable has a value of `C:\Windows\system32;C:\Windows`. Then the default value of the DLL extension search path might look like this.

``` syntax
0:000> .extpath
Extension search path is: C:\Program Files\Debugging Tools for Windows (x64)\WINXP;C:\Program Files\
Debugging Tools for Windows (x64)\winext;C:\Program Files\Debugging Tools for Windows (x64)\winext\
arcade;C:\Program Files\Debugging Tools for Windows (x64);C:\Program Files\Debugging Tools for 
Windows (x64)\winext\arcade;C:\Windows\system32;C:\Windows
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.extpath%20%28Set%20Extension%20Path%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




