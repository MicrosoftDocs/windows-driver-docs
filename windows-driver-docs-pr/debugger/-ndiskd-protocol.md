---
title: ndiskd.protocol
description: The ndiskd.protocol command displays information about an NDIS protocol driver. 
keywords: ["ndiskd.protocol Windows Debugging"]
ms.date: 06/26/2020
topic_type:
- apiref
api_name:
- ndiskd.protocol
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.protocol

The **!ndiskd.protocol** command displays information about an NDIS protocol driver. If you run this extension with no parameters, !ndiskd will display a list of NDIS protocol drivers that are active on the system.

```console
!ndiskd.protocol [-handle <x>] [-findname <any>] 
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of an NDIS protocol.

<span id="_______-findname______"></span><span id="_______-FINDNAME______"></span> *-findname*   
Filters protocols by name prefix.

## DLL

Ndiskd.dll

### Examples

Enter the **!ndiskd.protocol** command to see a list of all NDIS protocols, their handles, and open bindings to miniports (if any). In the following example, look for the TCPIP6TUNNEL protocol's handle, ffff8083e1a95c00.

```console
3: kd> !ndiskd.protocol
ffff8083e0114730 - NDISUIO
  ffff8083e55f3010 - Microsoft Kernel Debug Network Adapter

ffff8083e3e90c10 - MSLLDP
  ffff8083e3926010 - Microsoft Kernel Debug Network Adapter

ffff8083e3e98c10 - WANARPV6

ffff8083e3e97010 - WANARP

ffff8083e3e8f6b0 - RSPNDR
  ffff8083e11902c0 - Microsoft Kernel Debug Network Adapter

ffff8083e3e90800 - LLTDIO
  ffff8083e15537d0 - Microsoft Kernel Debug Network Adapter

ffff8083e1a9ac10 - RDMANDK

ffff8083e1a95c00 - TCPIP6TUNNEL
  ffff8083e56b8110 - Microsoft ISATAP Adapter #2

ffff8083e19bec10 - TCPIPTUNNEL

ffff8083e19bfc10 - TCPIP6
  ffff8083e504c770 - Microsoft Kernel Debug Network Adapter

ffff8083e11cec10 - TCPIP
  ffff8083e0c565a0 - Microsoft Kernel Debug Network Adapter
```

With the protocol's handle, now you can enter either click the handle or enter the **!ndiskd.protocol -handle** command to see information for that protocol, such as the handles for the miniports that are bound to it.

```console
3: kd> !ndiskd.protocol ffff8083e1a95c00


PROTOCOL

    TCPIP6TUNNEL

    Ndis handle        ffff8083e1a95c00
    Ndis API version   v6.40
    Driver context     fffff80e2e4f9de0
    Driver version     v0.0
    Reference count    2
    Flags              [No flags set]
    Driver image       [Not available]     Why not?


BINDINGS

    Open               Miniport            Miniport Name                        
    ffff8083e56b8110   ffff8083e02ce1a0    Microsoft ISATAP Adapter #2


HANDLERS

    Protocol handler                       Function pointer   Symbol (if available)
    BindAdapterHandlerEx                   fffff80e2e3baab0  bp
    UnbindAdapterHandlerEx                 fffff80e2e3c1c80  bp
    OpenAdapterCompleteHandlerEx           fffff80e2e4bc940  bp
    CloseAdapterCompleteHandlerEx          fffff80e2e3d19b0  bp
    NetPnPEventHandler                     fffff80e2e3bb140  bp
    UninstallHandler                       [None]
    SendNetBufferListsCompleteHandler      fffff80e2e3919a0  bp
    ReceiveNetBufferListsHandler           fffff80e2e3918a0  bp
    StatusHandlerEx                        fffff80e2e3a9550  bp
    OidRequestCompleteHandler              fffff80e2e398120  bp
    DirectOidRequestCompleteHandler        fffff80e2e398120  bp
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](https://channel9.msdn.com/Shows/Defrag-Tools/Defrag-Tools-175-Debugging-the-Network-Stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)
