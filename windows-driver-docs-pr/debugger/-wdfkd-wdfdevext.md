---
title: wdfkd.wdfdevext
description: The wdfkd.wdfdevext extension displays information that is associated with the DeviceExtension member of a Microsoft Windows Driver Model (WDM) DEVICE_OBJECT structure.
ms.assetid: 89559cae-7323-4c91-b20a-7d42069cdb93
keywords: ["wdfkd.wdfdevext Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfdevext
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfdevext


The **!wdfkd.wdfdevext** extension displays information that is associated with the **DeviceExtension** member of a Microsoft Windows Driver Model (WDM) DEVICE\_OBJECT structure.

```dbgcmd
!wdfkd.wdfdevext DeviceExtension
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______DeviceExtension______"></span><span id="_______deviceextension______"></span><span id="_______DEVICEEXTENSION______"></span> *DeviceExtension*   
A pointer to a device extension.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

Here is an example for HdAudBus.sys, which is a KMDF driver. Use [**!devnode**](-devnode.md) to find a device node that has HdAudBus as its function driver. Take the physical device object (PDO) from the output and pass it to [**!devstack**](-devstack.md). Take the device extension address from the output of **!devstack** and pass it to **!wdfdevext**.

```dbgcmd
0: kd> !devnode 0 1 hdaudbus
Dumping IopRootDeviceNode (= 0xffffe000002cfd30)
DevNode 0xffffe000009b7a50 for PDO 0xffffe00000226880
  InstancePath is "PCI\VEN_8086&DEV_293E&SUBSYS_2819103C&REV_02\3&33fd14ca&0&D8"
  ServiceName is "HDAudBus"
  ...
0: kd> !devstack 0xffffe00000226880
  !DevObj           !DrvObj            !DevExt           ObjectName
  ffffe00001351e20  \Driver\HDAudBus   ffffe000009a3c00  
> ffffe00000226880  \Driver\pci        ffffe000002269d0  NTPNP_PCI0009
!DevNode ffffe000009b7a50 :
  DeviceInst is "PCI\VEN_8086&DEV_293E&SUBSYS_2819103C&REV_02\3&33fd14ca&0&D8"
  ServiceName is "HDAudBus"
0: kd> *
0: kd> !wdfdevext ffffe000009a3c00
Device context is 0xffffe000009a3c00
    context:  dt 0xffffe000009a3c00 HDAudBus!HDAudioDeviceExtension (size is 0xa8 bytes)
    EvtCleanupCallback fffff80001f35950 HDAudBus!HdAudBusEvtDeviceCleanupCallback

!wdfdevice 0x00001fffff65c6e8                        
!wdfobject 0xffffe000009a3910
```

Here is an example for Wudfrd.sys, which is the function driver for the kernel-mode portion of a UMDF 2 driver stack. Use [**!devnode**](-devnode.md) to find a device node that has Wudfrd as its function driver. Take the physical device object (PDO) from the output and pass it to [**!devstack**](-devstack.md). Take the device extension address from the output of **!devstack** and pass it to **!wdfdevext**.

```dbgcmd
0: kd> !devnode 0 1 wudfrd
Dumping IopRootDeviceNode (= 0xffffe000002cfd30)
DevNode 0xffffe00000a1e530 for PDO 0xffffe00000b15b00
  InstancePath is "ROOT\SAMPLE\0001"
  ServiceName is "WUDFRd"
  ...
0: kd> !devstack 0xffffe00000b15b00
  !DevObj           !DrvObj            !DevExt           ObjectName
  ffffe00000c11040  \Driver\WUDFRd     ffffe00000c11190  
> ffffe00000b15b00  \Driver\PnpManager 00000000  00000052
!DevNode ffffe00000a1e530 :
  DeviceInst is "ROOT\SAMPLE\0001"
  ServiceName is "WUDFRd"
0: kd> *
0: kd> !wdfdevext ffffe00000c11190
## Device context is 0xffffe00000c11190

##  UMDF Device Instances for this Redirector extension

  DriverManagerProcess: 0xffffe00003470500

  ImageName              Ver   DevStack           HostProcess        DeviceID      
  MyUmdf2Driver.dll      v2.0  0x000000a5a3ab5f70 0xffffe00000c32900  \Device\00000052
```

 

 





