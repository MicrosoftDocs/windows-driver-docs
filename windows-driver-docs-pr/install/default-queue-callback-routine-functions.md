---
title: Default Queue Callback Routine Functions
description: Default Queue Callback Routine Functions
keywords:
- SetupAPI functions WDK , default queue callback routines
- default queue callback routines
- queue callback routines WDK SetupAPI
- callback routines WDK SetupAPI
- queue files WDK SetupAPI
- file queuing WDK SetupAPI
ms.date: 04/20/2017
---

# Default Queue Callback Routine Functions





If you associate a callback routine with a file queue, the callback routine will be called every time that the system performs one of the queued file operations. Typically, you can use the default queue callback routine, [**SetupDefaultQueueCallback**](/windows/win32/api/setupapi/nf-setupapi-setupdefaultqueuecallbacka), to handle these notifications.

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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupdefaultqueuecallbacka" data-raw-source="[&lt;strong&gt;SetupDefaultQueueCallback&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupdefaultqueuecallbacka)"><strong>SetupDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Handles notifications sent by the system when queued file operations are performed.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupinitdefaultqueuecallback" data-raw-source="[&lt;strong&gt;SetupInitDefaultQueueCallback&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupinitdefaultqueuecallback)"><strong>SetupInitDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Initializes context information that is needed by <strong>SetupDefaultQueueCallback</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupinitdefaultqueuecallbackex" data-raw-source="[&lt;strong&gt;SetupInitDefaultQueueCallbackEx&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupinitdefaultqueuecallbackex)"><strong>SetupInitDefaultQueueCallbackEx</strong></a></p></td>
<td align="left"><p>Initializes context information that is needed by <strong>SetupDefaultQueueCallback</strong>, and provides a separate window for displaying progress messages.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setuptermdefaultqueuecallback" data-raw-source="[&lt;strong&gt;SetupTermDefaultQueueCallback&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setuptermdefaultqueuecallback)"><strong>SetupTermDefaultQueueCallback</strong></a></p></td>
<td align="left"><p>Notifies the system that the <a href="/windows-hardware/drivers/#wdkgloss-device-installation-application" data-raw-source="&lt;em&gt;device installation application&lt;/em&gt;"><em>device installation application</em></a> will not commit any additional file queue operations.</p></td>
</tr>
</tbody>
</table>

 

