---
title: IPrintCorePS2 COM Interface
author: windows-driver-content
description: IPrintCorePS2 COM Interface
ms.assetid: d5eb6962-2201-405f-9a22-2b11fb6d0360
keywords:
- IPrintCorePS2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IPrintCorePS2 COM Interface


## <a href="" id="ddk-iprintcoreps2-com-interface-gg"></a>


The `IPrintCorePS2` COM interface provides a set of helper methods for Pscript5 render plug-ins. The following table lists and describes all of the methods defined by the `IPrintCorePS2` interface.

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
<td><p>[<strong>IPrintCorePS2::DrvWriteSpoolBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552978)</p></td>
<td><p>Is provided by the Pscript5 driver so that [rendering plug-ins](rendering-plug-ins.md) can send printer data to the spooler.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCorePS2::EnumFeatures</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552990)</p></td>
<td><p>Enumerates a printer's available features.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCorePS2::EnumOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552996)</p></td>
<td><p>Enumerates the available options of a specific feature.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCorePS2::GetFeatureAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553006)</p></td>
<td><p>Retrieves the feature attribute list or the value of a specific feature attribute.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCorePS2::GetGlobalAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553009)</p></td>
<td><p>Retrieves the global attribute list or the value of a specific global attribute.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCorePS2::GetOptionAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553013)</p></td>
<td><p>Retrieves the option attribute list or the value of a specific option attribute.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCorePS2::GetOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553019)</p></td>
<td><p>Retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




