# Debugging a Universal Windows driver

Starting in Windows 10, you can build your KMDF or UMDF driver so that it gets additional driver debugging information through the [Inflight Trace Recorder](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Dn914610). Universal Windows drivers can take advantage of this feature.

In addition, if you used the Visual Studio KMDF template, your driver uses Windows software trace preprocessor (WPP) to write trace messages. Your driver is an ETW provider with a provider GUID.

To send a trace message from your driver, use this code:

   ```
   TraceEvents(TRACE_LEVEL_INFORMATION, TRACE_DRIVER, &quot;%!FUNC! Entry&quot;);
   ```
       
You can access the ETW logs either using Tracelog via the [TShell tool](http://go.microsoft.com/fwlink/p/?linkid=617388) on a phone, or by using [!wmitrace](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Ff561362) in a debugger session.

To use Tracelog on a phone:

1.  Establish a kernel-mode debugging session between a host computer and the phone.
2.  On the host computer, in TShell, enter this command:

       ```
       exec-device tracelog -addautologger MyLogger05 -guid c:\SteveGuid.txt -level 4 -flag 0xF –kd
       ```
       
3.  Reboot the phone, and watch for trace messages in the debugger.

All existing kernel mode debug transports continue to work on Windows 10 for desktop editions. However, for both user-mode and kernel-mode drivers, you must use a remote debugger session over KDNET to test Windows 10 Mobile. For more info, see [Setting Up Kernel-Mode Debugging over a Network Cable Manually](https://msdn.microsoft.com/en-us/Library/Windows/Hardware/Hh439346) in Visual Studio.
