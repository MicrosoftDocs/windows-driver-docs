---
title: rpcexts.rpctime
description: The rpcexts.rpctime extension displays the current system time.
ms.assetid: 72d54357-6b16-4d53-9909-ba201bb33519
keywords: ["rpcexts.rpctime Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- rpcexts.rpctime
api_type:
- NA
---

# !rpcexts.rpctime


The **!rpcexts.rpctime** extension displays the current system time.

```
    !rpcexts.rpctime 
```

## <span id="ddk__rpcexts_rpctime_dbg"></span><span id="DDK__RPCEXTS_RPCTIME_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Rpcexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

This extension can only be used with CDB or with user-mode WinDbg.

Here is an example:

```
0:001> !rpcexts.rpctime
Current time is: 059931.126  (0x00ea1b.07e)
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!rpcexts.rpctime%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




