---
title: Preparing to Debug the Service Application
description: Preparing to Debug the Service Application
ms.assetid: 332b7bcf-22e4-4b98-bcb3-3646f8bd63fd
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Preparing to Debug the Service Application


This topic lists all the preparatory steps that may be required prior to debugging a service application. Which steps are required in your scenario depends on which attach option you have chosen and which debugging configuration you have chosen. For a list of these choices, see [Choosing the Best Method](choosing-the-best-method.md).

Each of the preparatory steps described in this topic specifies the conditions under which it is required. These steps can be done in any order.

### <span id="enabling-the-debugging-of-the-initialization_code"></span><span id="ENABLING_THE_DEBUGGING_OF_THE_INITIALIZATION_CODE"></span> Enabling the Debugging of the Initialization Code

If you plan to debug the service application from the beginning of its execution, including its initialization code, this preparatory step is required.

Locate or create the following registry key, where *ProgramName* is the name of the service application's executable file:

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\ProgramName 
```

*ProgramName* should include the file name extension, but not the path. For example, *ProgramName* might be Myservice.exe or Thisservice.dll.

Under this registry key, create a string data value entitled **Debugger**. The value of this string should be set to the full path and file name of a debugger to be attached to the service application.

-   If you plan to debug locally, use a string such as the following:

    ```console
    c:\Debuggers\windbg.exe 
    ```

    Do not choose this option if you are running Windows Vista or a later version of Windows.

-   If you plan to use remote debugging, specify NTSD with the -noio option. This causes NTSD to run without any console of its own, accessible only through the remote connection. For example:

    ```console
    c:\Debuggers\ntsd.exe -server ServerTransport -noio -y SymbolPath 
    ```

    If your debugging session begins before Windows is fully loaded, you may not be able to access symbols from a remote share; in such a case, you must use local symbols. *ServerTransport* must specify a transport protocol that is implemented by the Windows kernel without interfacing with a user-mode service, such as TCP or NPIPE. For the syntax of *ServerTransport*, see [**Activating a Debugging Server**](activating-a-debugging-server.md).

-   If you plan to control the user-mode debugger from a kernel-mode debugger, specify NTSD with the -d option. For example:

    ```console
    c:\Debuggers\ntsd.exe -d -y SymbolPath 
    ```

    If you plan to use this method and your user-mode symbols will be accessed from a symbol server, you should combine this method with remote debugging. In this case, specify NTSD with the -ddefer option. Choose a transport protocol that is implemented by the Windows kernel without interfacing with a user-mode service, such as TCP or NPIPE. For example:

    ```console
    c:\Debuggers\ntsd.exe -server ServerTransport -ddefer -y SymbolPath 
    ```

    For details, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

After this registry edit is complete, the debugger is launched whenever a service with this name is started or restarted.

### <span id="enabling-the-service-application-to-break-into-the-debugger"></span><span id="ENABLING_THE_SERVICE_APPLICATION_TO_BREAK_INTO_THE_DEBUGGER"></span> Enabling the Service Application to Break Into the Debugger

If you want the service application to break into the debugger when it crashes or encounters an exception, this preparatory step is required. This step is also required if you want the service application to break into the debugger by calling the **DebugBreak** function.

**Note**   If you have enabled debugging of the initialization code (the step described in the subsection "Enabling the Debugging of the Initialization Code"), you should skip this step. When initialization code debugging is enabled, the debugger attaches to the service application when it starts, which causes all crashes, exceptions, and calls to **DebugBreak** to be routed to the debugger without additional preparations being needed.

 

This preparatory step involves registering the chosen debugger as the postmortem debugger. This is done by using the -iae or -iaec options on the debugger command line. We recommend the following commands, but if you want to vary them, see the syntax details in [Enabling Postmortem Debugging](enabling-postmortem-debugging.md).

-   If you plan to debug locally, use a command such as the following:

    ```console
    windbg -iae 
    ```

    Do not choose this option if you are running Windows Vista or a later version of Windows.

-   If you plan to use remote debugging, specify NTSD with the -noio option. This causes NTSD to run without any console of its own, accessible only through the remote connection. To install a postmortem debugger that includes the -server parameter, you must manually edit the registry; for details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md). For example, the **Debugger** value of the **AeDebug** key could be the following:

    ```console
    ntsd -server npipe:pipe=myproc%x -noio -p %ld -e %ld -g -y SymbolPath 
    ```

    In the pipe specification, the **%x** token is replaced with the process ID of the process that launches the debugger. This guarantees that if more than one process launches a postmortem debugger, each has a unique pipe name. If your debugging session begins before Windows is fully loaded, you may not be able to access symbols from a remote share; in such a case, you must use local symbols. *ServerTransport* must specify a transport protocol that is implemented by the Windows kernel without interfacing with a user-mode service, such as TCP or NPIPE. For the syntax of *ServerTransport*, see [**Activating a Debugging Server**](activating-a-debugging-server.md).

-   If you plan to control the user-mode debugger from a kernel-mode debugger, specify NTSD with the -d option. For example:

    ```console
    ntsd -iaec -d -y SymbolPath 
    ```

    If you choose this method and intend to access user-mode symbols from a symbol server, you should combine this method with remote debugging. In this case, specify NTSD with the -ddefer option. Choose a transport protocol that is implemented by the Windows kernel without interfacing with a user-mode service, such as TCP or NPIPE. To install a postmortem debugger that includes the -server parameter, you must manually edit the registry; for details, see [Enabling Postmortem Debugging](enabling-postmortem-debugging.md). For example, the **Debugger** value of the **AeDebug** key could be the following:

    ```console
    ntsd -server npipe:pipe=myproc%x -ddefer -p %ld -e %ld -g -y SymbolPath 
    ```

    For details, see [Controlling the User-Mode Debugger from the Kernel Debugger](controlling-the-user-mode-debugger-from-the-kernel-debugger.md).

When you issue one of these commands, the postmortem debugger is registered. This debugger will be launched whenever any user-mode program, including a service application, encounters an exception or runs a **DebugBreak** function.

### <span id="adjusting-the-service-application-timeout"></span><span id="ADJUSTING_THE_SERVICE_APPLICATION_TIMEOUT"></span> Adjusting the Service Application Timeout

If you plan to launch the debugger automatically (either when the service starts or when it encounters an exception), this preparatory step is required.

Locate the following registry key:

```text
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control
```

Under this key, locate or create a DWORD data value called **ServicesPipeTimeout**. Set this entry to the amount of time in milliseconds that you want the service to wait before timing out. For example, a value of 60,000 is one minute, while a value of 86,400,000 is 24 hours. When this registry value is not set, the default timeout is about thirty seconds.

The significance of this value is that a clock starts to run when each service is launched, and when the timeout value is reached, any debugger attached to the service is terminated. Therefore, the value you choose should be longer than the total amount of time that elapses between the launching of the service and the completion of your debugging session.

This setting applies to every service that is started or restarted after the registry edit is complete. If some service crashes or hangs and this setting is still in effect, the problem is not detected by Windows. Therefore, you should use this setting only while you are debugging, and return the registry key to its original value after your debugging is complete.

### <span id="isolating-the-service"></span><span id="ISOLATING_THE_SERVICE"></span> Isolating the Service

Sometimes, multiple services are combined in a single Service Host (Svchost) process. If you want to debug such a service, you must first isolate it into a separate Svchost process.

There are three methods by which you can isolate a service. Microsoft recommends the Moving the Service to its Own Group method, as follows. The alternative methods (Changing the Service Type and Duplicating the SvcHost Binary) can be used on a temporary basis for debugging, but because they alter the way the service runs, they are not as reliable as the first method.

**Preferred Method: Moving the Service to its Own Group**

1.  Issue the following Service Configuration tool (Sc.exe) command, where *ServiceName* is the name of the service:

    ```console
    sc qc ServiceName 
    ```

    This displays the current configuration values for the service. The value of interest is BINARY\_PATH\_NAME, which specifies the command line used to launch the service control program. In this scenario, because your service is not yet isolated, this command line includes a directory path, Svchost.exe, and some SvcHost parameters, including the -k switch, followed by a group name. For example, it may look something like this:

    ```console
    %SystemRoot%\System32\svchost.exe -k LocalServiceNoNetwork 
    ```

    Remember this path and the group name; they are used in steps 5 and 6.

2.  Locate the following registry key:

    ```text
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SvcHost 
    ```

    Create a new REG\_MULTI\_SZ value with a unique name (for example, **TempGrp**).

3.  Set this new value equal to the name of the service that you want to isolate. Do not include any directory path or file name extension. For example, you might set the new value **TempGrp** equal to **MyService**.

4.  Under the same registry key, create a new key with the same name you used in step 2. For example:

    ```text
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SvcHost\TempGrp 
    ```

    Now the SvcHost key contains a value with the new name and also has a subordinate key with this same name.

5.  Look for another key subordinate to the SvcHost key that has the same name as the group you found in step 1. If such a key exists, examine all the values in it, and create duplicates of them in the new key you created in step 4.

    For example, the old key might be named this:

    ```text
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SvcHost\LocalServiceNoNetwork 
    ```

    and it might contain values such as **CoInitializeSecurityParam**, **AuthenticationCapabilities**, and other values. You would go to the newly created key:

    ```text
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SvcHost\TempGrp 
    ```

    and create values in it that are identical in name, type, and data to those in the old key.

    If the old key does not exist, you do not need to create a new key.

6.  Use the following Service Configuration tool command to revise the path found in step 1:

    ```console
    sc config ServiceName binPath= "RevisedPath" 
    ```

    In this command, *ServiceName* is the name of the service, and *RevisedPath* is the new value you are supplying for BINARY\_PATH\_NAME. For *RevisedPath*, use the exact same path as the one displayed in step 1, including all the options shown on that line, making only one change: replace the parameter following the -k switch with the name of the new registry value you created in step 2. Enclose *RevisedPath* in quotation marks. The space after the equal sign is required.

    For example, your command might look like this:

    ```console
    sc config MyService binPath= "%SystemRoot%\System32\svchost.exe -k TempGrp" 
    ```

    You may want to use the **sc qc** command again to review the change you have made.

These settings will take effect the next time the service is started. To clear the effects of the old service, we recommend that you restart Windows rather than just restarting the service.

After you have completed your debugging, if you want to return this service to the shared service host, use the **sc config** command again to return the binary path to its original value, and delete the new registry keys and values you created..

**Alternative Method: Changing the Service Type**

1.  Issue the following Service Configuration tool (Sc.exe) command, where *ServiceName* is the name of the service:

    ```console
    sc config ServiceName type= own 
    ```

    The space after the equal sign is required.

2.  Restart the service, by using the following commands:
    ```console
    net stop ServiceName 
    net start ServiceName 
    ```

This alternative is not the recommended method because it can alter the behavior of the service. If you do use this method, use the following command to revert to the normal behavior after you have completed your debugging:

```console
sc config ServiceName type= share 
```

**Alternative Method: Duplicating the SvcHost Binary**

1.  The Svchost.exe executable file is located in the system32 directory of Windows. Make a copy of this file, name it svhost2.exe, and place it in the system32 directory as well.

2.  Issue the following Service Configuration tool (Sc.exe) command, where *ServiceName* is the name of the service:

    ```console
    sc qc ServiceName 
    ```

    This command displays the current configuration values for the service. The value of interest is BINARY\_PATH\_NAME, which specifies the command line used to launch the service control program. In this scenario, because your service is not yet isolated, this command line will include a directory path, Svchost.exe, and probably some SvcHost parameters. For example, it may look something like this:

    ```console
    %SystemRoot%\System32\svchost.exe -k LocalServiceNoNetwork 
    ```

3.  To revise this path, issue the following command:

    ```console
    sc config ServiceName binPath= "RevisedPath" 
    ```

    In this command, *ServiceName* is the name of the service, and *RevisedPath* is the new value you are supplying for BINARY\_PATH\_NAME. For *RevisedPath*, use the exact same path as the one displayed in step 2, including all the options shown on that line, making only one change: replace Svchost.exe with Svchost2.exe. Enclose *RevisedPath* in quotation marks. The space after the equal sign is required.

    For example, your command might look like this:

    ```console
    sc config MyService binPath= "%SystemRoot%\System32\svchost2.exe -k LocalServiceNoNetwork" 
    ```

    You can use the **sc qc** command again to review the change you have made.

4.  Restart the service by using the following commands:
    ```console
    net stop ServiceName 
    net start ServiceName 
    ```

This alternative is not the recommended method because it can alter the behavior of the service. If you do use this method, use the **sc config** command to change the path back to its original value after you have completed your debugging.

 

 





