---
title: wdfkd.wdfdevice
description: The wdfkd.wdfdevice extension displays information that is associated with a WDFDEVICE-typed object handle.
ms.assetid: c6dd98e5-a0ed-437d-a313-5d8a416105dd
keywords: ["wdfkd.wdfdevice Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- wdfkd.wdfdevice
api_type:
- NA
ms.localizationpriority: medium
---

# !wdfkd.wdfdevice


The **!wdfkd.wdfdevice** extension displays information that is associated with a WDFDEVICE-typed object handle.

```dbgcmd
!wdfkd.wdfdevice Handle [Flags]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______Handle______"></span><span id="_______handle______"></span><span id="_______HANDLE______"></span> *Handle*   
A handle to a WDFDEVICE-typed object.

<span id="_______Flags______"></span><span id="_______flags______"></span><span id="_______FLAGS______"></span> *Flags*   
Optional. The kind of information to display. *Flags* can be any combination of the following bits:

<span id="Bit_0__0x1_"></span><span id="bit_0__0x1_"></span><span id="BIT_0__0X1_"></span>Bit 0 (0x1)  
The display will include verbose information about the device, such as the associated WDFCHILDLIST-typed handles, synchronization scope, and execution level.

<span id="Bit_1__0x2_"></span><span id="bit_1__0x2_"></span><span id="BIT_1__0X2_"></span>Bit 1 (0x2)  
The display will include detailed power state information.

<span id="Bit_2__0x4_"></span><span id="bit_2__0x4_"></span><span id="BIT_2__0X4_"></span>Bit 2 (0x4)  
The display will include detailed power policy state information.

<span id="Bit_3__0x8_"></span><span id="bit_3__0x8_"></span><span id="BIT_3__0X8_"></span>Bit 3 (0x8)  
The display will include detailed Plug and Play (PnP) state information.

<span id="Bit_4__0x10_"></span><span id="bit_4__0x10_"></span><span id="BIT_4__0X10_"></span>Bit 4 (0x10)  
The display will include the device object's callback functions.

### <span id="DLL"></span><span id="dll"></span>DLL

Wdfkd.dll

### <span id="Frameworks"></span><span id="frameworks"></span><span id="FRAMEWORKS"></span>Frameworks

KMDF 1, UMDF 2

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information, see [Kernel-Mode Driver Framework Debugging](kernel-mode-driver-framework-debugging.md).

Remarks
-------

The following example uses the **!wdfkd.wdfdevice** extension on a WDFDEVICE handle that represents a physical device object (PDO), without specifying any flags.

```dbgcmd
kd> !wdfdevice 0x7cad31c8 

# Dumping WDFDEVICE 0x7cad31c8
=================================

WDM PDEVICE_OBJECTs:  self 81fb00e8

Pnp state:  119 ( WdfDevStatePnpStarted )
Power state:  31f ( WdfDevStatePowerDx )
Power Pol state:  508 ( WdfDevStatePwrPolWaitingUnarmed )

Parent WDFDEVICE 7ca7b1c0
Parent states:
   Pnp state:  119 ( WdfDevStatePnpStarted )
   Power state:  307 ( WdfDevStatePowerD0 )
   Power Pol state:  565 ( WdfDevStatePwrPolStarted )

No pended pnp or power irps
Device is the power policy owner for the stack
```

The following example displays the same device object as the preceding example, but this time with a flag value of 0xF. This flag value, a combination of the bits 0x1, 0x2, 0x4, and 0x8, causes the display to include verbose device information, power state information, power policy state information, and PnP state information.

```dbgcmd
kd> !wdfdevice 0x7cad31c8 f 

# Dumping WDFDEVICE 0x7cad31c8
=================================

WDM PDEVICE_OBJECTs:  self 81fb00e8

Pnp state:  119 ( WdfDevStatePnpStarted )
Power state:  31f ( WdfDevStatePowerDx )
Power Pol state:  508 ( WdfDevStatePwrPolWaitingUnarmed )

Parent WDFDEVICE 7ca7b1c0
Parent states:
   Pnp state:  119 ( WdfDevStatePnpStarted )
   Power state:  307 ( WdfDevStatePowerD0 )
   Power Pol state:  565 ( WdfDevStatePwrPolStarted )

No pended pnp or power irps
Device is the power policy owner for the stack

Pnp state history:
[0] WdfDevStatePnpObjectCreated (0x100)
[1] WdfDevStatePnpInit (0x105)
[2] WdfDevStatePnpInitStarting (0x106)
[3] WdfDevStatePnpHardwareAvailable (0x108)
[4] WdfDevStatePnpEnableInterfaces (0x109)
[5] WdfDevStatePnpStarted (0x119)

Power state history:
[0] WdfDevStatePowerD0StartingConnectInterrupt (0x310)
[1] WdfDevStatePowerD0StartingDmaEnable (0x311)
[2] WdfDevStatePowerD0StartingStartSelfManagedIo (0x312)
[3] WdfDevStatePowerDecideD0State (0x313)
[4] WdfDevStatePowerD0BusWakeOwner (0x309)
[5] WdfDevStatePowerGotoDx (0x31a)
[6] WdfDevStatePowerGotoDxIoStopped (0x31c)
[7] WdfDevStatePowerDx (0x31f)

Power policy state history:
[0] WdfDevStatePwrPolStarting (0x501)
[1] WdfDevStatePwrPolStartingSucceeded (0x502)
[2] WdfDevStatePwrPolStartingDecideS0Wake (0x504)
[3] WdfDevStatePwrPolStartedIdleCapable (0x505)
[4] WdfDevStatePwrPolTimerExpiredNoWake (0x506)
[5] WdfDevStatePwrPolTimerExpiredNoWakeCompletePowerDown (0x507)
[6] WdfDevStatePwrPolWaitingUnarmedQueryIdle (0x509)
[7] WdfDevStatePwrPolWaitingUnarmed (0x508)

WDFCHILDLIST Handles:
 !WDFCHILDLIST 0x7ce710c8

SyncronizationScope is WdfSynchronizationScopeNone
ExecutionLevel is WdfExecutionLevelDispatch
```

 

 





