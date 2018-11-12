---
title: Default Queue Callback Routine Functions
description: Default Queue Callback Routine Functions
ms.assetid: 46d767ed-cfeb-4bd0-8792-08781a1335d6
keywords:
- SetupAPI functions WDK , default queue callback routines
- default queue callback routines
- queue callback routines WDK SetupAPI
- callback routines WDK SetupAPI
- queue files WDK SetupAPI
- file queuing WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Default Queue Callback Routine Functions





If you associate a callback routine with a file queue, the callback routine will be called every time that the system performs one of the queued file operations. Typically, you can use the default queue callback routine, [**SetupDefaultQueueCallback**](https://msdn.microsoft.com/library/windows/desktop/aa376993), to handle these notifications.

The following table lists functions associated with the default queue callback routine. For detailed function descriptions, and for more information about how to use callback routines with file queues, see the Microsoft Windows SDK documentation.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Function</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376993" data-raw-source="[&lt;strong&gt;SetupDefaultQueueCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376993)"><strong>SetupDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Handles notifications sent by the system when queued file operations are performed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377395" data-raw-source="[&lt;strong&gt;SetupInitDefaultQueueCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377395)"><strong>SetupInitDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Initializes context information that is needed by <strong>SetupDefaultQueueCallback</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377396" data-raw-source="[&lt;strong&gt;SetupInitDefaultQueueCallbackEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377396)"><strong>SetupInitDefaultQueueCallbackEx</strong></a></p></td>
<td align="left"><p>Initializes context information that is needed by <strong>SetupDefaultQueueCallback</strong>, and provides a separate window for displaying progress messages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377442" data-raw-source="[&lt;strong&gt;SetupTermDefaultQueueCallback&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377442)"><strong>SetupTermDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Notifies the system that the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application" data-raw-source="[&lt;em&gt;device installation application&lt;/em&gt;](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application)"><em>device installation application</em></a> will not commit any additional file queue operations.</p></td>
</tr>
</tbody>
</table>

 

 

 





