---
title: Using Dirids
description: Using Dirids
ms.assetid: 231bc313-b5c3-48ef-b2e2-c4e287517679
keywords:
- dirids WDK
- INF files WDK device installations , directory identifiers
- directory identifiers WDK INF files
- directories WDK INF files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using Dirids





Many of the directories that appear in INF files can be expressed by using directory identifiers (*dirids*), which are numbers that identify specific directories. Applications can use, but cannot reassign the system-defined directories that are associated with *dirids* whose values are from -1 through 32767.

To create *dirids* with user-defined values from 32768 through 65534, or 65536 and up, use the **SetupSetDirectoryId** function (described in the Microsoft Windows SDK documentation).

Be aware that a *dirid* with a value of 65535 is considered synonymous with a *dirid* with a value of -1, although the latter (*dirid* -1) is preferred.

If you intend to use *dirids* in your INF file, consider the following two guidelines:

1. When the syntax for an INF file entry explicitly specifies a *dirid* value (the [**INF DestinationDirs section**](inf-destinationdirs-section.md), for example), express that value as a number.

   The following example demonstrates this syntax:

   ```cpp
   [DestinationDirs]
   DefaultDestDir = 11  ;  \system32 directory on Windows 2000 and later versions
   ```

2. When the syntax for an INF file entry specifies a file path, you can use a system-supplied string substitution to represent part or all of this path. This substitution has the following form:

   **%**<em>dirid</em>**%**

   This form consists of a percent (%) character, followed by the *dirid* for the directory that you want to specify, followed by another percent (%) character. A terminating backslash (\) character separates this expression from a following file name or additional directories in the path<strong>.</strong>

   The following example demonstrates this syntax:

   ```cpp
   [aic78xx_Service_Inst]
   ServiceBinary = %12%\aic78xx.sys
   ```

   When fully expanded, the path shown in the previous example becomes *c:*\\*windows*\\*system32*\\*drivers*\\*aic78xx.sys* (assuming that Windows was installed in the *c:*\\*windows* directory). Be aware that the string substitution, or %*dirid*% form, can be used anywhere a string is expected, with the exception of the [**INF Strings section**](inf-strings-section.md) of the INF file.

   The two following examples show how string substitution should *not* be used.

   ```cpp
   [DestinationDirs]
   DefaultDestDir = %11%  ; Error! - number expected

   [aic78xx_Service_Inst]
   ServiceBinary = 12\aic78xx.sys  ; Error! - unknown directory name
   ```

   In the first example, the syntax for the **DefaultDestDir** entry requires its value to be a number. However, the %11% expression expands to a string. In the second example, the INF writer apparently intended to set the value for the **ServiceBinary** entry to a file in the directory that contains drivers (see the following table for more information). The error occurs because Windows looks for the specified file in a directory named "12", which probably does not exist on the computer.

The following table shows several commonly used *dirids*, and the directories they represent. The values most commonly specified by device INF files and driver INF files are listed toward the top of the table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Destination Directory</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>01</strong></p></td>
<td align="left"><p><em>SourceDrive</em><strong>:\</strong><em>pathname</em> (the directory from which the INF file was installed)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>10</strong></p></td>
<td align="left"><p>Windows directory.</p>
<p>This is equivalent to <em>%SystemRoot%</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>11</strong></p></td>
<td align="left"><p>System directory.</p>
<p>This is equivalent to <em>%SystemRoot%</em><strong>\</strong><em>system32</em> for Windows 2000 and later versions of Windows..</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>12</strong></p></td>
<td align="left"><p>Drivers directory.</p>
<p>This is equivalent to <em>%SystemRoot%</em><strong>\</strong><em>system32</em><strong>\</strong><em>drivers</em> for Windows 2000 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>13</strong></p></td>
<td align="left"><p>Driver package&#39;s <a href="https://msdn.microsoft.com/windows/hardware/drivers/install/driver-store">Driver Store</a> directory.</p>
<p>For Windows 8.1 and later versions of Windows, specifies the path to the Driver Store directory where the driver package was imported.

Don&#39;t use <a href="inf-delfiles-directive.md" data-raw-source="[DelFiles](inf-delfiles-directive.md)">DelFiles</a> on a file for which <strong>DestinationDirs</strong> includes <em>dirid</em> 13.

The optional subdirectory in the <strong>SourceDiskFiles</strong> section for a file must match the subdirectory in the <strong>DestinationDirs</strong> section for the entry that applies to this file.

Don&#39;t use <a href="inf-copyfiles-directive.md" data-raw-source="[CopyFiles](inf-copyfiles-directive.md)">CopyFiles</a> to rename a file for which <strong>DestinationDirs</strong> includes <em>dirid</em> 13.
</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>17</strong></p></td>
<td align="left"><p>INF file directory</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>18</strong></p></td>
<td align="left"><p>Help directory</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>20</strong></p></td>
<td align="left"><p>Fonts directory</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>21</strong></p></td>
<td align="left"><p>Viewers directory</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>23</strong></p></td>
<td align="left"><p>Color directory (ICM) (<em>not</em> used for installing printer drivers)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>24</strong></p></td>
<td align="left"><p>Root directory of the system disk.</p>
<p>This is the root directory of the disk on which Windows files are installed. For example, if <em>dirid</em> 10 is &quot;<em>C:\winnt</em>&quot;, then <em>dirid</em> 24 is &quot;<em>C:\</em>&quot;.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>25</strong></p></td>
<td align="left"><p>Shared directory</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>30</strong></p></td>
<td align="left"><p>Root directory of the boot disk, also known as &quot;ARC system partition&quot;. (This might or might not be the same directory as the one represented by <em>dirid</em> 24.)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>50</strong></p></td>
<td align="left"><p>System directory</p>
<p>This is equivalent to <em>%SystemRoot%</em><strong>\</strong><em>system</em>.</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>51</strong></p></td>
<td align="left"><p>Spool directory (<em>not</em> used for installing printer drivers − see <a href="https://msdn.microsoft.com/library/windows/hardware/ff560821">Printer Dirids</a>)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>52</strong></p></td>
<td align="left"><p>Spool drivers directory (<em>not</em> used for installing printer drivers)</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>53</strong></p></td>
<td align="left"><p>User profile directory</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>54</strong></p></td>
<td align="left"><p>Directory where <em>Ntldr.exe</em> and <em>Osloader.exe</em> are located</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>55</strong></p></td>
<td align="left"><p>Print processors directory (<em>not</em> used for installing printer drivers)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>-1</strong></p></td>
<td align="left"><p>Absolute path</p></td>
</tr>
</tbody>
</table>

 

*Dirid* values from 16384 through 32767 are reserved for special shell folders. The following table shows *dirid* values for these folders.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Value</th>
<th align="left">Shell Special Folder</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>16406</strong></p></td>
<td align="left"><p><em>All Users\Start Menu</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16407</strong></p></td>
<td align="left"><p><em>All Users\Start Menu\Programs</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16408</strong></p></td>
<td align="left"><p><em>All Users\Start Menu\Programs\Startup</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16409</strong></p></td>
<td align="left"><p><em>All Users\Desktop</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16415</strong></p></td>
<td align="left"><p><em>All Users\Favorites</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16419</strong></p></td>
<td align="left"><p><em>All Users\Application Data</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16422</strong></p></td>
<td align="left"><p><em>Program Files</em></p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16425</strong></p></td>
<td align="left"><p><em>%SystemRoot%\system32</em> (valid for Microsoft Win32 user-mode applications that are running under Windows on Windows (WOW64))</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16426</strong></p></td>
<td align="left"><p><em>Program Files</em> (valid for Win32 user-mode applications that are running under WOW64)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16427</strong></p></td>
<td align="left"><p><em>Program Files\Common</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16428</strong></p></td>
<td align="left"><p><em>Program Files\Common</em> (valid for Win32 user-mode applications that are running under WOW64)</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>16429</strong></p></td>
<td align="left"><p><em>All Users\Templates</em></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>16430</strong></p></td>
<td align="left"><p><em>All Users\Documents</em></p></td>
</tr>
</tbody>
</table>

 

In addition to the values in this table that are defined in *Setupapi.h*, you can use any of the CSIDL_*Xxx* values that are defined in *Shlobj.h*. To define a *dirid* value for a folder not listed in this table, add 16384 (0x4000) to the CSIDL_*Xxx* value. For more information about CSIDL_*Xxx* values, see the Windows SDK documentation.

 

 





