---
title: ndiskd.nbllog
description: The ndiskd.nbllog extension displays the log of all NBL (NET\_BUFFER\_LIST) activity on the system.
ms.assetid: 59CB6B60-E0B3-435E-A6F6-82A715E87C69
keywords: ["ndiskd.nbllog Windows Debugging"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- ndiskd.nbllog
api_type:
- NA
---

# !ndiskd.nbllog


The **!ndiskd.nbllog** extension displays the log of all NBL ([**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)) activity on the system.

```
!ndiskd.nbllog [-stacks] 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-stacks______"></span><span id="_______-STACKS______"></span> *-stacks*   
Include callstacks.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Remarks
-------

**Important**  
**!ndiskd.nbllog** requires NBL tracking to be enabled on the debugee target machine. NBL tracking is not enabled by default in all configurations of Windows. If NBL tracking is not enabled, !ndiskd will give you instructions on how to enable it, as shown in the following snippet.

```
0: kd> !ndiskd.nbllog
    This command requires NBL tracking to be enabled on the debugee target
    machine.  (By default, client operating systems have level 1, and servers
    have level 0).  To enable, set this REG_DWORD value to a nonzero value on
    the target machine and reboot the target machine:
    
    HKLM\SYSTEM\CurrentControlSet\Services\NDIS\Parameters ! TrackNblOwner
    Possible Values (features are cumulative)
    * 0:  Disable all tracking.
    * 1:  Track the most recent owner of each NBL (enables !ndiskd.pendingnbls)
    * 2:  Scan for leaks at runtime (use with StuckNblReaction)
    * 3:  Keep a full history of all activity (enables !ndiskd.nbl -log)
    * 4:  Take stack capture snapshots (enables !ndiskd.nbl -log -stacks)
    This command requires level 3 or higher.
```

 

The NBL log shows network traffic on the system. [**!ndiskd.netreport**](-ndiskd-netreport.md) parses the NBL tracking log to display this network traffic visually. Therefore, if NBL tracking is not enabled, **!ndiskd.netreport** will not be able to show you this information.

Examples
--------

After you have enabled NBL tracking on the target debugee machine, enter the **!ndiskd.nbllog** command to see the log of all NBL traffic on the system. As shown in the example below, running **!ndiskd.nbllog** with no parameters will limit output to 200 events, which can be bypassed by rerunning the command with the *-force* option. The middle of the output in this example has been excised for brevity.

```
0: kd> !ndiskd.nbllog
    NBLs               Processor           Event              Detail            
                                                                     
    ffffe00bc71453f0   CPU  0              Freed
    ffffe00bc7163b40   CPU  2              Allocated
    ffffe00bc7163b40   CPU  2              ProtocolSent       ffffe00bc5ac4880 - QoS Packet Scheduler-0000
    ffffe00bc7163b40   CPU  2              FilterSent         ffffe00bc5ac5c70 - WFP Native MAC Layer LightWeight Filter-0000
    ffffe00bc7163b40   CPU  2, IRQL=DPC    FilterSent         ffffe00bc3f701a0 - Microsoft Kernel Debug Network Adapter
    ffffe00bc7163b40   CPU  2, IRQL=DPC    SentToMiniport     ffffe00bc3f701a0 - Microsoft Kernel Debug Network Adapter
    ffffe00bc7163b40   CPU  0, IRQL=DPC    MiniportSendCompleted ffffe00bc5ac5c70 - WFP Native MAC Layer LightWeight Filter-0000
    ffffe00bc7163b40   CPU  0, IRQL=DPC    FilterSendCompleted ffffe00bc5ac4880 - QoS Packet Scheduler-0000
    ffffe00bc7163b40   CPU  0, IRQL=DPC    FilterSendCompleted send complete in NDIS, sorting to Opens
    ffffe00bc7163b40   CPU  0, IRQL=DPC    SendCompleted      ffffe00bc5ab7c10 - TCPIP6

...

    ffffe00bc6b469b0   CPU  2              Allocated
    ffffe00bc6b469b0   CPU  2              Freed
    ffffe00bc64a3690   CPU  2              Allocated
    ffffe00bc64a3690   CPU  2              ProtocolSent       ffffe00bc5ac4880 - QoS Packet Scheduler-0000
    ffffe00bc64a3690   CPU  2              FilterSent         ffffe00bc5ac5c70 - WFP Native MAC Layer LightWeight Filter-0000
    ffffe00bc64a3690   CPU  2, IRQL=DPC    FilterSent         ffffe00bc3f701a0 - Microsoft Kernel Debug Network Adapter
    ffffe00bc64a3690   CPU  2, IRQL=DPC    SentToMiniport     ffffe00bc3f701a0 - Microsoft Kernel Debug Network Adapter
    ffffe00bc3cf2d10   CPU  1              Allocated
    ffffe00bc7bc6030   CPU  1              Allocated
    ffffe00bc3cf2d10   CPU  1              ProtocolSent       ffffe00bc5ac4880 - QoS Packet Scheduler-0000

    Maximum of 200 events printed; quitting early.
    Rerun with the '-force' option to bypass this limit.
```

For a more detailed description of how to interpret the results of **!ndiskd.nbllog**, see [!ndiskd.nbl -log](https://go.microsoft.com/fwlink/p/?linkid=846176) on the NDIS blog.

## <span id="see_also"></span>See also


[Network Driver Design Guide](https://msdn.microsoft.com/windows/hardware/drivers/network/index)

[Windows Vista and Later Networking Reference](https://msdn.microsoft.com/library/windows/hardware/ff571081)

[Debugging the Network Stack](https://go.microsoft.com/fwlink/p/?linkid=845311)

[**NDIS extensions (Ndiskd.dll)**](ndis-extensions--ndiskd-dll-.md)

[**!ndiskd.help**](-ndiskd-help.md)

[**NET\_BUFFER\_LIST**](https://msdn.microsoft.com/windows/hardware/drivers/network/net-buffer-list-structure)

[!ndiskd.nbl -log](https://go.microsoft.com/fwlink/p/?linkid=846176)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.nbllog%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





