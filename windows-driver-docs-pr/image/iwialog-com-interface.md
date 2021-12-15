---
title: IWiaLog COM Interface
description: IWiaLog COM Interface
ms.date: 04/20/2017
---

# IWiaLog COM Interface





The [**IWiaLog interface**](/windows-hardware/drivers/ddi/wia_lh/nn-wia_lh-iwialog) is obsolete in Microsoft Windows XP and later and is no longer supported. Use the WIA Diagnostic Log Macros instead.

It is provided for backward compatibility only. The methods in this interface allow a minidriver to write error, trace, and warning messages to a log. The **IWiaLog** interface provides the following methods.

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
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-initializelog" data-raw-source="[&lt;strong&gt;IWiaLog::InitializeLog&lt;/strong&gt;](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-initializelog)"><strong>IWiaLog::InitializeLog</strong></a></p></td>
<td><p>Initializes the logging utility.</p></td>
</tr>
<tr class="even">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-log" data-raw-source="[&lt;strong&gt;IWiaLog::Log&lt;/strong&gt;](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-log)"><strong>IWiaLog::Log</strong></a></p></td>
<td><p>Logs a message to a file or other target.</p></td>
</tr>
<tr class="odd">
<td><p><a href="/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-hresult" data-raw-source="[&lt;strong&gt;IWiaLog::hResult&lt;/strong&gt;](/windows-hardware/drivers/ddi/wia_lh/nf-wia_lh-iwialog-hresult)"><strong>IWiaLog::hResult</strong></a></p></td>
<td><p>Translates an HRESULT into a string.</p></td>
</tr>
</tbody>
</table>

 

For more information about this interface, see [IWiaLog Interface and Diagnostic Log Macros](/windows-hardware/drivers/ddi/_image/index).

