---
title: .scroll_prefs (Control Source Scrolling Preferences)
description: The .scroll_prefs command controls the positioning of the source in a Source window when scrolling to a line.
ms.assetid: 08978751-c4b7-491a-9e1f-de21d74a10a8
keywords: [".scroll_prefs (Control Source Scrolling Preferences) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .scroll_prefs (Control Source Scrolling Preferences)
api_type:
- NA
---

# .scroll\_prefs (Control Source Scrolling Preferences)


The **.scroll\_prefs** command controls the positioning of the source in a Source window when scrolling to a line.

```
.scroll_prefs Before After 
.scroll_prefs 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Before______"></span><span id="_______before______"></span><span id="_______BEFORE______"></span> *Before*   
Specifies how many source lines before the line you are scrolling to should be visible in the Source window.

<span id="_______After______"></span><span id="_______after______"></span><span id="_______AFTER______"></span> *After*   
Specifies how many source lines after the line you are scrolling to should be visible in the Source window.

### <span id="Environment"></span><span id="environment"></span><span id="ENVIRONMENT"></span>Environment

This command is available only in WinDbg and cannot be used in script files.

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

When this command is used with no parameters, the current source scrolling preferences are displayed.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.scroll_prefs%20%28Control%20Source%20Scrolling%20Preferences%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




