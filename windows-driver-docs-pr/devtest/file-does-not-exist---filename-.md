---
title: File does not exist filename
description: File does not exist filename
ms.assetid: 21b754db-3043-410d-b3b2-be23fa6b186f
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File does not exist: &lt;filename&gt;


SDV reports this error in the **Compile** step when it cannot create a required file. The method for resolving this error depends on which file SDV cannot find.

The following table lists the files that are reported with this error, a description of the file, and how to resolve this error.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">File Name</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>check_sdv.xml</p>
<p>driver_sdv.xml</p></td>
<td align="left"><p>SDV creates these files when it verifies a driver (in the Check step.) It requires these files when it creates the Static Driver Verifier Report.</p>
<p>If you have deleted files from the SDV directories in the driver's sources directory, rerun the verification to recreate the files.</p>
<p>If you have not deleted any files, this error indicates an internal error in SDV. To resolve this error, uninstall and reinstall SDV.</p></td>
</tr>
<tr class="even">
<td align="left"><p>sdv-default.xml</p></td>
<td align="left"><p>This file is installed in the \tools\data\WDM subdirectory of the WDK.</p>
<p>You can edit and copy the file, but you cannot move, rename, or delete it.</p>
<p>For more information about this file, see [Static Driver Verifier Options File](static-driver-verifier-options-file.md).</p></td>
</tr>
</tbody>
</table>

 

 

 





