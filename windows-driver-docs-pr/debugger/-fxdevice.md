---
title: fxdevice
description: The fxdevice extension displays summary information about all Power Management Framework (PoFx) registered devices. This command can be used only during kernel-mode debugging.
ms.assetid: 98E34825-467F-46E5-BC29-AF241FF30B90
keywords: ["fxdevice Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- fxdevice
api_type:
- NA
ms.localizationpriority: medium
---

# !fxdevice


The !fxdevice extension displays summary information about all Power Management Framework (PoFx) registered devices. This command can be used only during kernel-mode debugging.

For more information about PoFX, see [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637).

Syntax

```dbgcmd
!fxdevice[<FxDevice Address>]
```

## <span id="ddk__thread_dbg"></span><span id="DDK__THREAD_DBG"></span>Parameters


<span id="___________FxDevice__Address_______"></span><span id="___________fxdevice__address_______"></span><span id="___________FXDEVICE__ADDRESS_______"></span> **&lt; FxDevice Address&gt;**   
Provides the address of the FxDevice to display.

## <span id="DLL"></span><span id="dll"></span>DLL


<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Windows 10 and later</strong></p></td>
<td align="left"><p>Kdexts.dll</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

The !fxdevice extension displays the following information when it is present on the target system.

-   Non-idle PoFx devices
-   Idle D0 PoFx devices
-   Idle non-D0 PoFx devices

The following is example out from the !fxdevice extension with a supplied device address.

```dbgcmd
kd> !fxdevice ffffe0012ccbda60
!fxdevice 0xffffe0012ccbda60
    DevNode: 0xffffe0012bbb09f0
    UniqueId: "HDAUDIO\FUNC_01&VEN_10EC&DEV_0662&SUBSYS_103C304A&REV_1001\4&25ff998c&0&0001"
    InstancePath: "HDAUDIO\FUNC_01&VEN_10EC&DEV_0662&SUBSYS_103C304A&REV_1001\4&25ff998c&0&0001"
    Device Power State: PowerDeviceD0
    PEP Owner: Default PEP
    Acpi Plugin: 0
    Acpi Handle: 0
    Device Status Flags: IdleTimerOn DevicePowerNotRequired_ReceivedFromPEP 
    Device Idle Timeout: 0x1869ffffe7960
    Device Power On: No Activity
    Device Power Off: No Activity
    Device Unregister: No Activity
    Component Count: 1
        Component 0: F0/F0 - IDLE   (RefCount = 0)
        Pep Component: 0xffffe0012cfe1800
            Active: 0   Latency: 0  Residency: 0    Wake: 0 Dx IRP: 0   WW IRP: 0
            Component Idle State Change: No Activity
            Component Activation: No Activity
            Component Active: No Activity
```

The following is the default output from the !fxdevice extension.

```dbgcmd
kd> !fxdevice 
********************************************************************************
Dumping non-idle PoFx devices
********************************************************************************
!fxdevice 0xffffe0012bbd08d0
    DevNode: 0xffffe0012b3f87b0
    UniqueId: "\_SB.PCI0"
    InstancePath: "ACPI\PNP0A08\2&daba3ff&1"
    Device Power State: PowerDeviceD0
    Component Count: 1
        Component 0: F0/F1 - ACTIVE (RefCount = 28)

!fxdevice 0xffffe0012c587940
    DevNode: 0xffffe0012b3f9d30
    UniqueId: "\_SB.PCI0.PEGL"
    InstancePath: "PCI\VEN_8086&DEV_D138&SUBSYS_304A103C&REV_11\3&33fd14ca&0&18"
    Device Power State: PowerDeviceD0
    Component Count: 1
        Component 0: F0/F1 - ACTIVE (RefCount = 1)

...

********************************************************************************
Dumping idle D0 PoFx devices
********************************************************************************
!fxdevice 0xffffe0012c5838c0
    DevNode: 0xffffe0012bbdfd30
    UniqueId: "\_SB.PCI0.PCX1"
    InstancePath: "PCI\VEN_8086&DEV_3B42&SUBSYS_304A103C&REV_05\3&33fd14ca&0&E0"
    Device Power State: PowerDeviceD0
    Component Count: 1
        Component 0: F1/F1 - IDLE   (RefCount = 0)

!fxdevice 0xffffe0012c581ac0
    DevNode: 0xffffe0012bbdfa50
    UniqueId: "\_SB.PCI0.PCX5"
    InstancePath: "PCI\VEN_8086&DEV_3B4A&SUBSYS_304A103C&REV_05\3&33fd14ca&0&E4"
    Device Power State: PowerDeviceD0
    Component Count: 1
        Component 0: F1/F1 - IDLE   (RefCount = 0)

...
```

 

 





