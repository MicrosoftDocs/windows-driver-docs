---
title: File Queuing Functions
description: File Queuing Functions
ms.assetid: ad777cd9-99ca-4468-b1fa-608503f96cd4
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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376984" data-raw-source="[&lt;strong&gt;SetupCloseFileQueue&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376984)"><strong>SetupCloseFileQueue</strong></a></p></td>
<td align="left"><p>Destroys a file queue together with any uncommitted file operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376987" data-raw-source="[&lt;strong&gt;SetupCommitFileQueue&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376987)"><strong>SetupCommitFileQueue</strong></a></p></td>
<td align="left"><p>Commits (performs) all queued operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377408" data-raw-source="[&lt;strong&gt;SetupOpenFileQueue&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377408)"><strong>SetupOpenFileQueue</strong></a></p></td>
<td align="left"><p>Creates and returns a handle to a file queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377413" data-raw-source="[&lt;strong&gt;SetupPromptReboot&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377413)"><strong>SetupPromptReboot</strong></a></p></td>
<td align="left"><p>Prompts the user to restart his or her computer, if necessary.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377421" data-raw-source="[&lt;strong&gt;SetupQueueCopy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377421)"><strong>SetupQueueCopy</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377422" data-raw-source="[&lt;strong&gt;SetupQueueCopyIndirect&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377422)"><strong>SetupQueueCopyIndirect</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying, and provides file location and security information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377423" data-raw-source="[&lt;strong&gt;SetupQueueCopySection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377423)"><strong>SetupQueueCopySection</strong></a></p></td>
<td align="left"><p>Queues the files in a specified INF file section for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377424" data-raw-source="[&lt;strong&gt;SetupQueueDefaultCopy&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377424)"><strong>SetupQueueDefaultCopy</strong></a></p></td>
<td align="left"><p>Queues a specified file for copying, using default source and destination settings contained in the INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377425" data-raw-source="[&lt;strong&gt;SetupQueueDelete&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377425)"><strong>SetupQueueDelete</strong></a></p></td>
<td align="left"><p>Queues a specified file for deletion.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377426" data-raw-source="[&lt;strong&gt;SetupQueueDeleteSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377426)"><strong>SetupQueueDeleteSection</strong></a></p></td>
<td align="left"><p>Queues the files in an INF file section for deletion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377427" data-raw-source="[&lt;strong&gt;SetupQueueRename&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377427)"><strong>SetupQueueRename</strong></a></p></td>
<td align="left"><p>Queues a specified file for renaming.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377428" data-raw-source="[&lt;strong&gt;SetupQueueRenameSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377428)"><strong>SetupQueueRenameSection</strong></a></p></td>
<td align="left"><p>Queues the files in an INF section for renaming.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377435" data-raw-source="[&lt;strong&gt;SetupScanFileQueue&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377435)"><strong>SetupScanFileQueue</strong></a></p></td>
<td align="left"><p>Scans a file queue and performs a specified operation on each queue entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377440" data-raw-source="[&lt;strong&gt;SetupSetPlatformPathOverride&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377440)"><strong>SetupSetPlatformPathOverride</strong></a></p></td>
<td align="left"><p>Sets the value that is used for overriding the default platform-specific source path.</p></td>
</tr>
</tbody>
</table>

 

 

 





