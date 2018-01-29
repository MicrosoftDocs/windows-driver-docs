---
title: Remote Client Syntax
description: To start the client side of the Remote tool, use the following syntax at the command line.
ms.assetid: 4728ef17-a365-4024-815c-2719b51b81f6
keywords: ["Remote Client Syntax Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- Remote Client Syntax
api_type:
- NA
---

# Remote Client Syntax


To start the client side of the Remote tool, use the following syntax at the command line.

```
remote /c Server SessionName [/L Lines] [/f] [/b] [/k ColorFile] 
```

## <span id="ddk_remote_client_syntax_dtools"></span><span id="DDK_REMOTE_CLIENT_SYNTAX_DTOOLS"></span>Parameters


<span id="________c______"></span><span id="________C______"></span> **/c**   
Connects the client to a remote session.

<span id="_______Server______"></span><span id="_______server______"></span><span id="_______SERVER______"></span> *Server*   
Specifies the computer name of the server that established the session.

<span id="_______SessionName______"></span><span id="_______sessionname______"></span><span id="_______SESSIONNAME______"></span> *SessionName*   
Specifies the name of the remote session. This parameter is not case-sensitive.

<span id="________L_______Lines______"></span><span id="________l_______lines______"></span><span id="________L_______LINES______"></span> **/L** *Lines*   
Specifies the number of lines from the console display that are sent to the client computer. The default is 200 lines. *Lines* is a decimal number.

<span id="________f______"></span><span id="________F______"></span> **/f**   
Specifies the color of the text in the server command window.

<span id="________b______"></span><span id="________B______"></span> **/b**   
Specifies the background color of the server command window.

<span id="_______Color______"></span><span id="_______color______"></span><span id="_______COLOR______"></span> *Color*   
Specifies a color. Valid values are black, blue, green, cyan, red, purple, yellow, white, lblack, lblue, lgreen, lred, lpurple, lyellow, and lwhite.

<span id="________k_______ColorFile______"></span><span id="________k_______colorfile______"></span><span id="________K_______COLORFILE______"></span> **/k** *ColorFile*   
Indicates the path (optional) and name of a formatted text file that specifies the colors for displaying the output on the client computer.

The color file associates keywords in the output with text colors. When the keywords appear in a line of output, the Remote tool applies the associated text color to that line. For the format of the file, see "Remarks".

<span id="________q_______Computer______"></span><span id="________q_______computer______"></span><span id="________Q_______COMPUTER______"></span> **/q** *Computer*   
Displays the remote sessions available on the specified computer. Only visible sessions appear in the list. (See **/v** in [**Remote Server Syntax**](remote-server-syntax.md).)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The *Server* and *SessionName* parameters must appear in the order shown on the syntax line.

To disconnect from a remote session, type **@q**. For more information, see [Remote Session Commands](remote-session-commands.md).

**Keyword Color File.** The format of the keyword color file is as follows. The keyword interpreter is not case sensitive.

The keyword or phrase appears on a line by itself. The colors associated with that keyword appear by themselves on the following line, as shown in the syntax:

```
Keyword
TextColor[, BackgroundColor]
```

For example, the following file directs Remote to display lines that include the word "error" in black text on a light red background; to display lines that include the word "warning" in light blue (on the default background), and lines that include the phrase "Windows Vista" in light green on the default background.

```
ERROR
black, lred
WARNING
lblue
Windows Vista
lgreen
```

### <span id="sample_usage"></span><span id="SAMPLE_USAGE"></span>Sample Usage

```
remote /c Server01 TestSession
remote /c Domain1\ComputerA0 "cmd" "My Remote Session"
remote /c Server01 TestSession /L 50 /f black /b white /k c:\remote_file.txt
remote /q Server01
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Remote%20Client%20Syntax%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




