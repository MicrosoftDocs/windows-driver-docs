---
title: usbkd.usbhubpd
description: The usbkd.usbhubpd command displays information about a USB port.
ms.assetid: 41D5E65D-76C2-45E0-9AC7-C2B50D806935
keywords: ["usbkd.usbhubpd Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
topic_type:
- apiref
api_name:
- usbkd.usbhubpd
api_type:
- NA
---

# !usbkd.usbhubpd


The **!usbkd.usbhubpd** command displays information about a USB port.

```
!usbkd.usbhubpd StructAddr
```

## <span id="ddk__devobj_dbg"></span><span id="DDK__DEVOBJ_DBG"></span>Parameters


<span id="_______StructAddr______"></span><span id="_______structaddr______"></span><span id="_______STRUCTADDR______"></span> *StructAddr*   
Address of a **usbhub!\_HUB\_PORT\_DATA** structure. To get the addresses of these structures, use [**!usbhubext**](-usbkd-usbhubext.md).

## <span id="DLL"></span><span id="dll"></span>DLL


Usbkd.dll

Examples
--------

Here is one way to find the address of a **usbhub!\_HUB\_PORT\_DATA**. First enter [**!usbkd.usb2tree**](-usbkd-usb2tree.md).

```
0: kd> !usbkd.usb2tree
...
2)!ehci_info ffffe00001ca11a0 !devobj ffffe00001ca1050 PCI: VendorId 8086 DeviceId 293c RevisionId 0002 
    RootHub !hub2_info ffffe000023201a0 !devstack ffffe00002320050
        ...
```

In the preceding output, you can see the suggested command **!devstack ffffe00002320050**. Enter this command.

```
0: kd> !kdexts.devstack ffffe00002320050

  !DevObj           !DrvObj            !DevExt           ObjectName
> ffffe00002320050  \Driver\usbhub     ffffe000023201a0  0000002d
  ffffe0000213c050  \Driver\usbehci    ffffe0000213c1a0  USBPDO-3
...
```

In the preceding output, you can see that the address of the device extension for the FDO of the hub is `ffffe000023201a0`.

Pass the address of the device extension to the [**!usbhubext**](-usbkd-usbhubext.md) command.

```
0: kd> !usbkd.usbhubext ffffe000023201a0

FDO ffffe00002320050 PDO ffffe0000213c050 HubNumber# 3
dt USBHUB!_DEVICE_EXTENSION_HUB ffffe000023201a0
!usbhublog ffffe000023201a0
RemoveLock ffffe00002320668
FdoFlags ffffe00002320ba0

CurrentPowerIrp: System (0000000000000000) Device (0000000000000000)
...
## PORT DATA

PortData 1: !port2_info ffffe000021bf000 Port State = PS_WAIT_CONNECT PortChangeLock: 0, Pcq_State: Pcq_Run_Idle             
     PDO 0000000000000000 
....
```

In the preceding output, `ffffe000021bf000` is the address of a **\_HUB\_PORT\_DATA** structure. Pass this address to **!usbhubpd**.

```
0: kd> !usbkd.usbhubpd ffffe000021bf000
PortNumber: 1
Parent Hub FDO ffffe00002320050
Device PDO <NULL>
dt USBHUB!_HUB_PORT_DATA ffffe000021bf000
dt USBHUB!_PORTDATA_FLAGS ffffe000021bf968

PortChangelist: !usblist ffffe000021bf1c8, CL [Empty]

## Port Indicators Log (latest at bottom)

##     Event           State                Next

    [EMPTY]

## Port Change Queue History (latest at bottom)

##     Event                State                    Next                     PcqEv_Suspend PcqEv_Resume  PcqEv_ChDone  Tag 

01. PCE_Resume           Pcq_Stop                 Pcq_Pause                              PcqEv_Reset   PcqEv_Reset   REQUEST_RESUME     
...          Pcq_Run_wBusy            Pcq_Run_Idle                                                                            

## Port Status History (latest at bottom)

##     Current State          Change Eve nt        PDO              CEOSP H/W Port REG Frame Inserted

01. PS_WAIT_CONNECT        REQUEST_PAUSE       0000000000000000 00000 100  Age:000 512498
...
```

## <span id="see_also"></span>See also


[USB 2.0 Debugger Extensions](usb-2-0-extensions.md)

[Universal Serial Bus (USB) Drivers](http://go.microsoft.com/fwlink/p?LinkID=227351)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!usbkd.usbhubpd%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





