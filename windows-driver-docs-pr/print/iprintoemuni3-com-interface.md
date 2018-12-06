---
title: IPrintOemUni3 COM Interface
description: IPrintOemUni3 COM Interface
ms.assetid: 2b3a43fe-52f8-4cb2-993e-d8fcdc878e90
keywords:
- IPrintOemUni3
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554201" data-raw-source="[&lt;strong&gt;IPrintOemUni3::DownloadPattern&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554201)"><strong>IPrintOemUni3::DownloadPattern</strong></a></p></td>
<td><p>Enables a plug-in to download a pattern to a printer.</p></td>
</tr>
<tr class="even">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff554205" data-raw-source="[&lt;strong&gt;IPrintOemUni3::GetPDEVAdjustment&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554205)"><strong>IPrintOemUni3::GetPDEVAdjustment</strong></a></td>
<td><p>Enables a plug-in to override specific <a href="https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev" data-raw-source="[&lt;em&gt;PDEV&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev)"><em>PDEV</em></a> settings.</p></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/library/windows/hardware/ff554209" data-raw-source="[&lt;strong&gt;IPrintOemUni3::SetBandSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554209)"><strong>IPrintOemUni3::SetBandSize</strong></a></td>
<td><p>Enables a plug-in to specify the desired band size on the printed output</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




