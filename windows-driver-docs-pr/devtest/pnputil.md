---
title: PnPUtil
description: PnPUtil
ms.assetid: 3678fd41-c3ee-4538-b783-6f099ac104a6
---

# PnPUtil


PnPUtil (PnPUtil.exe) is a command line tool that lets an administrator perform the following actions on [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840):

-   Adds a driver package to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868).

-   Deletes a driver package from the driver store.

-   Enumerates the driver packages that are currently in the driver store. Only driver packages that are not in-box packages are listed. An *in-box* driver package is one which is included in the default installation of Windows or its service packs.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Where can I download PnPUtil?</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the %windir%\system32 directory). There isn't a separate PnPUtil download package.</p>
<ul>
<li>Open a <strong>Command Prompt</strong> window (<strong>Run as administrator</strong>).</li>
<li>Type <strong>pnputil /?</strong> to view command options. See [<strong>PnPUtil Command Syntax</strong>](pnputil-command-syntax.md) for more information.</li>
</ul>
<div class="alert">
<strong>Note</strong>  PnPUtil is supported on Windows Vista and later versions of Windows. PnPUtil is not available for Windows XP, however, you can use the [Driver Install Frameworks (DIFx)](https://msdn.microsoft.com/library/windows/hardware/ff544838) tools to create and customize the installation of driver packages.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

This section includes the following:

[**PnPUtil Command Syntax**](pnputil-command-syntax.md)

[PnPUtil Examples](pnputil-examples.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PnPUtil%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




