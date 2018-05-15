---
title: IPrintOemDriverUni COM Interface
author: windows-driver-content
description: IPrintOemDriverUni COM Interface
ms.assetid: 84b3f43c-039a-4e9d-b596-41c08f1e0284
keywords:
- IPrintOemDriverUni
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IPrintOemDriverUni COM Interface





The `IPrintOemDriverUni COM` interface provides a rendering plug-in with access to utility operations supplied by the printer graphics DLL for Unidrv. These operations send a data stream to the print spooler, and obtain driver-managed information.

The following table lists and describes all of the methods defined by the **IPrintOemDriverUni** interface.

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
<td><p>[<strong>IPrintOemDriverUni::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553126)</p></td>
<td><p>Returns the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUni::DrvGetGPDData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553128)</p></td>
<td><p>Enables rendering plug-ins to obtain data defined in a printer's [<em>generic printer description (GPD)</em>](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUni::DrvGetStandardVariable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553129)</p></td>
<td><p>Enables rendering plug-ins to obtain the current value of Unidrv's [standard variables](standard-variables.md).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUni::DrvUniTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553132)</p></td>
<td><p>Enables a rendering plug-in using a device-managed drawing surface to easily output text strings.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUni::DrvWriteAbortBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553135)</p></td>
<td><p>Enables a rendering plug-in to reset a printer after a user has terminated a print job.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUni::DrvWriteSpoolBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553138)</p></td>
<td><p>Sends printer data to the spooler.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUni::DrvXMoveTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553141)</p></td>
<td><p>Notifies Unidrv of cursor x-position changes.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUni::DrvYMoveTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553144)</p></td>
<td><p>Notifies Unidrv of cursor y-position changes.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




