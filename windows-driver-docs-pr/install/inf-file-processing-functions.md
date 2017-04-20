---
title: INF File Processing Functions
description: INF File Processing Functions
ms.assetid: df769d05-9843-44d2-971d-13f1a81755c2
keywords:
- SetupAPI functions WDK , INF files
- INF files WDK SetupAPI
- SetupCopyOEMInf
- INF file processing functions WDK SetupAPI
- processing functions WDK INF files
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# INF File Processing Functions


## <a href="" id="ddk-inf-file-processing-functions-dg"></a>


The INF file processing functions provide setup and installation functionality that includes the following:

-   Opening and closing an INF file.

-   Retrieving information about an INF file.

-   Retrieving information about source files and target directories for copy operations.

-   Performing the installation actions specified in an INF file section.

The following table lists the functions that are used for processing INF files. For detailed function descriptions, see the Microsoft Windows SDK documentation.

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
<td align="left"><p>[<strong>InstallHinfSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376957)</p></td>
<td align="left"><p>Executes a specified section in a specified INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupCloseInfFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376985)</p></td>
<td align="left"><p>Frees resources and closes the INF handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupCopyOEMInf</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376990)</p></td>
<td align="left"><p>Copies a file into <em>%SystemRoot%\Inf</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupDecompressOrCopyFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376992)</p></td>
<td align="left"><p>Copies a file and, if necessary, decompresses it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupFindFirstLine</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376996)</p></td>
<td align="left"><p>Finds a pointer to the first line in a section of an INF file or, if a key is specified, the first line that matches the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupFindNextLine</strong>](https://msdn.microsoft.com/library/windows/desktop/aa376997)</p></td>
<td align="left"><p>Returns a pointer to the next line in an INF file section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupFindNextMatchLine</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377202)</p></td>
<td align="left"><p>Returns a pointer to the next line in an INF file section or, if a key is specified, the next line that matches the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetBinaryField</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377254)</p></td>
<td align="left"><p>Retrieves binary data from a field in a specified line, in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetFieldCount</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377258)</p></td>
<td align="left"><p>Returns the number of fields in a line.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetFileCompressionInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377265)</p></td>
<td align="left"><p>Retrieves file compression information from an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetInfDriverStoreLocation</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552194)</p></td>
<td align="left"><p>Retrieves the fully qualified file name (directory path and file name) of an INF file in the [driver store](driver-store.md) that corresponds to a specified INF file in the system INF file directory or a specified INF file in the driver store.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetInfFileList</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377381)</p></td>
<td align="left"><p>Returns a list of the INF files in a specified directory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetInfInformation</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377383)</p></td>
<td align="left"><p>Returns information about an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetIntField</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377385)</p></td>
<td align="left"><p>Obtains the integer value of a specified field in a specified line, in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetInfPublishedName</strong>](https://msdn.microsoft.com/library/windows/hardware/ff552200)</p></td>
<td align="left"><p>Retrieves the fully qualified name (directory path and file name) of an INF file in the system INF file directory that corresponds to a specified INF file in the system INF file directory or a specified INF file in the [driver store](driver-store.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetLineByIndex</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377386)</p></td>
<td align="left"><p>Returns a pointer to the line associated with a specified index value in a specified section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetLineCount</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377387)</p></td>
<td align="left"><p>Returns the number of lines in the specified section.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetLineText</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377388)</p></td>
<td align="left"><p>Retrieves the contents of a specified line from an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetMultiSzField</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377389)</p></td>
<td align="left"><p>Returns multiple strings, starting at a specified field in a line.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetSourceFileLocation</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377390)</p></td>
<td align="left"><p>Returns the location of a source file that is listed in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetSourceFileSize</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377391)</p></td>
<td align="left"><p>Returns the size of a specified file or a set of files that are listed in a specified section of an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetSourceInfo</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377392)</p></td>
<td align="left"><p>Retrieves the path, tag file, or description for a source.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupGetStringField</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377393)</p></td>
<td align="left"><p>Retrieves string data from a field in a specified line, in an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupGetTargetPath</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377394)</p></td>
<td align="left"><p>Determines the target path for the files that are listed in a specified INF file section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupInstallFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377398)</p></td>
<td align="left"><p>Installs a specified file into a specific target directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupInstallFileEx</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377399)</p></td>
<td align="left"><p>Installs a specified file into a specific target directory. The installation is postponed if an existing version of the file is in use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupInstallFilesFromInfSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377400)</p></td>
<td align="left"><p>Queues the files in a specified INF file section for copying. (Same as [<strong>SetupQueueCopySection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377423).)</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupInstallFromInfSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377401)</p></td>
<td align="left"><p>Performs the directives specified in an INF <em>DDInstall</em> section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupInstallServicesFromInfSection</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377402)</p></td>
<td align="left"><p>Performs service installation and deletion operations as specified in an INF <em>DDInstall</em><strong>.Services</strong> section.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupOpenAppendInfFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377407)</p></td>
<td align="left"><p>Opens an INF file and appends it to an existing INF handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupOpenInfFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377409)</p></td>
<td align="left"><p>Opens an INF file and returns a handle to it.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupOpenMasterInf</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377411)</p></td>
<td align="left"><p>Opens the master INF file that contains file and layout information for files that were included with the default installation of the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupQueryInfFileInformation</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377416)</p></td>
<td align="left"><p>Returns the name of one of the constituent INF files of a specified INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupQueryInfVersionInformation</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377418)</p></td>
<td align="left"><p>Returns the version number of one of the constituent INF files of a specified INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupSetDirectoryId</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377436)</p></td>
<td align="left"><p>Assigns a directory ID (DIRID) to a specified directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p>[<strong>SetupUninstallOEMInf</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377446)</p></td>
<td align="left"><p>Uninstalls a specified INF file, and deletes the associated .<em>pnf</em> and .<em>cat</em> files, if they exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>[<strong>SetupVerifyInfFile</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377447)</p></td>
<td align="left"><p>Verifies that a digitally-signed INF file has not been modified. (Windows XP and later.)</p></td>
</tr>
</tbody>
</table>

 

 

 





