---
title: powertriage
description: The powertriage extension displays summary information about the system and device power related components.
ms.assetid: A202ED64-B706-42AC-B058-C44321C9171F
keywords: ["powertriage Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- powertriage
api_type:
- NA
ms.localizationpriority: medium
---

# !powertriage


The !powertriage extension displays summary information about the system and device power related components. It also provides links to related commands that can be used to gather additional information. The !powertriage command has no parameters. This command can be used with both live kernel-mode debugging and for crash dump file analysis.

Syntax

```dbgcmd
!powertriage
```

## <span id="ddk__thread_dbg"></span><span id="DDK__THREAD_DBG"></span>Parameters


None

### <span id="DLL"></span><span id="dll"></span>DLL

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

The !powertriage extension displays the following information.

1. Power state of the device node along with !podev for all the device objects.
2. Links to [**!rcdrkd.rcdrlogdump**](-rcdrkd-rcdrlogdump.md) if the driver has enabled the IFR. For more information about IFR, see [Using Inflight Trace Recorder (IFR) in KMDF and UMDF 2 Drivers](https://msdn.microsoft.com/library/windows/hardware/dn940485).
3. Links to [**!wdfkd.wdfdriverinfo**](-wdfkd-wdfdriverinfo.md) and [**!wdfkd.wdflogdump**](-wdfkd-wdflogdump.md) for WDF drivers.
4. Links to !fxdevice for PoFx devices. For more information about PoFX, see [Overview of the Power Management Framework](https://msdn.microsoft.com/library/windows/hardware/hh406637).
Here is example output from the !powertriage command.

```dbgcmd
kd> !powertriage

System Capabilities :
  Machine is not AOAC capable.

Power Capabilities:
PopCapabilities @ 0xfffff8022f6c4380
  Misc Supported Features:  PwrButton S1 S3 S4 S5 HiberFile FullWake
  Processor Features:      
  Disk Features:           
  Battery Features:        
  Wake Caps
    Ac OnLine Wake:         Sx
    Soft Lid Wake:          Sx
    RTC Wake:               S4
    Min Device Wake:        Sx
    Default Wake:           Sx



Power Action:

PopAction :fffff8022f6ba550
    Current System State..: Working
    Target System State...: Unspecified
    State.................: - Idle(0)

Devices with allocated Power IRPs:

    +  ACPI\PNP0C0C\2&daba3ff&1
       0xffffe00023939ad0 ACPI D0 !podev  WAIT_WAKE_IRP !irp Related Threads 

    +  USB\ROOT_HUB30\5&2c60645a&0&0
       0xffffe0002440ac40 USBXHCI D2 !podev  WAIT_WAKE_IRP !irp Related Threads !rcdrlogdump !wdfdriverinfo !wdflogdump 
         Upper DO 0xffffe00024415a10 USBHUB3 !podev 


    +  USB\ROOT_HUB30\5&d91dce5&0&0
       0xffffe00023ed4d30 USBXHCI D2 !podev  WAIT_WAKE_IRP !irp Related Threads !rcdrlogdump !wdfdriverinfo !wdflogdump 
         Upper DO 0xffffe000249d8040 USBHUB3 !podev 

    +  PCI\VEN_8086&DEV_27E2&SUBSYS_01DE1028&REV_01\3&172e68dd&0&E5
       0xffffe000239e5880 pci D0 !podev FxDevice: !fxdevice  WAIT_WAKE_IRP !irp Related Threads 
         Upper DO 0xffffe000239c0e50 ACPI !podev 
           Upper DO 0xffffe000239f7040 pci !podev 


    +  PCI\VEN_14E4&DEV_167A&SUBSYS_01DE1028&REV_02\4&24ac2e11&0&00E5
       0xffffe000231e6060 pci D0 !podev  WAIT_WAKE_IRP !irp Related Threads 
         Upper DO 0xffffe00024359050 b57nd60a !podev 


Device Tree Info: 

    !devpowerstate

    !devpowerstate Complete


Links:
!poaction
!cstriage
!pdctriage
!pdcclients
!fxdevice
!pnptriage
```

**Dump File Power Failure Analysis**

The !powertriage extension can be useful in examining system crashes related to incorrect power state information. For example, in the case of [**Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE**](bug-check-0x9f--driver-power-state-failure.md), the extension will display all the allocated power IRPs, the associated device stacks along with:

1. Links to the [**!irp**](-irp.md) command for the related IRPs.
2. Links to the [**!findthreads**](-findthreads.md) command with the related IRP. The IRP is added as part of the search criteria and displays the threads starting with higher correlation to the search criteria threads listed first.
Dumping all device stacks with power IRPs can help in debugging cases where !analyze has not been able to correctly identify the IRP associated with the crash.

 

 





