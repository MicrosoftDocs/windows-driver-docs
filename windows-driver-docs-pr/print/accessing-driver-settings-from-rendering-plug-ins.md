---
title: Accessing Driver Settings from Rendering Plug-Ins
author: windows-driver-content
description: Accessing Driver Settings from Rendering Plug-Ins
ms.assetid: d13526f5-85e1-4036-98fb-aea2c6d5a1e3
keywords: ["rendering plug-ins WDK print , accessing driver settings", "status information WDK print plug-ins"]
---

# Accessing Driver Settings from Rendering Plug-Ins


## <a href="" id="ddk-accessing-driver-settings-from-rendering-plug-ins-gg"></a>


A rendering plug-in can obtain the current status of printer features and other internal driver information. The following COM interface methods are implemented within Microsoft's printer drivers and can be called by rendering plug-ins.

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Unidrv rendering plug-ins implement the following methods:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUni::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553126)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IPrintOemDriverUni::DrvGetStandardVariable</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553129)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverUni::DrvGetGPDData</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553128)</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Pscript5 rendering plug-ins implement the following methods:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>IPrintOemDriverPS::DrvGetDriverSetting</strong>](https://msdn.microsoft.com/library/windows/hardware/ff553102)</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Accessing%20Driver%20Settings%20from%20Rendering%20Plug-Ins%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


