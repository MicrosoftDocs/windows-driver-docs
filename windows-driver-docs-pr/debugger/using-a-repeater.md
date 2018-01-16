---
title: Using a Repeater
description: Using a Repeater
ms.assetid: c6904b6d-f28b-4494-95d0-9e6fc3dc10f3
keywords: ["repeater, using a repeater"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Using%20a%20Repeater%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




