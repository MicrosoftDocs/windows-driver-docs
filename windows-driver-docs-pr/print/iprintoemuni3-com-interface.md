---
title: IPrintOemUni3 COM Interface
author: windows-driver-content
description: IPrintOemUni3 COM Interface
ms.assetid: 2b3a43fe-52f8-4cb2-993e-d8fcdc878e90
keywords:
- IPrintOemUni3
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IPrintOemUni3 COM Interface





The `IPrintOemUni3` COM interface contains all the methods of, and extends the capabilities of, the [IPrintOemUni COM Interface](iprintoemuni-com-interface.md) and the [IPrintOemUni2 COM Interface](iprintoemuni2-com-interface.md).

The following table lists and describes all of the methods provided by the `IPrintOemUni3` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IPrintOemUni3::DownloadPattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554201)</p></td>
<td><p>Enables a plug-in to download a pattern to a printer.</p></td>
</tr>
<tr class="even">
<td>[<strong>IPrintOemUni3::GetPDEVAdjustment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554205)</td>
<td><p>Enables a plug-in to override specific [<em>PDEV</em>](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) settings.</p></td>
</tr>
<tr class="odd">
<td>[<strong>IPrintOemUni3::SetBandSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554209)</td>
<td><p>Enables a plug-in to specify the desired band size on the printed output</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




