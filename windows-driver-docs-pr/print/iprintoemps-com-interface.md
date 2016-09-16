---
title: IPrintOemPS COM Interface
author: windows-driver-content
description: IPrintOemPS COM Interface
MS-HAID:
- 'custdrvr\_99e3e9db-4c3f-4e5f-a1cf-ff1931fef953.xml'
- 'print.iprintoemps\_com\_interface'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 504db6ab-291e-4fba-995d-49a22a3a7c7f
keywords: ["IPrintOemPS"]
---

# IPrintOemPS COM Interface


## <a href="" id="ddk-iprintoemps-com-interface-gg"></a>


The `IPrintOemPS` COM interface is the means by which the [printer graphics DLL](printer-graphics-dll.md) for Pscript5 communicates with a rendering plug-in. The `IPrintOemPS` interface is implemented by each rendering plug-in.

The following table lists and describes all of the methods provided by the `IPrintOemPS` interface. Rendering plug-ins must define all the listed methods. If a method is not needed, it can simply return E\_NOTIMPL.

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
<td><p>[<strong>IPrintOemPS::Command</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553199)</p></td>
<td><p>Allows a rendering plug-in to insert Postscript commands into the print job's data stream.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemPS::DevMode</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553205)</p></td>
<td><p>Performs operations on a rendering plug-in's private [<strong>DEVMODEW</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552837) members.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemPS::DisableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553207)</p></td>
<td><p>Frees resources that were allocated by a rendering plug-in's [<strong>IPrintOemPS::EnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553212) method.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemPS::DisablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553209)</p></td>
<td><p>Allows a rendering plug-in to delete the private PDEV structure that was allocated by its [<strong>IPrintOemPS::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553215) method.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemPS::EnableDriver</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553212)</p></td>
<td><p>Allows a rendering plug-in to hook out some graphics DDI functions. Note that this method and <strong>IPrintOemPS::DisableDriver</strong> must be considered as a pair; if one is implemented, the other must be implemented as well.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemPS::EnablePDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553215)</p></td>
<td><p>Allows a rendering plug-in to create its own PDEV structure.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemPS::GetInfo</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553221)</p></td>
<td><p>(Implementation required.) Returns rendering plug-in identification information.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemPS::PublishDriverInterface</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553228)</p></td>
<td><p>(Implementation required.) Supplies a pointer to the Pscript5 driver's [IPrintOemDriverPS COM interface](iprintoemdriverps-com-interface.md), [IPrintCorePS2 COM interface](iprintcoreps2-com-interface.md), or [IPrintCoreHelperPS interface](https://msdn.microsoft.com/library/windows/hardware/ff552906).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemPS::ResetPDEV</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553233)</p></td>
<td><p>Allows a rendering plug-in to reset its PDEV structure.</p></td>
</tr>
</tbody>
</table>

 

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20IPrintOemPS%20COM%20Interface%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


