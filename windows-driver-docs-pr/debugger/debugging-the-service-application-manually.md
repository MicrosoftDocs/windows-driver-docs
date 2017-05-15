---
title: Debugging the Service Application Manually
description: Debugging the Service Application Manually
ms.assetid: 9be3976f-dd56-42f2-ac85-1c5a1f87a4ee
---

# Debugging the Service Application Manually


Manually attaching to a service application after it has been started is much like debugging any running user-mode process.

Use [the TList tool](tlist.md) with the **/s** option to display the process ID (PID) of each running process and the services active in each process.

If the service application you want to debug is combined with other services in a single process, you must isolate it before debugging it. To do this, perform the procedure described in Isolating the Service. At the end of this procedure, restart the service.

To determine the new PID of the service, issue the following Service Configuration tool (Sc.exe) command, where *ServiceName* is the name of the service:

```
sc queryex ServiceName 
```

Now start WinDbg or CDB with this service application as the target. There are three ways to do this: by specifying the PID with the -p option, by specifying the executable name with the -pn option (if the executable name is unique), or by specifying the service name with the -psn option.

For example, if the process SpoolSv.exe has a PID of 651 and contains the service named *Spooler*, the following three commands are equivalent:

```
windbg -p 651 [AdditionalOptions] 
windbg -pn spoolsv.exe [AdditionalOptions] 
windbg -psn spooler [AdditionalOptions] 
```

After the debugger starts, proceed as you would in any other user-mode debugging session.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20the%20Service%20Application%20Manually%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




