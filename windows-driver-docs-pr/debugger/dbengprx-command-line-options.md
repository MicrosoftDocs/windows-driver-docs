---
title: DbEngPrx Command-Line Options
description: The DbEngPrx command line uses the following syntax.
ms.assetid: 3c0675a4-93f0-4aaa-9f33-9a45c48c1ff4
keywords: ["DbEngPrx Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- DbEngPrx Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# DbEngPrx Command-Line Options


The DbEngPrx command line uses the following syntax.

```dbgcmd
dbengprx [-p] -c ClientTransport -s ServerTransport 

dbengprx -? 
```

## <span id="ddk_dbengprx_command_line_options_dbg"></span><span id="DDK_DBENGPRX_COMMAND_LINE_OPTIONS_DBG"></span>Parameters


<span id="_______-p______"></span><span id="_______-P______"></span> **-p**   
Causes DbEngPrx to continue existing even after all connections to it are dropped.

<span id="_______-c_______ClientTransport______"></span><span id="_______-c_______clienttransport______"></span><span id="_______-C_______CLIENTTRANSPORT______"></span> **-c** *ClientTransport*   
Specifies the protocol settings to be used in connecting to the server. The protocol should match that used when the server was created. For details, see [**Activating a Repeater**](activating-a-repeater.md).

<span id="_______-s_______ServerTransport______"></span><span id="_______-s_______servertransport______"></span><span id="_______-S_______SERVERTRANSPORT______"></span> **-s** *ServerTransport*   
Specifies the protocol settings that will be used when the client connects to the repeater. For details, see [**Activating a Repeater**](activating-a-repeater.md).

<span id="_______-_______"></span> **-?**   
Displays a message box with help text for the DbEngPrx command line.

For information about using DbEngPrx, see [Repeaters](repeaters.md).

 

 





