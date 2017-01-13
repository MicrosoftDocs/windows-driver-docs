---
title: How WER collects and classifies error reports
description: How WER collects and classifies error reports
MS-HAID:
- 'p\_dashboard.how\_wer\_collects\_and\_classifies\_error\_reports'
- 'hw\_dashboard.how\_wer\_collects\_and\_classifies\_error\_reports'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: f6af24c7-90f7-42cf-93f3-8e3ba26b793a
---

# How WER collects and classifies error reports


The Microsoft Windows Error Reporting (WER) service captures both kernel-mode (operating system) and user-mode (application) crashes, including information on drivers and applications, as well as about the modules (controls and plug-ins) running at the time of the crash.

## <span id="Windows_Error_Reporting__WER___Classifications"></span><span id="windows_error_reporting__wer___classifications"></span><span id="WINDOWS_ERROR_REPORTING__WER___CLASSIFICATIONS"></span>Windows Error Reporting (WER): Classifications


When an end user chooses to send an error report to Microsoft over the Internet, the WER service collects technical information about the crash. This data is used for quality control purposes only and is not used for tracking individual users or installations for any marketing purpose. If information is available that will help the end user solve the problem, Windows displays a message to the user with a link to that information.

WER classifies error reports for the same problem into one bucket. When a customer sends an error report, WER determines if a bucket for that problem already exists. If it does, then the report is added to the existing bucket. If not, then a new bucket is created.

The types of data collected and the schemas for defining a bucket are different for user-mode crashes and for kernel-mode crashes.

## <span id="Classifying_kernel-mode_crashes"></span><span id="classifying_kernel-mode_crashes"></span><span id="CLASSIFYING_KERNEL-MODE_CRASHES"></span>Classifying kernel-mode crashes


Kernel-mode crashes are first grouped by stop codes and then by additional parameters, depending on the individual stop code. The bucket name is based on the type of error and the device. For example:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Bucket name</th>
<th>Error</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>OLD_IMAGE_SAMPLE.SYS_DEV_3577</p></td>
<td><p>Crash caused by an old version of sample.sys on device ID 3577</p></td>
</tr>
<tr class="even">
<td><p>0x44_BUGCHECKING_DRIVER_ SAMPLE</p></td>
<td><p>Driver sample.sys may have caused Bugcheck 0x44</p></td>
</tr>
<tr class="odd">
<td><p>POOL_CORRUPTION_ SAMPLE</p></td>
<td><p>Driver sample.sys may have caused pool corruption</p></td>
</tr>
<tr class="even">
<td><p>0xBE_sample!bar+1a</p></td>
<td><p>Driver sample.sys crashed in routine bar</p></td>
</tr>
</tbody>
</table>

 

An error report for a kernel-mode crash consists of a minidump file generated at the time of the crash and an XML file generated when the computer restarts and is about to send the error report.

When Windows stops responding, it reverts to a low-level troubleshooting mode. In this mode, a dump file is captured that contains low-level operating system data structures that identify what was happening in the computer at the time of the crash. These data structures include the functions being executed by the processor at the time of the crash, the CPU register state, and stack, thread, and process information. This data can be viewed in a debugger and used to identify the faulting component.

The dump file also contains the list of all drivers loaded in the computer at the time of the crash. This data is used by the debugger to determine which driver images and symbols need to be loaded to debug the crash. The list of modules also helps determine whether known bad or outdated drivers are running on the computer.

Starting with Windows XP Service Pack 1 (SP1), the dump files have been enhanced to allow a driver to store information in the crash dump file that can be used for troubleshooting. The routine for collecting crash data from a driver is **KeRegisterBugCheckCallback**.

## <span id="Classifying_User-Mode_Crashes"></span><span id="classifying_user-mode_crashes"></span><span id="CLASSIFYING_USER-MODE_CRASHES"></span>Classifying User-Mode Crashes


User-mode crashes are classified according to the following parameters:

1.  Application name — for example, winword.exe

2.  Application version — for example, 10.0.2627.0

3.  Module name — for example, mso.dll

4.  Module version — for example, 10.0.2613.1

5.  Offset into module — for example, 00003cbb

The .cab files for user-mode crashes include such information plus a minidump file. The minidump file for user-mode crashes contains the state of the process at the time the crash occurred—specifically, the registers and stack for every thread in the application. This information is used to identify which application component caused the crash. The minidump also includes a list of all modules loaded in the application at the time of the crash, so you can get information about each module loaded in the process and to get symbols for each of these modules.

## <span id="Error_classification_resources"></span><span id="error_classification_resources"></span><span id="ERROR_CLASSIFICATION_RESOURCES"></span>Error classification resources


-   [KeRegisterBugCheckCallback routine](http://msdn.microsoft.com/library/ff553105.aspx)

-   [Windows Vista Privacy Notice Highlights](http://go.microsoft.com/fwlink/p/?LinkId=618595)

-   [Privacy Statement for the Microsoft Error Reporting Service](http://go.microsoft.com/fwlink/p/?LinkId=618596)

## <span id="WER_resources"></span><span id="wer_resources"></span><span id="WER_RESOURCES"></span>WER resources


-   [Debugging in the (Very) Large: Ten Years of Implementation and Experience (PDF)](http://www.sigops.org/sosp/sosp09/papers/glerum-sosp09.pdf)

-   [Debugging OCA minidump files](https://msdn.microsoft.com/library/windows/hardware/dn641143.aspx)

-   [WER Services blog](http://blogs.msdn.com/b/wer/)

-   [Privacy Statement for the Microsoft Error Reporting Service](http://windows.microsoft.com/Windows/microsoft-error-reporting-privacy-statement)

-   [Queries about SysDev online submission website](mailto:winqual@microsoft.com)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bhw_dashboard\hw_dashboard%5D:%20How%20WER%20collects%20and%20classifies%20error%20reports%20%20RELEASE:%20%281/3/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




