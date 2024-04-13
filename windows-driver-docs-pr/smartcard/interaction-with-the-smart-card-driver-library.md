---
title: Interaction with the Smart Card Driver Library
description: Interaction with the Smart Card Driver Library
keywords:
- IOCTLs WDK smart card
- vendor-supplied drivers WDK smart card , IOCTL request management
ms.date: 04/20/2017
---

# Interaction with the Smart Card Driver Library


## <span id="_ntovr_interaction_with_the_smart_card_driver_library"></span><span id="_NTOVR_INTERACTION_WITH_THE_SMART_CARD_DRIVER_LIBRARY"></span>


The following figure shows how a reader driver interacts with the smart card driver library in order to process IOCTL requests that it receives from the resource manager:

![diagram illustrating how a reader driver interacts with the smart card driver library to process ioctl requests .](images/memnum3.png)

The following numbers correspond with the numbers in the previous figure. Starting with the number 1, the figure shows the steps that a reader driver must complete (together with the system-supplied driver library) to process an IOCTL request:

1.  The reader driver passes all IOCTL requests to the [**SmartcardDeviceControl (WDM)**](/previous-versions/ff548939(v=vs.85)) driver library routine.

2.  If the parameters that the reader driver passes to [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)) are incorrect, **SmartcardDeviceControl** returns with an error message. **SmartcardDeviceControl** returns without completing the IOCTL request. In this situation, the reader driver must complete the IOCTL request.

3.  If the parameters are valid, [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)) processes the IOCTL request if it can.

4.  [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)) checks whether the reader driver has a callback routine defined for the IOCTL request that it is processing. If the callback exists, **SmartcardDeviceControl** calls it.

5.  The callback routine calls all the driver library routines that are required to complete the processing of the IOCTL request.

6.  After processing the IOCTL request, the callback routine returns to [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)).

7.  [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)) completes the IRP that carried the IOCTL.

8.  [**SmartcardDeviceControl**](/previous-versions/ff548939(v=vs.85)) returns control to the reader-driver dispatch routine.

The smart card library synchronizes access to the reader driver. No two callback functions will be called at the same time. However, the event handling for card insertion and removal must be processed asynchronously.

 

