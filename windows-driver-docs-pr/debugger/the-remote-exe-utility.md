---
title: The Remote.exe Utility
description: The Remote.exe Utility
ms.assetid: 3780d632-939e-4adb-82f1-fd7c25706b54
keywords: ["remote debugging through remote.exe, remote.exe utility"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# The Remote.exe Utility


## <span id="ddk_the_remote_exe_utility_dbg"></span><span id="DDK_THE_REMOTE_EXE_UTILITY_DBG"></span>


The remote.exe utility is a versatile server/client tool that allows you to run command-line programs on remote computers.

Remote.exe provides remote network access by means of named pipes to applications that use STDIN and STDOUT for input and output. Users at other computers on a network, or connected by a direct-dial modem connection. can either view the remote session or enter commands themselves.

This utility has a large number of uses. For example, when you are developing software, you can compile code with the processor and resources of a remote computer while you perform other tasks on your computer. You can also use remote.exe to distribute the processing requirements for a particular task across several computers.

Please note that remote.exe does no security authorization, and will permit anyone running Remote.exe Client to connect to your Remote.exe Server. This leaves the account under which the Remote.exe Server was run open to anyone who connects.

 

 





