---
title: timer
description: The timer extension displays a detailed listing of all system timer use.
ms.assetid: 795bdfe1-1ee4-4bf2-9fcd-80415fe84754
keywords: ["timer Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- timer
api_type:
- NA
---

# !timer


The **!timer** extension displays a detailed listing of all system timer use.

```
    !timer 
```

## <span id="ddk__timer_dbg"></span><span id="DDK__TIMER_DBG"></span>


### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>Kdextx86.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about timer objects, see the Windows Driver Kit (WDK) documentation.

Remarks
-------

The **!timer** extension displays the timer tree, which stores all timer objects in the system.

Here is an example:

```
kd> !timer
Dump system timers

Interrupt time: 9f760774 00000000 [12/ 8/2000 10:59:22.685 (Pacific Standard Time)]

List Timer    Interrupt Low/High     Fire Time              DPC/thread
 0 8016aea0 P 9fbd8e00 00000000 [12/ 8/2000 10:59:23.154]  ntoskrnl!PopScanIdleList 
  1 8257f118   e4e4225a 00000000 [12/ 8/2000 11:01:19.170]  thread 8257f030 
 3 80165fc0   286be1c9 0000594a [ 4/ 1/2001 01:59:59.215]  ntoskrnl!ExpTimeZoneDpcRoutine 
    80165f40   2a7bf8d9 006f105e [12/31/2099 23:59:59.216]  ntoskrnl!ExpCenturyDpcRoutine 
  5 825a0bf8   a952e1c2 00000000 [12/ 8/2000 10:59:39.232]  thread 825a0b10 
 10 8251c7a8   41f54d84 00000001 [12/ 8/2000 11:03:55.310]  thread 8251c6c0 
    8249fe88   41f54d84 00000001 [12/ 8/2000 11:03:55.310]  thread 8249fda0 
 11 8250e7e8   bc73ffde 00000000 [12/ 8/2000 11:00:11.326]  thread 8250e700 

.....

237 82757070   9f904152 00000000 [12/ 8/2000 10:59:22.857]  +f7a56f2e 
    82676348   9f904152 00000000 [12/ 8/2000 10:59:22.857]  +fe516352 
    82728b78   9f904152 00000000 [12/ 8/2000 10:59:22.857]  +fe516352 
238 fe4b5d78   9f92a3ac 00000000 [12/ 8/2000 10:59:22.873]  thread 827ceb10 
    801658f0   9f92a3ac 00000000 [12/ 8/2000 10:59:22.873]  ntoskrnl!CcScanDpc 
239 8259ad40   765a6f19 00000bba [12/23/2000 09:07:22.900]  thread 825d3670 
250 826d42f0   1486bed8 80000000 [         NEVER         ]  thread 825fa030 

Total Timers: 193, Maximum List: 7
Current Hand: 226, Maximum Search: 0

Wakeable timers:
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!timer%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




