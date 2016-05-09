---
title: IRP\_MJ\_CLEANUP
description: IRP\_MJ\_CLEANUP
ms.assetid: 5e078575-cbb8-4460-9986-4c546b8c20be
---

# IRP\_MJ\_CLEANUP


The following only applies when a *stream* is being closed.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Request Type</th>
<th align="left">Conditions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Level 1</p>
<p>Batch</p>
<p>Filter</p>
<p>Read-Handle</p>
<p>Read-Write</p>
<p>Read-Write-Handle</p></td>
<td align="left"><ul>
<li><p>Always break to None.</p></li>
<li><p>No acknowledgment is required, the operation proceeds immediately. Note that any I/O operations (IRPs) waiting for an acknowledgment from a pending break request are completed immediately.</p></li>
</ul></td>
</tr>
<tr class="even">
<td align="left"><p>Level 2</p>
<p>Read</p></td>
<td align="left"><ul>
<li><p>Always break to None. Note that other Level 2 or Read oplocks on the same stream are not affected; only the Level 2 or Read oplock associated with this FILE_OBJECT is broken.</p></li>
<li><p>No acknowledgment is required, the operation proceeds immediately.</p></li>
</ul></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20IRP_MJ_CLEANUP%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




