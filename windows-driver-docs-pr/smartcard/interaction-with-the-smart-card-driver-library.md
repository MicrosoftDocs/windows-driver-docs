---
title: Interaction with the Smart Card Driver Library
description: Interaction with the Smart Card Driver Library
ms.assetid: 44cf41f4-bbff-4193-afad-6d4106ce50c3
keywords:
- IOCTLs WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Interaction with the Smart Card Driver Library


## <span id="_ntovr_interaction_with_the_smart_card_driver_library"></span><span id="_NTOVR_INTERACTION_WITH_THE_SMART_CARD_DRIVER_LIBRARY"></span>


The following figure shows how a reader driver interacts with the smart card driver library in order to process IOCTL requests that it receives from the resource manager:

![diagram illustrating how a reader driver interacts with the smart card driver library to process ioctl requests ](images/memnum3.png)

The following numbers correspond with the numbers in the previous figure. Starting with the number 1, the figure shows the steps that a reader driver must complete (together with the system-supplied driver library) to process an IOCTL request:

1.  The reader driver passes all IOCTL requests to the [**SmartcardDeviceControl (WDM)**](https://msdn.microsoft.com/library/windows/hardware/ff548939) driver library routine.

2.  If the parameters that the reader driver passes to [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) are incorrect, **SmartcardDeviceControl** returns with an error message. **SmartcardDeviceControl** returns without completing the IOCTL request. In this situation, the reader driver must complete the IOCTL request.

3.  If the parameters are valid, [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) processes the IOCTL request if it can.

4.  [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) checks whether the reader driver has a callback routine defined for the IOCTL request that it is processing. If the callback exists, **SmartcardDeviceControl** calls it.

5.  The callback routine calls all the driver library routines that are required to complete the processing of the IOCTL request.

6.  After processing the IOCTL request, the callback routine returns to [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939).

7.  [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) completes the IRP that carried the IOCTL.

8.  [**SmartcardDeviceControl**](https://msdn.microsoft.com/library/windows/hardware/ff548939) returns control to the reader-driver dispatch routine.

The smart card library synchronizes access to the reader driver. No two callback functions will be called at the same time. However, the event handling for card insertion and removal must be processed asynchronously.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Interaction%20with%20the%20Smart%20Card%20Driver%20Library%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




