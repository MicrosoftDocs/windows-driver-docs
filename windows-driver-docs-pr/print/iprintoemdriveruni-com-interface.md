---
title: IPrintOemDriverUni COM Interface
description: IPrintOemDriverUni COM Interface
ms.assetid: 84b3f43c-039a-4e9d-b596-41c08f1e0284
keywords:
- IPrintOemDriverUni
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553126" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvGetDriverSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553126)"><strong>IPrintOemDriverUni::DrvGetDriverSetting</strong></a></p></td>
<td><p>Returns the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553128" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvGetGPDData&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553128)"><strong>IPrintOemDriverUni::DrvGetGPDData</strong></a></p></td>
<td><p>Enables rendering plug-ins to obtain data defined in a printer&#39;s <a href="https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-" data-raw-source="[&lt;em&gt;generic printer description (GPD)&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-)"><em>generic printer description (GPD)</em></a> file.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553129" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvGetStandardVariable&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553129)"><strong>IPrintOemDriverUni::DrvGetStandardVariable</strong></a></p></td>
<td><p>Enables rendering plug-ins to obtain the current value of Unidrv&#39;s <a href="standard-variables.md" data-raw-source="[standard variables](standard-variables.md)">standard variables</a>.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553132" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvUniTextOut&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553132)"><strong>IPrintOemDriverUni::DrvUniTextOut</strong></a></p></td>
<td><p>Enables a rendering plug-in using a device-managed drawing surface to easily output text strings.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553135" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvWriteAbortBuf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553135)"><strong>IPrintOemDriverUni::DrvWriteAbortBuf</strong></a></p></td>
<td><p>Enables a rendering plug-in to reset a printer after a user has terminated a print job.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553138" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvWriteSpoolBuf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553138)"><strong>IPrintOemDriverUni::DrvWriteSpoolBuf</strong></a></p></td>
<td><p>Sends printer data to the spooler.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553141" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvXMoveTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553141)"><strong>IPrintOemDriverUni::DrvXMoveTo</strong></a></p></td>
<td><p>Notifies Unidrv of cursor x-position changes.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553144" data-raw-source="[&lt;strong&gt;IPrintOemDriverUni::DrvYMoveTo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553144)"><strong>IPrintOemDriverUni::DrvYMoveTo</strong></a></p></td>
<td><p>Notifies Unidrv of cursor y-position changes.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




