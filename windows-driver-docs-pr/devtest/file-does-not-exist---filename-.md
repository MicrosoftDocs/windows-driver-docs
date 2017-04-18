---
title: File does not exist filename
description: File does not exist filename
ms.assetid: 21b754db-3043-410d-b3b2-be23fa6b186f
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

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20File%20does%20not%20exist:%20<filename>%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




