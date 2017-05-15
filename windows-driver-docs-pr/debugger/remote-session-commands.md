---
title: Remote Session Commands
description: Remote Session Commands
ms.assetid: 8c7da3e9-c983-4253-92fb-ce64f22cdc6c
keywords: ["Remote Tool, remote session commands"]
---

# Remote Session Commands


## <span id="ddk_remote_session_commands_dtools"></span><span id="DDK_REMOTE_SESSION_COMMANDS_DTOOLS"></span>


Use the following commands to communicate with the Remote tool during a console session.

<span id="_H"></span><span id="_h"></span>**@H**  
Displays the session commands on server and client computers. Works on server and client computers.

<span id="_M_Message"></span><span id="_m_message"></span><span id="_M_MESSAGE"></span>**@M** *Message*  
Displays the specified message on all server and client computers in the session. Works on server and client computers.

<span id="_P_Message"></span><span id="_p_message"></span><span id="_P_MESSAGE"></span>**@P** *Message*  
Generates a pop-up window on the server computer with the specified message. On client computers, the message appears in the command window. Works on server and client computers.

<span id="_Q"></span><span id="_q"></span>**@Q**  
Quit. Disconnects a client computer from the session. Works only on a client computer.

<span id="_K"></span><span id="_k"></span>**@K**  
Disconnects all clients and ends the remote session. Works only on a server computer.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

For samples, see "Using the Session Commands" in [Remote Tool Examples](remote-tool-examples.md).

In response to the session commands, the Remote tool displays a label with the day and time that the command was executed. The time for all events is displayed in the time zone of the server computer.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Session%20Commands%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




