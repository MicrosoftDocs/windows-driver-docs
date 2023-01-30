---
title: IPrintOemDriverUI COM Interface
description: IPrintOemDriverUI COM Interface
keywords:
- IPrintOemDriverUI
ms.date: 01/27/2023
---

# IPrintOemDriverUI COM Interface

[!include[Print Support Apps](../includes/print-support-apps.md)]

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
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvgetdriversetting" data-raw-source="[&lt;strong&gt;IPrintOemDriverUI::DrvGetDriverSetting&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvgetdriversetting)"><strong>IPrintOemDriverUI::DrvGetDriverSetting</strong></a></p></td>
<td><p>Enables a UI plug-in to obtain the current status of printer features and other internal information.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupdateuisetting" data-raw-source="[&lt;strong&gt;IPrintOemDriverUI::DrvUpdateUISetting&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupdateuisetting)"><strong>IPrintOemDriverUI::DrvUpdateUISetting</strong></a></p></td>
<td><p>Enables a UI plug-in to notify the driver of a modified user interface option.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupgraderegistrysetting" data-raw-source="[&lt;strong&gt;IPrintOemDriverUI::DrvUpgradeRegistrySetting&lt;/strong&gt;](/windows-hardware/drivers/ddi/prcomoem/nf-prcomoem-iprintoemdriverui-drvupgraderegistrysetting)"><strong>IPrintOemDriverUI::DrvUpgradeRegistrySetting</strong></a></p></td>
<td><p>Enables a UI plug-in to update device settings stored in the registry.</p></td>
</tr>
</tbody>
</table>

For more information, see [Implementing Printer Driver COM Interfaces](implementing-printer-driver-com-interfaces.md).
