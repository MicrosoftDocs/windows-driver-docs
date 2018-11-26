---
title: Preventing an Imbalance of Create and Close Notifications to a Driver
description: Preventing an Imbalance of Create and Close Notifications to a Driver
ms.assetid: e6678226-44d3-4b1d-a296-2017bc9c7c37
keywords:
- create-file notifications WDK UMDF
- cleanup-file notifications WDK UMDF
- close-file notifications WDK UMDF
- notifications WDK UMDF
- notifications WDK UMDF , preventing create and close imbalance
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Preventing an Imbalance of Create and Close Notifications to a Driver


[!include[UMDF 1 Deprecation](../umdf-1-deprecation.md)]

An upper UMDF driver can use the [**IWDFDeviceInitialize::AutoForwardCreateCleanupClose**](https://msdn.microsoft.com/library/windows/hardware/ff556971) method to control when the framework automatically forwards create-file, cleanup-file, and close-file notifications to the next lower driver in the device stack. However, because the upper driver sets **AutoForwardCreateCleanupClose** to automatically forward only on a device level and not on a per-file level, forwarding must be the same for all files for a device. The framework ensures this forwarding behavior for cleanup-file and close-file notifications. If the upper driver implements the [**IQueueCallbackCreate::OnCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556841) callback function, it must ensure that its forwarding behavior is the same for all create-file requests and is consistent with the forwarding behavior for cleanup-file and close-file notifications. Failing to do so might cause lower drivers to receive an unequal amount of calls to their **IQueueCallbackCreate::OnCreateFile** method and [**IFileCallbackCleanup::OnCleanupFile**](https://msdn.microsoft.com/library/windows/hardware/ff554905) and [**IFileCallbackClose::OnCloseFile**](https://msdn.microsoft.com/library/windows/hardware/ff554910) methods.

To prevent lower drivers from receiving an unequal amount of create-file and close-file notifications, the upper driver must ensure, in its [**IQueueCallbackCreate::OnCreateFile**](https://msdn.microsoft.com/library/windows/hardware/ff556841) callback function, that:

-   Its forwarding behavior is the same for all files for a device.

-   Its forwarding behavior is consistent with how it set the flag parameter of [**IWDFDeviceInitialize::AutoForwardCreateCleanupClose**](https://msdn.microsoft.com/library/windows/hardware/ff556971). That is:
    -   If the driver set the flag to **WdfTrue**, the driver must forward all the create-file requests down the device stack.
    -   If the driver set the flag to **WdfFalse**, the driver must not forward any of the create-file requests down the stack.
    -   If the driver set the flag to **WdfUseDefault** and:
        -   If the driver is a function driver, it must not forward any create-file requests down the stack.
        -   If the driver is a filter driver, it must forward all create-file requests down the stack.

In situations where the driver cannot forward a create-file request, the driver can still generate a new create-file request for lower drivers by calling the [**IWDFDevice::CreateWdfFile**](https://msdn.microsoft.com/library/windows/hardware/ff558828) method to create a new WDF file. The driver can then complete the original create-file request based on the results of the newly generated create-file request (that is, from the results of **CreateWdfFile**).

 

 





