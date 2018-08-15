---
title: IPrintOemDriverPS COM Interface
author: windows-driver-content
description: IPrintOemDriverPS COM Interface
ms.assetid: 32975728-501f-45ac-a53d-34cf286bc433
keywords:
- IPrintOemDriverPS
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# IPrintOemDriverPS COM Interface





The `IPrintOemDriverPS` COM interface provides a rendering plug-in with access to utility operations supplied by the printer graphics DLL for Pscript5. These operations send a data stream to the print spooler and obtain driver-managed information.

The following table lists and describes all of the methods defined by the `IPrintOemDriverPS` interface.

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
<td><p>[<strong>IPrintOemDriverPS::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553102)</p></td>
<td><p>Returns the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverPS::DrvWriteSpoolBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553103)</p></td>
<td><p>Sends printer data to the spooler.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




