---
title: Installing a Print Monitor
author: windows-driver-content
description: Installing a Print Monitor
ms.assetid: 2ab993fd-647b-40aa-981c-1bc270ec79a4
keywords:
- print monitors WDK , installing
- installing print monitors WDK
- INF files WDK print , print monitors
- language monitors WDK print , installing
- port monitors WDK print , installing
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Installing a Print Monitor


## <a href="" id="ddk-installing-a-print-monitor-gg"></a>


This section describes the methods that can be used to install print monitors. (You can install a print monitor with the same INF file that you use to install your printer. For more information about INF files, see [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) and [Power Management](https://msdn.microsoft.com/library/windows/hardware/ff547131).)

### <a href="" id="ddk-installing-a-language-monitor-gg"></a>Installing a Language Monitor

To install a language monitor, add a LanguageMonitor entry to the [**INF DDInstall section**](https://msdn.microsoft.com/library/windows/hardware/ff547344) of the INF file. In the LanguageMonitor entry, list the displayed name of the language monitor and the name of its DLL, similar to the following INF example. A LanguageMonitor entry must be included for every printer driver that controls a printer requiring the use of the language monitor. For more information, see [Printer INF Files](printer-inf-files.md).

```
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

Alternatively, custom installation applications can install language monitors by calling the spooler's **AddMonitor** function, to explicitly install only a specific monitor DLL.

(The **AddMonitor** function is described in the Microsoft Windows SDK documentation.)

### <a href="" id="ddk-installing-a-port-monitor-gg"></a>Installing a Port Monitor

To install a port monitor, your installation medium must include a printer INF file (that is, an INF file for which Class = Printer) that contains a PortMonitors section. The single entry in this section points to an install section containing two entries: an [**INF CopyFiles directive**](https://msdn.microsoft.com/library/windows/hardware/ff546346) that lists all of the files that make up the port monitor, and a PortMonitorDll entry that specifies which DLL in the previous list implements the port monitor interface. The following example code illustrates these points. The PortMonitors section points to an install section named SamplePortMon. In that section, an INF **CopyFiles** directive copies three files that make up the port monitor. Following that, a PortMonitorDll entry identifies the DLL that implements the port monitor interface.

```
[PortMonitors]
"Sample Port Monitor" = SamplePortMon

[SamplePortMon]
CopyFiles = @file1.dll, @file2.dll, @file3.hlp
PortMonitorDll = file1.dll
```

To install a port monitor, open the Printers folder in Control Panel. On the Printers folder's **File** menu, select **Server Properties**. On the **File Server Properties** dialog, click the **Ports** tab, and then click the **Add Port...** button. On the **Printer Ports** dialog, click the **New Port Type...** button. Type the path to the INF file in the text input box, and then click **OK**.

Alternatively, a custom installation application can install the port monitor DLL by a call to the **AddMonitor** function as described in [Port Monitors](http://msdn.microsoft.com/library/windows/desktop/dd162825.aspx).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Installing%20a%20Print%20Monitor%20%20RELEASE:%20%289/1/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


