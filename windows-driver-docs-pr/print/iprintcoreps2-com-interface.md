---
title: IPrintCorePS2 COM Interface
description: IPrintCorePS2 COM Interface
ms.assetid: d5eb6962-2201-405f-9a22-2b11fb6d0360
keywords: ["IPrintCorePS2"]
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
<th align="left">Method</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>[<strong>IPrintCorePS2::DrvWriteSpoolBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552978)</p></td>
<td align="left"><p>Is provided by the Pscript5 driver so that [rendering plug-ins](rendering-plug-ins.md) can send printer data to the spooler.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintCorePS2::EnumFeatures</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552990)</p></td>
<td align="left"><p>Enumerates a printer's available features.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintCorePS2::EnumOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552996)</p></td>
<td align="left"><p>Enumerates the available options of a specific feature.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintCorePS2::GetFeatureAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553006)</p></td>
<td align="left"><p>Retrieves the feature attribute list or the value of a specific feature attribute.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintCorePS2::GetGlobalAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553009)</p></td>
<td align="left"><p>Retrieves the global attribute list or the value of a specific global attribute.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintCorePS2::GetOptionAttribute</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553013)</p></td>
<td align="left"><p>Retrieves the option attribute list or the value of a specific option attribute.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintCorePS2::GetOptions</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553019)</p></td>
<td align="left"><p>Retrieves the driver's current feature settings in the format of a list of feature/option keyword pairs.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintCorePS2%20COM%20Interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




