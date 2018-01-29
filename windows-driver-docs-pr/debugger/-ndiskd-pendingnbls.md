---
title: ndiskd.pendingnbls
description: The ndiskd.pendingnbls extension displays pending NBLs (NET_BUFFER_LISTs) that are in transit.
ms.assetid: 9137B995-FCCA-4E25-85D3-FCB5B717EBDF
keywords: ["ndiskd.pendingnbls Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.pendingnbls
api_type:
- NA
---

# !ndiskd.pendingnbls


The **!ndiskd.pendingnbls** extension displays pending NBLs ([**NET\_BUFFER\_LISTs**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)) that are in transit.

```
!ndiskd.pendingnbls [-handle <x>] [-fullstack] [-verbosity <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS miniport, filter, or open.

<span id="_______-fullstack______"></span><span id="_______-FULLSTACK______"></span> *-fullstack*   
Shows pending NBLs from the entire stack associated with the handle.

<span id="_______-verbosity______"></span><span id="_______-VERBOSITY______"></span> *-verbosity*   
Level of detail to display.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

**!ndiskd.pendingnbls** can be passed the handle of an NDIS miniport, filter, or open. The following series of examples use a miniport handle. To see a list of all miniports and their associated minidrivers, run the [**!ndiskd.netadapter**](-ndiskd-netadapter.md) extension with no parameters. In the following example output, look for the Microsoft Kernel Debug Network Adapter, whose handle is ffffe00bc3f701a0. Its minidriver's handle is ffffe00bc51b9ae0.

```
0: kd> !ndiskd.netadapter
    Driver             NetAdapter          Name                                 
    ffffe00bc6e12ae0   ffffe00bc6e4e1a0    Microsoft ISATAP Adapter #2
    ffffe00bc51b9ae0   ffffe00bc3f701a0    Microsoft Kernel Debug Network Adapter
```

To see the pending NBLs for a miniport, set a breakpoint on its minidriver's SendNetBufferListsHandler. Use the minidriver's handle to run the [**!ndiskd.minidriver -handle -handlers**](-ndiskd-minidriver.md) command to see a list of its handlers, then click the "bp" link to the right of the SendNetBufferListsHandler. You can alternatively enter the [**bp -handle**](bp--bu--bm--set-breakpoint-.md) command in the command line.

```
0: kd> !ndiskd.minidriver ffffe00bc51b9ae0 -handlers


HANDLERS

    NDIS Handler                           Function pointer   Symbol (if available)
    InitializeHandlerEx                    fffff80ae9618230  bp
    SetOptionsHandler                      fffff80ae9612800  bp
    HaltHandlerEx                          fffff80ae9618040  bp
    ShutdownHandlerEx                      fffff80ae96122c0  bp

    CheckForHangHandlerEx                  fffff80ae9612810  bp
    ResetHandlerEx                         fffff80ae9612f70  bp

    PauseHandler                           fffff80ae9618000  bp
    RestartHandler                         fffff80ae9618940  bp

    OidRequestHandler                      fffff80ae9611c90  bp
    CancelOidRequestHandler                fffff80ae96122c0  bp
    DirectOidRequestHandler                [None]
    CancelDirectOidRequestHandler          [None]
    DevicePnPEventNotifyHandler            fffff80ae96189a0  bp

    SendNetBufferListsHandler              fffff80ae9611870  bp
    ReturnNetBufferListsHandler            fffff80ae9611b50  bp
    CancelSendHandler                      fffff80ae96122c0  bp
```

After setting the breakpoint on the SendNetBufferListsHandler, enter the **g** command to let the debugee target machine run and hit the breakpoint.

```
0: kd> bp fffff80ae9611870
0: kd> g
Breakpoint 0 hit
fffff80a`e9611870 4053            push    rbx
```

Now, after hitting the minidriver's SendNetBufferListsHandler breakpoint, you can see any pending NBLs for the miniport by entering the **!ndiskd.pendingnbls -handle** command with the miniport's handle.

**Note**  
The debugee target machine in this example was loading a web page when it hit the breakpoint, so traffic was flowing through the miniport's datapath. Therefore, it had a pending NBL to send. Even after setting a breakpoint on one or more of the NBL handlers for the minidriver, you may not see any pending NBLs if there were no activity in the datapath.

 

```
0: kd> !ndiskd.pendingnbls ffffe00bc3f701a0

PHASE 1/3: Found 20 NBL pool(s).                 
PHASE 2/3: Found 342 freed NBL(s).                                    

    Pending Nbl        Currently held by                                        
    ffffe00bc5545c60   ffffe00bc3f701a0 - Microsoft Kernel Debug Network Adapter  [NetAdapter]                    
    

PHASE 3/3: Found 1 pending NBL(s) of 4817 total NBL(s).                      
Search complete.
```

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)

[**!ndiskd.netadapter**](-ndiskd-netadapter.md)

[**!ndiskd.minidriver**](-ndiskd-minidriver.md)

[**bp, bu, bm (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.pendingnbls%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





