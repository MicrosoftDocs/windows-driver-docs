---
title: ".netuse (Control Network Connections)"
description: "The .netuse command adds a connection to a network share."
keywords: [".netuse (Control Network Connections) Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- .netuse (Control Network Connections)
api_type:
- NA
---

# .netuse (Control Network Connections)


The **.netuse** command adds a connection to a network share.

```dbgcmd
.netuse /a "[Local]" "Remote" "[User]" "[Password]" 
```

## <span id="ddk_meta_control_network_connections_dbg"></span><span id="DDK_META_CONTROL_NETWORK_CONNECTIONS_DBG"></span>Parameters


<span id="________a______"></span><span id="________A______"></span> **/a**   
Adds a new connection. You must always use the **/a** switch.

<span id="_______Local______"></span><span id="_______local______"></span><span id="_______LOCAL______"></span> *Local*   
Specifies the drive letter to use for the connection. You must enclose *Local* in quotation marks. If you omit this parameter, you must include an empty pair of quotation marks as the parameter.

<span id="_______Remote______"></span><span id="_______remote______"></span><span id="_______REMOTE______"></span> *Remote*   
Specifies the UNC path of the share that is being connected. You must enclose *Remote* in quotation marks.

<span id="_______User______"></span><span id="_______user______"></span><span id="_______USER______"></span> *User*   
Specifies the user name of an account that is authorized to establish the connection. You must enclose *User* in quotation marks. If you omit this parameter, you must include an empty pair of quotation marks as the parameter.

<span id="_______Password______"></span><span id="_______password______"></span><span id="_______PASSWORD______"></span> *Password*   
Specifies the password that is associated with the *User* account. You must enclose *Password* in quotation marks. If you omit this parameter, you must include an empty pair of quotation marks as the parameter.

## Environment

|  Item  | Description          |
|--------|----------------------|
|Modes   |User mode, kernel mode|
|Targets |Live, crash dump      |
|Platforms|All                  |

 

## Remarks

The **.netuse** command behaves like the **net use** Microsoft MS-DOS command.

If you use **.netuse** during a remote debugging session, this command affects the debugging server, not the debugging client.

The following example shows this command.

```dbgcmd
0:000> .netuse "m:" "\\myserver\myshare" "" "" 
```

