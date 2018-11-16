---
title: IPrintOemUI2 COM Interface
description: IPrintOemUI2 COM Interface
ms.assetid: 9aee61af-e8e2-4bc4-a17b-783242d1ac1f
keywords:
- IPrintOemUI2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemUI2 COM Interface





The `IPrintOemUI2` COM interface extends the [IPrintOemUI COM interface](iprintoemui-com-interface.md). In addition to all the methods in the **IPrintOemUI** interface, the `IPrintOemUI2` interface provides the following methods.

**Note**  If you are using the Windows Vista version of the Unidrv and Pscript DLLs, you can implement the following methods in Unidrv or Pscript5 plug-ins that run on Windows XP and later versions of Windows operating systems. Previous versions of the DLLs support the **IPrintOEM2::HideStandardUI** method in Pscript5 plug-ins only.

 

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554141" data-raw-source="[&lt;strong&gt;IPrintOemUI2::DocumentEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554141)"><strong>IPrintOemUI2::DocumentEvent</strong></a></p></td>
<td><p>Enables a UI plug-in to replace the core driver UI module&#39;s default implementation of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548544" data-raw-source="[&lt;strong&gt;DrvDocumentEvent&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548544)"><strong>DrvDocumentEvent</strong></a> DDI.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554142" data-raw-source="[&lt;strong&gt;IPrintOemUI2::HideStandardUI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554142)"><strong>IPrintOemUI2::HideStandardUI</strong></a></p></td>
<td><p>Enables a UI plug-in to specify whether the standard property sheets should be displayed or hidden.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff554146" data-raw-source="[&lt;strong&gt;IPrintOemUI2::QueryJobAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff554146)"><strong>IPrintOemUI2::QueryJobAttributes</strong></a></p></td>
<td><p>Enables a UI plug-in to post-process the core driver&#39;s results after a call to the <a href="https://msdn.microsoft.com/library/windows/hardware/ff548581" data-raw-source="[&lt;strong&gt;DrvQueryJobAttributes&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff548581)"><strong>DrvQueryJobAttributes</strong></a> DDI.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




