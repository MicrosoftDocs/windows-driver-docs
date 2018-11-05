---
title: ndiskd.nbpool
description: The ndiskd.nbpool extension displays information about a NET_BUFFER (NB) pool. 
ms.assetid: 4FCD48B7-C469-4057-A279-20522B00E80B
keywords: ["ndiskd.nbpool Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.nbpool
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.nbpool


The **!ndiskd.nbpool** extension displays information about a [**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure) (NB) pool. If you run this extension with no parameters, !ndiskd will display a list of all allocated NB pools in the system.

```console
!ndiskd.nbpool [-handle <x>] [-allocations] [-find <str>] [-findva <x>] [-findpa <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NB pool.

<span id="_______-allocations______"></span><span id="_______-ALLOCATIONS______"></span> *-allocations*   
Displays all allocated NBs.

<span id="_______-find______"></span><span id="_______-FIND______"></span> *-find*   
Filter the list of allocated NBs using a debugger expression.

<span id="_______-findva______"></span><span id="_______-FINDVA______"></span> *-findva*   
Find NBs that straddle the given virtual address.

<span id="_______-findpa______"></span><span id="_______-FINDPA______"></span> *-findpa*   
Find NBs that straddle the given physical address.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Enter the **!ndiskd.nbpool** command with no parameters to see a list of all allocated NB pools. In this example, look for the NB pool allocated by the Netio service with the Nnbf Tag. Its handle is ffffdf801308ca40.

```console
2: kd> !ndiskd.nbpool
    NB Pool            Tag                 Allocated by                         
    ffffdf8013963a40   UDNb                NETIO!NetioAllocateNetBufferMdlAndDataPool+3c
    ffffdf801396aa40   TSNb                NETIO!NetioAllocateNetBufferMdlAndDataPool+3c
    ffffdf801397d4c0   StBn                NETIO!StreamPoolsInit+90
    ffffdf801308ca40   Nnbf                NETIO!NetioInitializeNetBufferListLibrary+dd
    ffffdf80131cba40   NDnd                ndis!DriverEntry+615
```

Click on the NB pool's handle or enter the **!ndiskd.nbpool -handle** command to examine its details.

```console
2: kd> !ndiskd.nbpool ffffdf801308ca40


NB POOL

    Ndis handle        ffffdf801308ca40
    Allocation tag     Nnbf
    Owner
    Allocated by       NETIO!NetioInitializeNetBufferListLibrary+dd

    Flags              [No flags set]
    Structure size     0n176
    Data size          0

    All allocated NBs
```

To explore the NBs contained in this NB pool, click on the "All allocated NBs" link at the bottom. Alternatively, you can also enter the **!ndiskd.nbpool -handle -allocations** command. As shown in the following example, this NB pool contains more than 1024 NBs so !ndiskd quit early. You can use the -force option to work around this limit and see all of the NBs in this NB pool.

```console
2: kd> !ndiskd.nbpool ffffdf801308ca40 -allocations


ALL ALLOCATED NBs

    NB                 Active?                                                  
    ffffdf8016ea4360   Allocated
    ffffdf801744df50   Allocated
    ffffdf8016932860   Allocated
    ffffdf8016e31500   Allocated
    ffffdf80174eade0   Allocated
    ffffdf8017daa900   Allocated
    ffffdf8017c8c680   Allocated
    ffffdf80166b23b0   Allocated
    ffffdf80164fea70   Allocated
    ffffdf8012845990   Allocated
    ffffdf8017d692d0   Allocated
    ffffdf8017cdc090   Allocated
    ffffdf8012771780   Allocated
    ffffdf80158a3550   Allocated
    ffffdf8012eef5c0   Allocated
    ffffdf80127719d0   Allocated
    ffffdf8015119570   Allocated
    ffffdf8012e18d40   Allocated
    ffffdf8017929b10   Allocated
    ffffdf8016d4e430   Allocated

...

    ffffdf8015ffbbd0   Allocated
    ffffdf8015ec1b10   Freed
    ffffdf80158e56d0   Allocated
    ffffdf8016272110   Freed
    ffffdf8015d8e030   Freed
    ffffdf8015d8e770   Freed
    ffffdf80158ddc30   Freed
    ffffdf801584acc0   Freed
    ffffdf8015846b40   Freed
    ffffdf8015a06c50   Freed
    ffffdf801480c300   Freed
    ffffdf8015e48f50   Freed
    ffffdf8015de64e0   Freed
    ffffdf8015ddff50   Freed
    [Maximum of 1024 items read; quitting early. Rerun with the '-force' option
    to bypass this limit.]
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-structure)

 

 






