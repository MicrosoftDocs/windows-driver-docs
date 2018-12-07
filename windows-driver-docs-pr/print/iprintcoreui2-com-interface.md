---
title: IPrintCoreUI2 COM Interface
description: IPrintCoreUI2 COM Interface
ms.assetid: 3c9df0ac-d823-4c27-bd34-85765f48b972
keywords:
- IPrintCoreUI2
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553036" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::DrvGetDriverSetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553036)"><strong>IPrintCoreUI2::DrvGetDriverSetting</strong></a></p></td>
<td><p>Enables a UI plug-in to obtain the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553039" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::DrvUpdateUISetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553039)"><strong>IPrintCoreUI2::DrvUpdateUISetting</strong></a></p></td>
<td><p>Enables a UI plug-in to notify the driver of a modified user interface option.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553041" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::DrvUpgradeRegistrySetting&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553041)"><strong>IPrintCoreUI2::DrvUpgradeRegistrySetting</strong></a></p></td>
<td><p>Enables OEM plug-ins to upgrade private registry settings.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553045" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::EnumConstrainedOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553045)"><strong>IPrintCoreUI2::EnumConstrainedOptions</strong></a></p></td>
<td><p>Determines which options of a feature are constrained.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553050" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::EnumFeatures&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553050)"><strong>IPrintCoreUI2::EnumFeatures</strong></a></p></td>
<td><p>Enumerates a printer&#39;s available features.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553052" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::EnumOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553052)"><strong>IPrintCoreUI2::EnumOptions</strong></a></p></td>
<td><p>Enumerates the available options of a specific feature.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553056" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::GetFeatureAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553056)"><strong>IPrintCoreUI2::GetFeatureAttribute</strong></a></p></td>
<td><p>Retrieves the feature attribute list or the value of a specific feature attribute.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553059" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::GetGlobalAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553059)"><strong>IPrintCoreUI2::GetGlobalAttribute</strong></a></p></td>
<td><p>Retrieves the global attribute list or the value of a specific global attribute.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553064" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::GetOptionAttribute&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553064)"><strong>IPrintCoreUI2::GetOptionAttribute</strong></a></p></td>
<td><p>Retrieves the option attribute list or the value of a specific option attribute.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553069" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::GetOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553069)"><strong>IPrintCoreUI2::GetOptions</strong></a></p></td>
<td><p>Retrieves the driver&#39;s current feature settings in the format of a list of feature/option keyword pairs.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553074" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::QuerySimulationSupport&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553074)"><strong>IPrintCoreUI2::QuerySimulationSupport</strong></a></p></td>
<td><p>Retrieves a spooler simulation capability structure, which indicates the kinds of simulation the spooler supports.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553081" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::SetOptions&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553081)"><strong>IPrintCoreUI2::SetOptions</strong></a></p></td>
<td><p>Sets the driver&#39;s feature settings.</p></td>
</tr>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff553087" data-raw-source="[&lt;strong&gt;IPrintCoreUI2::WhyConstrained&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff553087)"><strong>IPrintCoreUI2::WhyConstrained</strong></a></p></td>
<td><p>Determines why the specified feature/option selection is constrained.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 




