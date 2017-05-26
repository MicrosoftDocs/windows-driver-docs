---
title: ah (Assertion Handling)
description: The ah command controls the assertion handling status for specific addresses.
ms.assetid: a55aa34f-c861-45de-bacf-92549ab98fdc
keywords: ["ah (Assertion Handling) Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ah (Assertion Handling)
api_type:
- NA
---

# ah (Assertion Handling)


The **ah** command controls the assertion handling status for specific addresses.

``` syntax
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

The **ah\*** command controls the assertion handling status for a specific address. The [**sx\* asrt**](sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md) command controls the global assertion handling status. If you use **ah\*** for a certain address and then an assert occurs there, the debugger responds based on the **ah\*** settings and ignores the **sx\* asrt** settings.

When the debugger encounters an assertion, the debugger first checks whether handling has been configured for that specific address. If you have not configured the handling, the debugger uses the global setting.

The **ah\*** command affects only the current process. When the current process ends, all status settings are lost.

Assertion handling status affects only STATUS\_ASSERTION\_EXCEPTION exceptions. This handling does not affect the kernel-mode ASSERT routine.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ah%20%28Assertion%20Handling%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




