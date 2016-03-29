---
title: IPrintOemDriverUni COM Interface
description: IPrintOemDriverUni COM Interface
ms.assetid: 84b3f43c-039a-4e9d-b596-41c08f1e0284
keywords: ["IPrintOemDriverUni"]
---

# IPrintOemDriverUni COM Interface


## <a href="" id="ddk-iprintoemdriveruni-com-interface-gg"></a>


The `IPrintOemDriverUni COM` interface provides a rendering plug-in with access to utility operations supplied by the printer graphics DLL for Unidrv. These operations send a data stream to the print spooler, and obtain driver-managed information.

The following table lists and describes all of the methods defined by the **IPrintOemDriverUni** interface.

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
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553126)</p></td>
<td align="left"><p>Returns the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvGetGPDData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553128)</p></td>
<td align="left"><p>Enables rendering plug-ins to obtain data defined in a printer's [<em>generic printer description (GPD)</em>](https://msdn.microsoft.com/library/windows/hardware/ff556283#wdkgloss-generic-printer-description--gpd-) file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvGetStandardVariable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553129)</p></td>
<td align="left"><p>Enables rendering plug-ins to obtain the current value of Unidrv's [standard variables](standard-variables.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvUniTextOut</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553132)</p></td>
<td align="left"><p>Enables a rendering plug-in using a device-managed drawing surface to easily output text strings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvWriteAbortBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553135)</p></td>
<td align="left"><p>Enables a rendering plug-in to reset a printer after a user has terminated a print job.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvWriteSpoolBuf</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553138)</p></td>
<td align="left"><p>Sends printer data to the spooler.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvXMoveTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553141)</p></td>
<td align="left"><p>Notifies Unidrv of cursor x-position changes.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>IPrintOemDriverUni::DrvYMoveTo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553144)</p></td>
<td align="left"><p>Notifies Unidrv of cursor y-position changes.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUni%20COM%20Interface%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




