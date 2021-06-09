---
title: DTrace Live Dump
description: DTrace supports live dump file creation using using LKD(). 
keywords:
- DTrace WDK
- software tracing WDK , DTrace
- displaying trace messages
- formatting trace messages WDK DTrace
- trace message formatting WDK DTrace
- software tracing WDK , formatting messages
- tracing WDK , DTrace
- trace message format files WDK
ms.date: 11/04/2019
ms.localizationpriority: medium
---

# DTrace Live Dump

DTrace provides a facility to capture live dump from within the D-script using lkd(). Memory dump files are used for debugging complex problems in Windows using the Windows Debugger. For more information, see [Analyze crash dump files by using WinDbg](../debugger/crash-dump-files.md). To download the debugger, see [WinDbg Preview - Installation](../debugger/windbg-install-preview.md).

 DTrace live dump provides the ability to trigger the dump at the exact point where the error occurred. For instance, the error could be a function returning an error. You can use DTrace to hook into this function return and trigger a live dump when the return value is "error".

> [!NOTE]
> DTrace is supported in the Insider builds of Windows after version 18980 and Windows Server Insider Preview Build 18975.

For general information about working with DTrace on Windows, see [DTrace](dtrace.md).

## DTrace Live Dump Usage

Usage: **lkd (parameter);**

The following options can be set to change what information is included in the live mini dump.

0x0 - Full kernel dump (default value)

0x1 - User pages + Kernel pages (works only with KD attach)

0x2 - Minidump

0x4 - Hyper-V pages + Kernel pages)

0x5 - User, kernel and hypervisor pages.

## Live Dump Example Code

```dtrace
#pragma D option destructive

inline uint32_t STATUS_UNSUCCESSFUL = 0xc0000001UL;

syscall:::return
{ 
	this->status = (uint32_t)arg0;

	if (this->status == STATUS_UNSUCCESSFUL)
	{ 
		printf ("Return value arg0:%x \n", this->status);
		printf ("Triggering LiveDump \n");
		lkd(0);
		exit(0);
	}
}
```

Save the file as livedumpstatuscheck.d.

Open a command prompt as an Administrator and run the script using the -s option.

```dtrace
C:\Windows\System32>dtrace -s livedumpstatuscheck.d
dtrace: script 'livedumpstatuscheck.d' matched 1881 probes
dtrace: allowing destructive actions
CPU     ID                    FUNCTION:NAME
  0     93 NtAlpcSendWaitReceivePort:return Return value arg0:c0000001
Triggering LiveDump
```

The dump file that is created is typically located in `C:\Windows\LiveKernelReports`.

If the dump file location has been changed, the value is stored in this registry key: `hklm\system\currentcontrolset\control\crashcontrol\livekernelreports`

Use WinDbg to work with a dump file as described above.

## Troubleshooting

### Viewing live dump related events

Open the Windows Event Viewer: Go to: Applications and Services Logs->Microsoft->Windows->Kernel-Livedump->Operational

If you didn't find any logs, enable the analytic channel from the command prompt or the event viewer as described below.

**Enable  analytic channel from command prompt**

Use this command to enable the analytic channel from and administrator command prompt.

`wevtutil sl Microsoft-Windows-Kernel-LiveDump/Analytic /e:true`

**Enable  analytic channel using Event Viewer**

1. Start Windows Event Viewer

2. Click on View and check "Show Analytic and Debug logs". This will show the analytic channel for livedump.

3. Right-click on and enable *Microsoft-Windows-Kernel-LiveDump/Analytic*.

### Enabling full live dumps

These example settings below, show setting the maximum number of full live dumps that may be on disk at any given time to 10 and stores the full memory dumps, not just a mini dump.

`reg add "HKLM\System\CurrentControlSet\Control\CrashControl\FullLiveKernelReports" /f /t REG_DWORD /v FullLiveReportsMax /d 10`

`reg add "HKLM\System\CurrentControlSet\Control\CrashControl" /f /t REG_DWORD /v AlwaysKeepMemoryDump /d 1`

For more information on these settings, see [WER Settings](/windows/win32/wer/wer-settings).

### Disable throttling

Throttling is a feature that prevents the dumps and logging system from impacting the normal use of Windows. This feature can interfere with the creation of live dumps in certain resource constrained environments.

Check live dump throttle settings and if necessary retry by disabling throttling by setting SystemThrottleThreshold and ComponentThrottleThreshold keys to zero as shown here.

```registry
reg add "HKLM\System\CurrentControlSet\Control\CrashControl\FullLiveKernelReports" /f /t REG_DWORD /v SystemThrottleThreshold /d 0
reg add "HKLM\System\CurrentControlSet\Control\CrashControl\FullLiveKernelReports" /f /t REG_DWORD /v ComponentThrottleThreshold /d 0
```

### Disk space issues (Event ID 202 -Error Text: Live Dump Write Deferred Dump Data API ended. NT Status: 0xC000007F.)

This means the disk space is insufficient. Update the registry key shown below to change the path for live dump creation, in this example to a drive d: that has additional storage space available.

`reg add hklm\system\currentcontrolset\control\crashcontrol\livekernelreports /v "LiveKernelReportsPath" /t reg_sz /d "\??\d:\livedumps"`

This command sets the live dump root path to `d:\livedumps` (as an example).

Do not manually create the folder as it is managed by the OS and will be created when the dump is triggered with the proper permissions.

## See Also

[DTrace on Windows](dtrace.md)

[DTrace Windows Programming](dtrace-programming.md)

[DTrace Windows Code Samples](dtrace-code-samples.md)
