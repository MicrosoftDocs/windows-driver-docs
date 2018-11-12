---
title: ndiskd.nblpool
description: The ndiskd.nblpool extension displays information about a NET_BUFFER_LIST (NBL) pool. If you run this extension with no parameters, ndiskd will display a list of all allocated NBL pools in the system.
ms.assetid: 78F8E45C-D13D-4628-A387-529291B4C50C
keywords: ["ndiskd.nblpool Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.nblpool
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.nblpool


The **!ndiskd.nblpool** extension displays information about a [**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure) (NBL) pool. If you run this extension with no parameters, !ndiskd will display a list of all allocated NBL pools in the system.

```console
!ndiskd.nblpool [-handle <x>] [-basic] [-allocations] [-find <str>] [-findnb <str>] 
    [-findctx <str>] [-findctxtype <str>] [-findva <x>] [-findpa <x>]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NBL pool.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about the NBL pool.

<span id="_______-allocations______"></span><span id="_______-ALLOCATIONS______"></span> *-allocations*   
Displays all allocated NBLs.

<span id="_______-find______"></span><span id="_______-FIND______"></span> *-find*   
Filter the list of allocated NBLs using a debugger expression.

<span id="_______-findnb______"></span><span id="_______-FINDNB______"></span> *-findnb*   
Filter the list of allocated NBLs by linked [**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)s (NBs).

<span id="_______-findctx______"></span><span id="_______-FINDCTX______"></span> *-findctx*   
Filter the list of allocated NBLs by context area.

<span id="_______-findctxtype______"></span><span id="_______-FINDCTXTYPE______"></span> *-findctxtype*   
Override the datatype of the context area.

<span id="_______-findva______"></span><span id="_______-FINDVA______"></span> *-findva*   
Find NBLs that contain an NB that straddles the given virtual address.

<span id="_______-findpa______"></span><span id="_______-FINDPA______"></span> *-findpa*   
Find NBLs that contain an NB that straddles the given physical address.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Enter the **!ndiskd.nblpool** command with no parameters to see a list of all allocated NBL pools. In this example, look for the NBL pool allocated by the kernel debugger network interface card (kdnic) with the KDNr Tag. Its handle is ffffdf80147e4a40.

```console
2: kd> !ndiskd.nblpool
    NBL Pool           Tag                 Allocated by                         
    ffffdf80179b6a40   NiBP                WdNisDrv!CWFPLayer::Initialize+c6
    ffffdf8015ac6a40   EUNP                tunnel!TunnelEtherUdpGlobalInit+81
    ffffdf8015a78040   Nuio                ndisuio!ndisuioCreateBinding+15f
    ffffdf8015a77800   Nuio                ndisuio!ndisuioCreateBinding+13c
    ffffdf8015a63040   BaNB                rspndr!TopStartNetBufferModule+6d
    ffffdf8015a68a40   LLnb                mslldp!lldpProtSetOptions+49
    ffffdf8014654040   BaNB                lltdio!TopStartNetBufferModule+6d
    ffffdf801494ca40   Pcsb                pacer!PcFilterAttach+142
    ffffdf80147e4a40   KDNr                kdnic!NICAllocAdapter+178
    ffffdf80131ce040   bnvW                wfplwfs!DriverEntry+7a0
    ffffdf80139ffa40   Wfdp                wfplwfs!WfpRioInitialize+a4
    ffffdf8012061200   UNbl                NETIO!NetioAllocateNetBufferListNetBufferMdlAndDataPool+49
    ffffdf8013968a40   TcDN                NETIO!NetioAllocateNetBufferListNetBufferMdlAndDataPool+49
    ffffdf8013969a40   TNbl                NETIO!NetioAllocateNetBufferListNetBufferMdlAndDataPool+49
    ffffdf801397c040   StBn                NETIO!StreamPoolsInit+c1
    ffffdf8013088040   Wfra                NETIO!WfpNblInfoLibraryInit+b8
    ffffdf8012067440   Nnnn                NETIO!NetioInitializeNetBufferListLibrary+13e
    ffffdf8012067a40   Nnbl                NETIO!NetioInitializeNetBufferListLibrary+112
    ffffdf80131caa40   NDrt                ndis!ndisInitializePeriodicReceives+22f
    ffffdf80131d5a40   NDnd                ndis!DriverEntry+5e9
```

Click on the NBL pool's handle or enter the **!ndiskd.nblpool -handle** command to examine its details.

```console
2: kd> !ndiskd.nblpool ffffdf80147e4a40


NBL POOL

    Ndis handle        ffffdf80147e4a40
    Allocation tag     KDNr
    Owner
    Allocated by       kdnic!NICAllocAdapter+178

    Flags              CONTAINS_NET_BUFFER
    Structure size     0n544
    Context size       0
    Data size          0

    All allocated NBLs
```

To explore the NBLs contained in this NBL pool, click on the "All allocated NBLs" link at the bottom. Alternatively, you can also enter the **!ndiskd.nblpool -handle -allocations** command. As shown in the following example, this NBL pool contains more than 1024 NBLs so !ndiskd quit early. You can use the -force option to work around this limit and see all of the NBLs in this NBL pool.

```console
2: kd> !ndiskd.nblpool ffffdf80147e4a40 -allocations


ALL ALLOCATED NBLs

    NBL                Active?                                                  
    ffffdf8014951940   Allocated
    ffffdf8014951b90   Allocated
    ffffdf8014951de0   Allocated
    ffffdf8014951030   Allocated
    ffffdf80149524a0   Allocated
    ffffdf80149526f0   Allocated
    ffffdf8014952940   Allocated
    ffffdf8014952b90   Allocated
    ffffdf8014952de0   Allocated
    ffffdf8014952030   Allocated
    ffffdf80149534a0   Allocated
    ffffdf80149536f0   Allocated
    ffffdf8014953940   Allocated
    ffffdf8014953b90   Allocated
    ffffdf8014953de0   Allocated
    ffffdf8014953030   Allocated
    ffffdf80149544a0   Allocated
    ffffdf80149546f0   Allocated
    ffffdf8014954940   Allocated

...

    ffffdf80148b0b90   Allocated
    ffffdf80148b0de0   Allocated
    ffffdf80148b0030   Allocated
    ffffdf80148b14a0   Allocated
    ffffdf80148b16f0   Allocated
    ffffdf80148b1940   Allocated
    ffffdf80148b1b90   Allocated
    ffffdf80148b1de0   Allocated
    ffffdf80148b1030   Allocated
    [Maximum of 1024 items read; quitting early. Rerun with the '-force' option
    to bypass this limit.]
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)

[**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)

 

 






