---
title: Remote Server Syntax
description: To start the server side of the Remote tool, use the following syntax at the command line.
ms.assetid: fecc9f43-6946-4d99-840b-a85c75ac397c
keywords: ["Remote Server Syntax Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- Remote Server Syntax
api_type:
- NA
---

# Remote Server Syntax


To start the server side of the Remote tool, use the following syntax at the command line.

```
    remote /s Command SessionName [/f Color] [/b] [/u User [/u User...]] [/ud User [/ud User...]] [/v | /-v]

   
```

## <span id="ddk_remote_server_syntax_dtools"></span><span id="DDK_REMOTE_SERVER_SYNTAX_DTOOLS"></span>Parameters


<span id="________s______"></span><span id="________S______"></span> **/s**   
Starts a server session.

<span id="_______Command______"></span><span id="_______command______"></span><span id="_______COMMAND______"></span> *Command*   
Specifies the command that starts the console-based program. The command can include parameters. If the command includes spaces, enclose it in quotation marks.

<span id="_______SessionName______"></span><span id="_______sessionname______"></span><span id="_______SESSIONNAME______"></span> *SessionName*   
Assigns a name to the remote session. If the name includes spaces, enclose it in quotation marks. This parameter is not case-sensitive.

<span id="________f______"></span><span id="________F______"></span> **/f**   
Specifies the color of the text in the server command window.

<span id="________b______"></span><span id="________B______"></span> **/b**   
Specifies the background color of the server command window.

<span id="_______Color______"></span><span id="_______color______"></span><span id="_______COLOR______"></span> *Color*   
Specifies a color. Valid values are black, blue, green, cyan, red, purple, yellow, white, lblack, lblue, lgreen, lred, lpurple, lyellow, and lwhite.

<span id="________u______"></span><span id="________U______"></span> **/u**   
Specifies users or groups that are permitted to connect to the remote session; by default, everyone is permitted. When you use this parameter, everyone is denied permission, except for the users and groups specified by the *User* subparameter.

<span id="________ud______"></span><span id="________UD______"></span> **/ud**   
Specifies users or groups that are denied permission to connect to the remote session; by default, no one is denied permission.

<span id="_______User______"></span><span id="_______user______"></span><span id="_______USER______"></span> *User*   
Specifies the name of a user or group in \[*domain* | *computer*\]\\{*user* | *group*} format. When specifying users or groups on the local computer, omit the computer name.

<span id="________v______"></span><span id="________V______"></span> **/v**   
Makes a session visible. For more information, see [Visible Session](remote-tool-concepts.md#visible-session).

By default, only debugger sessions are visible, that is, sessions in which the value of the *Command* parameter include the words **kd**, **dbg**, **remoteds**, **ntsd**, or **cdb**; otherwise, the session is not visible.

<span id="_______-v______"></span><span id="_______-V______"></span> **-v**   
Makes a remote debugger session invisible. For more information, see [Visible Session](remote-tool-concepts.md#visible-session).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The *Command* and *SessionName* parameters must appear in the order shown on the syntax line.

To end a remote session, type **@k**. For more information, see [Remote Session Commands](remote-session-commands.md).

The Remote tool will not create a session that the current user does not have permission to join.

When starting more than one remote session on a single computer, open a new command window for each session. Also, use a different session name for each session. Because the session names are used to label the named pipes, they must be unique on the computer.

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
remote /s "i386kd -v" TestSession
remote /s "cmd" "My Remote Session" /f white /b black /u Server01\Administrators
remote /s "ntsd -d -g -x" DebugIt /-v
remote /q Server01
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Server%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




