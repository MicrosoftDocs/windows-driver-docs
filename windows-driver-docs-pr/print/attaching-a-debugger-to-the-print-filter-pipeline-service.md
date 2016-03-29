---
title: Attaching a Debugger to the Print Filter Pipeline Service
description: Attaching a Debugger to the Print Filter Pipeline Service
ms.assetid: d2e032f8-bdce-415a-8cf4-d9816b7c9de5
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Attaching%20a%20Debugger%20to%20the%20Print%20Filter%20Pipeline%20Service%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




