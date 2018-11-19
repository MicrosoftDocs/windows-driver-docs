---
title: Accessing UMDF Metadata in WER Reports
description: This topic describes the location and contents of the Windows Error Reporting (WER) reports that the operating system creates when a User-Mode Driver Framework (UMDF) crashes.The system generates WER reports for three different UMDF event types WUDFHostProblem, WUDFUnhandledException, and WUDFVerifierFailure.When the reflector terminates the driver host process, sometimes due to the host timeout threshold being exceeded, the system generates a file called Report.wer, which contains the WER information. Specifically, Report.wer contains UMDF metadata that may be helpful if you are trying to debug a UMDF driver with no access to a live debugging target.
ms.assetid: ca5fe108-b4fb-4c90-87bc-9901854780d3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Accessing UMDF Metadata in WER Reports


This topic describes the location and contents of the Windows Error Reporting (WER) reports that the operating system creates when a User-Mode Driver Framework (UMDF) crashes.

The system generates WER reports for three different UMDF event types: **WUDFHostProblem**, **WUDFUnhandledException**, and **WUDFVerifierFailure**.

When the reflector terminates the driver host process, sometimes due to the [host timeout](how-umdf-enforces-time-outs.md) threshold being exceeded, the system generates a file called Report.wer, which contains the WER information. Specifically, Report.wer contains UMDF metadata that may be helpful if you are trying to debug a UMDF driver with no access to a live debugging target.

In Windows 8.1, you can find the Report.wer file in the C:\\ProgramData\\Microsoft\\Windows\\WER\\ReportQueue directory. In this directory, open the most recent NonCritical\_HostProblem\_\* folder and locate Report.wer.

You can also access WER reports for UMDF using the following PowerShell command:

```cpp
get-winevent -providername "Windows Error Reporting" | where-object {$_.Message -like "*wudf*"} | format-list | out-file UmdfReports.txt
```

## WUDFHostProblem sample report


The following is a sample UMDF WER report of type **WUDFHostProblem**. It was obtained from the ReportQueue directory described above. If you use PowerShell to retrieve the reports, the fields may be labeled P0, P1, P2 instead of Sig\[0\], Sig\[1\], Sig\[2\]. Otherwise, the fields are the same and contain the same possible values. This sample was generated from one of the WDK samples that use the OSR USB-FX2 hardware reference board.

```cpp
Sig[0].Name=EventClass
Sig[0].Value=HostProblem
Sig[1].Name=Problem
Sig[1].Value=HostTimeout
Sig[2].Name=DetectedBy
Sig[2].Value=2
Sig[3].Name=UMDFVersion
Sig[3].Value=6.3.9600
Sig[4].Name=ExitCode
Sig[4].Value=103
Sig[5].Name=Operation
Sig[5].Value=3
Sig[6].Name=Message
Sig[6].Value=11b00
Sig[7].Name=Status
Sig[7].Value=ffffffff
Sig[8].Name=HardwareId
Sig[8].Value=USB\VID_0547&PID_1002&REV_0000
```

## WUDFHostProblem fields


The following table describes the possible values for the fields in a report of type **WUDFHostProblem.**

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index</th>
<th align="left">Name</th>
<th align="left">Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">0</td>
<td align="left">EventClass</td>
<td align="left"><p>The framework sets this value to <strong>HostProblem</strong>.</p></td>
</tr>
<tr class="even">
<td align="left">1</td>
<td align="left">Problem</td>
<td align="left"><p>This field contains one of the following values:</p>
<ul>
<li>HostFailure</li>
<li>SendFailure</li>
<li>HostTimeout</li>
<li>BadRequest</li>
<li>BadReply</li>
<li>HostFailure</li>
<li>Other</li>
<li>HostDisconnect</li>
<li>LeakedHandle</li>
<li>InvalidInterruptState</li>
<li>IsrTimedOut</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">2</td>
<td align="left">DetectedBy</td>
<td align="left"><p>Contains one of the following enumeration values:</p>
<div class="code">
<code>cpp
WdfComponentInvalid = 0,
WdfComponentPlatform,
WdfComponentReflector,
WdfComponentDriverManager,
WdfComponentHost,
WdfComponentFramework,
WdfComponentTest,
WdfComponentMax</code>
</div></td>
</tr>
<tr class="even">
<td align="left">3</td>
<td align="left">UMDFVersion</td>
<td align="left"><p>Specifies the version of the UMDF libraries currently in use. Note that this may be a later version than came with the operating system if the user took action to update the framework libraries.</p></td>
</tr>
<tr class="odd">
<td align="left">4</td>
<td align="left">ExitCode</td>
<td align="left"><p>Contains one of the following enumeration values:</p>
<div class="code">
<code>cpp
    WdfHostExit_StillActive = 0x103,
    WdfHostExit_CodeUnknown = 0x70000000,
    WdfHostExit_InternalDriverStopReported,
    WdfHostExit_InternalDriverStopReportFailed,
    WdfHostExit_ExternalTermination</code>
</div>
<p><strong>WdfHostExit_StillActive</strong> indicates that the host process was running at the time the framework created the error report.</p></td>
</tr>
<tr class="even">
<td align="left">5</td>
<td align="left">Operation</td>
<td align="left"><p>Contains one of the following enumeration values:</p>
<div class="code">
<code>cpp
    WudfOperation_Invalid,
    WudfOperation_Init,
    WudfOperation_HostShutdown,
    WudfOperation_Pnp,
    WudfOperation_Cleanup,
    WudfOperation_Close,
    WudfOperation_Cancel,
    WudfOperation_IO,
    WudfOperation_Interrupt,
    WudfOperation_PoFx,
    WudfOperation_Other,
    WudfOperation_Max</code>
</div></td>
</tr>
<tr class="odd">
<td align="left">6</td>
<td align="left">Message</td>
<td align="left"><p>The first digit is of this field is always 1, which indicates that an IRP is involved in the operation. Subsequent pairs of digits indicate the <strong>MajorFunction</strong> and <strong>MinorFunction</strong> of the IRP, respectively.</p>
<p>In the sample report above, for example, this field contains the value 11b00. This means that the operation was an IRP that the reflector handled on behalf of the driver host process with a major function value of IRP_MJ_PNP and minor function value of IRP_MN_START_DEVICE (1 = IRP message, 1b = IRP_MJ_PNP, 00 = IRP_MN_START_DEVICE).</p></td>
</tr>
<tr class="even">
<td align="left">7</td>
<td align="left">Status</td>
<td align="left"><p>The framework always sets to this value to 0xffffffff.</p></td>
</tr>
<tr class="odd">
<td align="left">8</td>
<td align="left">HardwareId</td>
<td align="left"><p>This field contains the hardware ID of the device associated with the driver that had a problem.</p></td>
</tr>
</tbody>
</table>



## WUDFUnhandledException fields


The following table describes the possible values for the fields in a report of type **WUDFUnhandledException**.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index</th>
<th align="left">Name</th>
<th align="left">Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">0</td>
<td align="left">EventClass</td>
<td align="left"><p>The framework sets this value to <strong>UnhandledException</strong>.</p></td>
</tr>
<tr class="even">
<td align="left">1</td>
<td align="left">Component</td>
<td align="left"><p>This field contains one of the following values:</p>
<ul>
<li>Invalid</li>
<li>Platform</li>
<li>Reflector</li>
<li>DriverManager</li>
<li>Host</li>
<li>Framework</li>
<li>Test</li>
</ul></td>
</tr>
<tr class="odd">
<td align="left">2</td>
<td align="left">ExceptionCode</td>
<td align="left"><p>The reason the exception occurred. For a list of values, see <a href="https://msdn.microsoft.com/library/windows/desktop/aa363082" data-raw-source="[&lt;strong&gt;EXCEPTION_RECORD&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/desktop/aa363082)"><strong>EXCEPTION_RECORD</strong></a>.</p></td>
</tr>
<tr class="even">
<td align="left">3</td>
<td align="left">RelativeFaultingAddress</td>
<td align="left"><p>The address where the exception occurred.</p></td>
</tr>
<tr class="odd">
<td align="left">4</td>
<td align="left">CrashingModuleName</td>
<td align="left">Name of the driver that raised the exception.</td>
</tr>
<tr class="even">
<td align="left">5</td>
<td align="left">CrashingFileVersion</td>
<td align="left">Framework version of the driver.</td>
</tr>
<tr class="odd">
<td align="left">6</td>
<td align="left">LastDriverName</td>
<td align="left">Name of the first non-UMDF driver component in the driver stack.</td>
</tr>
<tr class="even">
<td align="left">7</td>
<td align="left">LastDriverVersion</td>
<td align="left">Version number of the first non-UMDF driver component in the driver stack.</td>
</tr>
<tr class="odd">
<td align="left">8</td>
<td align="left">UMDFVersion</td>
<td align="left"><p>Specifies the version of the UMDF libraries currently in use. Note that this may be a later version than came with the operating system if the user took action to update the framework libraries.</p></td>
</tr>
<tr class="even">
<td align="left">9</td>
<td align="left">HardwareId</td>
<td align="left"><p>Starting in Windows 8, the hardware ID is provided in a separate file. In this case, the framework sets this value to <strong>Dumped Separately</strong>.</p></td>
</tr>
</tbody>
</table>



## WUDFVerifierFailure fields


The following table describes the possible values for the fields in a report of type **WUDFVerifierFailure**.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Index</th>
<th align="left">Name</th>
<th align="left">Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left">0</td>
<td align="left">EventClass</td>
<td align="left"><p>The framework sets this value to <strong>VerifierFailure</strong>.</p></td>
</tr>
<tr class="even">
<td align="left">1</td>
<td align="left">FoundBy</td>
<td align="left"><p>The framework sets this value to <strong>Framework</strong>.</p></td>
</tr>
<tr class="odd">
<td align="left">2</td>
<td align="left">Category</td>
<td align="left"><p>This field contains one of the following values:</p>
<ul>
<li>Internal</li>
<li>Driver</li>
<li>Caller</li>
<li>External</li>
<li>UnhandledException</li>
</ul></td>
</tr>
<tr class="even">
<td align="left">3</td>
<td align="left">ErrorNumber</td>
<td align="left">Internal use only.</td>
</tr>
<tr class="odd">
<td align="left">4</td>
<td align="left">Location</td>
<td align="left">Internal use only.</td>
</tr>
<tr class="even">
<td align="left">5</td>
<td align="left">Driver</td>
<td align="left">The name of the driver module that failed.</td>
</tr>
<tr class="odd">
<td align="left">6</td>
<td align="left">CallerAddress</td>
<td align="left">The address of the routine that initiated generation of the report.</td>
</tr>
<tr class="even">
<td align="left">7</td>
<td align="left">UMDFVersion</td>
<td align="left"><p>Specifies the version of the UMDF libraries currently in use. Note that this may be a later version than came with the operating system if the user took action to update the framework libraries.</p></td>
</tr>
<tr class="odd">
<td align="left">8</td>
<td align="left">HardwareId</td>
<td align="left"><p>Starting in Windows 8, the hardware ID is provided in a separate file. In this case, the framework sets this value to <strong>Dumped Separately</strong>.</p></td>
</tr>
</tbody>
</table>











