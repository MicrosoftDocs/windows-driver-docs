---
title: Debugging Still Image Components
author: windows-driver-content
description: Debugging Still Image Components
MS-HAID:
- 'stillimg\_654c9678-e111-49bc-9bae-d3363c0e5a5a.xml'
- 'image.debugging\_still\_image\_components'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 587b8db7-7fca-4b70-8901-3adbde07718f
---

# Debugging Still Image Components


## <a href="" id="ddk-debugging-still-image-components-si"></a>


To aid the debugging of vendor-supplied still image components, the still image event monitor's behavior can be modified with command-line options, using the **Run** option of the **Start** menu. The following options are available:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Command Line Option</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>stimon /h</strong></p></td>
<td><p>Hides the message window.</p></td>
</tr>
<tr class="even">
<td><p><strong>Stimon /r</strong></p></td>
<td><p>Refreshes the event monitor's device list.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Stimon /t</strong><em>number</em></p></td>
<td><p>Modifies the polling interval to the number of seconds specified by <em>number</em>. Typically used for increasing the polling interval.</p></td>
</tr>
<tr class="even">
<td><p><strong>Stimon /v</strong></p></td>
<td><p>Makes a window visible that displays event monitor messages.</p></td>
</tr>
</tbody>
</table>

 

The event monitor can be stopped and started by using the Windows 2000 and later Computer Management window. The event monitor is listed as the "Still Image Service".

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Debugging%20Still%20Image%20Components%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


