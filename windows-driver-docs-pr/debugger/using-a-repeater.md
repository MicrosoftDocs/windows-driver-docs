---
title: Using a Repeater
description: Using a Repeater
ms.assetid: c6904b6d-f28b-4494-95d0-9e6fc3dc10f3
keywords: ["repeater, using a repeater"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using a Repeater


## <span id="ddk_using_a_repeater_dbg"></span><span id="DDK_USING_A_REPEATER_DBG"></span>


A repeater connection obeys very simple rules:

-   Any communication that the server and client intend for each other passes through the repeater without alteration.

-   Any action that the server performs with respect to the transport connection affects the repeater (and only indirectly affects the client).

-   Any action that the client performs with respect to the transport connection affects the repeater (and only indirectly affects the server).

This means that any debugging commands, debugger output, control keys, and file access will take place exactly as if the client and server were directly connected. The repeater will be invisible to all these commands.

Actions that terminate the connection itself will affect the repeater. For example, if you issue a [**qq (Quit)**](q--qq--quit-.md) command from the client, the server will shut down and will send a shutdown signal to the transport. This will cause the repeater to exit (unless it was started with the **-p** option). As another example, the [**.clients (List Debugging Clients)**](-clients--list-debugging-clients-.md) command will list the client's computer name, but it will show the connection protocol used to connect the server with the repeater.

If the server is shut down, the repeater will automatically exit (unless it was started with the **-p** option). When the repeater shuts down, this will cause a debugging client to exit as well, although a smart client will not. If for some reason you need to terminate the repeater directly, you can use Task Manager or the kill.exe tool.

 

 





