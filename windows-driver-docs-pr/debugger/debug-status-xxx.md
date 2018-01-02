---
title: DEBUG\_STATUS\_XXX
description: DEBUG\_STATUS\_XXX
ms.assetid: 3f5fcdb6-b4fc-4155-bf39-929d00fb210c
ms.author: windowsdriverdev
ms.date: 12/07/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["DEBUG_STATUS_XXX Windows Debugging"]
topic_type:
- apiref
api_name:
- DEBUG_STATUS_XXX
api_location:
- DbgEng.h
api_type:
- HeaderDef
---

# DEBUG\_STATUS\_XXX


## <span id="ddk_debug_status_xxx_dbx"></span><span id="DDK_DEBUG_STATUS_XXX_DBX"></span>


The DEBUG\_STATUS\_*XXX* status codes have two purposes. They instruct the engine on how execution in the target should proceed, and they are used by the engine to report the execution status of the target.

After an event occurs, the engine can receive several instructions that tell it how execution in the target should proceed. In this case, it acts on the instruction with the highest precedence. Typically, the higher precedence status codes represent less execution for the target.

The values in the following table are reverse ordered by precedence; the values that appear earlier in the table have higher precedence.

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Status Code</th>
<th align="left">When reporting</th>
<th align="left">When instructing</th>
<th align="left">Precedence</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_NO_DEBUGGEE</p></td>
<td align="left"><p>No debugging session is active.</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_OUT_OF_SYNC</p></td>
<td align="left"><p>The debugger communications channel is out of sync.</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_WAIT_INPUT</p></td>
<td align="left"><p>The target is awaiting input from the user.</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_TIMEOUT</p></td>
<td align="left"><p>The debugger communications channel has timed out.</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_BREAK</p></td>
<td align="left"><p>The target is suspended.</p></td>
<td align="left"><p>Suspend the target.</p></td>
<td align="left"><p>Highest precedence</p></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_STEP_INTO</p></td>
<td align="left"><p>The target is executing a single instruction.</p></td>
<td align="left"><p>Continue execution of the target for a single instruction.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_STEP_BRANCH</p></td>
<td align="left"><p>The target is executing until the next branch instruction.</p></td>
<td align="left"><p>Continue execution of the target until the next branch instruction.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_STEP_OVER</p></td>
<td align="left"><p>The target is executing a single instruction or--if that instruction is a subroutine call--subroutine.</p></td>
<td align="left"><p>Continue execution of the target for a single instruction. If the instruction is a subroutine call, the call is entered and the target is allowed to run until the subroutine returns.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_GO_NOT_HANDLED</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>Continue execution of the target, flagging the event as not handled.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_GO_HANDLED</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>Continue execution of the target, flagging the event as handled.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_GO</p></td>
<td align="left"><p>The target is executing normally.</p></td>
<td align="left"><p>Continue normal execution of the target.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_IGNORE_EVENT</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>Continue previous execution of the target, ignoring the event.</p></td>
<td align="left"></td>
</tr>
<tr class="odd">
<td align="left"><p>DEBUG_STATUS_RESTART_REQUESTED</p></td>
<td align="left"><p>The target is restarting.</p></td>
<td align="left"><p>Restart the target.</p></td>
<td align="left"></td>
</tr>
<tr class="even">
<td align="left"><p>DEBUG_STATUS_NO_CHANGE</p></td>
<td align="left"><p>N/A</p></td>
<td align="left"><p>No instruction. This value is returned by an event callback method when it does not wish to instruct the engine how to proceed with execution in the target.</p></td>
<td align="left"><p>Lowest precedence</p></td>
</tr>
</tbody>
</table>

 

&gt; \[!Note\]
&gt;   The precedence of the status codes does not follow the numeric values of the constants.

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">DbgEng.h (include DbgEng.h)</td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20DEBUG_STATUS_XXX%20%20RELEASE:%20%2811/30/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




