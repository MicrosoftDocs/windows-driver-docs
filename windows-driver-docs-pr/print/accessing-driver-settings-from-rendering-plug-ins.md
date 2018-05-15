---
title: Accessing Driver Settings from Rendering Plug-Ins
author: windows-driver-content
description: Accessing Driver Settings from Rendering Plug-Ins
ms.assetid: d13526f5-85e1-4036-98fb-aea2c6d5a1e3
keywords:
- rendering plug-ins WDK print , accessing driver settings
- status information WDK print plug-ins
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Accessing Driver Settings from Rendering Plug-Ins





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

 

 

 




