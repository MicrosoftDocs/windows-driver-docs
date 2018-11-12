---
title: ndiskd.af
description: The ndiskd.af extension displays a Connection-Oriented NDIS (CoNDIS) address family (AF).
ms.assetid: 737AB46E-DFAA-42D6-A9BD-B7223167D0DD
keywords: ["ndiskd.af Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.af
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.af


The **!ndiskd.af** extension displays a Connection-Oriented NDIS (CoNDIS) address family (AF).

```console
!ndiskd.af [-handle <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of a CoNDIS address family.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Remarks
-------

For more information about CoNDIS, see [Connection-Oriented NDIS](https://msdn.microsoft.com/windows/hardware/drivers/network/connection-oriented-ndis).

For more information about CoNDIS address families, see [Address Families](https://msdn.microsoft.com/windows/hardware/drivers/network/address-families).

Examples
--------

CoNDIS is used in certain situations such as connecting to a VPN, so running **!ndiskd.af** will not show you results unless a miniport driver on your system has created and activated a CoNDIS virtual connection. The following example shows results from a machine that is connected to a VPN network. First, run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension with no parameters to see a list of miniports and miniport drivers on the system. In the following output, look for the miniport driver for the Marvell AVASTAR Wireless-AC Network Controller network adapter. Its handle is ffffc804af2e3710.

```console
1: kd> !ndiskd.netadapter
    Driver             NetAdapter          Name                                 
    ffffc804af2e3710   ffffc804b9e6f1a0    Marvell AVASTAR Wireless-AC Network Controller
    ffffc804b99b9020   ffffc804b9c301a0    WAN Miniport (Network Monitor)
    ffffc804b99b9020   ffffc804b9c2a1a0    WAN Miniport (IPv6)
    ffffc804b99b9020   ffffc804b8a8a1a0    WAN Miniport (IP)
    ffffc804ae9d7020   ffffc804b9ceb1a0    WAN Miniport (PPPOE)
    ffffc804b9ca5900   ffffc804b9e601a0    WAN Miniport (PPTP)
    ffffc804b99dc720   ffffc804b99b01a0    WAN Miniport (L2TP)
    ffffc804b86581b0   ffffc804b9c6c1a0    WAN Miniport (IKEv2)
    ffffc804ad4a7250   ffffc804b99651a0    WAN Miniport (SSTP)
    ffffc804b11c4020   ffffc804b85821a0    Microsoft ISATAP Adapter
    ffffc804b11c4020   ffffc804b71731a0    Microsoft ISATAP Adapter #2
    ffffc804ad725020   ffffc804b05e71a0    Surface Ethernet Adapter #2
    ffffc804b0bf0020   ffffc804b0c011a0    Bluetooth Device (Personal Area Network)
    ffffc804aef695e0   ffffc804aed331a0    TAP-Windows Adapter V9
```

Next, enter the **!ndiskd.af** command with the miniport driver's handle to see the address family for this miniport driver, which is acting as a connection-oriented client.

```console
1: kd> !ndiskd.af ffffc804af2e3710


ADDRESS FAMILY

    Ndis handle        ffffc804af2e3710
    Flags              [Unrecognized flags 399b9020] AF_CLOSING
    References         ffffc804
    Close Requested?   0

    Miniport           0 - [Unreadable NetAdapter]

    Call Manager       ffffc804b90a4ac0 - [Invalid Open]
    Call Manager Context 007a0078

    Client             00060000 - [Unreadable Open]
    Client Context     ffffc804af2e3888


CLIENT HANDLERS

    Client Handler                         Function pointer   Symbol (if available)
    ClCreateVcHandler                      fffff80965fd5888   mrvlpcie8897!Globals+8
    ClDeleteVcHandler                      [None]
    ClRequestHandler                       ffffc804af96fd78
    ClRequestCompleteHandler               ffffc804af96fd78
    ClOpenAfCompleteHandler                [None]
    ClCloseAfCompleteHandler               [None]
    ClRegisterSapCompleteHandler           000132060098028a
    ClDeregisterSapCompleteHandler         [None]
    ClMakeCallCompleteHandler              fffff80965ff9ec0   wdiwifi!MPWrapperSetOptions
    ClCloseCallCompleteHandler             fffff80965ff9c70   wdiwifi!MPWrapperHalt
    ClModifyCallQoSCompleteHandler         fffff80965ff9b50   wdiwifi!MPWrapperInitializeEx
    ClAddPartyCompleteHandler              fffff80965e71a08   mrvlpcie8897!MPUnload
    ClDropPartyCompleteHandler             fffff80965ffa070   wdiwifi!MPWrapperPause
    ClIncomingDropPartyHandler             fffff80965ffaa20   wdiwifi!MPWrapperReturnNetBufferLists
    ClIncomingCallHandler                  fffff80965ffa1e0   wdiwifi!MPWrapperRestart
    ClCallConnectedHandler                 fffff80965ffaad0   wdiwifi!MPWrapperCancelSendNetBufferLists
    ClIncomingCloseCallHandler             fffff80965ffa870   wdiwifi!MPWrapperSendNetBufferLists
    ClIncomingCallQoSChangeHandler         fffff80965ffa610   wdiwifi!MPWrapperOidRequest
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Connection-Oriented NDIS](https://msdn.microsoft.com/windows/hardware/drivers/network/connection-oriented-ndis)

[Address Families](https://msdn.microsoft.com/windows/hardware/drivers/network/address-families)

 

 






