---
title: "!ndiskd.mopen"
description: "The !ndiskd.mopen extension displays information about bindings between miniports and protocols. "
keywords: ["!ndiskd.mopen Windows Debugging"]
ms.date: 06/15/2020
topic_type:
- apiref
ms.topic: reference
api_name:
- ndiskd.mopen
api_type:
- NA
---

# !ndiskd.mopen

The **!ndiskd.mopen** extension displays information about bindings between miniports and protocols. If you run this extension with no parameters, !ndiskd will display a list of all open bindings between NDIS miniport drivers and protocol drivers.

```console
!ndiskd.mopen [-handle <x>] [-ref] 
```

## <span id="ddk__ndiskd_mopen_dbg"></span><span id="DDK__NDISKD_MOPEN_DBG"></span>Parameters

<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Optional handle of an NDIS open binding.

<span id="_______-ref______"></span><span id="_______-REF______"></span> *-ref*   
Shows refcounts of open bindings.

### DLL

Ndiskd.dll

### Examples

Enter the !ndiskd.mopen command to get a list of all open bindings. In this example, look for the binding between the Microsoft ISATAP Adapter \#2 miniport and the TCPIP6TUNNEL protocol. Its handle is ffff8083e56b8110.

```console
3: kd> !ndiskd.mopen
Open ffff8083e56b8110
  Miniport: ffff8083e02ce1a0 - Microsoft ISATAP Adapter #2
  Protocol: ffff8083e1a95c00 - TCPIP6TUNNEL

Open ffff8083e11902c0
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e3e8f6b0 - RSPNDR

Open ffff8083e55f3010
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e0114730 - NDISUIO

Open ffff8083e15537d0
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e3e90800 - LLTDIO

Open ffff8083e3926010
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e3e90c10 - MSLLDP

Open ffff8083e0c565a0
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e11cec10 - TCPIP

Open ffff8083e504c770
  Miniport: ffff8083e0f501a0 - Microsoft Kernel Debug Network Adapter
  Protocol: ffff8083e19bfc10 - TCPIP6
```

Now you can either click on the handle or use the handle to enter the **!ndiskd.mopen -handle** command, which enables you to see more details about that open binding such as its Datapath state and Receive path information.

```console
3: kd> !ndiskd.mopen ffff8083e56b8110


OPEN

    Ndis handle        ffff8083e56b8110
    Flags              [No flags set]
    References         1                   Show detail
    Source             1
    Datapath state     Running

    Protocol           ffff8083e1a95c00 - TCPIP6TUNNEL
    Protocol context   ffff8083e15b62e0

    Miniport           ffff8083e02ce1a0 - Microsoft ISATAP Adapter #2
    Miniport context   ffff8083e0772010


RECEIVE PATH

    Packet filter      [No flags set]
    Frame Type(s)      0x86dd
```

## See also

[Network Driver Design Guide](../network/index.md)

[Windows Vista and Later Networking Reference](/windows-hardware/drivers/ddi/_netvista/)

[Debugging the Network Stack](/shows/defrag-tools/175-debugging-network-stack)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

