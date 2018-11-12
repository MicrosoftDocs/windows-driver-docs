---
title: Remote Tool
description: The Remote tool, Remote.exe, is a command-line tool that lets you run and control any console program from a remote computer.
ms.assetid: b6fbde9b-1a2a-46b8-9edc-7fa143f5a711
keywords: ["Remote Tool", "Remote.exe", "Remote.exe, See Remote Tool"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Tool


The Remote tool, Remote.exe, is a command-line tool that lets you run and control any console program from a remote computer.

## <span id="Where_to_get_the_Remote_tool"></span><span id="where_to_get_the_remote_tool"></span><span id="WHERE_TO_GET_THE_REMOTE_TOOL"></span>Where to get the Remote tool


Remote.exe is included in [Debugging Tools for Windows](index.md).

## <span id="ddk_remote_tool_dtools"></span><span id="DDK_REMOTE_TOOL_DTOOLS"></span>Remote tool components


The Remote tool includes the following components:

-   A server application that starts a console program and opens a named pipe for client connections.

-   A client application that establishes a connection to a server. Commands typed on the client computer are sent to the console application on the server, and the remote client displays the output from the server's console window.

-   A query feature that lists the remote sessions running on a server computer.

With the Remote tool, you can start multiple server sessions on a single computer where multiple clients can connect to each session. The sessions are limited only by the computer's resources.

This is an older tool that has been eclipsed by more sophisticated tools, primarily Remote Desktop. However, because it is simple and uses very few resources, it is still widely used, typically for remote debugging.

The Remote tool requires that commands be submitted on both the local and remote computers. As such, to use this tool on a computer without a local user, you must develop an alternate way to submit the commands and to restart the computer, if necessary.

The Remote tool can compromise security on your computer, because it does not authenticate users or use Microsoft Windows permissions. By default, any remote computer that can connect and provide the session name can use the named pipe that this tool creates, although you can use Remote tool options to include and exclude particular users and groups.

This section includes:

[Remote Tool Concepts](remote-tool-concepts.md)

[Remote Tool Commands](remote-tool-commands.md)

[Remote Tool Examples](remote-tool-examples.md)

## <span id="related_topics"></span>Related topics


[Tools Included in Debugging Tools for Windows](extra-tools.md)

 

 






