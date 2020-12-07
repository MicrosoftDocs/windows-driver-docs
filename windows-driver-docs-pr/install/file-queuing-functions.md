---
title: File Queuing Functions
description: File Queuing Functions
keywords:
- SetupAPI functions WDK , file queuing
- file queuing WDK SetupAPI
- queue files WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File Queuing Functions





Using the general Setup functions, you can queue files for various operations. File queues can be established for copying, renaming, and deleting files. Typically, an application queues all the file operations necessary for an entire installation and then "commits" the queue so the operations are performed in a single batch.

The following table provides a summary of file queuing functions. For detailed function descriptions, see the Microsoft Windows SDK documentation.

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
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupclosefilequeue" data-raw-source="[&lt;strong&gt;SetupCloseFileQueue&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupclosefilequeue)"><strong>SetupCloseFileQueue</strong></a></p></td>
<td align="left"><p>Destroys a file queue together with any uncommitted file operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupcommitfilequeuea" data-raw-source="[&lt;strong&gt;SetupCommitFileQueue&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupcommitfilequeuea)"><strong>SetupCommitFileQueue</strong></a></p></td>
<td align="left"><p>Commits (performs) all queued operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupopenfilequeue" data-raw-source="[&lt;strong&gt;SetupOpenFileQueue&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupopenfilequeue)"><strong>SetupOpenFileQueue</strong></a></p></td>
<td align="left"><p>Creates and returns a handle to a file queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setuppromptreboot" data-raw-source="[&lt;strong&gt;SetupPromptReboot&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setuppromptreboot)"><strong>SetupPromptReboot</strong></a></p></td>
<td align="left"><p>Prompts the user to restart his or her computer, if necessary.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuecopya" data-raw-source="[&lt;strong&gt;SetupQueueCopy&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuecopya)"><strong>SetupQueueCopy</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuecopyindirecta" data-raw-source="[&lt;strong&gt;SetupQueueCopyIndirect&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuecopyindirecta)"><strong>SetupQueueCopyIndirect</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying, and provides file location and security information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuecopysectiona" data-raw-source="[&lt;strong&gt;SetupQueueCopySection&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuecopysectiona)"><strong>SetupQueueCopySection</strong></a></p></td>
<td align="left"><p>Queues the files in a specified INF file section for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuedefaultcopya" data-raw-source="[&lt;strong&gt;SetupQueueDefaultCopy&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuedefaultcopya)"><strong>SetupQueueDefaultCopy</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying, using default source and destination settings contained in the INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuedeletea" data-raw-source="[&lt;strong&gt;SetupQueueDelete&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuedeletea)"><strong>SetupQueueDelete</strong></a></p></td>
<td align="left"><p>Queues a specified file for deletion.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuedeletesectiona" data-raw-source="[&lt;strong&gt;SetupQueueDeleteSection&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuedeletesectiona)"><strong>SetupQueueDeleteSection</strong></a></p></td>
<td align="left"><p>Queues the files in an INF file section for deletion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuerenamea" data-raw-source="[&lt;strong&gt;SetupQueueRename&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuerenamea)"><strong>SetupQueueRename</strong></a></p></td>
<td align="left"><p>Queues a specified file for renaming.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupqueuerenamesectiona" data-raw-source="[&lt;strong&gt;SetupQueueRenameSection&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupqueuerenamesectiona)"><strong>SetupQueueRenameSection</strong></a></p></td>
<td align="left"><p>Queues the files in an INF section for renaming.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupscanfilequeuea" data-raw-source="[&lt;strong&gt;SetupScanFileQueue&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupscanfilequeuea)"><strong>SetupScanFileQueue</strong></a></p></td>
<td align="left"><p>Scans a file queue and performs a specified operation on each queue entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="/windows/win32/api/setupapi/nf-setupapi-setupsetplatformpathoverridea" data-raw-source="[&lt;strong&gt;SetupSetPlatformPathOverride&lt;/strong&gt;](/windows/win32/api/setupapi/nf-setupapi-setupsetplatformpathoverridea)"><strong>SetupSetPlatformPathOverride</strong></a></p></td>
<td align="left"><p>Sets the value that is used for overriding the default platform-specific source path.</p></td>
</tr>
</tbody>
</table>

 

