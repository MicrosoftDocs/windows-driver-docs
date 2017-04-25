---
title: R
description: Glossary page
Robots: noindex, nofollow
ms.assetid: 77bd1a66-39b3-4990-801e-4192a6e9cf47
---

# R


<span id="remote_debugging"></span><span id="REMOTE_DEBUGGING"></span>**remote debugging**  
Remote debugging is the practice of using a remote connection to perform debugging.

Since user-mode debugging is usually done on one machine, remote user-mode debugging typically uses two machines. In this scenario, one computer contains the target application and a debugging server, while the other computer contains the debugging client. An alternate method is to have the target application and a process server on one computer, and a smart client on the other.

Since kernel-mode debugging is usually done on two machines, remote kernel-mode debugging requires three machines. The target computer is the computer being debugged. The server is attached to the target; it contains the kernel-mode debugger. The client is the computer which is controlling the session remotely. Typically, one computer is the being debugged, another contains the debugging server, and the third contains the debugging client.

In addition, there are other methods of remote debugging: using the Remote tool, using a KD connection server, or using a repeater. The method you should choose depends on the configuration of the machines in question and the available connections.

For more information, see [Remote Debugging](remote-debugging.md).

<span id="register"></span><span id="REGISTER"></span>**register**  
A very fast temporary memory location in the CPU.

<span id="register_context"></span><span id="REGISTER_CONTEXT"></span>**register context**  
The full processor state which includes all the processor's registers.

For more information, see [**Register Context**](https://msdn.microsoft.com/library/windows/hardware/ff565449).

<span id="retail_build"></span><span id="RETAIL_BUILD"></span>**retail build**  
See free build.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20R%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




