---
title: logexts.logo
description: The logexts.logo extension sets or displays the Logger output options.
ms.assetid: b094cf4b-1d01-4b84-9032-aa865d680df4
keywords: ["logexts.logo Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- logexts.logo
api_type:
- NA
---

# !logexts.logo


The **!logexts.logo** extension sets or displays the Logger output options.

```
!logexts.logo {e|d} {d|t|v} 
!logexts.logo 
```

## <span id="ddk__logexts_logo_dbg"></span><span id="DDK__LOGEXTS_LOGO_DBG"></span>Parameters


<span id="_______e_d"></span><span id="_______E_D"></span> **e|d**  
Specifies whether to enable (e) or disable (d) the indicated output type.

<span id="_______d_t_v"></span><span id="_______D_T_V"></span> **d|t|v**  
Specifies the output type. Three types of Logger output are possible: messages sent directly to the debugger (d), a text file (t), or a verbose .lgv file (v).

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Logexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Logger and LogViewer](logger-and-logviewer.md).

Remarks
-------

If **!logexts.logo** is used without any parameters, then the current logging status, the output directory, and the current settings for the debugger, text file, and verbose log are displayed:

```
0:000> !logo
Logging currently enabled.

Output directory: MyLogs\LogExts\

Output settings:
  Debugger            Disabled
  Text file           Enabled
  Verbose log         Enabled
```

In the previous example, the output directory is a relative path, so it is located relative to the directory in which the debuggers were started.

To disable verbose logging, you would use the following command:

```
0:000> !logo d v
  Debugger            Disabled
  Text file           Enabled
  Verbose log         Disabled
```

Text file and .lgv files will be placed in the current output directory. To read an .lgv file, use LogViewer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!logexts.logo%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




