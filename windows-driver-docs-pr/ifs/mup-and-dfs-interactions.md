---
title: MUP and DFS Interactions
author: windows-driver-content
description: MUP and DFS Interactions
ms.assetid: 39c1f1e3-fb2d-46e7-b3dc-3d4bfab9608c
keywords: ["DFS WDK network redirectors", "Distributed File System WDK network redirectors", "kernel network redirectors WDK , MUP", "MUP WDK network redirectors", "multiple UNC provider WDK network redirectors", "UNC WDK network redirectors"]
---

# MUP and DFS Interactions


When a Universal Naming Convention (UNC) path is used by an application, a request is sent to the multiple UNC provider (MUP) to determine which network provider to use. MUP channels the request to the appropriate network redirector (the UNC provider) that is capable of handling the remote file system request. If the Distributed File System (DFS) client is enabled, MUP first passes the request for a particular "\\\\server\\share" to the DFS client to determine if the request is for a DFS share rather than a normal remote file share.

The default behavior is that the DFS client is enabled. The DFS client is disabled depending on the value of a registry entry located below the following:

```
HKLM\System\CurrentControlSet\Services\Mup
```

When the DisableDfs registry entry has a DWORD value of 1, the DFS client is disabled.

Assuming the prefix of a path specified in a name-based operation is not in the prefix cache maintained by MUP, the DFS client (when enabled) implicitly takes precedence over all redirectors. The DFS client attempts to determine whether a UNC path specified is a DFS path. It does this by sending a referral request to the IPC$ share of an appropriate server. If the path is determined to be a DFS path, the DFS client handles the operation. Otherwise, the DFS client passes the name-based request to MUP for prefix resolution to be handled by an appropriate redirector.

When a request to access the IPC$ share is sent to a system where the LAN Manager Server (sometimes called SMB Server), srv.sys, is disabled or not installed (a UNIX system, for example), there may be a delay introduced because several attempts are made to connect to the IPC$ share. This delay is typically 5-7 seconds, but can be longer based on the speed and latency of the connecting network infrastructure and other conditions.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20MUP%20and%20DFS%20Interactions%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


