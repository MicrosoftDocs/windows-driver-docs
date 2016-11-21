---
title: Index of Windows Driver Kit Tools
description: Index of Windows Driver Kit Tools
ms.assetid: 26db88c4-8fb8-4308-ab8a-1a1eef5e19d8
keywords: ["Disabler tool", "DbgCon tool", "Sniffir tool", "Sledge tool", "Call Usage Verifier tool", "CUV tool", "tools WDK , listed", "driver development tools WDK , listed", "Sleep State Chooser", "sleeper", "Acpislp", "Manual Power State Change Test", "GUIDGen WDK", "GUID Generator WDK", "GUIDGen.exe WDK"]
---

# Index of Windows Driver Kit Tools


This topic supplies basic information about the tools that are included in the Windows Driver Kit (WDK). This topic also includes references to other tools that are useful for driver development. These other tools are either available as part of the operating system or are available as separate download. For more information about each tool, see the documentation in this topic that describes the tool.

For information about how to obtain the latest WDK, see [Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p/?linkid=261797).

This topic includes the following:

-   [Index of WDK Tools](#index-of-wdk-tools)
-   [What's New in the WDK for Windows 8.1](#what-s-new-in-the-wdk-for-windows8-1)
-   [What's New in the WDK for Windows 8](#what-s-new-in-the-wdk-for-windows8)
-   [What's Changed in the WDK for Windows 8](#what-s-changed-in-the-wdk-for-windows8)
-   [Supported platforms](#supported-os-wdk-for-win8)

### <span id="index_of_wdk_tools"></span><span id="INDEX_OF_WDK_TOOLS"></span>Index of WDK Tools

The information in the following tables describes the tools that are useful for Windows driver developers. The list of tools includes tools that ship with the WDK (as indicated by the **WDK tool** field) and also includes some tools that are available separately or that are installed with Windows. Tools that can generally be used with all drivers are listed under [All Drivers](#tech-all). Tools that are specific to a technology are grouped together, for example, tools that are specific for [Windows Portable Devices (WPD) Drivers](#tech-wpd) or [Sensors](#tech-sensors).

-   [Audio/Video Drivers](#tech-audio-video)
-   [Bluetooth Drivers](#tech-bluetooth)
-   [Windows Image Acquisition (WIA) Drivers](#tech-wia)
-   [Windows Portable Devices (WPD) Drivers](#tech-wpd)
-   [Printer Drivers](#tech-printer)
-   [Sensors](#tech-sensors)
-   [All Drivers](#tech-all)

**Note**  The Visual Studio environment variable, %WindowsSdkDir%, represents the path to the Windows kits directory where this version of the WDK is installed, for example, C:\\Program Files (x86)\\Windows Kits\\8.1.

 

### <span id="tech_audio_video"></span><span id="TECH_AUDIO_VIDEO"></span>Technology: Audio / Video Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Display Color Calibration tool (Dccw.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>%Windir%\System32\Dccw.exe</p></td>
<td align="left"><p>A calibration tool that lets users adjust their display color to be closer to the Windows and World Wide Web international standard red-green-blue (sRGB) color space.</p>
<p>WHDC Documentation:</p>
<p>[MCCS Use by Windows 7 Display Color Calibration Tool](http://go.microsoft.com/fwlink/p/?linkid=150003)</p></td>
</tr>
<tr class="even">
<td align="left"><p>GraphEdt (Graphedt.exe)</p>
<p><strong>Tool in WDK:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\graphedt.exe</p>
<p>%WindowsSdkDir%\tools\x64\graphedt.exe</p></td>
<td align="left"><p>Builds filter graphs to test streaming audio/video capture drivers.</p>
<p>MSDN Documentation:</p>
<p>[Overview of GraphEdit](http://go.microsoft.com/fwlink/p/?linkid=9230)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>KSStudio (KsStudio.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\KsStudio.exe</p>
<p>%WindowsSdkDir%\tools\x64\KsStudio.exe</p>
<div class="alert">
<strong>Note</strong>   This tool must be run by someone who has administrator privileges.
</div>
<div>
 
</div></td>
<td align="left"><p>This tool can construct a graphical representation of a filter graph that shows the pin-to-pin connections between filters and the filters' internal nodes.</p>
<p>%WindowsSdkDir%\tools\x86\KsStudio.chm</p>
<p>%WindowsSdkDir%\tools\x64\KsStudio.chm</p>
<p>See [AVStream Testing and Debugging](https://msdn.microsoft.com/library/windows/hardware/ff554257) for more information.</p></td>
</tr>
<tr class="even">
<td align="left"><p>USB Device Viewer (Usbview.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\Usbview.exe</p>
<p>%WindowsSdkDir%\tools\x64\Usbview.exe</p></td>
<td align="left"><p>Enumerates the USB host controllers, USB hubs, and attached USB devices and can query information about the devices from the registry and through USB requests to the devices.</p>
<p>The source code for the USB Device Viewer is available from the code gallery, see [USBVIEW Sample Application](http://go.microsoft.com/fwlink/p/?linkid=256205).</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_bluetooth"></span><span id="TECH_BLUETOOTH"></span>Technology: Bluetooth Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Bluetooth Inquiry Record Verifier (Sdpverify.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\Sdpverifiy.exe</p>
<p>%WindowsSdkDir%\tools\x64\Sdpverifiy.exe</p></td>
<td align="left"><p>Displays a Bluetooth device's Inquiry Record as Windows interprets it.</p>
<p>WDK documentation:</p>
<p>[Bluetooth Inquiry Record Verifier](bluetooth-inquiry-record-verifier.md)</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_wia"></span><span id="TECH_WIA"></span>Technology: Windows Image Acquisition (WIA) Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WIADbgCfg (Wiadbgcfg.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\wiadbgcfg.exe</p>
<p>%WindowsSdkDir%\tools\x64\wiadbgcfg.exe</p></td>
<td align="left"><p>Enables logging for WIA drivers (Windows Server 2008 and later versions of Windows).</p>
<div class="alert">
<strong>Note</strong>   For earlier versions of Windows, use WIALogCfg.
</div>
<div>
 
</div>
<p>%WindowsSdkDir%\tools\x86\wiadbgcfg.htm</p>
<p>%WindowsSdkDir%\tools\x64\wiadbgcfg.htm</p></td>
</tr>
<tr class="even">
<td align="left"><p>WIAInfo2 (Wiainfo2.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\wiainfo2.exe</p>
<p>%WindowsSdkDir%\tools\x64\wiainfo2.exe</p></td>
<td align="left"><p>Displays the WIA item tree so that you can view and edit WIA device driver properties.</p>
<p>%WindowsSdkDir%\tools\x86\wiainfo2.htm</p>
<p>%WindowsSdkDir%\tools\x64\wiainfo2.htm</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WIAPreview (Wiapreview.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\wiapreview.exe</p>
<p>%WindowsSdkDir%\tools\x86\wiapreview.exe</p></td>
<td align="left"><p>Shows how to use the WIA Preview component and the driver's segmentation filter.</p>
<p>%WindowsSdkDir%\tools\x64\wiapreview.htm</p>
<p>%WindowsSdkDir%\tools\x86\wiapreview.htm</p></td>
</tr>
<tr class="even">
<td align="left"><p>WIATest (Wiatest.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\wiatest.exe</p>
<p>%WindowsSdkDir%\tools\x86\wiatest.exe</p></td>
<td align="left"><p>Displays the item tree that is created by the driver, the Windows Image Acquisition (WIA) properties exposed by the driver, and the current value of each property. You can use this tool to debug your driver during development and unit test.</p>
<p>%WindowsSdkDir%\tools\x64\wiatest.htm</p>
<p>%WindowsSdkDir%\tools\x64\wiatest.htm</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Windows Imaging Trace File Viewer (Wiatrcvw.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\Wiatrcvw.exe</p>
<p>%WindowsSdkDir%\tools\x86\Wiatrcvw.exe</p></td>
<td align="left"><p>Displays the WIA trace log (%WINDIR%\Debug\WIA\wiatrace.log) and lets you change the WIA tracing parameters for each module.</p>
<p>%WindowsSdkDir%\tools\x64\Wiatrcvw.mht</p>
<p>%WindowsSdkDir%\tools\x64\Wiatrcvw.mht</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_wpd"></span><span id="TECH_WPD"></span>Technology: Windows Portable Devices (WPD) Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>WpdDeviceInspector (WpdDeviceInspector.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\WpdDeviceInspector.exe</p>
<p>%WindowsSdkDir%\tools\x86\WpdDeviceInspector.exe</p></td>
<td align="left"><p>Queries a WPD driver and generates a comprehensive HTML report that describes your device and its capabilities. For example, you can use it to retrieve a list of supported device commands and objects. And, this tool will generate a list of all properties supported by each object.</p>
<p>WDK Documentation:</p>
<p>[Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527)</p>
<p>[WPD Driver Development Tools](http://go.microsoft.com/fwlink/p/?linkid=262664)</p></td>
</tr>
<tr class="even">
<td align="left"><p>WpdInfo (WpdInfo.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\WpdInfo.exe</p>
<p>%WindowsSdkDir%\tools\x86\WpdInfo.exe</p></td>
<td align="left"><p>Performs common WPD operations such as: opening and closing a device, creating or deleting objects on a device, and issuing device commands.</p>
<p>WDK Documentation:</p>
<p>[Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527)</p>
<p>[WPD Driver Development Tools](http://go.microsoft.com/fwlink/p/?linkid=262664)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Microsoft Network Monitor (NetMon.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>Download the Microsoft Network Monitor (NetMon.exe [here](http://go.microsoft.com/fwlink/p/?linkid=248501).</p></td>
<td align="left"><p>Displays trace information from WPD components. This tool replaces WpdMon.exe which had shipped in previous versions of the WDK.</p>
<p>WDK Documentation:</p>
<p>[Windows Portable Devices](http://go.microsoft.com/fwlink/p/?linkid=106527)</p>
<p>[WPD Driver Development Tools](http://go.microsoft.com/fwlink/p/?linkid=262664), see [Using the Network Monitor Tool](https://msdn.microsoft.com/library/windows/hardware/hh451296).</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_printer"></span><span id="TECH_PRINTER"></span>Technology: Printer Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>GPDCheck (Gpdcheck.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\gpdcheck.exe</p>
<p>%WindowsSdkDir%\tools\x86\gpdcheck.exe</p></td>
<td align="left"><p>Validates the syntactical correctness of a Generic Printer Description File (GPD).</p>
<p>For information about command options, type</p>
<p><strong>gpdcheck /?</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>INFGate (Infgate.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\infgate.exe</p>
<p>%WindowsSdkDir%\tools\x86\infgate.exe.exe</p></td>
<td align="left"><p>Validates the conformance of a printer INF file.</p>
<p>For information about command options, type</p>
<p><strong>infgate /?</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>isXPS (isXPS.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\isxps\isxps.exe</p>
<p>%WindowsSdkDir%\tools\x86\isxps\isxps.exe</p></td>
<td align="left"><p>Validates the conformance of an XPS file to the XPS and OPC specifications.</p>
<p>For information about command options, type</p>
<p><strong>isxps /?</strong> in a Command prompt window.</p>
<p>For more information, see [isXPS Conformance Tool](http://go.microsoft.com/fwlink/p/?linkid=150004) in the Windows MSDN library.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Looksgood (Looksgood.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\looksgood.exe</p>
<p>%WindowsSdkDir%\tools\x86\looksgood.exe</p></td>
<td align="left"><p>Validates the correctness of an XPS rendering engine.</p>
<p>For information about command options, type</p>
<p><strong>looksgood /?</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>MakeNTF (Makentf.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\makentf.exe</p>
<p>%WindowsSdkDir%\tools\x86\makentf.exe</p></td>
<td align="left"><p>Converts Adobe Font Metrics (AFM) files and East Asian font AFM files to Windows font files (.ntf).</p>
<p>WDK Documentation:</p>
<p>[Converting AFM Files to NTF Files](https://msdn.microsoft.com/library/windows/hardware/ff546364)</p>
<p>[Converting East Asian AFM Files to NTF Files](https://msdn.microsoft.com/library/windows/hardware/ff546366)</p></td>
</tr>
<tr class="even">
<td align="left"><p>PPDCheck (Ppdcheck.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\ppdcheck.exe</p>
<p>%WindowsSdkDir%\tools\x86\ppdcheck.exe</p></td>
<td align="left"><p>Validates the syntactical correctness of a PostScript Printer Description File (PPD).</p>
<p>For information about command options, type</p>
<p><strong>ppdcheck /?</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>PTConform (PTConform.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\PTConform.exe</p>
<p>%WindowsSdkDir%\tools\x86\PTConform.exe</p></td>
<td align="left"><p>Validates a Print Ticket or Print Capabilities document for conformance to the Print Schema.</p>
<p>For information about command options, type</p>
<p><strong>ptconform /?</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>XpsAnalyzer (XpsAnalyzer.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\XpsAnalyzer.exe</p>
<p>%WindowsSdkDir%\tools\x86\XpsAnalyzer.exe</p></td>
<td align="left"><p>Analyzes XML Paper Specification (XPS) files for compatibility with the XPS 1.0 specification.</p>
<p>WDK Documentation:</p>
<p>[XpsAnalyzer](xpsanalyzer.md)</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_sensors"></span><span id="TECH_SENSORS"></span>Technology: Sensors

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Sensor Diagnostic Tool (sensordiagnostictool.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\\</p>
<p>%WindowsSdkDir%\tools\x86\\</p></td>
<td align="left"><p>Tests the driver, firmware, and hardware for sensor and location functionality. The tool invokes the sensor and location API to test data retrieval, event handling, report intervals, change sensitivity, property retrieval.</p>
<p>WDK Documentation:</p>
<p>[Testing sensor functionality with the Sensor Diagnostic Tool](https://msdn.microsoft.com/library/windows/hardware/hh780319)</p></td>
</tr>
</tbody>
</table>

 

### <span id="tech_all"></span><span id="TECH_ALL"></span>Technology: All Drivers

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Tool name</th>
<th align="left">Tool location</th>
<th align="left">Description and Help file location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>BinPlace (Binplace.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x86\binplace.exe</p></td>
<td align="left"><p>Manages large coding projects by moving files, extracting symbols from executable files, and removing private symbols from symbol files.</p>
<p>WDK Documentation:</p>
<p>[BinPlace](binplace.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Code Analysis for Drivers</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>The Code Analysis tool is included in Visual Studio. The driver-specific component is added when you install the WDK.</p></td>
<td align="left"><p>A static verification tool that detects C and C++ coding errors. This version is specifically designed to detect errors in kernel-mode drivers.</p>
<div class="alert">
<strong>Note</strong>  In previous versions of the WDK, this feature was part of OACR and was also available as the standalone tool PREfast for Drivers. Starting with Visual Studio 2012, the feature is now integrated into Visual Studio.
</div>
<div>
 
</div>
<p>WDK Documentation:</p>
<p>[Code Analysis for Drivers](code-analysis-for-drivers.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>CertMgr (CertMgr.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\CertMgr.exe</p>
<p>%WindowsSdkDir%\bin\x86\CertMgr.exe</p></td>
<td align="left"><p>Manages certificates, certificate trust lists (CTLs), and certificate revocation lists (CRLs) that are used to sign drivers and [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840).</p>
<p>WDK Documentation:</p>
<p>[<strong>CertMgr</strong>](certmgr.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>ChkINF</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x86\Chkinf</p></td>
<td align="left"><p>A set of Perl scripts that verify the structure and syntax of setup information (INF) files for drivers.</p>
<p>WDK Documentation:</p>
<p>[ChkINF](chkinf.md)</p>
<p>[Using ChkINF with Modem INF Files](https://msdn.microsoft.com/library/windows/hardware/ff542789)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Computer Hardware Identification Tool (ComputerHardwareIds.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p><strong>Windows Driver Kit (WDK) 8:</strong></p>
<p>%WindowsSdkDir%\tools\x64\ComputerHardwareIds.exe</p>
<p>%WindowsSdkDir%\tools\x86\ComputerHardwareIds.exe</p>
<p>WDKPath\tools\Other\ia64\ComputerHardwareIds.exe</p>
<p><strong>Windows Driver Kit (WDK) 8.1:</strong></p>
<p>%WindowsSdkDir%\bin\x64\ComputerHardwareIds.exe</p>
<p>%WindowsSdkDir%\bin\x86\ComputerHardwareIds.exe</p>
<p>%WindowsSdkDir%\bin\arm\ComputerHardwareIds.exe</p></td>
<td align="left"><p>Derives the computer hardware IDs from SMBIOS information.</p>
<p>WDK Documentation:</p>
<p>[ComputerHardwareIds](computerhardwareids.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>DC2WMIParser (DC2WMIParser.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\DC2WMIParser.exe</p>
<p>%WindowsSdkDir%\tools\x86\DC2WMIParser.exe</p></td>
<td align="left"><p>DC2WMIParser is a tool that collects the WMI IRP records created by Driver Verifier and converts this log to a text file.</p>
<p>MSDN Documentation:</p>
<p>[IRP Logging](http://go.microsoft.com/fwlink/p/?LinkId=698758)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Dependency Walker (Depends.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\depends.exe</p>
<p>%WindowsSdkDir%\tools\x86\depends.exe</p></td>
<td align="left"><p>Displays the dependence patterns of the modules that are required by an application in a tree diagram. The display includes numerous details, including the functions exported by each module, the functions actually called by other modules, and the minimum set of files that are required for a module to load and run.</p>
<p>In the tool, from the <strong>Dependency Walker</strong> Help menu, select <strong>Help Topics</strong>.</p></td>
</tr>
<tr class="even">
<td align="left"><p>DevCon (Devcon.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\devcon.exe</p>
<p>%WindowsSdkDir%\tools\x86\devcon.exe</p></td>
<td align="left"><p>A command-line version of Device Manager. DevCon enables, disables, installs, configures, and removes devices on the local computer and displays detailed information about devices on local and remote computers.</p>
<p>WDK Documentation:</p>
<p>[DevCon](devcon.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Drivers (Drivers.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\drivers.exe</p>
<p>%WindowsSdkDir%\tools\x86\drivers.exe</p></td>
<td align="left"><p>Displays a list of all drivers that are installed on the computer.</p>
<p>WDK Documentation:</p>
<p>None</p></td>
</tr>
<tr class="even">
<td align="left"><p>Driver Verifier (Verifier.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>%Windir%\system32\verifier.exe</p></td>
<td align="left"><p>Monitors kernel-mode drivers and graphics drivers to detect illegal function calls or actions that might corrupt the system. It can subject the drivers to a variety of stresses and tests to find improper behavior.</p>
<p>WDK Documentation:</p>
<p>[Driver Verifier](driver-verifier.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Driver Verification Log (DVL)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>Requires Microsoft Visual Studio and the WDK. From the <strong>Driver</strong> menu, click <strong>Create Driver Verification Log....</strong></p></td>
<td align="left"><p>The [Windows Server 2012 Hardware Certification Program](http://go.microsoft.com/fwlink/p/?linkid=227016) requires a Driver Verification Log (DVL) for all applicable driver submissions. The DVL contains a summary of the results from the Code Analysis and Static Driver Verifier log files. See [Creating a Driver Verification Log](https://msdn.microsoft.com/windows-drivers/develop/creating_a_driver_verification_log).</p></td>
</tr>
<tr class="even">
<td align="left"><p>Enhanced Storage Certificate Management Tool (EhStorCertMgrCmd.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\ehstorcertmgrcmd.exe</p>
<p>%WindowsSdkDir%\tools\x86\ehstorcertmgrcmd.exe</p></td>
<td align="left"><p>Manages certificates on USB storage devices that are compliant with the IEEE 1667 standard.</p>
<p>WDK Documentation:</p>
<p>[Enhanced Storage Certificate Management Tool](enhanced-storage-certificate-management-tool.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Event and Performance Counter Manifest Generator Tool (ECManGen.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\ECManGen.exe</p>
<p>%WindowsSdkDir%\bin\x86\ECManGen.exe</p></td>
<td align="left"><p>A tool for creating an event or performance counter manifest (*.man) from scratch without ever having to use XML tags. For information about creating manifest files, see [Writing an Instrumentation Manifest (Windows)](https://msdn.microsoft.com/library/windows/desktop/dd996930) section and [Adding Event Tracing to Kernel-Mode Drivers](adding-event-tracing-to-kernel-mode-drivers.md).</p></td>
</tr>
<tr class="even">
<td align="left"><p>GUIDgen (Guidgen.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>Download available from [Microsoft Exchange Server GUID Generator](http://go.microsoft.com/fwlink/p/?linkid=121586)</p></td>
<td align="left"><p>Generates globally unique identifiers (GUID) that you can use to identify your classes, objects, and interfaces. The generated GUID is copied to the Clipboard in one of four formats so that you can insert it into your source code.</p>
<p>GUIDGEN.doc (included in the download package)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Inf2Cat (Inf2cat.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\inf2cat.exe</p>
<p>%WindowsSdkDir%\bin\x86\inf2cat.exe</p></td>
<td align="left"><p>Determines whether a [driver package's](https://msdn.microsoft.com/library/windows/hardware/ff544840) INF file can be digitally-signed for a specified list of Windows versions, and, if so, generates the unsigned [catalog files](https://msdn.microsoft.com/library/windows/hardware/ff537872) that apply to the specified Windows versions.</p>
<p>WDK Documentation:</p>
<p>[<strong>Inf2Cat</strong>](inf2cat.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>MakeCat (MakeCat.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>WDKPath\bin\amd64\MakeCat.exe</p>
<p>WDKPath\bin\ia64\MakeCat.exe</p>
<p>WDKPath\bin\x86\MakeCat.exe</p></td>
<td align="left"><p>Creates a [catalog file](https://msdn.microsoft.com/library/windows/hardware/ff537872) for a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840).</p>
<p>WDK Documentation:</p>
<p>[MakeCat](makecat.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>MakeCert (MakeCert.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\MakeCert.exe</p>
<p>%WindowsSdkDir%\bin\x86\MakeCert.exe</p></td>
<td align="left"><p>Creates an X.509 certificate that is signed by a system test root key or by another specified key.</p>
<p>WDK Documentation:</p>
<p>[<strong>MakeCert</strong>](makecert.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>MSBuild (MSBuild.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>Installed with Visual Studio</p></td>
<td align="left"><p>Builds the samples, drivers, and associated software components that are supplied in the Microsoft WDK.</p>
<p>[MSBuild]( http://go.microsoft.com/fwlink/p/?linkid=262804)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PnpCpu (PnPCpu.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\PnPCpu.exe</p>
<p>%WindowsSdkDir%\tools\x86\PnPCpu.exe</p></td>
<td align="left"><p>Simulates a hot add of processors to a running instance of Windows Server 2008.</p>
<p>WDK Documentation:</p>
<p>[PNPCPU](pnpcpu.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>PnPUtil (PnPUtil.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>%Windir%\system32\pnputil.exe</p></td>
<td align="left"><p>A command-line tool that installs or deletes [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840) from the Windows driver store.</p>
<p>This tool is available in Windows 7 and later versions of Windows.</p>
<p>WDK Documentation:</p>
<p>[PnPUtil](pnputil.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>PoolMon (Poolmon.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\poolmon.exe</p>
<p>%WindowsSdkDir%\tools\x86\poolmon.exe</p></td>
<td align="left"><p>Displays data that the operating system collects about memory allocations from the system's paged and nonpaged kernel pools, and the memory pools used for Terminal Services sessions. The data is grouped by pool allocation tag.</p>
<p>WDK Documentation:</p>
<p>[PoolMon](poolmon.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>PowerCfg (PowerCfg.exe)</p>
<p><strong>WDK tool:</strong> No</p></td>
<td align="left"><p>%Windir%\system32\powercfg.exe</p></td>
<td align="left"><p>A command-line tool that is used to evaluate system energy efficiency.</p>
<p>This tool is available in Windows 7 and later versions of Windows.</p>
<p>Dev Center Documentation:</p>
[Using PowerCfg to Evaluate System Energy Efficiency](http://go.microsoft.com/fwlink/p/?linkid=168800)
<p>For information about command options, type</p>
<p></p>
<p><strong>PowerCfg /?</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>Pvk2Pfx (Pvk2Pfx.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\Pvk2Pfx.exe</p>
<p>%WindowsSdkDir%\bin\x86\Pvk2Pfx.exe</p></td>
<td align="left"><p>Copies public key and private key information contained in .spc, .cer, and .pvk files to a personal information exchange (.pfx) file.</p>
<p>WDK Documentation:</p>
<p>[<strong>Pvk2Pfx</strong>](pvk2pfx.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>PwrTest (Pwrtest.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\pwrtest.exe</p>
<p>%WindowsSdkDir%\tools\x86\pwrtest.exe</p></td>
<td align="left"><p>A power management tool for Windows 7 and later that exercises and records power management information from the computer.</p>
<p>WDK Documentation:</p>
<p>[PwrTest](pwrtest.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>SignTool (SignTool.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\SignTool.exe</p>
<p>%WindowsSdkDir%\bin\x86\SignTool.exe</p></td>
<td align="left"><p>Digitally-signs files, verifies signatures in files, and time-stamps files.</p>
<p>WDK Documentation:</p>
<p>[<strong>SignTool</strong>](signtool.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Stampinf (Stampinf.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\stampinf.exe</p>
<p>%WindowsSdkDir%\bin\x86\stampinf.exe</p></td>
<td align="left"><p>Updates common INF file directives, including the <strong>DriverVer</strong> directive.</p>
<p>WDK Documentation:</p>
<p>[Stampinf](stampinf.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Static Driver Verifier</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\SDV</p>
<p></p>
<div class="alert">
<strong>Note</strong>  Launch Static Driver Verifier from the <strong>Driver</strong> menu in Visual Studio.
</div>
<div>
 
</div></td>
<td align="left"><p>A static verification tool for drivers that systematically analyzes the source code of Windows drivers and determines whether the driver properly interacts with the Windows operating system kernel.</p>
<p>WDK Documentation:</p>
<p>[Static Driver Verifier](static-driver-verifier.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Tracefmt (Tracefmt.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\tracefmt.exe</p>
<p>%WindowsSdkDir%\bin\x86\tracefmt.exe</p></td>
<td align="left"><p>Formats and displays trace messages from an event trace log file (.etl) or a real-time trace session.</p>
<p>WDK Documentation:</p>
<p>[Tracefmt](tracefmt.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TraceLog (Tracelog.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p><strong>WDK 8:</strong></p>
<p>%WindowsSdkDir%\tools\x64\tracelog.exe</p>
<p>%WindowsSdkDir%\tools\x86\tracelog.exe</p>
<p><strong>WDK 8.1:</strong></p>
<p>%WindowsSdkDir%\bin\x64\tracelog.exe</p>
<p>%WindowsSdkDir%\bin\x86\tracelog.exe</p>
<p>%WindowsSdkDir%\bin\arm\tracelog.exe</p></td>
<td align="left"><p>Configures and controls trace sessions from the command line. Measures time spent in deferred procedure calls (DPCs) and interrupt service routines (ISRs).</p>
<p>WDK Documentation:</p>
<p>[Tracelog](tracelog.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>TracePDB (Tracepdb.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\tracepdb.exe</p>
<p>%WindowsSdkDir%\bin\x86\tracepdb.exe</p></td>
<td align="left"><p>Creates trace message format (.tmf) files from the full or private PDB symbol file for a WPP trace provider.</p>
<p>WDK Documentation:</p>
<p>[Tracepdb](tracepdb.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>TraceView (Traceview.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\TraceView.exe</p>
<p>%WindowsSdkDir%\tools\x86\TraceView.exe</p></td>
<td align="left"><p>Configures and controls trace sessions and displays formatted trace messages from real-time trace sessions and trace logs. TraceView has a graphic user interface and a command-line interface for batch processing and scripting.</p>
<p>WDK Documentation:</p>
<p>[TraceView](traceview.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>TraceWPP (Tracewpp.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\tracewpp.exe</p>
<p>%WindowsSdkDir%\bin\x86\tracewpp.exe</p></td>
<td align="left"><p>Runs the Windows Software Trace Preprocessor (WPP).</p>
<p>WDK Documentation:</p>
<p>[WPP Preprocessor](wpp-preprocessor.md)</p>
<p>[Survey of Software Tracing Tools](survey-of-software-tracing-tools.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WDF Tester</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\\</p>
<p>%WindowsSdkDir%\tools\x86\\</p></td>
<td align="left"><p>A set of tools that can be used to test, verify, and debug WDF drivers. The toolset provides a WMI programming interface that can be used in a script or a compiled application.</p>
<p>WDK Documentation:</p>
<p>[WdfTester: WDF Driver Testing Toolset](wdftester--wdf-driver-testing-toolset.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>WDF Verifier (Wdfverifier.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\wdfverifier.exe</p>
<p>%WindowsSdkDir%\tools\x86\wdfverifier.exe</p></td>
<td align="left"><p>Provides an easy-to-use interface to the framework's verifier for KMDF and UMDF drivers.</p>
<p>WDK Documentation:</p>
<p>[WDF Verifier Control Application](wdf-verifier-control-application.md)</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Web Services on devices (WSD) Basic Interoperability Tool (WSDBIT)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p><strong>WSDBIT Client:</strong></p>
<p>%WindowsSdkDir%\tools\x64\wsdbit_client.exe</p>
<p>%WindowsSdkDir%\tools\x86\wsdbit_client.exe</p>
<p><strong>WSDBIT Server:</strong></p>
<p>%WindowsSdkDir%\tools\x64\wsdbit_server.exe</p>
<p>%WindowsSdkDir%\tools\x86\wsdbit_server.exe</p></td>
<td align="left"><p>Verifies an implementation of [Device Profile for Web Services (DPWS)](http://go.microsoft.com/fwlink/p/?linkid=81255) works with WSDAPI.</p>
<p>WDK Documentation:</p>
<p>[WSD Interoperability Tool](wsdapi-basic-interoperability-tool.md)</p></td>
</tr>
<tr class="even">
<td align="left"><p>Winerror (Winerror.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\tools\x64\winerror.exe</p>
<p>%WindowsSdkDir%\tools\x86\winerror.exe</p></td>
<td align="left"><p>Returns the error message identifier and mapping information for the specified error (Winerror.h) or success codes (Ntstatus.h).</p>
<p>For information about command options, type</p>
<p><strong>winerror /?</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>WMIMofCk (Wmimofck.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x86\wmimofck.exe</p></td>
<td align="left"><p>WDK Documentation:</p>
<p>[Using wmimofck.exe](https://msdn.microsoft.com/library/windows/hardware/ff565588)</p>
<p>For information about command options, type</p>
<p><strong>wmimofck -?</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>WsdCodeGen (Wsdcodegen.exe)</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p>%WindowsSdkDir%\bin\x64\wsdcodegen.exe</p>
<p>%WindowsSdkDir%\bin\x86\wsdcodegen.exe</p></td>
<td align="left"><p>Automatically generates proxies and stubs based on a Web Services contract. Primarily, you can use this tool to create client applications. However, you can use it for testing or for creating user-mode drivers.</p>
<p>Verifies that the classes, properties, methods and events specified in a binary MOF file (.bmf) are valid for WMI use. Generates MOF support files.</p>
<p>Windows SDK:</p>
<p>See the [Web Services on Devices](http://go.microsoft.com/fwlink/p/?linkid=81407) section</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WSDDebug_client and WSDDebug_host</p>
<p><strong>WDK tool:</strong> Yes</p></td>
<td align="left"><p><strong>Debug Client:</strong></p>
<p>%WindowsSdkDir%\bin\x64\WSDDebug_client.exe</p>
<p>%WindowsSdkDir%\bin\x86\WSDDebug_client.exe</p>
<p><strong>Debug Host:</strong></p>
<p>%WindowsSdkDir%\bin\x64\WSDDebug_host.exe</p>
<p>%WindowsSdkDir%\bin\x86\WSDDebug_host.exe</p></td>
<td align="left"><p>These tools are a soft device and client that you can use to troubleshoot devices or applications.</p>
<p>Windows SDK:</p>
<p>See the [Web Services on Devices](http://go.microsoft.com/fwlink/p/?linkid=81407) section</p></td>
</tr>
</tbody>
</table>

 

### <span id="what_s_new_in_the_wdk_for_windows8.1"></span><span id="WHAT_S_NEW_IN_THE_WDK_FOR_WINDOWS8.1"></span>What's New in the WDK for Windows 8.1

The following tools have been added or have changed in the WDK 8.1:

-   HCK Test Suites (see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime) and [How to run the HCK Test Suites in WDK 8.1](https://msdn.microsoft.com/windows-drivers/develop/run_the_hck_test_suites_in_the_wdk).)

-   [Driver Verifier](driver-verifier.md)—now has four new options for detecting errors in Windows drivers.
-   [PwrTest](pwrtest.md)—updated documentation, new test scenarios, including support for connected standby power states.
-   [Tracelog](tracelog.md)—new options.

### <span id="what_s_new_in_the_wdk_for_windows8"></span><span id="WHAT_S_NEW_IN_THE_WDK_FOR_WINDOWS8"></span>What's New in the WDK for Windows 8

The following tools have been added to the WDK for Windows 8:

-   Bluetooth Inquiry Record Verifier (Sdpverify.exe)

-   Device Fundamentals tests (see [How to test a driver at runtime using Visual Studio](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver_at_runtime) and [How to select and configure the Device Fundamentals tests](https://msdn.microsoft.com/windows-drivers/develop/how_to_select_and_configure_the_device_fundamental_tests).

-   Sensor Diagnostic Tool (sensordiagnostictool.exe)

### <span id="what_s_changed_in_the_wdk_for_windows8"></span><span id="WHAT_S_CHANGED_IN_THE_WDK_FOR_WINDOWS8"></span>What's Changed in the WDK for Windows 8

The following tools were in the Microsoft WDK for Windows 7, but are not included in the WDK for Windows 8.

-   Windows Biometric Framework Tools (BioTest.exe, WBDIDriverTest.exe)

-   Device Path Exerciser (devpathexer.exe). Now part of the Device Fundamental fuzz tests.

-   IoSpy and IoAttack (IoSpyCmd.exe, IoAttack.exe). Now part of the Device Fundamental tests.

-   Kernrate (Kernrate.exe) Kernrate is no longer supported. Instead, use the [Windows Performance Analysis Toolkit](http://go.microsoft.com/fwlink/p/?linkid=294280).

-   Microsoft Auto Code Review (OACR) (The driver components now part of the Code Analysis tool in Visual Studio.)

-   Plug and Play Driver Test (pnpdtest.exe). Now part of the Device Fundamental tests.

-   ProCalc

-   WWAN Driver Test App (wwandrivertestapp.exe)

### <span id="supported_OS_wdk_for_win8"></span><span id="supported_os_wdk_for_win8"></span><span id="SUPPORTED_OS_WDK_FOR_WIN8"></span>Supported platforms

WDK 8.1 supports development of drivers that run on these versions of Windows:

-   Windows 8.1 and Windows 8

-   Windows Server 2012 R2 and Windows Server 2012

-   Windows 7

-   Windows Server 2008 R2

-   For Windows Vista (including SP1 and SP2), you must use WDK 8. For Windows XP, you must use WDK 7.

You can run the integrated Visual Studio driver development environment on these versions of Windows.

-   Windows 8.1 and Windows 8

-   Windows Server 2012 R2 and Windows Server 2012

-   Windows 7

-   Windows Server 2008 R2

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Index%20of%20Windows%20Driver%20Kit%20Tools%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




