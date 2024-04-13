---
title: Management of IOCTL Requests in a Smart Card Reader Driver
description: Management of IOCTL Requests in a Smart Card Reader Driver
keywords:
- smart card drivers WDK , IOCTL request management
- IOCTLs WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.date: 04/20/2017
---

# Management of IOCTL Requests in a Smart Card Reader Driver


## <span id="_ntovr_management_of_ioctl_requests_in_a_smart_card_reader_driver"></span><span id="_NTOVR_MANAGEMENT_OF_IOCTL_REQUESTS_IN_A_SMART_CARD_READER_DRIVER"></span>


Management of IOCTL requests is centered in the smart card driver library. For the most part, smart card reader drivers can simply pass IOCTL requests to the [**SmartcardDeviceControl (WDM)**](/previous-versions/ff548939(v=vs.85)) library routine.

However, the standard set of IOCTL requests serviced by the smart card driver library are not always sufficient to fully support the capabilities of a reader device. Therefore, vendors might need to create their own IOCTL requests. Furthermore, some of the standard IOCTL requests might require additional processing after being handled by the driver library. For both of these reasons, with the driver architecture for smart card readers vendor-supplied reader drivers can implement a series of callback routines. These callback routines provide further processing of IOCTLs when needed.

The following sections explain how reader drivers manage IOCTL requests, how the callback routine mechanism works, and what a reader driver must do to initialize its callback routines.

In particular, the following topics are covered:

[Interaction with the Smart Card Driver Library](interaction-with-the-smart-card-driver-library.md)

[Smart Card Driver Library Callback Routines](smart-card-driver-library-callback-routines.md)

[Smart Card Callback Parameters](smart-card-callback-parameters.md)

 

