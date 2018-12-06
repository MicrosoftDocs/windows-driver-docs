---
title: MB Device Readiness
description: MB Device Readiness
ms.assetid: 67a67ff7-dcff-4aec-bea9-7b1be9593649
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Device Readiness


This topic describes the procedures to ensure that an MB device is accessible and ready to be used for network-related activities before the MB Service proceeds to setup data connections. The device is ready to use when the user subscription has been activated and subscriber-related information stored to the device or the Subscriber Identity Module (SIM card)

The MB Service assumes that a miniport driver automatically initializes its MB device's hardware (radio stack, SIM card or equivalent circuitry) after the system has loaded it, without waiting for any instruction from the service.

Miniport drivers set the initial ready-state of their MB device to **WwanReadyStateOff**. As they proceed with initializing, miniport drivers must send event notifications to inform the MB Service of changes to their device's ready state.

Miniport drivers must stop the initialization process if they run into any error conditions. After the error condition is cleared, miniport drivers can resume the initialization process until their device has reached the **WwanReadyStateInitialized** ready-state.

The following are examples of some error scenarios:

-   If the device requires a SIM card and the miniport driver detects that no SIM card is present, the miniport driver must send a **WwanReadyStateSimNotInserted** ready-state event notification, and the miniport driver must remain in that state until the user inserts a SIM card into the device.

-   If the device requires a SIM card and the miniport driver cannot read the SIM card that has been inserted (for example, a U-RIM is inserted into a GSM-based device or a USIM is inserted into a CDMA-based device) or the SIM card is not compatible with the device (for example, a 3G USIM is inserted into a 2G device, which cannot interpret the USIM format), the miniport driver must send a **WwanReadyStateBadSim** ready-state event notification, and the miniport driver must remain in that state until the user inserts a correct SIM card into the device.

-   If the device is locked by the PIN (for devices that use SIM cards) or by a password (for devices that do not use SIM cards) that prevents further device initialization progress, the miniport driver must send a **WwanReadyStateDeviceLocked** ready-state event notification, and the miniport driver must remain in that state until the user enters the correct PIN or password.

-   If the miniport driver detects that service activation is required to proceed, the miniport driver must send a **WwanReadyStateNotActivated** ready-state event notification, and it must remain in that state until the service has been activated. This is typical behavior for CDMA-based devices in North America.

-   If the miniport driver runs into failures other than the ones mentioned previously, the miniport driver must send a **WwanReadyStateFailure** ready-state event notification, and it must remain in that state until the problem has been identified and corrected.

Be aware that the MB Service does not assume that miniport drivers can detect all these errors. Nor does the service assume the order in which miniport drivers detect these error conditions. However, it is best to implement the error scenarios in the order listed previously.

Until a miniport driver sends a **WwanReadyStateInitialized** ready-state event notification, the service will not proceed any further with network-related activities until the problem has been identified and corrected. However, the service may still send OIDs to the miniport driver.

Miniport drivers do not need to wait for the SMS subsystem to be ready before reporting the **WwanReadyStateInitialized** ready-state. Instead, miniport drivers should send a separate [OID\_WWAN\_SMS\_CONFIGURATION](https://msdn.microsoft.com/library/windows/hardware/ff569837) notification when the SMS subsystem is ready to send and receive SMS messages.

### Emergency Mode Support

If the miniport driver indicates that it supports emergency call services while processing [OID\_WWAN\_READY\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569833) the miniport driver must set the **EmergencyMode** member of the [**WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff571226) structure to **WwanEmergencyModeOn**. In this case, the miniport driver should continue to send registration notifications to the MB Service, but the service will not invoke any automatic configuration related functionalities.

Miniport drivers can specify that they support emergency call services even in scenarios where they detect that the SIM is no longer valid, perhaps because the subscription is unpaid, or service has been deactivated because the device has been reported stolen.

For more information about device readiness, see [OID\_WWAN\_READY\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569833).

 

 





