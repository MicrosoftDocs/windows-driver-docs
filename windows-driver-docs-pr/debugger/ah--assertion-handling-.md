---
title: ah (Assertion Handling)
description: The ah command controls the assertion handling status for specific addresses.
ms.assetid: a55aa34f-c861-45de-bacf-92549ab98fdc
keywords: ["ah (Assertion Handling) Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ah (Assertion Handling)
api_type:
- NA
ms.localizationpriority: medium
---

# ah (Assertion Handling)


The **ah** command controls the assertion handling status for specific addresses.

```dbgcmd
ahb [Address] 
ahi [Address] 
ahd [Address] 
ahc 
ah 
```

## <span id="ddk_cmd_assertion_handling_dbg"></span><span id="DDK_CMD_ASSERTION_HANDLING_DBG"></span>Parameters


<span id="_______ahb______"></span><span id="_______AHB______"></span> **ahb**   
Breaks into the debugger if an assertion fails at the specified address.

<span id="_______ahi"></span><span id="_______AHI"></span> **ahi**  
Ignores an assertion failure at the specified address.

<span id="_______ahd______"></span><span id="_______AHD______"></span> **ahd**   
Deletes any assertion-handling information at the specified address. This deletion causes the debugger to return to its default state for that address.

<span id="_______Address______"></span><span id="_______address______"></span><span id="_______ADDRESS______"></span> *Address*   
Specifies the address of the instruction whose assertion-handling status is being set. If you omit this parameter, the debugger uses the current program counter.

<span id="_______ahc"></span><span id="_______AHC"></span> **ahc**  
Deletes all assertion-handling information for the current process.

<span id="_______ah______"></span><span id="_______AH______"></span> **ah**   
Displays the current assertion-handling settings.

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
<td align="left"><p>Live debugging only</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Platforms</strong></p></td>
<td align="left"><p>All</p></td>
</tr>
</tbody>
</table>

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about break status and handling status, descriptions of all event codes, a list of the default status for all events, and details about other methods of controlling this status, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

Remarks
-------

The **ah\\*** command controls the assertion handling status for a specific address. The [**sx\* asrt**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command controls the global assertion handling status. If you use **ah\\*** for a certain address and then an assert occurs there, the debugger responds based on the **ah\\*** settings and ignores the **sx\* asrt** settings.

When the debugger encounters an assertion, the debugger first checks whether handling has been configured for that specific address. If you have not configured the handling, the debugger uses the global setting.

The **ah\\*** command affects only the current process. When the current process ends, all status settings are lost.

Assertion handling status affects only STATUS\_ASSERTION\_EXCEPTION exceptions. This handling does not affect the kernel-mode ASSERT routine.

 

 





