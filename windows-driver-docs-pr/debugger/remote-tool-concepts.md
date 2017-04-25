---
title: Remote Tool Concepts
description: Remote Tool Concepts
ms.assetid: 509b25cd-d69a-442d-bd5b-a69266d341c3
keywords: ["Remote Tool, Remote Tool Concepts"]
---

# Remote Tool Concepts


## <span id="ddk_remote_tool_concepts_dtools"></span><span id="DDK_REMOTE_TOOL_CONCEPTS_DTOOLS"></span>


The following concepts are used in the Remote tool.

### <span id="client_and_server"></span><span id="CLIENT_AND_SERVER"></span>Client and Server

The Remote tool uses a client-server paradigm that avoids the words *local* and *remote*, which are relative terms that can be confusing when there are multiple users and multiple computers.

Commands that you type at the client and server computers appear in the Command Prompt windows of both computers.

### <span id="the_server"></span><span id="THE_SERVER"></span>The Server

The *server* is the computer on which the console program runs. The *Remote Server* is the instance of the Remote tool running on the server. The server establishes and names the remote session (named pipe), issues the command to start the console program, and determines who is permitted to connect to the session.

### <span id="the_client"></span><span id="THE_CLIENT"></span>The Client

The *client* is a remote computer that sends commands to the console program. The *Remote Client* is the instance of the Remote tool running on the client computer. The client connects to the remote session that the server established and uses the remote session (named pipe) that the server created to send commands to the console program that runs on the server.

The Remote tool supports multiple clients in each remote session. Each client is running one Remote Client. All of the clients can send commands to the console program running on the server, and all of the clients can see the commands sent and output displayed.

### <span id="visible_session"></span><span id="VISIBLE_SESSION"></span>Visible Session

When remote sessions are *visible*, they appear in the list of remote sessions on the computer. To display the list, use the [**Remote Server query command**](remote-server-query-command.md) (**/q**).

By default, only debugger sessions are visible, that is, sessions in which the value of the *Command* parameter include the words **kd**, **dbg**, **remoteds**, **ntsd**, or **cdb**; otherwise, the session is not visible. The *Command* parameter is part of the Remote tool command on the server.

To make a session visible, add the **/v** parameter to the [**Remote Server**](remote-server-syntax.md) command. To make a debugger session invisible, add the **/-v** parameter to the command.

For help with the Remote Server query command, see [**Remote Server Query Command**](remote-server-query-command.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Tool%20Concepts%20%20RELEASE:%20%284/24/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




