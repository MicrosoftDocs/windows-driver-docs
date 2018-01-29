---
title: Time travel debugging extensions
description: This section describes how to use the time travel debugger extension commands.
ms.author: domars
ms.date: 09/22/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---


> [!NOTE]
> The information in this topic is preliminary. Updated information will be provided in a later release of the documentation. 
>


# ![Small time travel logo showing clock](images/ttd-time-travel-debugging-logo.png) Time travel debugging extension commands

This section introduces the time travel debugger extension commands.


## <span id="in_this_section"></span>In this section


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Topic</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>!tt (time travel)</strong>](time-travel-debugging-extension-tt.md)</p></td>
<td align="left"><p>The [<strong>!tt (time travel)</strong>](time-travel-debugging-extension-tt.md) debugger extension that allows you to navigate forward and backwards in time.</p></td>

</tr>
<tr class="even">
<td align="left"><p>[<strong>!position</strong>](time-travel-debugging-extension-positions.md)</p></td>
<td align="left"><p>The [<strong>!positions</strong>](time-travel-debugging-extension-positions.md) extension displays all the active threads, including their current positions in the time travel trace.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>!index</strong>](time-travel-debugging-extension-index.md)</p></td>
<td align="left"><p>The [<strong>!index</strong>](time-travel-debugging-extension-index.md) extension indexes time travel traces or displays index status information.</p></td>
</tr>
</tbody>
</table>

### </span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

### DLL

The time travel debugger extension commands are implemented in ttdext.dll. The time travel command dll is loaded automatically in WinDbg Preview. You don't need to use the load command to manually load the ttdext.dll.
 
## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)

---

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20HID%20Extensions%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





