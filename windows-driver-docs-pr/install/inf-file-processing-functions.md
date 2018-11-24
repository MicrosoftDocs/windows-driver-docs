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
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF File Processing Functions





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
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376957" data-raw-source="[&lt;strong&gt;InstallHinfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376957)"><strong>InstallHinfSection</strong></a></p></td>
<td align="left"><p>Executes a specified section in a specified INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376985" data-raw-source="[&lt;strong&gt;SetupCloseInfFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376985)"><strong>SetupCloseInfFile</strong></a></p></td>
<td align="left"><p>Frees resources and closes the INF handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376990" data-raw-source="[&lt;strong&gt;SetupCopyOEMInf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376990)"><strong>SetupCopyOEMInf</strong></a></p></td>
<td align="left"><p>Copies a file into <em>%SystemRoot%\Inf</em>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376992" data-raw-source="[&lt;strong&gt;SetupDecompressOrCopyFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376992)"><strong>SetupDecompressOrCopyFile</strong></a></p></td>
<td align="left"><p>Copies a file and, if necessary, decompresses it.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376996" data-raw-source="[&lt;strong&gt;SetupFindFirstLine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376996)"><strong>SetupFindFirstLine</strong></a></p></td>
<td align="left"><p>Finds a pointer to the first line in a section of an INF file or, if a key is specified, the first line that matches the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa376997" data-raw-source="[&lt;strong&gt;SetupFindNextLine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa376997)"><strong>SetupFindNextLine</strong></a></p></td>
<td align="left"><p>Returns a pointer to the next line in an INF file section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377202" data-raw-source="[&lt;strong&gt;SetupFindNextMatchLine&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377202)"><strong>SetupFindNextMatchLine</strong></a></p></td>
<td align="left"><p>Returns a pointer to the next line in an INF file section or, if a key is specified, the next line that matches the key.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377254" data-raw-source="[&lt;strong&gt;SetupGetBinaryField&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377254)"><strong>SetupGetBinaryField</strong></a></p></td>
<td align="left"><p>Retrieves binary data from a field in a specified line, in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377258" data-raw-source="[&lt;strong&gt;SetupGetFieldCount&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377258)"><strong>SetupGetFieldCount</strong></a></p></td>
<td align="left"><p>Returns the number of fields in a line.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377265" data-raw-source="[&lt;strong&gt;SetupGetFileCompressionInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377265)"><strong>SetupGetFileCompressionInfo</strong></a></p></td>
<td align="left"><p>Retrieves file compression information from an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552194" data-raw-source="[&lt;strong&gt;SetupGetInfDriverStoreLocation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552194)"><strong>SetupGetInfDriverStoreLocation</strong></a></p></td>
<td align="left"><p>Retrieves the fully qualified file name (directory path and file name) of an INF file in the <a href="driver-store.md" data-raw-source="[driver store](driver-store.md)">driver store</a> that corresponds to a specified INF file in the system INF file directory or a specified INF file in the driver store.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377381" data-raw-source="[&lt;strong&gt;SetupGetInfFileList&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377381)"><strong>SetupGetInfFileList</strong></a></p></td>
<td align="left"><p>Returns a list of the INF files in a specified directory.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377383" data-raw-source="[&lt;strong&gt;SetupGetInfInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377383)"><strong>SetupGetInfInformation</strong></a></p></td>
<td align="left"><p>Returns information about an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377385" data-raw-source="[&lt;strong&gt;SetupGetIntField&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377385)"><strong>SetupGetIntField</strong></a></p></td>
<td align="left"><p>Obtains the integer value of a specified field in a specified line, in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff552200" data-raw-source="[&lt;strong&gt;SetupGetInfPublishedName&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff552200)"><strong>SetupGetInfPublishedName</strong></a></p></td>
<td align="left"><p>Retrieves the fully qualified name (directory path and file name) of an INF file in the system INF file directory that corresponds to a specified INF file in the system INF file directory or a specified INF file in the <a href="driver-store.md" data-raw-source="[driver store](driver-store.md)">driver store</a>.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377386" data-raw-source="[&lt;strong&gt;SetupGetLineByIndex&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377386)"><strong>SetupGetLineByIndex</strong></a></p></td>
<td align="left"><p>Returns a pointer to the line associated with a specified index value in a specified section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377387" data-raw-source="[&lt;strong&gt;SetupGetLineCount&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377387)"><strong>SetupGetLineCount</strong></a></p></td>
<td align="left"><p>Returns the number of lines in the specified section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377388" data-raw-source="[&lt;strong&gt;SetupGetLineText&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377388)"><strong>SetupGetLineText</strong></a></p></td>
<td align="left"><p>Retrieves the contents of a specified line from an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377389" data-raw-source="[&lt;strong&gt;SetupGetMultiSzField&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377389)"><strong>SetupGetMultiSzField</strong></a></p></td>
<td align="left"><p>Returns multiple strings, starting at a specified field in a line.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377390" data-raw-source="[&lt;strong&gt;SetupGetSourceFileLocation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377390)"><strong>SetupGetSourceFileLocation</strong></a></p></td>
<td align="left"><p>Returns the location of a source file that is listed in an INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377391" data-raw-source="[&lt;strong&gt;SetupGetSourceFileSize&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377391)"><strong>SetupGetSourceFileSize</strong></a></p></td>
<td align="left"><p>Returns the size of a specified file or a set of files that are listed in a specified section of an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377392" data-raw-source="[&lt;strong&gt;SetupGetSourceInfo&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377392)"><strong>SetupGetSourceInfo</strong></a></p></td>
<td align="left"><p>Retrieves the path, tag file, or description for a source.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377393" data-raw-source="[&lt;strong&gt;SetupGetStringField&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377393)"><strong>SetupGetStringField</strong></a></p></td>
<td align="left"><p>Retrieves string data from a field in a specified line, in an INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377394" data-raw-source="[&lt;strong&gt;SetupGetTargetPath&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377394)"><strong>SetupGetTargetPath</strong></a></p></td>
<td align="left"><p>Determines the target path for the files that are listed in a specified INF file section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377398" data-raw-source="[&lt;strong&gt;SetupInstallFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377398)"><strong>SetupInstallFile</strong></a></p></td>
<td align="left"><p>Installs a specified file into a specific target directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377399" data-raw-source="[&lt;strong&gt;SetupInstallFileEx&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377399)"><strong>SetupInstallFileEx</strong></a></p></td>
<td align="left"><p>Installs a specified file into a specific target directory. The installation is postponed if an existing version of the file is in use.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377400" data-raw-source="[&lt;strong&gt;SetupInstallFilesFromInfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377400)"><strong>SetupInstallFilesFromInfSection</strong></a></p></td>
<td align="left"><p>Queues the files in a specified INF file section for copying. (Same as <a href="https://msdn.microsoft.com/library/windows/desktop/aa377423" data-raw-source="[&lt;strong&gt;SetupQueueCopySection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377423)"><strong>SetupQueueCopySection</strong></a>.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377401" data-raw-source="[&lt;strong&gt;SetupInstallFromInfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377401)"><strong>SetupInstallFromInfSection</strong></a></p></td>
<td align="left"><p>Performs the directives specified in an INF <em>DDInstall</em> section.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377402" data-raw-source="[&lt;strong&gt;SetupInstallServicesFromInfSection&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377402)"><strong>SetupInstallServicesFromInfSection</strong></a></p></td>
<td align="left"><p>Performs service installation and deletion operations as specified in an INF <em>DDInstall</em><strong>.Services</strong> section.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377407" data-raw-source="[&lt;strong&gt;SetupOpenAppendInfFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377407)"><strong>SetupOpenAppendInfFile</strong></a></p></td>
<td align="left"><p>Opens an INF file and appends it to an existing INF handle.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377409" data-raw-source="[&lt;strong&gt;SetupOpenInfFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377409)"><strong>SetupOpenInfFile</strong></a></p></td>
<td align="left"><p>Opens an INF file and returns a handle to it.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377411" data-raw-source="[&lt;strong&gt;SetupOpenMasterInf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377411)"><strong>SetupOpenMasterInf</strong></a></p></td>
<td align="left"><p>Opens the master INF file that contains file and layout information for files that were included with the default installation of the operating system.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377416" data-raw-source="[&lt;strong&gt;SetupQueryInfFileInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377416)"><strong>SetupQueryInfFileInformation</strong></a></p></td>
<td align="left"><p>Returns the name of one of the constituent INF files of a specified INF file.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377418" data-raw-source="[&lt;strong&gt;SetupQueryInfVersionInformation&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377418)"><strong>SetupQueryInfVersionInformation</strong></a></p></td>
<td align="left"><p>Returns the version number of one of the constituent INF files of a specified INF file.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377436" data-raw-source="[&lt;strong&gt;SetupSetDirectoryId&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377436)"><strong>SetupSetDirectoryId</strong></a></p></td>
<td align="left"><p>Assigns a directory ID (DIRID) to a specified directory.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377446" data-raw-source="[&lt;strong&gt;SetupUninstallOEMInf&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377446)"><strong>SetupUninstallOEMInf</strong></a></p></td>
<td align="left"><p>Uninstalls a specified INF file, and deletes the associated .<em>pnf</em> and .<em>cat</em> files, if they exist.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><a href="https://msdn.microsoft.com/library/windows/desktop/aa377447" data-raw-source="[&lt;strong&gt;SetupVerifyInfFile&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa377447)"><strong>SetupVerifyInfFile</strong></a></p></td>
<td align="left"><p>Verifies that a digitally-signed INF file has not been modified. (Windows XP and later.)</p></td>
</tr>
</tbody>
</table>

 

 

 





