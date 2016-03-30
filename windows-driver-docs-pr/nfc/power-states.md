---
title: Power States
description: The NFC class extension driver serves as the power policy owner for the device, so it calls WdfDeviceInitSetPowerPolicyOwnership(TRUE) during its device initialization routine.
ms.assetid: 12433344-9C33-415B-BA14-4BD4C7E838CC
---

# Power States


The NFC class extension driver serves as the power policy owner for the device, so it calls [**WdfDeviceInitSetPowerPolicyOwnership**](https://msdn.microsoft.com/library/windows/hardware/ff546776)(TRUE) during its device initialization routine.

The NFC CX driver supports device power states D0 and D3. The state diagram below shows the transition between the two power states. The device on idle is in the D3 power state where the NFCC does not have power. When radio mode is active and any modules such as NFP (active publications or subscriptions from NFP DDI), SE (active secure elements in emulation mode from NFCSE DDI) or SmartCard is active, the state transitions to D0. During this transition, the polling state of the device is updated to meet the requirement of all active modules.

![power states](images/powerstate.png)

Furthermore, the built-in idle detection logic of UMDF is used to power manager the device. During initialization, the WdfDevice is assigned its S0 Idle settings as follows:

```
WdfDeviceAssignS0IdleSettings(
    IdleCannotWakeFromS0,
    PowerDeviceD3,
    IdleTimeout, 
    IdleAllowUserControl,
    WdfUseDefault
);
```

The IdleTimeout defaults to 1 second. This setting is configurable via *PowerIdleTimeout* parameter in [**NFC\_CX\_CLIENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn905540). The state diagram below illustrates the various power transitions that are implied by the use of the WDF idle detection method.

The client driver can choose to be the power policy owner of the stack through the **IsPowerPolicyOwner** member of the [**NFC\_CX\_CLIENT\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/dn905540) structure. This might be useful for transports such as USB where additional device power states must be configured.

![power management operations](images/powermanagementoperations.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20Power%20States%20%20RELEASE:%20%283/30/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




