---
title: Debugging XPSDrv Printer Drivers
description: Debugging XPSDrv Printer Drivers
ms.assetid: 7193f007-de25-4b77-9133-9937b3d37db0
keywords:
- debugging XPSDrv drivers WDK print
- XPSDrv driver debugging WDK print
- XPSDrv printer drivers WDK , debugging
- spoolsv.exe process WDK print
- printfilterpipelinesvc.exe process WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Debugging XPSDrv Printer Drivers


Print queues with XPSDrv printer drivers are hosted in the spoolsv.exe process. Unlike GDI-based printer drivers, however, the filters of an XPSDrv printer driver are hosted in the printfilterpipelinesvc.exe process, which is separate from spoolsv.exe. As a result, you must attach your debugger to the printfilterpipelinesvc.exe process to debug the filters in an XPSDrv printer driver.

### <a href="" id="configuring-the-printfilterpipelinesvc-exe-process-time-out"></a>Configuring the printfilterpipelinesvc.exe Process Time-Out

The printfilterpipelinesvc.exe process starts when a print job is sent to a print queue with an XPSDrv printer driver. The process exits after it has been inactive for a period of time that is defined by a value in the registry. The intermittent nature of the printfilterpipelinesvc.exe process makes it difficult to attach a debugger to printfilterpipelinesvc.exe to debug the filters in an XPSDriv printer driver.

However, you can configure the inactivity time-out period in the registry. The PipelineHostTimeout value under the **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print** subkey in the registry defines the printfilterpipelinesvc.exe process time-out in milliseconds. You can increase this value to make it easier to debug an XPSDrv printer driver. Note that the printfilterpipelinesvc.exe process is started to parse the configuration file so that even if there are no filters defined for the driver, the process will still be started.

### Configuring the System for Debugging

To debug an XPSDrv printer driver, you must:

1.  Assign the print queue that uses the driver you want to debug to print to a file port.

2.  Set the PipelineHostTimeout value to a value that will give you enough time to debug the problem.

3.  Send a print job to the print queue that you created in step 1 to start the Printfilterpipelinesvc.exe process.

4.  Attach the debugger to the Printfilterpipelinesvc.exe process and begin debugging.

After you have attached the debugger, you can set breakpoints in the filter modules and begin debugging the printer driver.

If the printer driver that you want to debug causes the printfilterpipelinesvc.exe process to exit before you can attach the debugger, you can do the following:

1.  Create an XPSDrv printer driver that does not have any filters defined in the configuration file.

2.  Create a print queue with the printer driver created in the previous step.

3.  Assign the print queue that uses the driver you want to debug to print to a file port.

4.  Set the PipelineHostTimeout value to a value that will give you enough time to debug the problem.

5.  Send a print job to the print queue that you created in step 2.

6.  Attach the debugger to the Printfilterpipelinesvc.exe process.

7.  Set breakpoints in the printer driver that you want to debug.

8.  Print to the print queue with the driver that you want to debug.

 

 




