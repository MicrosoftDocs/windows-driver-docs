---
title: IPrintOemDriverUI COM Interface
author: windows-driver-content
description: IPrintOemDriverUI COM Interface
MS-HAID:
- 'custdrvr\_1c50662a-4f79-4978-9e94-8d79783085da.xml'
- 'print.iprintoemdriverui\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: ed11789f-750d-4f29-b5e0-ab299a1388db
keywords: ["IPrintOemDriverUI"]
---

# IPrintOemDriverUI COM Interface


## <a href="" id="ddk-iprintoemdriverui-com-interface-gg"></a>


The `IPrintOemDriverUI` COM interface enables a UI plug-in to view and modify information managed by the [printer interface DLL](printer-interface-dll.md) for Unidrv or Pscript.

The following table lists and describes all the methods that the `IPrintOemDriverUI` interface defines.

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
<td><p>[<strong>IPrintOemDriverUI::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553114)</p></td>
<td><p>Enables a UI plug-in to obtain the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUI::DrvUpdateUISetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553115)</p></td>
<td><p>Enables a UI plug-in to notify the driver of a modified user interface option.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUI::DrvUpgradeRegistrySetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553118)</p></td>
<td><p>Enables a UI plug-in to update device settings stored in the registry.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemDriverUI%20COM%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


