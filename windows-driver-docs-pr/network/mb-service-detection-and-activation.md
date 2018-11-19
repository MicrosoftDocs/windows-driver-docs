---
title: MB Service Detection and Activation
description: MB Service Detection and Activation
ms.assetid: 7c53528b-722d-44a1-9eac-ee1fe89f21f3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Service Detection and Activation


This topic describes the procedures to detect whether an MB device must have its service activated, and how to gain access to a provider's network.

### Service Activation Detection

Miniport drivers can determine whether they must perform service activation in a couple of ways:

-   For CDMA-based devices, in North America or other places where U-RIM is not used, there should be a flag on the device to indicate activation status. Miniport drivers should be able to detect the activation status during initialization without contacting the provider network. Miniport drivers should perform service activation automatically when the device first connects over-the-air to the home network. After activation has been completed, miniport drivers should clear the flag so that they will not need to perform service activation again.

    Miniport drivers inform the MB Service about service activation progress by sending [**NDIS\_STATUS\_WWAN\_READY\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567856) notifications during MB device initialization. Alternatively, to determine service activation status, the service may send an [OID\_WWAN\_READY\_INFO](https://msdn.microsoft.com/library/windows/hardware/ff569833) query request to a miniport driver. In both cases, the initial ready-state should be **WwanReadyStateNotActivated**. After service has been activated, miniport drivers should resume the initialization process and notify the service as the device ready-state changes.

-   For GSM-based devices, there is no general method to detect whether a device must have its service activated. Miniport drivers can implement their own proprietary method, specific to its carrier, to perform service detection and activation.

### MB Service Activation

Service activation refers to the process of activating the MB service subscription so that the device can gain access to the provider's network. The MB Service is not equipped with service activation logic because the exact activation procedure must be performed by the miniport driver and/or third-party software because the actual activation process varies from cellular technologies and is usually customized for different provider networks. Service activation can be automatic, or manual, or a combination of both. Miniport drivers should only need to perform service activation one time for each new subscription.

For more information about service detection and activation, see [OID\_WWAN\_SERVICE\_ACTIVATION](https://msdn.microsoft.com/library/windows/hardware/ff569835).

 

 





