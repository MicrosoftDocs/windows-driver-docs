---
title: "!wudfext.wudfdevice"
description: "The !wudfext.wudfdevice extension displays the Plug and Play (PnP) and power-management state systems for a device."
keywords: ["!wudfext.wudfdevice Windows Debugging"]
ms.date: 05/23/2017
topic_type:
- apiref
ms.topic: reference
api_name:
- wudfext.wudfdevice
api_type:
- NA
---

# !wudfext.wudfdevice

The **!wudfext.wudfdevice** extension displays the Plug and Play (PnP) and power-management state systems for a device.

```dbgcmd
!wudfext.wudfdevice pWDFDevice
```

## Parameters

<span id="_______pWDFDevice______"></span><span id="_______pwdfdevice______"></span><span id="_______PWDFDEVICE______"></span> *pWDFDevice*   
Specifies the address of the **IWDFDevice** interface to display PnP or power-management state about.

## DLL

Wudfext.dll

## Additional Information

For more information, see [User-Mode Driver Framework Debugging](../debugger/user-mode-driver-framework-debugging.md).

## Remarks

You can use the **!wudfext.wudfdevice** extension to determine the current PnP or power-management state of the device that the *pWDFDevice* parameter specifies.

The following is an example of the **!wudfext.wudfdevice** display:

```dbgcmd
kd> !wudfdevice 0xf2f80 
Pnp Driver Callbacks:
  IPnpCallback: 0x0
  IPnpCallbackHardware: 0x0
  IPnpSelfManagedIo: 0x0
Pnp State Machine:
  CurrentState:  WdfDevStatePnpStarted
  Pending UMIrp: 0x00000000
    Could not read event queue depth, assuming 8
  Event queue:
    Processed/in-process events:
      PnpEventAddDevice
      PnpEventStartDevice
      PnpEventPwrPolStarted
    Pending events:
    State History:
      WdfDevStatePnpInit
      WdfDevStatePnpInitStarting
      WdfDevStatePnpHardwareAvailable
      WdfDevStatePnpEnableInterfaces
      WdfDevStatePnpStarted
Power State Machine:
  CurrentState:      WdfDevStatePowerD0
  Pending UMIrp:     0x00000000
  IoCallbackFailure: false
    Could not read event queue depth, assuming 8
  Event queue:
    Processed/in-process events:
      PowerImplicitD0
    Pending events:
    State History:
      WdfDevStatePowerStartingCheckDeviceType
      WdfDevStatePowerD0Starting
      WdfDevStatePowerD0StartingConnectInterrupt
      WdfDevStatePowerD0StartingDmaEnable
      WdfDevStatePowerD0StartingStartSelfManagedIo
      WdfDevStatePowerDecideD0State
      WdfDevStatePowerD0
Power Policy State Machine:
  CurrentState             : WdfDevStatePwrPolStartingSucceeded
  PowerPolicyOwner         : false
  PendingSystemPower UMIrp : 0x00000000
  PowerFailed              : false
    Could not read event queue depth, assuming 8
  Event queue:
    Processed/in-process events:
      PwrPolStart
      PwrPolPowerUp
    Pending events:
    State History:
      WdfDevStatePwrPolStarting
      WdfDevStatePwrPolStarted
      WdfDevStatePwrPolStartingSucceeded
```
