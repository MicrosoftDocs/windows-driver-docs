---
title: Attaching a Debugger to the Print Filter Pipeline Service
description: Attaching a Debugger to the Print Filter Pipeline Service
ms.assetid: d2e032f8-bdce-415a-8cf4-d9816b7c9de5
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Attaching a Debugger to the Print Filter Pipeline Service


XPSDrv driver filters are hosted by the print filter pipeline service (printfilterpipelinesvc.exe). If you want to attach the Microsoft Windows Debugger (WinDbg) to the print filter pipeline service, there are two basic ways to do this:

1.  Use WinDbg from the command line to start the process.

2.  Attach WinDbg to an existing process.

The filter pipeline host must be started by the print spooler, so you must use the second option to attach WinDbg to the process. However, the filter pipeline host may not be persistent. A new instance of the service is started when an application submits a job to the print queue and the service is terminated shortly after the job is complete. It may be difficult to attach WinDbg to printfilterpipelinesvc.exe after the print job is submitted but before the filter that you are trying to debug starts running, especially if you want to debug the filter's startup or initialization code.

To work around this problem, you can modify the amount of time that printfilterpipelinesvc.exe persists after a print job is finished. That value is controlled by the **PipelineHostTimeout** value of the HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print registry key.

Use these steps to change the filter pipeline service timeout value:

1.  Run Microsoft Registry Editor (RegEdit) and navigate to HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print.

2.  Add a **PipelineHostTimeout** REG\_DWORD value to the key, if it is not already present.

3.  Set **PipelineHostTimeout** to the timeout value, in milliseconds. Set a large enough value to give yourself ample time to attach the process and set breakpoints. For example, if you want a timeout value of .5 minutes , set **PipelineHostTimeout** to 90000.

After setting the **PipelineHostTimeout** value, use the following procedure to attach WinDbg to the pipeline filter service:

1.  Run WinDbg with elevated privileges, but do not attach it to a process.

2.  Submit a print job to your driver and wait for it to complete. The filter pipeline service continues running for the specified timeout value.

3.  From the WinDbg File menu, select Attach to a Process.

4.  In the Attach to Process dialog box, select printfilterpipelinesvc.exe and click OK. If the process is listed as "Access Denied", it probably means that WinDbg is not running with elevated privileges.

5.  Set breakpoints, as appropriate.

6.  Submit the print job again.

The filter host process should break into the debugger at the first breakpoint or the first verifier stop, whichever comes first. From there, you can step through code, examine variables, and so on.

 

 




