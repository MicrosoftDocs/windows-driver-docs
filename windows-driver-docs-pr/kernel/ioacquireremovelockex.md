---
title: Windows kernel routines reserved for system use
description: Windows kernel routines reserved for system use
ms.localizationpriority: medium
ms.date: 10/17/2018
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
<td><p>See <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock" data-raw-source="[&lt;strong&gt;IoAcquireRemoveLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)"><strong>IoAcquireRemoveLock</strong></a>.</p></td>
</tr>
<tr class="even">
<td><strong>IoInitializeRemoveLockEx</strong></td>
<td><p>Use <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeremovelock" data-raw-source="[&lt;strong&gt;IoInitializeRemoveLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeremovelock)"><strong>IoInitializeRemoveLock</strong></a> instead.</p></td>
</tr>
<tr class="odd">
<td><strong>IoReleaseRemoveLockAndWaitEx</strong></td>
<td><p>See <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait" data-raw-source="[&lt;strong&gt;IoReleaseRemoveLockAndWait&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait)"><strong>IoReleaseRemoveLockAndWait</strong></a>.</p></td>
</tr>
<tr class="even">
<td><strong>IoReleaseRemoveLockEx</strong></td>
<td><p>See <a href="/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock" data-raw-source="[&lt;strong&gt;IoReleaseRemoveLock&lt;/strong&gt;](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock)"><strong>IoReleaseRemoveLock</strong></a>.</p></td>
</tr>
</tbody>
</table>

 

## Related topics
[**IoAcquireRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioacquireremovelock)  
[**IoInitializeRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializeremovelock)  
[**IoReleaseRemoveLock**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelock)  
[**IoReleaseRemoveLockAndWait**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioreleaseremovelockandwait)
