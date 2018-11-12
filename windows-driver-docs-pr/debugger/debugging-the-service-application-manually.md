---
title: Debugging the Service Application Manually
description: Debugging the Service Application Manually
ms.assetid: 9be3976f-dd56-42f2-ac85-1c5a1f87a4ee
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Debugging the Service Application Manually


Manually attaching to a service application after it has been started is much like debugging any running user-mode process.

Use [the TList tool](tlist.md) with the **/s** option to display the process ID (PID) of each running process and the services active in each process.

If the service application you want to debug is combined with other services in a single process, you must isolate it before debugging it. To do this, perform the procedure described in Isolating the Service. At the end of this procedure, restart the service.

To determine the new PID of the service, issue the following Service Configuration tool (Sc.exe) command, where *ServiceName* is the name of the service:

```console
sc queryex ServiceName 
```

Now start WinDbg or CDB with this service application as the target. There are three ways to do this: by specifying the PID with the -p option, by specifying the executable name with the -pn option (if the executable name is unique), or by specifying the service name with the -psn option.

For example, if the process SpoolSv.exe has a PID of 651 and contains the service named *Spooler*, the following three commands are equivalent:

```console
windbg -p 651 [AdditionalOptions] 
windbg -pn spoolsv.exe [AdditionalOptions] 
windbg -psn spooler [AdditionalOptions] 
```

After the debugger starts, proceed as you would in any other user-mode debugging session.

 

 





