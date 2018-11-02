---
title: ndiskd.wdiminidriver
description: The ndiskd.wdiminidriver extension displays information about one or more CMiniportDriver structures. 
ms.assetid: C7022CD7-6F3A-485B-8686-A686A5305DA5
keywords: ["ndiskd.wdiminidriver Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- ndiskd.wdiminidriver
api_type:
- NA
ms.localizationpriority: medium
---

# !ndiskd.wdiminidriver


The **!ndiskd.wdiminidriver** extension displays information about one or more CMiniportDriver structures. If you run this extension with no parameters, !ndiskd will display a list of all CMiniportDriver structures.

For more information about WDI miniport drivers, see the [WDI Miniport Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-miniport-driver-design-guide).

For more information about WDI miniport driver reference, see [WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075).

```console
!ndiskd.wdiminidriver [-handle <x>] [-pm] [-rcvfilter] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of a CMiniportDriver object.

<span id="_______-basic______"></span><span id="_______-BASIC______"></span> *-basic*   
Displays basic information about the miniport driver.

<span id="_______-handlers______"></span><span id="_______-HANDLERS______"></span> *-handlers*   
Displays this driver's miniport handlers.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

Run the **!ndiskd.wdiminidriver** extension with no parameters to see a list of all CMiniportDriver objects. In the following example, there is only one CMiniportDriver object. The handle of its WdiMiniDriver is ffffc804b8ce7c40.

```console
1: kd> !ndiskd.wdiminidriver
    WdiMiniDriver      Name                                                     
    ffffc804b8ce7c40 - WDI MiniDriver
```

Click on the WdiMiniDriver's handle or enter the **!ndiskd.wdiminidriver -handle** command to see details for this WDI miniport driver.

```console
1: kd> !ndiskd.wdiminidriver ffffc804b8ce7c40


WDI MINIPORT DRIVER

    Object             ffffc804b8ce7c40
    DRIVER_OBJECT      ffffc804b90a4ac0

    Ndis API version   v6.50
    NDIS driver        ffffc804af2e3710 - mrvlpcie8897
    Driver version     v1.0
    WDI API version    v1.0.1


    Handlers
```

Now you can click the "Handlers" link at the bottom of the WDI Miniport Driver's details, or you can use the handle to enter the **!ndiskd.wdiminidriver -handle -handlers** command, to see a list of all this WDI Miniport Driver's handlers.

```console
1: kd> !ndiskd.wdiminidriver ffffc804b8ce7c40 -handlers


HANDLERS

    Miniport Handler                       Function pointer   Symbol (if available)
    InitializeHandlerEx                    [None]
    SetOptionsHandler                      fffff80965e8cae0   mrvlpcie8897!wlan_cmd_queue_deinit
    UnloadHandler                          fffff80965e71a08   mrvlpcie8897!MPUnload
    HaltHandlerEx                          [None]
    ShutdownHandlerEx                      fffff80965e71974   mrvlpcie8897!MPShutdown

    CheckForHangHandlerEx                  [None]
    ResetHandlerEx                         [None]

    PauseHandler                           [None]
    RestartHandler                         [None]

    OidRequestHandler                      [None]
    SendNetBufferListsHandler              [None]
    ReturnNetBufferListsHandler            [None]
    CancelSendHandler                      [None]
    CancelOidRequestHandler                [None]
    DirectOidRequestHandler                [None]
    CancelDirectOidRequestHandler          [None]
    DevicePnPEventNotifyHandler            fffff80965e71868   mrvlpcie8897!MPPnPEventNotify

    AllocateAdapterHandler                 fffff80965e713ec   mrvlpcie8897!MPAllocateTalAdapter
    FreeAdapterHandler                     fffff80965e717e8   mrvlpcie8897!MPFreeTalAdapter
    OpenAdapterHandler                     fffff80965e719b8   mrvlpcie8897!MPTaskOpenHandler
    CloseAdapterHandler                    fffff80965e719ac   mrvlpcie8897!MPTaskCloseHandler
    StartOperationHandler                  [None]
    StopOperationHandler                   [None]
    PostPauseHandler                       [None]
    PostRestartHandler                     [None]
    HangDiagnoseHandler                    fffff80965e715d8   mrvlpcie8897!MPDiagnosticHandler
    TalTxRxInitializeHandler               fffff80965e752d4   mrvlpcie8897!TalDataPathInitialize
    TalTxRxDeinitializeHandler             fffff80965e7527c   mrvlpcie8897!TalDataPathDeinitialize

    OpenAdapterCompleteHandler             fffff80965ffab50   wdiwifi!WDIOpenAdapterCompleteHandler
    CloseAdapterCompleteHandler            fffff80965fface0   wdiwifi!WDICloseAdapterCompleteHandler
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[WDI Miniport Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/wdi-miniport-driver-design-guide)

[WDI Miniport Driver Reference](https://msdn.microsoft.com/library/windows/hardware/dn926075)

 

 






