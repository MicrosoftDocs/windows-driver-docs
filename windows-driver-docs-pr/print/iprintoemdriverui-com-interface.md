---
title: IPrintOemDriverUI COM Interface
author: windows-driver-content
description: IPrintOemDriverUI COM Interface
ms.assetid: ed11789f-750d-4f29-b5e0-ab299a1388db
keywords:
- IPrintOemDriverUI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPrintOemDriverUI COM Interface





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

 

 




