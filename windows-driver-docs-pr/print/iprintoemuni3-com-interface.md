---
title: IPrintOemUni3 COM Interface
description: IPrintOemUni3 COM Interface
ms.assetid: 2b3a43fe-52f8-4cb2-993e-d8fcdc878e90
keywords: ["IPrintOemUni3"]
---

# IPrintOemUni3 COM Interface


## <a href="" id="ddk-iprintoemuni3-com-interface-gg"></a>


The `IPrintOemUni3` COM interface contains all the methods of, and extends the capabilities of, the [IPrintOemUni COM Interface](iprintoemuni-com-interface.md) and the [IPrintOemUni2 COM Interface](iprintoemuni2-com-interface.md).

The following table lists and describes all of the methods provided by the `IPrintOemUni3` interface. Rendering plug-ins must define all listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

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
<td align="left"><p>[<strong>IPrintOemUni3::DownloadPattern</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554201)</p></td>
<td align="left"><p>Enables a plug-in to download a pattern to a printer.</p></td>
</tr>
<tr class="even">
<td align="left">[<strong>IPrintOemUni3::GetPDEVAdjustment</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554205)</td>
<td align="left"><p>Enables a plug-in to override specific [<em>PDEV</em>](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) settings.</p></td>
</tr>
<tr class="odd">
<td align="left">[<strong>IPrintOemUni3::SetBandSize</strong>](https://msdn.microsoft.com/library/windows/hardware/ff554209)</td>
<td align="left"><p>Enables a plug-in to specify the desired band size on the printed output</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemUni3%20COM%20Interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




