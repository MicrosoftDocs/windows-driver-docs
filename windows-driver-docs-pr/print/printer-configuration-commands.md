---
title: Printer Configuration Commands
description: Printer Configuration Commands
keywords:
- printer commands WDK Unidrv , configuration
- configuration commands WDK Unidrv
ms.date: 01/30/2023
---

# Printer Configuration Commands

[!include[Print Support Apps](../includes/print-support-apps.md)]

The following table lists the printer configuration commands. All commands are specified using the [command entry format](command-entry-format.md).

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Command</th>
<th>Description</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CmdStartJob</p></td>
<td><p>Command to initialize a print job.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdStartDoc</p></td>
<td><p>Command to initialize a document.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdStartPage</p></td>
<td><p>Command to initialize a page and set the cursor position to (0,0) in cursor coordinates.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdEndPage</p></td>
<td><p>Command to finish printing a page.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdEndDoc</p></td>
<td><p>Command to finish printing a document.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdEndJob</p></td>
<td><p>Command to complete a print job.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="odd">
<td><p>CmdCopies</p></td>
<td><p>Command to specify the number of copies to print.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
<tr class="even">
<td><p>CmdSleepTimeOut</p></td>
<td><p>Command to specify the number of minutes for the printer to wait before entering power-save mode.</p></td>
<td><p>Optional. <a href="command-execution-order.md" data-raw-source="[Command execution order](command-execution-order.md)">Command execution order</a> must be specified.</p></td>
</tr>
</tbody>
</table>

For examples, see the [sample GPD files](sample-gpd-files.md).
