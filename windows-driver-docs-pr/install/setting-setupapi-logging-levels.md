---
title: Setting SetupAPI Logging Levels
description: Setting SetupAPI Logging Levels
ms.assetid: e6fa4c9c-e210-42c7-8bc7-d36463073c28
keywords:
- logging levels WDK SetupAPI
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Setting SetupAPI Logging Levels





You can control the amount of information that is written to the SetupAPI log, either for all [*device installation applications*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application) or for individual device installation applications.

To change the level of information written to the SetupAPI log for all device installation applications, create (or modify) the following registry value:

```cpp
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Setup\LogLevel
```

By setting this value (using the values listed in the tables below) you can choose the level of errors that are logged, modify the verbosity of logging, or turn off logging. You can also log information to a debugger as well as to the log file.

To specify logging levels for individual device installation applications, create a registry entry under the following key:

```cpp
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Setup\AppLogLevels
```

Under this key, create a value name representing the application's executable file name, and assign the desired logging level to that name (using the values listed in the tables below), such as **service.exe=**<em>LoggingLevel</em>.

The logging level is a DWORD value. If this value is not specified or is zero, SetupAPI uses a default behavior, as indicated in the tables below.

The DWORD value is made up of three parts, formatted as 0x*SSSSDDGG*. The low eight bits, represented by the mask 0x000000FF, set the logging level for general device installation operations. The next-higher eight bits, represented by the mask 0x0000FF00, set the logging level for device installation operations. The highest bits are special flags.

The following tables contain the general logging levels, device installation logging levels, and special logging flags for Windows 2000 and later.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">General Logging Levels</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>Use default settings (currently 0x20).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000001</p></td>
<td align="left"><p>Off (no device installation logging).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000010</p></td>
<td align="left"><p>Log errors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000020</p></td>
<td align="left"><p>Log errors and warnings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000030</p></td>
<td align="left"><p>Log errors, warnings and other information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000040</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000050</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time-stamped entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000060</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time entries. Additionally, all entries are time-stamped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00000070</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time messages. All entries are time-stamped. Additional messages that can slow down the system, such as cache hits, are included.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x000000FF</p></td>
<td align="left"><p>Specifies the most verbose logging available.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Device Logging Levels</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x00000000</p></td>
<td align="left"><p>Use default settings (currently 0x3000).</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00000100</p></td>
<td align="left"><p>Off (no device installation logging).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00001000</p></td>
<td align="left"><p>Log errors.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00002000</p></td>
<td align="left"><p>Log errors and warnings.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00003000</p></td>
<td align="left"><p>Log errors, warnings and other information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00004000</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00005000</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time-stamped entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x00006000</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time entries. Additionally, all entries are time-stamped.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x00007000</p></td>
<td align="left"><p>Log errors, warnings and other information in verbose mode, plus time messages. All entries are time-stamped. Additional messages that can slow down the system, such as cache hits, are included.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x0000FF00</p></td>
<td align="left"><p>Specifies the most verbose logging available.</p></td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Special Flags</th>
<th align="left">Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>0x08000000</p></td>
<td align="left"><p>(<em>Windows XP and later</em>) Add a time stamp to all log entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x20000000</p></td>
<td align="left"><p>(<em>Windows XP and later</em>) Don&#39;t flush logging information to disk after each entry is written. (Logging is faster, but information could be lost if the system crashes.)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>0x40000000</p></td>
<td align="left"><p>Write log entries chronologically instead of grouping entries.</p></td>
</tr>
<tr class="even">
<td align="left"><p>0x80000000</p></td>
<td align="left"><p>Send the output to the debugger as well as to the log file.</p></td>
</tr>
</tbody>
</table>

 

For example, SetupAPI interprets some sample *LoggingFlags* values as follows:

-   0x00000000 means default logging.

-   0x0000FFFF means verbose logging.

-   0x8000FF00 means log verbose device installation information to both the log file and the debugger.

To modify the default SetupAPI logging levels during a clean installation, edit the registry during the period between text-mode setup and GUI-mode setup. The following steps describe the procedure. These steps assume that you are installing to *D:\\Winnt* and have a working build of the same version of Windows on another partition. Change the SetupAPI logging levels as follows:

1.  Start the installation of the clean build you are testing.

2.  Stop the setup process during the first boot after text-mode setup (that is, before GUI-mode setup).

3.  Boot into the working build by selecting it from the boot menu, and log on as Administrator.

4.  Find the registry hives (files) in *D:\\Winnt\\System32\\config*. In this case, you need to modify the registry hive in *Software.sav*.

5.  On Windows 2000, run *Regedt32*, select the "HKEY_LOCAL_MACHINE on Local Machine" window, and select the HKEY_LOCAL_MACHINE key. Then click the **Registry** menu and select **Load Hive**.

    On Windows XP and later, run *RegEdit*. Highlight HKEY_LOCAL_MACHINE, click the **File** menu and select **Load Hive**.

6.  Browse the files and select *D:\\Winnt\\System32\\config\\software.sav*. When prompted for key name, enter "_sw.sav "

7.  Open the _sw.sav key under HKEY_LOCAL_MACHINE and highlight the following key:

    ```cpp
    HKEY_LOCAL_MACHINE_sw.sav\Microsoft\Windows\CurrentVersion\Setup
    ```

    On Windows 2000, click the **Security** menu, select **Permissions**, and grant full control to Administrator.

    On Windows XP and later, click the **Edit** menu, select **Permissions**, and grant full control to Administrator.

8.  On Windows 2000, add the necessary registry values under this key using clicking on **Edit** and selecting **Add Value**.

    On Windows XP and later, click **Edit** and select **New DWORD Value**.

    Enter the value. For example, add "0xFFFF" to enable full verbose logging.

9.  Select HKEY_LOCAL_MACHINE\\_sw.sav, and unload the hive (using the **Registry** menu on Windows 2000, or the **File** menu on Windows XP and later)The _sw.sav key should disappear.

10. Copy *D:\\Winnt\\System32\\config\\software.sav* to *D:\\Winnt\\System32\\config\\software*.

11. Reboot and continue into Setup.

12. To verify this change, press SHIFT+F10 in GUI-mode Setup, then run *regedit.exe* and check the logging level.

 

 





