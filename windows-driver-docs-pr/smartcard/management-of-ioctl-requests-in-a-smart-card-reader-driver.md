---
title: Management of IOCTL Requests in a Smart Card Reader Driver
description: Management of IOCTL Requests in a Smart Card Reader Driver
ms.assetid: 610476fc-59e7-4981-9afa-20ed7cc697c1
keywords:
- smart card drivers WDK , IOCTL request management
- IOCTLs WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Management of IOCTL Requests in a Smart Card Reader Driver


## <span id="_ntovr_management_of_ioctl_requests_in_a_smart_card_reader_driver"></span><span id="_NTOVR_MANAGEMENT_OF_IOCTL_REQUESTS_IN_A_SMART_CARD_READER_DRIVER"></span>


Management of IOCTL requests is centered in the smart card driver library. For the most part, smart card reader drivers can simply pass IOCTL requests to the [**SmartcardDeviceControl (WDM)**](https://msdn.microsoft.com/library/windows/hardware/ff548939) library routine.

However, the standard set of IOCTL requests serviced by the smart card driver library are not always sufficient to fully support the capabilities of a reader device. Therefore, vendors might need to create their own IOCTL requests. Furthermore, some of the standard IOCTL requests might require additional processing after being handled by the driver library. For both of these reasons, with the driver architecture for smart card readers vendor-supplied reader drivers can implement a series of callback routines. These callback routines provide further processing of IOCTLs when needed.

The following sections explain how reader drivers manage IOCTL requests, how the callback routine mechanism works, and what a reader driver must do to initialize its callback routines.

In particular, the following topics are covered:

[Interaction with the Smart Card Driver Library](interaction-with-the-smart-card-driver-library.md)

[Smart Card Driver Library Callback Routines](smart-card-driver-library-callback-routines.md)

[Smart Card Callback Parameters](smart-card-callback-parameters.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[smartcrd\smartcrd]:%20Management%20of%20IOCTL%20Requests%20in%20a%20Smart%20Card%20Reader%20Driver%20%20RELEASE:%20%287/20/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




