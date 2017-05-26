---
title: IPrintOemUIMXDC COM Interface
author: windows-driver-content
description: IPrintOemUIMXDC COM Interface
ms.assetid: db6d575e-31d0-4a26-8cf9-5188935610e5
keywords:
- IPrintOemUIMXDC
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>IPrintOEMUIMXDC::AdjustImageableArea</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554151)</p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of the printable area, including orientation and direction of rotation.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOEMUIMXDC::AdjustImageCompression</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554153)</p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of compression level for JPEG images.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOEMUIMXDC::AdjustDPI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554147)</p></td>
<td><p>Enables an XPS filter pipeline driver to use UnidrvUI.dll or PS5UI.dll to support configuration of image resolution.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUIMXDC%20COM%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


