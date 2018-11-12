---
title: usbkd._ehciregs
description: The usbkd._ehciregs command displays the operational and root hub port status registers of a USB EHCI host controller.
ms.assetid: BFD58E6B-BC51-4F2F-B597-8C815826F931
keywords: ["usbkd._ehciregs Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- usbkd._ehciregs
api_type:
- NA
ms.localizationpriority: medium
---

# !usbkd.\_ehciregs


The **!usbkd.\_ehciregs** command displays the operational and root hub port status registers of a USB EHCI host controller.

```dbgcmd
!usbkd._ehciregs StructAddr[, NumPorts]
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbehci!\_HC\_OPERATIONAL\_REGISTER** structure. To find the address of a **usbehci!\_HC\_OPERATIONAL\_REGISTER** structure, use [**!usbkd.usbhcdlist**](-usbkd-usbhcdlist.md).

<span id="_______NumPorts______"></span><span id="_______numports______"></span><span id="_______NUMPORTS______"></span> *NumPorts*   
The number of root hub port status registers to display.

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to get the address of a **usbehci!\_HC\_OPERATIONAL\_REGISTER** structure. First enter [**!usbkd.usbhcdlist**](-usbkd-usbhcdlist.md).

```dbgcmd
0: kd> !usbkd.usbhcdlist
MINIPORT List @ fffff80001e5bbd0

## List of EHCI controllers

!drvobj ffffe00001fd33a0 dt USBPORT!_USBPORT_MINIPORT_DRIVER ...
...
02. Xxxx Corporation PCI: VendorID Xxxx DeviceID Xxxx RevisionId 0002
    !devobj ffffe00001ca1050
    !ehci_info ffffe00001ca11a0
    Operational Registers ffffd000228bf020
```

In the preceding output,` ffffd000228bf020` is the address of a **\_HC\_OPERATIONAL\_REGISTER** structure.

Now pass the structure address to **!\_ehciregs**. In this example, the second argument limits the display to two root hub port status registers.

```dbgcmd
0: kd> !usbkd._ehciregs ffffd000228bf020, 2
*(ehci)HC_OPERATIONAL_REGISTER ffffd000228bf020
    USBCMD 00010001
    .HostControllerRun: 1
    .HostControllerReset: 0
    .FrameListSize: 0
    .PeriodicScheduleEnable: 0
    .AsyncScheduleEnable: 0
    .IntOnAsyncAdvanceDoorbell: 0
    .HostControllerLightReset: 0
    .InterruptThreshold: 1
    .ParkModeEnable: 0
    .ParkModeCount: 0

    USBSTS 00002008
    .UsbInterrupt: 0
    .UsbError: 0
    .PortChangeDetect: 0
    .FrameListRollover: 1
    .HostSystemError: 0
    .IntOnAsyncAdvance: 0
    ----
    .HcHalted: 0
    .Reclimation: 1
    .PeriodicScheduleStatus: 0
    .AsyncScheduleStatus: 0

    USBINTR 0000003f
    .UsbInterrupt: 1
    .UsbError: 1
    .PortChangeDetect: 1
    .FrameListRollover: 1
    .HostSystemError: 1
    .IntOnAsyncAdvance: 1
    PeriodicListBase dec8e000
    AsyncListAddr dec91000
    PortSC[0] 00001000
        PortConnect x0
        PortConnectChange x0
        PortEnable x0
        PortEnableChange x0
        OvercurrentActive x0
        OvercurrentChange x0
        ForcePortResume x0
        PortSuspend x0
        PortReset x0
        HighSpeedDevice x0
        LineStatus x0
        PortPower x1
        PortOwnedByCC x0
        PortIndicator x0
        PortTestControl x0
        WakeOnConnect x0
        WakeOnDisconnect x0
        WakeOnOvercurrent x0
    PortSC[1] 00001000
        PortConnect x0
        PortConnectChange x0
        PortEnable x0
        PortEnableChange x0
        OvercurrentActive x0
        OvercurrentChange x0
        ForcePortResume x0
        PortSuspend x0
        PortReset x0
        HighSpeedDevice x0
        LineStatus x0
        PortPower x1
        PortOwnedByCC x0
        PortIndicator x0
        PortTestControl x0
        WakeOnConnect x0
        WakeOnDisconnect x0
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](https://go.microsoft.com/fwlink/p?LinkID=227351)

 

 






