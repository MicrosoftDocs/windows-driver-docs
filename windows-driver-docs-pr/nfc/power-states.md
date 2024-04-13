---
title: NFC Power States
description: The NFC class extension driver serves as the power policy owner for the device, so it calls WdfDeviceInitSetPowerPolicyOwnership(TRUE) during its device initialization routine.
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 01/11/2024
---

# NFC power states

The NFC class extension driver serves as the power policy owner for the device, so it calls **[WdfDeviceInitSetPowerPolicyOwnership](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetpowerpolicyownership)(TRUE)** during its device initialization routine.

The NFC CX driver supports device power states D0 and D3. The state diagram below shows the transition between the two power states. The device on idle is in the D3 power state where the NFCC does not have power. When radio mode is active and any modules such as NFP (active publications or subscriptions from NFP DDI), SE (active secure elements in emulation mode from NFCSE DDI) or SmartCard is active, the state transitions to D0. During this transition, the polling state of the device is updated to meet the requirement of all active modules.

![power states.](images/powerstate.png)

Furthermore, the built-in idle detection logic of UMDF is used to power manager the device. During initialization, the WdfDevice is assigned its S0 Idle settings as follows:

```cpp
WdfDeviceAssignS0IdleSettings(
    IdleCannotWakeFromS0,
    PowerDeviceD3,
    IdleTimeout,
    IdleAllowUserControl,
    WdfUseDefault
);
```

The IdleTimeout defaults to 1 second. This setting is configurable via *PowerIdleTimeout* parameter in **[NFC_CX_CLIENT_CONFIG](/windows-hardware/drivers/ddi/nfccx/ns-nfccx-_nfc_cx_client_config)**. The state diagram below illustrates the various power transitions that are implied by the use of the WDF idle detection method.

The client driver can choose to be the power policy owner of the stack through the **IsPowerPolicyOwner** member of the **[NFC_CX_CLIENT_CONFIG](/windows-hardware/drivers/ddi/nfccx/ns-nfccx-_nfc_cx_client_config)** structure. This might be useful for transports such as USB where additional device power states must be configured.

![power management operations.](images/powermanagementoperations.png)

## Related topics

- [NFC device driver interface (DDI) overview](/windows-hardware/drivers/ddi/index)
- [NFC class extension (CX) reference](/windows-hardware/drivers/ddi/index)
