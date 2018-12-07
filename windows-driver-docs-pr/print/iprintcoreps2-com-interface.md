---
title: IPrintCorePS2 COM Interface
description: IPrintCorePS2 COM Interface
ms.assetid: d5eb6962-2201-405f-9a22-2b11fb6d0360
keywords:
- IPrintCorePS2
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintCorePS2 COM Interface





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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552978" data-raw-source="[&lt;strong&gt;IPrintCorePS2::DrvWriteSpoolBuf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552978)"><strong>IPrintCorePS2::DrvWriteSpoolBuf</strong></a></p></td>
<td><p>Is provided by the Pscript5 driver so that <a href="rendering-plug-ins.md" data-raw-source="[rendering plug-ins](rendering-plug-ins.md)">rendering plug-ins</a> can send printer data to the spooler.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552990" data-raw-source="[&lt;strong&gt;IPrintCorePS2::EnumFeatures&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552990)"><strong>IPrintCorePS2::EnumFeatures</strong></a></p></td>
<td><p>Enumerates a printer&#39;s available features.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552996" data-raw-source="[&lt;strong&gt;IPrintCorePS2::EnumOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552996)"><strong>IPrintCorePS2::EnumOptions</strong></a></p></td>
<td><p>Enumerates the available options of a specific feature.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553006" data-raw-source="[&lt;strong&gt;IPrintCorePS2::GetFeatureAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553006)"><strong>IPrintCorePS2::GetFeatureAttribute</strong></a></p></td>
<td><p>Retrieves the feature attribute list or the value of a specific feature attribute.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553009" data-raw-source="[&lt;strong&gt;IPrintCorePS2::GetGlobalAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553009)"><strong>IPrintCorePS2::GetGlobalAttribute</strong></a></p></td>
<td><p>Retrieves the global attribute list or the value of a specific global attribute.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553013" data-raw-source="[&lt;strong&gt;IPrintCorePS2::GetOptionAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553013)"><strong>IPrintCorePS2::GetOptionAttribute</strong></a></p></td>
<td><p>Retrieves the option attribute list or the value of a specific option attribute.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553019" data-raw-source="[&lt;strong&gt;IPrintCorePS2::GetOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553019)"><strong>IPrintCorePS2::GetOptions</strong></a></p></td>
<td><p>Retrieves the driver&#39;s current feature settings in the format of a list of feature/option keyword pairs.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




