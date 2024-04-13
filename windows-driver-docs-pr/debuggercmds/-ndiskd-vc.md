---
title: "!ndiskd.vc (WinDbg)"
description: "The !ndiskd.vc extension displays a Connection-Oriented (CoNDIS) virtual connection (VC)."
keywords: ["!ndiskd.vc Windows Debugging"]
ms.date: 06/26/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.vc
api_type:
- NA
---

# !ndiskd.vc

The **!ndiskd.vc** extension displays a Connection-Oriented (CoNDIS) virtual connection (VC).

```console
!ndiskd.vc -handle <x>
```

## Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Required. Handle of a VC pointer.

### DLL

Ndiskd.dll

### Remarks

For more information about CoNDIS, see [Connection-Oriented NDIS](../network/connection-oriented-ndis.md).

For more information about CoNDIS virtual connections, see [Virtual Connections](../network/virtual-connections.md).

### Examples

CoNDIS is used in certain situations such as connecting to a VPN, so running **!ndiskd.vc** will not show you results unless a miniport driver on your system has created and activated a CoNDIS virtual connection. The following example shows results from a machine that is connected to a VPN network. First, run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension with no parameters to see a list of miniports and miniport drivers on the system. In the following output, look for the miniport driver for the Marvell AVASTAR Wireless-AC Network Controller network adapter. Its handle is ffffc804af2e3710.

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

Next, enter the **!ndiskd.vc** command with the miniport driver's handle to see the virtual connections opened by that miniport driver.

```console
1: kd> !ndiskd.vc ffffc804af2e3710


VIRTUAL CALL

    [Zero-length string]
    Ndis handle        ffffc804af2e3710
    VC Index           0

    AF                 fffff80965fd5888
    Call Flags         [No flags set]
    VC Flags           [Unrecognized flags 04a80100] VC_ACTIVATE_PENDING

    Miniport           fffff80965ffaa20 - [Invalid NetAdapter]
    Miniport Context   fffff80965ffaad0

    Call Manager       fffff80965ff9b50 - [Invalid Open]
    Call Manager Context fffff80965ff9c70

    Client             ffffc804af96fd78 - [Invalid Open]
    Client Context     00003206
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[Connection-Oriented NDIS](../network/connection-oriented-ndis.md)

[Virtual Connections](../network/virtual-connections.md)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

