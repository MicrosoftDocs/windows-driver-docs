---
title: IPrintCoreUI2 COM Interface
author: windows-driver-content
description: IPrintCoreUI2 COM Interface
ms.assetid: 3c9df0ac-d823-4c27-bd34-85765f48b972
keywords:
- IPrintCoreUI2
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# IPrintCoreUI2 COM Interface





The `IPrintCoreUI2` COM interface extends the [IPrintOemDriverUI COM interface](iprintoemdriverui-com-interface.md). In Windows XP and later, Pscript5 driver provides the `IPrintCoreUI2` COM interface. The methods in this interface are for use only by Pscript5 UI plug-ins.

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
<td><p>[<strong>IPrintCoreUI2::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553036)</p></td>
<td><p>Enables a UI plug-in to obtain the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::DrvUpdateUISetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553039)</p></td>
<td><p>Enables a UI plug-in to notify the driver of a modified user interface option.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::DrvUpgradeRegistrySetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553041)</p></td>
<td><p>Enables OEM plug-ins to upgrade private registry settings.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::EnumConstrainedOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553045)</p></td>
<td><p>Determines which options of a feature are constrained.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::EnumFeatures</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553050)</p></td>
<td><p>Enumerates a printer's available features.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::EnumOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553052)</p></td>
<td><p>Enumerates the available options of a specific feature.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::GetFeatureAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553056)</p></td>
<td><p>Retrieves the feature attribute list or the value of a specific feature attribute.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::GetGlobalAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553059)</p></td>
<td><p>Retrieves the global attribute list or the value of a specific global attribute.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::GetOptionAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553064)</p></td>
<td><p>Retrieves the option attribute list or the value of a specific option attribute.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::GetOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553069)</p></td>
<td><p>Retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::QuerySimulationSupport</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553074)</p></td>
<td><p>Retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintCoreUI2::SetOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553081)</p></td>
<td><p>Sets the driver's feature settings.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintCoreUI2::WhyConstrained</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553087)</p></td>
<td><p>Determines why the specified feature/option selection is constrained.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




