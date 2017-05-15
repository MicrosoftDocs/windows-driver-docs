---
title: The Remote.exe Utility
description: The Remote.exe Utility
ms.assetid: 3780d632-939e-4adb-82f1-fd7c25706b54
keywords: ["remote debugging through remote.exe, remote.exe utility"]
---

# The Remote.exe Utility


## <span id="ddk_the_remote_exe_utility_dbg"></span><span id="DDK_THE_REMOTE_EXE_UTILITY_DBG"></span>


The remote.exe utility is a versatile server/client tool that allows you to run command-line programs on remote computers.

Remote.exe provides remote network access by means of named pipes to applications that use STDIN and STDOUT for input and output. Users at other computers on a network, or connected by a direct-dial modem connection. can either view the remote session or enter commands themselves.

This utility has a large number of uses. For example, when you are developing software, you can compile code with the processor and resources of a remote computer while you perform other tasks on your computer. You can also use remote.exe to distribute the processing requirements for a particular task across several computers.

Please note that remote.exe does no security authorization, and will permit anyone running Remote.exe Client to connect to your Remote.exe Server. This leaves the account under which the Remote.exe Server was run open to anyone who connects.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20The%20Remote.exe%20Utility%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




