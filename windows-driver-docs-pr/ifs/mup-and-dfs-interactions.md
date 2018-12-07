---
title: MUP and DFS Interactions
description: MUP and DFS Interactions
ms.assetid: 39c1f1e3-fb2d-46e7-b3dc-3d4bfab9608c
keywords:
- DFS WDK network redirectors
- Distributed File System WDK network redirectors
- kernel network redirectors WDK , MUP
- MUP WDK network redirectors
- multiple UNC provider WDK network redirectors
- UNC WDK network redirectors
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MUP and DFS Interactions


When a Universal Naming Convention (UNC) path is used by an application, a request is sent to the multiple UNC provider (MUP) to determine which network provider to use. MUP channels the request to the appropriate network redirector (the UNC provider) that is capable of handling the remote file system request. If the Distributed File System (DFS) client is enabled, MUP first passes the request for a particular "\\\\server\\share" to the DFS client to determine if the request is for a DFS share rather than a normal remote file share.

The default behavior is that the DFS client is enabled. The DFS client is disabled depending on the value of a registry entry located below the following:

```cpp
HKLM\System\CurrentControlSet\Services\Mup
```

When the DisableDfs registry entry has a DWORD value of 1, the DFS client is disabled.

Assuming the prefix of a path specified in a name-based operation is not in the prefix cache maintained by MUP, the DFS client (when enabled) implicitly takes precedence over all redirectors. The DFS client attempts to determine whether a UNC path specified is a DFS path. It does this by sending a referral request to the IPC$ share of an appropriate server. If the path is determined to be a DFS path, the DFS client handles the operation. Otherwise, the DFS client passes the name-based request to MUP for prefix resolution to be handled by an appropriate redirector.

When a request to access the IPC$ share is sent to a system where the LAN Manager Server (sometimes called SMB Server), srv.sys, is disabled or not installed (a UNIX system, for example), there may be a delay introduced because several attempts are made to connect to the IPC$ share. This delay is typically 5-7 seconds, but can be longer based on the speed and latency of the connecting network infrastructure and other conditions.

 

 




