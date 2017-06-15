---
title: Windows kernel routines reserved for system use
author: windows-driver-content
description: Windows kernel routines reserved for system use
MS-HAID:
- 'k104\_ef41454c-f115-4c3a-bb2b-72afd690e887.xml'
- 'kernel.ioacquireremovelockex'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 78b0562a-903a-467d-9bf0-f5499ae47063
---

# Windows kernel routines reserved for system use


The following routines are reserved for system use:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>IoAcquireRemoveLockEx</strong></td>
<td><p>See [<strong>IoAcquireRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548204).</p></td>
</tr>
<tr class="even">
<td><strong>IoInitializeRemoveLockEx</strong></td>
<td><p>Use [<strong>IoInitializeRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549324) instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReleaseRemoveLockAndWaitEx</strong></td>
<td><p>See [<strong>IoReleaseRemoveLockAndWait</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549567).</p></td>
</tr>
<tr class="even">
<td><strong>IoReleaseRemoveLockEx</strong></td>
<td><p>See [<strong>IoReleaseRemoveLock</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549560).</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**IoAcquireRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff548204)  
[**IoInitializeRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549324)  
[**IoReleaseRemoveLock**](https://msdn.microsoft.com/library/windows/hardware/ff549560)  
[**IoReleaseRemoveLockAndWait**](https://msdn.microsoft.com/library/windows/hardware/ff549567)  

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Windows%20kernel%20routines%20reserved%20for%20system%20use%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


