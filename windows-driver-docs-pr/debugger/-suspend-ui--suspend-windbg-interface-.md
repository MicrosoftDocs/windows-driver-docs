---
title: .suspend\_ui (Suspend WinDbg Interface)
description: The .suspend\_ui command suspends the refresh of WinDbg debugging information windows.
ms.assetid: 7fa6ca5c-f960-49eb-b6f0-a6f2d454984f
keywords: [".suspend_ui (Suspend WinDbg Interface) Windows Debugging"]
topic_type:
- apiref
api_name:
- .suspend_ui (Suspend WinDbg Interface)
api_type:
- NA
---

# .suspend\_ui (Suspend WinDbg Interface)


The **.suspend\_ui** command suspends the refresh of WinDbg debugging information windows.

``` syntax
.suspend_ui 0 
.suspend_ui 1 
.suspend_ui 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______0______"></span> **0**   
Suspends the refresh of WinDbg debugging information windows.

<span id="_______1______"></span> **1**   
Enables the refresh of WinDbg debugging information windows.

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
<td align="left"><p>kernel mode only</p></td>
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

 

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For information about debugging information windows, see [Using Debugging Information Windows](using-debugging-information-windows.md).

Remarks
-------

Without any parameters, **.suspend\_ui** displays whether debugging information windows are currently suspended.

By default, debugging information windows are refreshed every time the information they display changes.

Suspending the refresh of these windows can speed up WinDbg during a sequence of quick operations -- for example, when tracing or stepping many times in quick succession.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20.suspend_ui%20%28Suspend%20WinDbg%20Interface%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




