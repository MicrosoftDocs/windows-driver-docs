---
title: l+, l- (Set Source Options)
description: The l+and l- commands set the source line options that control source display and program stepping options.
ms.assetid: 7b169af0-e799-47eb-b197-c4408a755702
keywords: ["l+, l- (Set Source Options) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- l+, l- (Set Source Options)
api_type:
- NA
---

# l+, l- (Set Source Options)


The **l+**and **l-** commands set the source line options that control source display and program stepping options.

```
l+Option 
l-Option 
l{+|-} 
```

## <span id="ddk_cmd_set_source_options_dbg"></span><span id="DDK_CMD_SET_SOURCE_OPTIONS_DBG"></span>Parameters


<span id="_________or_-"></span><span id="_________OR_-"></span> **+** or **-**  
Specifies whether a given option is to be turned on (plus sign \[+\])or turned off (minus sign \[-\]).

<span id="_______Option______"></span><span id="_______option______"></span><span id="_______OPTION______"></span> *Option*   
One of the following options. The options must be in lowercase letters.

<span id="l"></span><span id="L"></span>**l**  
Displays source line numbers at the command prompt. You can disable source line display through l-ls or .prompt\_allow -src. To make the source line numbers visible, you must enable source line display through both mechanisms.

<span id="o"></span><span id="O"></span>**o**  
Hides all messages (other than the source line and line number) when you are stepping through code. (The **s** option must also be active for the **o** option to have any effect.)

<span id="s"></span><span id="S"></span>**s**  
Displays source lines and source line numbers at the command prompt.

<span id="t"></span><span id="T"></span>**t**  
Starts [source mode](debugging-in-source-mode.md). If this mode is not set, the debugger is in [assembly mode](debugging-in-assembly-mode.md).

<span id="_"></span>**\***  
Turns on or turns off all options.

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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about source debugging and related commands, see [Debugging in Source Mode](debugging-in-source-mode.md). For more information about assembly debugging and related commands, see [Debugging in Assembly Mode](debugging-in-assembly-mode.md).

Remarks
-------

If you omit *Option*, the previously set options are displayed. In this case, the **l+** and **l-** commands have identical effects. However, you must include a plus sign (**+**) or minus sign (-) for the **l** command to work.

You can include only one *Option* every time that you issue this command. If you list more than one option, only the first option is detected. However, by repeatedly issuing this command, you can turn on or off as many options as you want. (In other words, **l+lst** does not work, but **l+l; l+s; l+t** does achieve the effect that you want.)

When you specify the **s** option, source lines and line numbers are displayed when you step through code, regardless of whether you specified the **l** option. The **o** option has no effect unless you specify the **s** option.

Source line options do not take effect unless you enable line number loading by using the [**.lines (Toggle Source Line Support)**](-lines--toggle-source-line-support-.md) command or the [-lines command-line option](command-line-options.md). By default, if you have not used these commands, WinDbg turns on source line support and CDB turns it off.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20l+,%20l-%20%28Set%20Source%20Options%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




