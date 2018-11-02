---
title: Remote Server Query Command
description: To display a list of available sessions on a local or Remote Server, use the following syntax.
ms.assetid: c95114a3-2ff5-456b-90e2-4d7bc6346f1f
keywords: ["Remote Server Query Command Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- Remote Server Query Command
api_type:
- NA
ms.localizationpriority: medium
---

# Remote Server Query Command


To display a list of available sessions on a local or Remote Server, use the following syntax.

```console
remote /q Computer
```dbgcmd

## <span id="ddk_remote_server_query_command_dtools"></span><span id="DDK_REMOTE_SERVER_QUERY_COMMAND_DTOOLS"></span>Parameters


<span id="________q______"></span><span id="________Q______"></span> **/q**   
Query. Displays the visible remote sessions on the specified computer.

<span id="_______Computer______"></span><span id="_______computer______"></span><span id="_______COMPUTER______"></span> *Computer*   
Specifies the name of the computer. This parameter is required (even on the local computer).

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The query display includes only server sessions; it does not display client connections to remote sessions.

The query display includes only visible sessions. There is no command to display invisible sessions.

The query display includes all visible sessions, including those that restrict users (**/u** and **/ud**). The user might not have permission to connect to all of the sessions in the list.

When there are no remote sessions running on the server, the Remote tool displays the following message:

```console
No Remote servers running on \\Computer
```

However, when the only remote sessions running on the computer are invisible remote sessions, the Remote tool displays the following message:

```console
No visible sessions on server \\Computer
```

 

 





