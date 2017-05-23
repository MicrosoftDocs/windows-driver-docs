---
title: .sound\_notify (Use Notification Sound)
description: The .sound\_notify command causes a sound to be played when WinDbg enters the wait-for-command state.
ms.assetid: 72ef33ea-1c75-4add-80eb-a0d824571948
keywords: [".sound_notify (Use Notification Sound) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- .sound_notify (Use Notification Sound)
api_type:
- NA
---

# .sound\_notify (Use Notification Sound)


The **.sound\_notify** command causes a sound to be played when WinDbg enters the wait-for-command state.

``` syntax
.sound_notify /ed 
.sound_notify /ef File 
.sound_notify /d 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________ed______"></span><span id="________ED______"></span> **/ed**   
Causes the default Windows alert sound to be played when WinDbg enters the wait-for-command state.

<span id="________ef_______File______"></span><span id="________ef_______file______"></span><span id="________EF_______FILE______"></span> **/ef** **** *File*   
Causes the sound contained in the specified file to be played when WinDbg enters the wait-for-command state.

<span id="________d"></span><span id="________D"></span> **/d**  
Disables the playing of sounds.

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
<td align="left"><p><strong>Targets</strong></p></td>
<td align="left"><p>all</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.sound_notify%20%28Use%20Notification%20Sound%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




