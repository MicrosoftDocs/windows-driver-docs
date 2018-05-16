---
title: DVD Related Clock Functions
author: windows-driver-content
description: DVD Related Clock Functions
ms.assetid: 495f25dc-cd79-4f7f-acbc-b8b271269fb3
keywords:
- DVD decoder minidrivers WDK , master clock
- decoder minidrivers WDK DVD , master clock
- master clocks WDK DVD decoder
- clocks WDK DVD decoder
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DVD Related Clock Functions





All clock handles should be stored with the appropriate individual streams. They should not be stored globally or in a static variable. For more information, see [KS Clocks](ks-clocks.md).

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>SRB_OPEN_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568190)</p></td>
<td><p>Indicates to the DVD decoder minidriver that the specified stream is being opened as a master clock, and provides a master clock handle to be used on all calls into the DVD decoder minidriver master clock routine for access to that clock.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SRB_CLOSE_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568163)</p></td>
<td><p>Indicates the specified master clock handle is no longer active.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SRB_INDICATE_MASTER_CLOCK</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568179)</p></td>
<td><p>Indicates the handle to be used when calling for time stamps and is provided to all streams.</p></td>
</tr>
</tbody>
</table>

 

 

 




