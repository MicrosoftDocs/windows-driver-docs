---
title: Remote Session Commands
description: Remote Session Commands
ms.assetid: 8c7da3e9-c983-4253-92fb-ce64f22cdc6c
keywords: ["Remote Tool, remote session commands"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Remote Session Commands


## <span id="ddk_remote_session_commands_dtools"></span><span id="DDK_REMOTE_SESSION_COMMANDS_DTOOLS"></span>


Use the following commands to communicate with the Remote tool during a console session.

<span id="_H"></span><span id="_h"></span><strong>@H</strong>  
Displays the session commands on server and client computers. Works on server and client computers.

<span id="_M_Message"></span><span id="_m_message"></span><span id="_M_MESSAGE"></span><strong>@M</strong> *Message*  
Displays the specified message on all server and client computers in the session. Works on server and client computers.

<span id="_P_Message"></span><span id="_p_message"></span><span id="_P_MESSAGE"></span><strong>@P</strong> *Message*  
Generates a pop-up window on the server computer with the specified message. On client computers, the message appears in the command window. Works on server and client computers.

<span id="_Q"></span><span id="_q"></span><strong>@Q</strong>  
Quit. Disconnects a client computer from the session. Works only on a client computer.

<span id="_K"></span><span id="_k"></span><strong>@K</strong>  
Disconnects all clients and ends the remote session. Works only on a server computer.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For samples, see "Using the Session Commands" in [Remote Tool Examples](remote-tool-examples.md).

In response to the session commands, the Remote tool displays a label with the day and time that the command was executed. The time for all events is displayed in the time zone of the server computer.

 

 





