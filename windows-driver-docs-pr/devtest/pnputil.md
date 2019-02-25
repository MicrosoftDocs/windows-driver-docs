---
title: PnPUtil
description: PnPUtil
ms.assetid: 3678fd41-c3ee-4538-b783-6f099ac104a6
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PnPUtil


PnPUtil (PnPUtil.exe) is a command line tool that lets an administrator perform the following actions on [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840):

-   Adds a driver package to the [driver store](https://msdn.microsoft.com/library/windows/hardware/ff544868).

-   Installs a driver package on the computer.

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
<td align="left"><p>PnPUtil (PnPUtil.exe) is included in every version of Windows, starting with Windows Vista (in the %windir%\system32 directory). There isn&#39;t a separate PnPUtil download package.</p>
<ul>
<li>Open a <strong>Command Prompt</strong> window (<strong>Run as administrator</strong>).</li>
<li>Type <strong>pnputil /?</strong> to view command options. See <a href="pnputil-command-syntax.md" data-raw-source="[&lt;strong&gt;PnPUtil Command Syntax&lt;/strong&gt;](pnputil-command-syntax.md)"><strong>PnPUtil Command Syntax</strong></a> for more information.</li>
</ul>
<div class="alert">
<strong>Note</strong>  PnPUtil is supported on Windows Vista and later versions of Windows. PnPUtil is not available for Windows XP, however, you can use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff544838" data-raw-source="[Driver Install Frameworks (DIFx)](https://msdn.microsoft.com/library/windows/hardware/ff544838)">Driver Install Frameworks (DIFx)</a> tools to create and customize the installation of driver packages.
</div>
<div>
 
</div></td>
</tr>
</tbody>
</table>

 

This section includes the following:

[PnPUtil Command Syntax](pnputil-command-syntax.md)

[PnPUtil Examples](pnputil-examples.md)

 

 





