---
title: IPrintOemUIMXDC COM Interface
description: IPrintOemUIMXDC COM Interface
keywords:
- IPrintOemUIMXDC
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemUIMXDC COM Interface


The `IPrintOemUIMXDC` COM interface enables an XPS filter-pipeline driver to view and modify information that the [printer interface DLL](printer-interface-dll.md) for printer configuration manages. The XPS driver accesses this COM interface through a [Unidrv or Pscript plug-in](xpsdrv-driver-options.md).

The following table lists and describes all the methods the `IPrintOemUIMXDC` interface defines.

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
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimageablearea" data-raw-source="[&lt;strong&gt;IPrintOEMUIMXDC::AdjustImageableArea&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimageablearea)"><strong>IPrintOEMUIMXDC::AdjustImageableArea</strong></a></p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimagecompression" data-raw-source="[&lt;strong&gt;IPrintOEMUIMXDC::AdjustImageCompression&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustimagecompression)"><strong>IPrintOEMUIMXDC::AdjustImageCompression</strong></a></p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of compression level for JPEG images.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustdpi" data-raw-source="[&lt;strong&gt;IPrintOEMUIMXDC::AdjustDPI&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemuimxdc-adjustdpi)"><strong>IPrintOEMUIMXDC::AdjustDPI</strong></a></p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

