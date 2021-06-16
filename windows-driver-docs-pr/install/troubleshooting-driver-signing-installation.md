---
title: Troubleshooting Driver Signing Installation
description: Installing a release-signed driver is the same as described in Installing, Uninstalling and Loading the Test-Signed Driver Package in Test Signing, except for two additional steps needed when installing using any of the four methods described there.
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Troubleshooting Driver Signing Installation


Installing a release-signed driver is the same as described in **Installing, Uninstalling and Loading the Test-Signed Driver Package** in [Test Signing](test-signing.md), except for two additional steps needed when installing using any of the four methods described there. Using the Add Hardware Wizard to install a release-signed driver shows the additional two steps, including some common installation issues.

1.  Open an elevated command window
2.  Run hdwwiz.cpl to start the Add Hardware Wizard, and select Next to go to the second page
3.  Select Advanced Option and select Next
4.  Select Show all devices from the list box and select Next
5.  Select the Have Disk option
6.  Enter the path to the folder that contains the C:\\toaster driver package
7.  Select the inf file and select Open
8.  Select OK
9.  Select Next in the next two pages, and then select Finish to complete the installation
10. Select Install on the dialog box that asks “Would you like to install this device software?”
11. Select Finish to complete the installation.

Step 10 shows the following Windows Security dialog box.

![screenshot showing the windows security dialog.](images/tutorialwindowssecurityinstalldialog.png)

Selecting the check box will not show this dialog box again on the computer if the driver is installed again or if the driver is removed for any reason.

**Note**  The system verifies that publisher information is accurate based on the SPC that was used to sign the catalog. If the publisher trust level is unknown—as will be true for Contoso.com—the system displays the dialog box. For the installation to proceed, the user must select Install. For more information on trust and driver installation, see [Code-Signing Best Practices](/previous-versions/windows/hardware/design/dn653556(v=vs.85)).

 

An unsigned driver will show the following dialog, which allows a user to install an unsigned driver (this may not work in x64 version of Windows).

![screen shot showing the windows security warning dialog.](images/tutorialwindowssecurityinstallwarning.png)

## Verify that the Release-Signed Driver is Operating Correctly


Use Device Manager to view the driver Properties (described earlier for the test-signed driver). Below is the screen shot to show if the driver is working.

![screen shot showing the toaster device in the device manager.](images/tutorialtoasterpackageindevicemgr.png)

## Troubleshoot Release-Signed Drivers


Several common ways to troubleshoot problems with loading signed or test signed drivers are listed below:

-   Use the Add Hardware Wizard or Device Manager to check whether the driver is loaded and signed, as described in **Verify that the Test-Signed Driver Is Operating Correctly** of [Test Signing](test-signing.md).
-   Open the setupapi.dev.log file created in the Windows\\inf directory after driver install. Refer to the section on setting the registry entry and renaming of the setupapi.dev.log file before installing the driver.
-   Check the Windows security audit log and Code Integrity event logs.

## Analyzing the Setupapi.dev.log File


As explained before, any driver installation information will be logged (appended) to the setupapi.dev.log file in the Windows\\inf directory. If the file is renamed before a driver is installed, a new log file will be generated. A new log file will be easier to search for important logs from a new driver install. The log file opens in the Notepad application.

The first left most column may have a single exclamation mark “!” or multiple exclamation marks “!!!”. The single mark is a warning message, but the triple exclamation mark indicates a failure.

You will see the following single exclamation mark when you install a driver package release signed with a CA vendor provided SPC certificate. These are warnings that the cat file has not been verified yet.

```cpp
!    sig:                Verifying file against specific (valid) catalog failed! (0x800b0109)
!    sig:                Error 0x800b0109: A certificate chain processed, but terminated in a root certificate which is not trusted by the trust provider.
     sig:                Success: File is signed in Authenticode(tm) catalog.
     sig:                Error 0xe0000242: The publisher of an Authenticode(tm) signed catalog has not yet been established as trusted.
```

Refer to step 10 of driver install and select the “Install” button. You will see the log below, which in most cases means the driver will install and load fine. The Device Manager will not report any errors or a yellow exclamation mark for the driver.

```cpp
!    sto:           Driver package signer is unknown but user trusts the signer.
```

If you also see the following error log in the log file, the driver may not be loaded.

The setupapi.dev.log file has also reported the following error:

```cpp
!!!  dvi:                          Device not started: Device has problem: 0x34: CM_PROB_UNSIGNED_DRIVER.
```

Note that 0x34 is Code 52.

To troubleshoot, review the log file and look for exclamation marks next to a driver binary. Run the `signtool verify` command on the cat file and other embedded signed binaries.

Usually the log file information is sufficient to resolve the issue. If the above checks fail to find the root cause, then check the Windows security audit log and code Integrity event logs, described in the next section.

If the service binary file copy has not been committed but the OS tries to start the service, the driver service will fail to start. If this happens, use the setupapi.dev.log file to check driver file copy and commit time information. A restart should successfully start the service. See the example sequence of operation below in the log file.

```cpp
>>>  Section start 2014/02/08 14:54:56.463
```

Next at a later time:

```cpp
!    inf:                     Could not start service 'toaster'.
```

Then we have the file copy operation:

```cpp
<snip>
flq:                {FILE_QUEUE_COPY}
     flq:                     CopyStyle      - 0x00000000
     flq:                     SourceRootPath - 'C:\Windows\System32\DriverStore\FileRepository\Toaster.inf_amd64_d9b35403a0fe4391\'
     flq:                     SourceFilename - 'toaster.exe'
     flq:                     TargetDirectory- 'C:\Windows\System32\drivers'
     flq:                     TargetFilename - 'toaster.exe'
```

The file is committed next. Compare the end time with the start time.

```cpp
flq:           {_commit_file_queue} 14:54:56.711
<snip>
     flq:                     {_commit_copyfile}
     flq:                          Copying 'C:\Windows\System32\DriverStore\FileRepository\Toaster.inf_amd64_d9b35403a0fe4391\o2flash.exe' to 'C:\Windows\System32\drivers\o2flash.exe'.
     flq:                          CopyFile: 'C:\Windows\System32\DriverStore\FileRepository\Toaster.inf_amd64_d9b35403a0fe4391\o2flash.exe' to 'C:\Windows\System32\drivers\SETDA81.tmp'
     flq:                          MoveFile: 'C:\Windows\System32\drivers\SETDA81.tmp' to 'C:\Windows\System32\drivers\toaster.exe'
     cpy:                          Applied 'OEM Legacy' protection on file 'C:\Windows\System32\drivers\toaster.exe'.
     flq:                          Caller applied security to file 'C:\Windows\System32\drivers\toaster.exe'.
     flq:                     {_commit_copyfile exit OK}
<snip>
     sto:      {Configure Driver Package: exit(0x00000bc3)}
     ndv:      Restart required for any devices using this driver.
<snip>
<<<  Section end 2014/02/08 14:54:57.024
<<<  [Exit status: SUCCESS]
```

The above example is a driver update that worked fine in Windows 7, but failed in Windows 8.0 and 8.1, which led to the discovery of a bug.

## Using the Windows Security Audit Log


If the driver failed to load because it lacked a valid signature, it will be recorded as an audit failure event. Audit failure events are recorded in the Windows security log, indicating that Code Integrity could not verify the image hash of the driver file. The log entries include the driver file's full path name. The security log audit events are generated only if the local security audit policy enables logging of system failure events.

**Note**  The security audit log must be explicitly enabled. For more information, see [Appendix 3: Enable Code Integrity Event Logging and System Auditing](appendix-3--enable-code-integrity-event-logging-and-system-auditing.md).

 

To examine the security log:

1.  Open an elevated command window.
2.  To start Windows Event Viewer, run Eventvwr.exe. Event Viewer can also be started from the Control Panel Computer Management application.
3.  Open the Windows security audit log.
4.  Check the log for system integrity events with an event ID of 5038.
5.  Select and hold (or right-click) the log entry and select Event Properties to display its Event Properties dialog box, which provides a detailed description of the event.

The screen shot below shows the Event Properties dialog box for a security audit log event that was caused by an unsigned Toaster.sys file.

![screen shot showig the event properties dialog.](images/tutorialeventprops.png)

## Using the Code Integrity Event Operational Event Log


If the driver failed to load because it was not signed or generated an image verification error, Code Integrity records the events in the Code Integrity operational event log. Code Integrity operational events are always enabled.

The Code Integrity events can be viewed with Event Viewer.

## To examine the Code Integrity operational log


1.  Open an elevated command window.
2.  To start Windows Event Viewer, run Eventvwr.exe. Event Viewer can also be started from the Computer Management Control Panel application.
3.  Open the Windows Code Integrity log.
4.  Select and hold (or right-click) a log entry and select Event Properties to display its Event Properties dialog box, which provides a detailed description of the event.

The screen shot below shows the Event Properties dialog box for a Code Integrity operational log event that was caused by an unsigned Toaster.sys file.

![screen shot showing the event viewer.](images/tutorialeventvwr.png)

## Using the Informational Events in the Code Integrity Verbose Log


The Code Integrity informational log's verbose view tracks events for all kernel-mode image verification checks. These events show successful image verification of all drivers that are loaded on the system.

To enable the Code Integrity verbose view:

1.  Start Event Viewer, as in the previous example.
2.  Selet the Code Integrity node to give it focus.
3.  Select and hold (or right-click) Code Integrity and select the View item from the shortcut menu.
4.  Select Show Analytic and Debug Logs. This creates a sub tree with two additional nodes: Operational and Verbose.
5.  Select and hold (or right-click) the Verbose node and select the Properties from the shortcut menu.
6.  On the General tab, select Enable Logging to enable the verbose logging mode.
7.  Reboot the system to reload all kernel-mode binaries.
8.  After rebooting, open the MMC Computer Management snap-in and view the Code Integrity verbose event log.

A few additional known driver signing issues are described in [Appendix 4: Driver Signing Issues](appendix-4--driver-signing-issues.md).

 

