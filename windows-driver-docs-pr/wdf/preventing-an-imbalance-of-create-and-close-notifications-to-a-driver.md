---
title: Preventing an Imbalance of Create and Close Notifications to a Driver
description: Preventing an Imbalance of Create and Close Notifications to a Driver
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: e6678226-44d3-4b1d-a296-2017bc9c7c37
keywords: ["create file notifications WDK UMDF", "cleanup file notifications WDK UMDF", "close file notifications WDK UMDF", "notifications WDK UMDF", "notifications WDK UMDF preventing create and close imbalance"]
---

# Preventing an Imbalance of Create and Close Notifications to a Driver


\[This topic applies to UMDF 1.*x*.\]

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Preventing%20an%20Imbalance%20of%20Create%20and%20Close%20Notifications%20to%20a%20Driver%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




