---
title: Installing a Print Monitor
description: Provides information about methods that can be used to install print monitors.
keywords:
- print monitors WDK, installing
- installing print monitors WDK
- INF files WDK print, print monitors
- language monitors WDK print, installing
- port monitors WDK print, installing
ms.date: 09/08/2022
---

# Installing a print monitor

This section describes the methods that can be used to install print monitors.

You can install a print monitor with the same INF file that you use to install your printer. For more information about INF files, see [Plug and Play](../kernel/introduction-to-plug-and-play.md) and [Power Management](../kernel/introduction-to-power-management.md).

## Installing a language monitor

To install a language monitor, add a LanguageMonitor entry to the [**INF DDInstall section**](../install/inf-ddinstall-section.md) of the INF file. In the LanguageMonitor entry, list the displayed name of the language monitor and the name of its DLL, similar to the following INF example. A LanguageMonitor entry must be included for every printer driver that controls a printer requiring the use of the language monitor. For more information, see [Printer INF Files](printer-inf-files.md).

```cpp
[AcmeInst]
CopyFiles=@ACME.PPD,ACMEMON
DataSection=PSCRIPT_DATA
DataFile=ACME.PPD
LanguageMonitor="Acme Language Monitor,acmemon.dll"
Include=ntprint.inf
Needs=PSCRIPT.OEM

[ACMEMON]
acmemon.dll,,,0x00000020

[DestinationDirs]
DefaultDestDir=66000
ACMEMON=66002

[SourceDisksNames]
1= %Location%,,,

[SourceDisksFiles]
acme.ppd = 1,\i386
acmemon.dll = 1,\i386
```

The Add Driver wizard or the Add Printer wizard reads this INF file and installs language monitors associated with printer drivers.

Alternatively, custom installation applications can install language monitors by calling the spooler's [**AddMonitor**](/windows/win32/printdocs/addmonitor) function, to explicitly install only a specific monitor DLL.

## Installing a port monitor

To install a port monitor, your installation medium must include a printer INF file (that is, an INF file for which Class = Printer) that contains a PortMonitors section. The single entry in this section points to an install section containing two entries: an [**INF CopyFiles directive**](../install/inf-copyfiles-directive.md) that lists all of the files that make up the port monitor, and a PortMonitorDll entry that specifies which DLL in the previous list implements the port monitor interface. The following example code illustrates these points. The PortMonitors section points to an install section named SamplePortMon. In that section, an INF **CopyFiles** directive copies three files that make up the port monitor. Following that, a PortMonitorDll entry identifies the DLL that implements the port monitor interface.

```cpp
[PortMonitors]
"Sample Port Monitor" = SamplePortMon

[SamplePortMon]
CopyFiles = @file1.dll, @file2.dll, @file3.hlp
PortMonitorDll = file1.dll
```

To install a port monitor, open the Printers folder in Control Panel. On the Printers folder's **File** menu, select **Server Properties**. On the **File Server Properties** dialog, click the **Ports** tab, and then click the **Add Port...** button. On the **Printer Ports** dialog, click the **New Port Type...** button. Type the path to the INF file in the text input box, and then click **OK**.

Alternatively, a custom installation application can install the port monitor DLL by a call to the **AddMonitor** function as described in [Port Monitors](/windows/desktop/printdocs/port-monitors).
