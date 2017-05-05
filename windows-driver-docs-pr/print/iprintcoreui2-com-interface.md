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


## <a href="" id="ddk-iprintcoreui2-com-interface-gg"></a>


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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCoreUI2%20COM%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


