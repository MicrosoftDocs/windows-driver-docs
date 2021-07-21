---
title: Index of Windows Driver Kit Tools
description: Index of Windows Driver Kit Tools
keywords:
- Disabler tool
- DbgCon tool
- Sniffir tool
- Sledge tool
- Call Usage Verifier tool
- CUV tool
- tools WDK , listed
- driver development tools WDK , listed
- Sleep State Chooser
- sleeper
- Acpislp
- Manual Power State Change Test
- GUIDGen WDK
- GUID Generator WDK
- GUIDGen.exe WDK
ms.date: 05/09/2018
ms.localizationpriority: medium
---

# Index of Windows Driver Kit Tools

This topic supplies basic information about the tools that are included in the Windows Driver Kit (WDK). This topic also includes references to other tools that are useful for driver development. These other tools are either available as part of the operating system or are available as separate download. For more information about each tool, see the documentation in this topic that describes the tool.

For information about how to obtain the latest WDK, see [Download the Windows Driver Kit (WDK)](../download-the-wdk.md).

## Index of WDK Tools

The information in the following tables describes the tools that are useful for Windows driver developers. The list of tools includes tools that ship with the WDK (as indicated by the **WDK tool** field) and also includes some tools that are available separately or that are installed with Windows. Tools that can generally be used with all drivers are listed under [All Drivers](#all-drivers). Tools that are specific to a technology are grouped together, for example, tools that are specific for [Windows Portable Devices (WPD) Drivers](#windows-portable-devices-wpd-drivers) or [Sensors](#sensors).

- [Audio/Video Drivers](#audio--video-drivers)
- [Bluetooth Drivers](#bluetooth-drivers)
- [Windows Image Acquisition (WIA) Drivers](#windows-image-acquisition-wia-drivers)
- [Windows Portable Devices (WPD) Drivers](#windows-portable-devices-wpd-drivers)
- [Printer Drivers](#printer-drivers)
- [Sensors](#sensors)
- [All Drivers](#all-drivers)

>[!NOTE]
>The Visual Studio environment variable, %WindowsSdkDir%, represents the path to the Windows kits directory where this version of the WDK is installed, for example, C:\\Program Files (x86)\\Windows Kits\\8.1.

### Audio / Video Drivers

|Tool Name|Tool Location|Description and Help file location|
|----|----|----|
|Display Color Calibration tool (Dccw.exe) </br>**WDK tool**: No|%Windir%\System32\Dccw.exe</br>|A calibration tool that lets users adjust their display color to be closer to the Windows and World Wide Web international standard red-green-blue (sRGB) color space.|
|GraphEdt (Graphedt.exe)</br>**Tool in WDK:** Yes|%WindowsSdkDir%\tools\x86\graphedt.exe</br>%WindowsSdkDir%\tools\x64\graphedt.exe|Builds filter graphs to test streaming audio/video capture drivers.</br>Documentation:</br>[Overview of GraphEdit](/windows/win32/directshow/simulating-graph-building-with-graphedit)|
|KSStudio (KsStudio.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x86\KsStudio.exe</br> %WindowsSdkDir%\tools\x64\KsStudio.exe</br></br>**Note** This tool must be run by someone who has administrator privileges.|This tool can construct a graphical representation of a filter graph that shows the pin-to-pin connections between filters and the filters' internal nodes.</br>%WindowsSdkDir%\tools\x86\KsStudio.chm</br>%WindowsSdkDir%\tools\x64\KsStudio.chm</br>See [AVStream Testing and Debugging](../stream/avstream-testing-and-debugging.md) for more information.|
|USB Device Viewer (Usbview.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x86\Usbview.exe</br>%WindowsSdkDir%\tools\x64\Usbview.exe|Enumerates the USB host controllers, USB hubs, and attached USB devices and can query information about the devices from the registry and through USB requests to the devices.</br>The source code for the USB Device Viewer is available from the code gallery, see [USBVIEW Sample Application](/samples/microsoft/windows-driver-samples/usbview-sample-application/)|

### Bluetooth Drivers

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|Bluetooth Inquiry Record Verifier (Sdpverify.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x86\Sdpverifiy.exe</br>%WindowsSdkDir%\tools\x64\Sdpverifiy.exe|Displays a Bluetooth device's Inquiry Record as Windows interprets it.</br>WDK documentation: [Bluetooth Inquiry Record Verifier](bluetooth-inquiry-record-verifier.md)|

### Windows Image Acquisition (WIA) Drivers

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|WIADbgCfg (Wiadbgcfg.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x86\wiadbgcfg.exe</br>%WindowsSdkDir%\tools\x64\wiadbgcfg.exe|Enables logging for WIA drivers (Windows Server 2008 and later versions of Windows).</br>**Note** For earlier versions of Windows, use WIALogCfg.</br>%WindowsSdkDir%\tools\x86\wiadbgcfg.htm</br>%WindowsSdkDir%\tools\x64\wiadbgcfg.htm|
|WIAInfo2 (Wiainfo2.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x86\wiainfo2.exe</br>%WindowsSdkDir%\tools\x64\wiainfo2.exe|Displays the WIA item tree so that you can view and edit WIA device driver properties.</br>%WindowsSdkDir%\tools\x86\wiainfo2.htm</br>%WindowsSdkDir%\tools\x64\wiainfo2.htm|
|WIAPreview (Wiapreview.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\wiapreview.exe</br>%WindowsSdkDir%\tools\x86\wiapreview.exe|Shows how to use the WIA Preview component and the driver's segmentation filter.</br>%WindowsSdkDir%\tools\x64\wiapreview.htm</br>%WindowsSdkDir%\tools\x86\wiapreview.htm|
|WIATest (Wiatest.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\wiatest.exe</br>%WindowsSdkDir%\tools\x86\wiatest.exe|Displays the item tree that is created by the driver, the Windows Image Acquisition (WIA) properties exposed by the driver, and the current value of each property. You can use this tool to debug your driver during development and unit test.</br>%WindowsSdkDir%\tools\x64\wiatest.htm</br>%WindowsSdkDir%\tools\x64\wiatest.htm|
|Windows Imaging Trace File Viewer (Wiatrcvw.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\Wiatrcvw.exe</br>%WindowsSdkDir%\tools\x86\Wiatrcvw.exe|Displays the WIA trace log (%WINDIR%\Debug\WIA\wiatrace.log) and lets you change the WIA tracing parameters for each module.</br>%WindowsSdkDir%\tools\x64\Wiatrcvw.mht</br>%WindowsSdkDir%\tools\x64\Wiatrcvw.mht|

### Windows Portable Devices (WPD) Drivers

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|WpdDeviceInspector (WpdDeviceInspector.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\WpdDeviceInspector.exe</br>%WindowsSdkDir%\tools\x86\WpdDeviceInspector.exe|Queries a WPD driver and generates a comprehensive HTML report that describes your device and its capabilities. For example, you can use it to retrieve a list of supported device commands and objects. And, this tool will generate a list of all properties supported by each object.</br>WDK Documentation:</br>[Windows Portable Devices](/windows/win32/windows-portable-devices)</br>[WPD Driver Development Tools](../portable/familiarizing-yourself-with-the-sample-driver.md)|
|WpdInfo (WpdInfo.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\WpdInfo.exe</br>%WindowsSdkDir%\tools\x86\WpdInfo.exe|Performs common WPD operations such as: opening and closing a device, creating or deleting objects on a device, and issuing device commands.</br>WDK Documentation:</br>[Windows Portable Devices](/windows/win32/windows-portable-devices)</br>[WPD Driver Development Tools](../portable/familiarizing-yourself-with-the-sample-driver.md)|
|Microsoft Network Monitor (NetMon.exe)</br>**WDK tool:** No|Download the Microsoft Network Monitor</br>[NetMon.exe](https://www.microsoft.com/download/details.aspx?displaylang=en&id=4865)|Displays trace information from WPD components. This tool replaces WpdMon.exe which had shipped in previous versions of the WDK.</br>WDK Documentation:</br>[Windows Portable Devices](/windows/win32/windows-portable-devices)</br>[WPD Driver Development Tools](../portable/familiarizing-yourself-with-the-sample-driver.md), see [Using the Network Monitor Tool](../portable/using-the-netmon-tool.md).|

### Printer Drivers

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|GPDCheck (Gpdcheck.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\gpdcheck.exe</br>%WindowsSdkDir%\tools\x86\gpdcheck.exe|Validates the syntactical correctness of a Generic Printer Description File (GPD).</br>For information about command options, type </br>**gpdcheck /?**|
|INFGate (Infgate.exe)</br>**WDK tool:** Yes|WindowsSdkDir%\tools\x64\infgate.exe</br>%WindowsSdkDir%\tools\x86\infgate.exe.exe|Validates the conformance of a printer INF file.</br>For information about command options, type</br>**infgate /?**|
|isXPS (isXPS.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\isxps\isxps.exe</br>%WindowsSdkDir%\tools\x86\isxps\isxps.exe|Validates the conformance of an XPS file to the XPS and OPC specifications.</br>For information about command options, type</br>**isxps /?** in a Command prompt window.</br>For more information, see [isXPS Conformance Tool](/previous-versions/aa348104(v=vs.110))|
|Looksgood (Looksgood.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\looksgood.exe</br>%WindowsSdkDir%\tools\x86\looksgood.exe|Validates the correctness of an XPS rendering engine.</br>For information about command options, type</br>**looksgood /?**|
|MakeNTF (Makentf.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\makentf.exe</br>%WindowsSdkDir%\tools\x86\makentf.exe|Converts Adobe Font Metrics (AFM) files and East Asian font AFM files to Windows font files (.ntf).</br>WDK Documentation:</br>[Converting AFM Files to NTF Files](../print/converting-afm-files-to-ntf-files.md)</br>[Converting East Asian AFM Files to NTF Files](../print/converting-east-asian-afm-files-to-ntf-files.md)|
|PPDCheck (Ppdcheck.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\ppdcheck.exe</br>%WindowsSdkDir%\tools\x86\ppdcheck.exe|Validates the syntactical correctness of a PostScript Printer Description File (PPD).</br>For information about command options, type</br>**ppdcheck /?**|
|PTConform (PTConform.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\PTConform.exe</br>%WindowsSdkDir%\tools\x86\PTConform.exe|Validates a Print Ticket or Print Capabilities document for conformance to the Print Schema.</br>For information about command options, type</br>**ptconform /?**|
|XpsAnalyzer (XpsAnalyzer.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\XpsAnalyzer.exe</br>%WindowsSdkDir%\tools\x86\XpsAnalyzer.exe|Analyzes XML Paper Specification (XPS) files for compatibility with the XPS 1.0 specification.</br>WDK Documentation:</br>[XpsAnalyzer](xpsanalyzer.md)|

### Sensors

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|Sensor Diagnostic Tool (sensordiagnostictool.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64</br>%WindowsSdkDir%\tools\x86|Tests the driver, firmware, and hardware for sensor and location functionality. The tool invokes the sensor and location API to test data retrieval, event handling, report intervals, change sensitivity, property retrieval.</br>WDK Documentation:</br>[Testing sensor functionality with the Sensor Diagnostic Tool](../sensors/the-sensor-diagnostic-tool.md)|

### All Drivers

|Tool name|Tool location|Description and Help file location|
|----|----|----|
|BinPlace (Binplace.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x86\binplace.exe|Manages large coding projects by moving files, extracting symbols from executable files, and removing private symbols from symbol files.</br>WDK Documentation:</br>[BinPlace](binplace.md)|
|Code Analysis for Drivers</br>**WDK tool:** Yes|The Code Analysis tool is included in Visual Studio. The driver-specific component is added when you install the WDK.|A static verification tool that detects C and C++ coding errors. This version is specifically designed to detect errors in kernel-mode drivers.</br>WDK Documentation:</br>[Code Analysis for Drivers](code-analysis-for-drivers.md)|
|CertMgr (CertMgr.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\CertMgr.exe</br>%WindowsSdkDir%\bin\x86\CertMgr.exe|Manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs) that are used to sign drivers and [driver packages](../install/driver-packages.md).</br>WDK Documentation:</br>[CertMgr](certmgr.md)|
|ChkINF</br>**WDK tool:** Deprecated|Previous path:</br>%WindowsSdkDir%\tools\x86\Chkinf|ChkInf has been deprecated. Instead, use [InfVerif](infverif.md).</br>WDK Documentation:</br>[InfVerif](infverif.md)|
|Computer Hardware Identification Tool (ComputerHardwareIds.exe)</br>**WDK tool:** Yes|**Windows Driver Kit (WDK) 8:**</br>%WindowsSdkDir%\tools\x64\ComputerHardwareIds.exe</br>%WindowsSdkDir%\tools\x86\ComputerHardwareIds.exe</br>WDKPath\tools\Other\ia64\ComputerHardwareIds.exe</br>**Windows Driver Kit (WDK) 8.1:**</br>%WindowsSdkDir%\bin\x64\ComputerHardwareIds.exe</br>%WindowsSdkDir%\bin\x86\ComputerHardwareIds.exe</br>%WindowsSdkDir%\bin\arm\ComputerHardwareIds.exe|Derives the computer hardware IDs from SMBIOS information.</br>WDK Documentation:</br>[ComputerHardwareIds](computerhardwareids.md)|
|DC2WMIParser (DC2WMIParser.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\DC2WMIParser.exe</br>%WindowsSdkDir%\tools\x86\DC2WMIParser.exe|DC2WMIParser is a tool that collects the WMI IRP records created by Driver Verifier and converts this log to a text file.</br>Documentation:</br>[IRP Logging](./irp-logging.md)|
|Dependency Walker (Depends.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\depends.exe</br>%WindowsSdkDir%\tools\x86\depends.exe|Displays the dependence patterns of the modules that are required by an application in a tree diagram. The display includes numerous details, including the functions exported by each module, the functions actually called by other modules, and the minimum set of files that are required for a module to load and run.</br>In the tool, from the **Dependency Walker** Help menu, select **Help Topics**.|
|DevCon (Devcon.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\devcon.exe</br>%WindowsSdkDir%\tools\x86\devcon.exe|A command-line version of Device Manager. DevCon enables, disables, installs, configures, and removes devices on the local computer and displays detailed information about devices on local and remote computers.</br>WDK Documentation:</br>[DevCon](devcon.md)|
|Drivers (Drivers.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\drivers.exe</br>%WindowsSdkDir%\tools\x86\drivers.exe|Displays a list of all drivers that are installed on the computer.</br>WDK Documentation:</br>None|
|Driver Verifier (Verifier.exe)</br>**WDK tool:** No|%Windir%\system32\verifier.exe|Monitors kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. It can subject the drivers to a variety of stresses and tests to find improper behavior.</br>WDK Documentation:</br>[Driver Verifier](driver-verifier.md)|
|Driver Verification Log (DVL)</br>**WDK tool:** Yes|Requires Microsoft Visual Studio and the WDK. From the **Driver** menu, select **Create Driver Verification Log....**|The [Static Tools Logo Test](/windows-hardware/test/hlk/testref/6ab6df93-423c-4af6-ad48-8ea1049155ae) requires a Driver Verification Log (DVL) for all applicable driver submissions. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. See [Creating a Driver Verification Log](../develop/creating-a-driver-verification-log.md).|
|Enhanced Storage Certificate Management Tool (EhStorCertMgrCmd.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\ehstorcertmgrcmd.exe</br>%WindowsSdkDir%\tools\x86\ehstorcertmgrcmd.exe|Manages certificates on USB storage devices that are compliant with the IEEE 1667 standard.</br>WDK Documentation:</br>[Enhanced Storage Certificate Management Tool](enhanced-storage-certificate-management-tool.md)|
|Event and Performance Counter Manifest Generator Tool (ECManGen.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\ECManGen.exe</br>%WindowsSdkDir%\bin\x86\ECManGen.exe|A tool for creating an event or performance counter manifest (*.man) from scratch without ever having to use XML tags. For information about creating manifest files, see [Writing an Instrumentation Manifest (Windows)](/windows/desktop/WES/writing-an-instrumentation-manifest) section and [Adding Event Tracing to Kernel-Mode Drivers](adding-event-tracing-to-kernel-mode-drivers.md)|
|Inf2Cat (Inf2cat.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\inf2cat.exe</br>%WindowsSdkDir%\bin\x86\inf2cat.exe|Determines whether a [driver package's](../install/driver-packages.md) INF file can be digitally-signed for a specified list of Windows versions, and, if so, generates the unsigned [catalog files](../install/catalog-files.md) that apply to the specified Windows versions.</br>WDK Documentation:</br>[Inf2Cat](inf2cat.md)|
|InfVerif (InfVerif.exe)</br>**WDK tool:** Yes|c:\Program Files(x86)\Windows Kits\10\tools\arm\infverif.exe</br>c:\Program Files(x86)\Windows Kits\10\tools\arm64\infverif.exe</br>c:\Program Files(x86)\Windows Kits\10\tools\x86\infverif.exe</br>c:\Program Files(x86)\Windows Kits\10\tools\x64\infverif.exe|Tests a driver INF file. In addition to reporting INF syntax problems, the tool reports if the INF file is universal.</br>WDK Documentation:</br>[InfVerif](infverif.md)|
|MakeCat (MakeCat.exe)</br>**WDK tool:** Yes|WDKPath\bin\amd64\MakeCat.exe</br>WDKPath\bin\ia64\MakeCat.exe</br>WDKPath\bin\x86\MakeCat.exe|Creates a [catalog file](../install/catalog-files.md) for a [driver package](../install/driver-packages.md).</br>WDK Documentation:</br>[MakeCat](makecat.md)|
|MakeCert (MakeCert.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\MakeCert.exe</br>%WindowsSdkDir%\bin\x86\MakeCert.exe|Creates an X.509 certificate that is signed by a system test root key or by another specified key.</br>WDK Documentation:</br>[MakeCert](makecert.md)|
|MSBuild (MSBuild.exe)/br>**WDK tool:** No|Installed with Visual Studio|Builds the samples, drivers, and associated software components that are supplied in the Microsoft WDK.</br>[MSBuild]( /visualstudio/msbuild/msbuild)|
|PnpCpu (PnPCpu.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\PnPCpu.exe</br>%WindowsSdkDir%\tools\x86\PnPCpu.exe|Simulates a hot add of processors to a running instance of Windows Server 2008.</br>WDK Documentation:</br>[PNPCPU](pnpcpu.md)|
|PnPUtil (PnPUtil.exe)</br>**WDK tool:** No|%Windir%\system32\pnputil.exe|A command-line tool that installs or deletes [driver packages](../install/driver-packages.md) from the Windows driver store.</br>WDK Documentation:</br>[PnPUtil](pnputil.md)|
|PoolMon (Poolmon.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\poolmon.exe</br>%WindowsSdkDir%\tools\x86\poolmon.exe|Displays data that the operating system collects about memory allocations from the system's paged and nonpaged kernel pools, and the memory pools used for Terminal Services sessions. The data is grouped by pool allocation tag.</br>WDK Documentation:</br>[PoolMon](poolmon.md)|
|PowerCfg (PowerCfg.exe)</br>**WDK tool:** No|%Windir%\system32\powercfg.exe|A command-line tool that is used to evaluate system energy efficiency.</br>Dev Center Documentation:</br>[Using PowerCfg to Evaluate System Energy Efficiency](https://download.microsoft.com/download/7/E/7/7E7662CF-CBEA-470B-A97E-CE7CE0D98DC2/PowerCfg.docx)</br>For information about command options, type</br>**PowerCfg /?**|
|Pvk2Pfx (Pvk2Pfx.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\Pvk2Pfx.exe</br>%WindowsSdkDir%\bin\x86\Pvk2Pfx.exe|Copies public key and private key information contained in .spc, .cer, and .pvk files to a personal information exchange (.pfx) file.</br>WDK Documentation:</br>[Pvk2Pfx](pvk2pfx.md)|
|PwrTest (Pwrtest.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\pwrtest.exe</br>%WindowsSdkDir%\tools\x86\pwrtest.exe|A power management tool that exercises and records power management information from the computer.</br>WDK Documentation:</br>[PwrTest](pwrtest.md)|
|SignTool (SignTool.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\SignTool.exe</br>%WindowsSdkDir%\bin\x86\SignTool.exe|Digitally-signs files, verifies signatures in files, and time-stamps files.</br>WDK Documentation:</br>[SignTool](signtool.md)|
|Stampinf (Stampinf.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\stampinf.exe</br>%WindowsSdkDir%\bin\x86\stampinf.exe|Updates common INF file directives, including the **DriverVer** directive.</br>WDK Documentation:</br>[Stampinf](stampinf.md)|
|Static Driver Verifier</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\SDV</br></br>**Note**  Launch Static Driver Verifier from the **Driver** menu in Visual Studio.|A static verification tool for drivers that systematically analyzes the source code of Windows drivers and determines whether the driver properly interacts with the Windows operating system kernel.</br>WDK Documentation:</br>[Static Driver Verifier](static-driver-verifier.md)|
|Tracefmt (Tracefmt.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\tracefmt.exe</br>%WindowsSdkDir%\bin\x86\tracefmt.exe|Formats and displays trace messages from an event trace log file (.etl) or a real-time trace session.</br>WDK Documentation:</br>[Tracefmt](tracefmt.md)|
|TraceLog (Tracelog.exe)</br>**WDK tool:** Yes|**WDK 8:**</br>%WindowsSdkDir%\tools\x64\tracelog.exe</br>%WindowsSdkDir%\tools\x86\tracelog.exe</br>**WDK 8.1:**</br>%WindowsSdkDir%\bin\x64\tracelog.exe</br>%WindowsSdkDir%\bin\x86\tracelog.exe</br>%WindowsSdkDir%\bin\arm\tracelog.exe|Configures and controls trace sessions from the command line. Measures time spent in deferred procedure calls (DPCs) and interrupt service routines (ISRs).</br>WDK Documentation:</br>[Tracelog](tracelog.md)|
|TracePDB (Tracepdb.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\tracepdb.exe</br>%WindowsSdkDir%\bin\x86\tracepdb.exe|Creates trace message format (.tmf) files from the full or private PDB symbol file for a WPP trace provider.</br>WDK Documentation:</br>[Tracepdb](tracepdb.md)|
|TraceView (Traceview.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\TraceView.exe</br>%WindowsSdkDir%\tools\x86\TraceView.exe|Configures and controls trace sessions and displays formatted trace messages from real-time trace sessions and trace logs. TraceView has a graphic user interface and a command-line interface for batch processing and scripting.</br>WDK Documentation:</br>[TraceView](traceview.md)|
|TraceWPP (Tracewpp.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\tracewpp.exe</br>%WindowsSdkDir%\bin\x86\tracewpp.exe|Runs the Windows Software Trace Preprocessor (WPP).</br>WDK Documentation:</br>[WPP Preprocessor](wpp-preprocessor.md)</br>[Survey of Software Tracing Tools](survey-of-software-tracing-tools.md)|
|WDF Tester</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64</br>%WindowsSdkDir%\tools\x86|A set of tools that can be used to test, verify, and debug WDF drivers. The toolset provides a WMI programming interface that can be used in a script or a compiled application.</br>WDK Documentation:</br>[WdfTester: WDF Driver Testing Toolset](wdftester--wdf-driver-testing-toolset.md)|
|WDF Verifier (Wdfverifier.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\wdfverifier.exe</br>%WindowsSdkDir%\tools\x86\wdfverifier.exe|Provides an easy-to-use interface to the framework's verifier for KMDF and UMDF drivers.</br>WDK Documentation:</br>[WDF Verifier Control Application](wdf-verifier-control-application.md)|
|Web Services on devices (WSD) Basic Interoperability Tool (WSDBIT)</br>**WDK tool:** Yes|**WSDBIT Client:**</br>%WindowsSdkDir%\tools\x64\wsdbit_client.exe</br>%WindowsSdkDir%\tools\x86\wsdbit_client.exe</br>**WSDBIT Server:**</br>%WindowsSdkDir%\tools\x64\wsdbit_server.exe</br>%WindowsSdkDir%\tools\x86\wsdbit_server.exe|Verifies an implementation of Device Profile for Web Services (DPWS) works with WSDAPI.</br>WDK Documentation:</br>[WSD Interoperability Tool](wsdapi-basic-interoperability-tool.md)|
|Winerror (Winerror.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\tools\x64\winerror.exe</br>%WindowsSdkDir%\tools\x86\winerror.exe|Returns the error message identifier and mapping information for the specified error (Winerror.h) or success codes (Ntstatus.h).</br>For information about command options, type</br>**winerror /?**|
|WMIMofCk (Wmimofck.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x86\wmimofck.exe|WDK Documentation:</br>[Using wmimofck.exe](../kernel/using-wmimofck-exe.md)</br>For information about command options, type</br>**wmimofck -?**|
|WsdCodeGen (Wsdcodegen.exe)</br>**WDK tool:** Yes|%WindowsSdkDir%\bin\x64\wsdcodegen.exe</br>%WindowsSdkDir%\bin\x86\wsdcodegen.exe|Automatically generates proxies and stubs based on a Web Services contract. Primarily, you can use this tool to create client applications. However, you can use it for testing or for creating user-mode drivers.</br>Verifies that the classes, properties, methods and events specified in a binary MOF file (.bmf) are valid for WMI use. Generates MOF support files.</br>Windows SDK:</br>See the [Web Services on Devices](/windows/win32/wsdapi/wsd-portal) section|
|WSDDebug_client and WSDDebug_host</br>**WDK tool:** Yes|**Debug Client:**</br>%WindowsSdkDir%\bin\x64\WSDDebug_client.exe</br>%WindowsSdkDir%\bin\x86\WSDDebug_client.exe</br>**Debug Host:**</br>%WindowsSdkDir%\bin\x64\WSDDebug_host.exe</br>
%WindowsSdkDir%\bin\x86\WSDDebug_host.exe|These tools are a soft device and client that you can use to troubleshoot devices or applications.</br>Windows SDK:</br>[Web Services on Devices](/windows/win32/wsdapi/wsd-portal) section|

### Supported platforms

You can run the Windows 10 WDK on Windows 7 and later, and use it to develop drivers for these operating systems:

RUNTIME REQUIREMENTS

|Client OS|Server OS|
|----|----|
|Windows 10|Windows Server 2019, Windows Server 2016|
|Windows 8.1|Windows Server 2012 R2|
|Windows 8|Windows Server 2012|
|Windows 7|Windows Server 2008 R2 SP1|
