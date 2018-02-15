---
title: ndiskd.oid
description: The ndiskd.oid extension displays information about an NDIS OID request.
ms.assetid: FCDE2F78-98C0-4437-999A-4566FEB5D7BB
keywords: ["ndiskd.oid Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.oid
api_type:
- NA
---

# !ndiskd.oid


The **!ndiskd.oid** extension displays information about an NDIS OID request. If you run this extension with no parameters, !ndiskd will display a list of all pending OID requests on all miniports and filters. Each miniport or filter has at most one pending OID request and any number of queued OID requests.

Note that filters typically clone OID requests and pass the clone down. This means that even if a protocol issues a single OID request, there may be multiple instances of cloned requests: one in each filter and another in the miniport. **!ndiskd.oid** will show each clone separately, so you may see more pending OIDs than the protocol has actually issued.

```
!ndiskd.oid [-handle <x>] [-legacyoid] [-nolimit>] [-miniport <x>] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-handle______"></span><span id="_______-HANDLE______"></span> *-handle*   
Handle of an NDIS\_OID\_REQUEST

<span id="_______-legacyoid______"></span><span id="_______-LEGACYOID______"></span> *-legacyoid*   
Treats as a legacy NDIS\_REQUEST instead of an NDIS\_OID\_REQUEST.

<span id="_______-nolimit______"></span><span id="_______-NOLIMIT______"></span> *-nolimit*   
Does not limit the number of pending OIDs that are displayed.

<span id="_______-miniport______"></span><span id="_______-MINIPORT______"></span> *-miniport*   
Finds pending OID requests on this miniport's stack.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Remarks
-------

**!ndiskd.oid** shows you a list of all the pending OIDs on the system at a time, so it can be very helpful in debugging system hangs or [0x9F bug check](https://msdn.microsoft.com/library/windows/hardware/ff559329) situations (DRIVER\_POWER\_STATE\_FAILURE). For example, suppose analyzing a fictitious 0x9F bug check revealed that the system was hung on an IRP and was waiting for NDIS. In NDIS, IRPs from the OS are translated into OIDs, including power transitions, so by running **!ndiskd.oid** you could see that, in this example, a device at the bottom of the stack might have been clinging to an [OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780) and hung the rest of the stack. NDIS drivers should not pend an OID for more than one second, so you could then investigate why that device kept the OID pending for too long to try to solve the issue.

Examples
--------

To see an example of pending OIDS on a system that is running normally, set a breakpoint on a miniport's OID request handler routine (in the miniport's corresponding miniport driver). First, run the [**!ndiskd.minidriver**](-ndiskd-minidriver.md) command with no parameters to get a list of miniport drivers on the system. In this example output, look for the handle for the kdnic minidriver, ffffdf801418d650..

```
3: kd> !ndiskd.minidriver
    ffffdf8015a98380 - tunnel
    ffffdf801418d650 - kdnic
```

Click on the handle for the minidriver, then click on the "Handlers" link at the bottom of its details page to see the list of its handlers. You can alternatively enter the **!ndiskd.minidriver -handle -handlers** command. Once you have the list of the minidriver's handlers, look for the OidRequestHandler, whose handle is fffff80f1fd71c90 in this example.

```
2: kd> !ndiskd.minidriver ffffdf801418d650 -handlers


HANDLERS

    NDIS Handler                           Function pointer   Symbol (if available)
    InitializeHandlerEx                    fffff80f1fd78230  bp
    SetOptionsHandler                      fffff80f1fd72800  bp
    HaltHandlerEx                          fffff80f1fd78040  bp
    ShutdownHandlerEx                      fffff80f1fd722c0  bp

    CheckForHangHandlerEx                  fffff80f1fd72810  bp
    ResetHandlerEx                         fffff80f1fd72f70  bp

    PauseHandler                           fffff80f1fd78000  bp
    RestartHandler                         fffff80f1fd78940  bp

    OidRequestHandler                      fffff80f1fd71c90  bp
    CancelOidRequestHandler                fffff80f1fd722c0  bp
    DirectOidRequestHandler                [None]
    CancelDirectOidRequestHandler          [None]
    DevicePnPEventNotifyHandler            fffff80f1fd789a0  bp

    SendNetBufferListsHandler              fffff80f1fd71870  bp
    ReturnNetBufferListsHandler            fffff80f1fd71b50  bp
    CancelSendHandler                      fffff80f1fd722c0  bp
```

Now either click on the "bp" link to the right of the OidRequestHandler or enter the [**bp -handle**](bp--bu--bm--set-breakpoint-.md) command with its handle to set a breakpoint on that routine. Next, type the **g** command to allow your debugee target machine to run and hit the breakpoint you just set.

```
2: kd> bp fffff80f1fd71c90
2: kd> g
Breakpoint 1 hit
fffff80f`1fd71c90 448b4204        mov     r8d,dword ptr [rdx+4]
```

Once you have triggered the breakpoint on a minidriver's OID request handler routine as shown by the previous example, you can run the !ndiskd.oid command to see a list of all the pending OIDs on the system.

```
1: kd> !ndiskd.oid


ALL PENDING OIDs

    NetAdapter         ffffdf80140c71a0 - Microsoft Kernel Debug Network Adapter
        Current OID        OID_GEN_STATISTICS
    Filter             ffffdf8014950c70 - Microsoft Kernel Debug Network Adapter-WFP Native MAC Layer LightWeight Filter-0000
        Current OID        OID_GEN_STATISTICS
    Filter             ffffdf801494dc70 - Microsoft Kernel Debug Network Adapter-QoS Packet Scheduler-0000
        Current OID        OID_GEN_STATISTICS
```

In this example, the OID pending is [OID\_GEN\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569640). When you look at the results of !ndiskd.oid, recall that filters clone OID requests and pass them down the stack, and OIDs typically get passed from filter to filter to miniport. Therefore, although it may look like there are three separate OID requests with the same name in this example, there is actually one logical operation taking place which was physically spread across 3 OIDs and on 3 drivers.

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[0x9F bug check](https://msdn.microsoft.com/library/windows/hardware/ff559329)

[OID\_PNP\_SET\_POWER](https://msdn.microsoft.com/library/windows/hardware/ff569780)

[**bp, bu, bm (Set Breakpoint)**](bp--bu--bm--set-breakpoint-.md)

[OID\_GEN\_STATISTICS](https://msdn.microsoft.com/library/windows/hardware/ff569640)

[NDIS OIDs](https://msdn.microsoft.com/library/windows/hardware/ff566707)

[NDIS OID Request Interface](https://msdn.microsoft.com/library/windows/hardware/ff566713)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.oid%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





