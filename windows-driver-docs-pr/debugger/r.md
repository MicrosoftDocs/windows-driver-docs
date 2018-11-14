---
title: R  (Windows Debugger Glossary)
description: Glossary page - R
Robots: noindex, nofollow
ms.assetid: 77bd1a66-39b3-4990-801e-4192a6e9cf47
ms.author: domars
ms.date: 11/28/2017
ms.localizationpriority: medium
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

For more information, see [**Register Context**](-thread--set-register-context-.md).

<span id="retail_build"></span><span id="RETAIL_BUILD"></span>**retail build**  
See free build.

 

 





