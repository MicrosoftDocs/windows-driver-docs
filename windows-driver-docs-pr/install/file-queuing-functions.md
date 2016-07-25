---
title: File Queuing Functions
description: File Queuing Functions
ms.assetid: ad777cd9-99ca-4468-b1fa-608503f96cd4
keywords: ["SetupAPI functions WDK , file queuing", "file queuing WDK SetupAPI", "queue files WDK SetupAPI"]
---

# File Queuing Functions


## <a href="" id="ddk-file-queuing-functions-dg"></a>


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
<td align="left"><p>[<strong>SetupCloseFileQueue</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376984)</p></td>
<td align="left"><p>Destroys a file queue together with any uncommitted file operations.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupCommitFileQueue</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376987)</p></td>
<td align="left"><p>Commits (performs) all queued operations.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupOpenFileQueue</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377408)</p></td>
<td align="left"><p>Creates and returns a handle to a file queue.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupPromptReboot</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377413)</p></td>
<td align="left"><p>Prompts the user to restart his or her computer, if necessary.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQueueCopy</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377421)</p></td>
<td align="left"><p>Queues a specified file for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueueCopyIndirect</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377422)</p></td>
<td align="left"><p>Queues a specified file for copying, and provides file location and security information.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQueueCopySection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377423)</p></td>
<td align="left"><p>Queues the files in a specified INF file section for copying.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueueDefaultCopy</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377424)</p></td>
<td align="left"><p>Queues a specified file for copying, using default source and destination settings contained in the INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQueueDelete</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377425)</p></td>
<td align="left"><p>Queues a specified file for deletion.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueueDeleteSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377426)</p></td>
<td align="left"><p>Queues the files in an INF file section for deletion.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQueueRename</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377427)</p></td>
<td align="left"><p>Queues a specified file for renaming.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueueRenameSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377428)</p></td>
<td align="left"><p>Queues the files in an INF section for renaming.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupScanFileQueue</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377435)</p></td>
<td align="left"><p>Scans a file queue and performs a specified operation on each queue entry.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupSetPlatformPathOverride</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377440)</p></td>
<td align="left"><p>Sets the value that is used for overriding the default platform-specific source path.</p></td>
</tr>
</tbody>
</table>

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20File%20Queuing%20Functions%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




