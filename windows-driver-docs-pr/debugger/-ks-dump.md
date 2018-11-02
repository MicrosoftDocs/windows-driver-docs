---
title: ks.dump
description: The ks.dump extension displays the specified object.
ms.assetid: 7878c79f-9de6-4fd2-9641-c636212429eb
keywords: ["ks.dump Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ks.dump
api_type:
- NA
ms.localizationpriority: medium
---

# !ks.dump


The **!ks.dump** extension displays the specified object.

```dbgcmd
!ks.dump Object [Level] [Flags]  
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Object______"></span><span id="_______object______"></span><span id="_______OBJECT______"></span> *Object*   
Specifies a pointer to an AVStream structure, an AVStream class object, or a PortCls object. Can also specify a pointer to an IRP or a file object.

<span id="_______Level______"></span><span id="_______level______"></span><span id="_______LEVEL______"></span> *Level*   
Optional. Specifies the level of detail to display on a 0-7 scale with progressively more information displayed for higher values. To display all available details, supply a value of 7. You can see more information about levels by issuing a **!ks.dump** command with no arguments.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. Specifies the kind of information to be displayed. *Flags* can be any combination of the following bits.

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
Display all queued IRPs.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
Display all pending IRPs.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
Analyze a stalled graph for suspects.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
Show all pin states.

### <span id="DLL"></span><span id="dll"></span>DLL

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 2000</strong></p></td>
<td align="left"><p>winxp\Ks.dll</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Windows XP and later</strong></p></td>
<td align="left"><p>Ks.dll</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel Streaming Debugging](kernel-streaming-debugging.md).

Remarks
-------

The **!ks.dump** command recognizes most AVStream objects, including pins, filters, factories, devices, pipes, and stream pointers. This command also recognizes some stream class structures, including stream objects, filter instances, device extensions, and SRBs.

Following is an example of the **!ks.dump** display for a filter:

```dbgcmd
kd> !dump 829493c4
Filter object 829493c4 [CKsFilter = 82949350]
    Descriptor     f7a233c8:
    Context        829dce28
```

Following is an example of the **!ks.dump** display for a pin:

```dbgcmd
kd> !dump 8160DDE0 7
Pin object 8160DDE0 [CKsPin = 8160DD50]
    DeviceState    KSSTATE_RUN
    ClientState    KSSTATE_RUN
    ResetState     KSRESET_END
    CKsPin object 8160DD50 [KSPIN = 8160DDE0]
        State                    KSSTATE_RUN
        Processing Mutex         8160DFD0 is not held
        And Gate &               8160DF88
        And Gate Count           1
```

Some important parts of this display are included in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Parameter</strong></p></td>
<td align="left"><p><strong>Meaning</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>DeviceState</p></td>
<td align="left"><p>The state that the pin was requested to enter. If different from ClientState, this is the state that the minidriver will transition to next.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>ClientState</p></td>
<td align="left"><p>The state that the minidriver is actually in. This reflects the state of the pipe.</p></td>
</tr>
<tr class="even">
<td align="left"><p>ResetState</p></td>
<td align="left"><p>Indicates whether or not the object is in the middle of a flush.</p>
<p>KSRESET_BEGIN indicates a flush.</p>
<p>KSRESET_END indicates no flush.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>State</p></td>
<td align="left"><p>The internal state of the pin&#39;s transport to non-AVStream filters.</p></td>
</tr>
</tbody>
</table>

 

Following is an example of the **!ks.dump** display for a stream class driver:

```dbgcmd
kd> !dump 81a0a170 7
Device Extension 81a0a228:
    Device Object          81a0a170 [\Driver\TESTCAP]
    Next Device Object     81bd56d8 [\Driver\PnpManager]
    Physical Device Object 81bd56d8 [\Driver\PnpManager]
    REGISTRY FLAGS:
        Page out driver when closed
        No suspend if running
    MINIDRIVER Data:
        Device Extension       81a0a44c
        Interrupt Routine      00000000
        Synchronize Routine    STREAM!StreamClassSynchronizeExecution
        Receive Device SRB     testcap!AdapterReceivePacket
        Cancel Packet          testcap!AdapterCancelPacket
        Timeout Packet         testcap!AdapterTimeoutPacket
        Size (d / r / s / f)   1a0(416), 14(20), 978(2424), 0(0)
        Sync Mode              Driver Synchronizes
    Filter Type 0:
        Symbolic Links:
            Information Paged Out
        Instances:
            816b7bd8
```

Note that the sizes are listed both in hexadecimal numbers, and then, parenthetically in the decimal equivalent. The Size abbreviations in this display are listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Size</strong></p></td>
<td align="left"><p><strong>Explanation</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>d</p></td>
<td align="left"><p>Device</p></td>
</tr>
<tr class="odd">
<td align="left"><p>r</p></td>
<td align="left"><p>Request</p></td>
</tr>
<tr class="even">
<td align="left"><p>s</p></td>
<td align="left"><p>Stream</p></td>
</tr>
<tr class="odd">
<td align="left"><p>f</p></td>
<td align="left"><p>Filter. If the filter size is 0, the filter is single instance. If it is greater than 0, it is multi-instance.</p></td>
</tr>
</tbody>
</table>

 

 

 





