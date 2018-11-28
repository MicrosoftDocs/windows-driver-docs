---
title: Power and State Changes in AVStream
description: Power and State Changes in AVStream
ms.assetid: f62f4306-97c0-40fe-89ec-d08eb18988c9
keywords:
- AVStream WDK , power and state changes
- power changes WDK , AVStream
- state changes WDK , AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Power and State Changes in AVStream


When AVStream receives an [**IRP\_MN\_SET\_POWER**](https://msdn.microsoft.com/library/windows/hardware/ff551744) request, it calls a minidriver's [*AVStrMiniDeviceSetPower*](https://msdn.microsoft.com/library/windows/hardware/ff554309) callback routine, if the minidriver has provided one.

When AVStream receives a set request of the [**KSPROPERTY\_CONNECTION\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff565110) property, it calls a minidriver's [*AVStrMiniPinSetDeviceState*](https://msdn.microsoft.com/library/windows/hardware/ff556359) callback routine, if the minidriver has provided one.

When the system wakes from a sleep state, AVStream may call a minidriver's *AVStrMiniPinSetDeviceState* and *AVStrMiniDeviceSetPower* callback routines in the reverse of the expected order. For example, *AVStrMiniPinSetDeviceState* may be called *beforeAVStrMiniDeviceSetPower*.

As a result, the driver *must be prepared to handle such a reversal of the expected callback order*.

This reversal does not happen when the system is powered down into a sleep state. On power down, these two callback routines always occur in the expected order. For example, *AVStrMiniPinSetDeviceState* is always called before *AVStrMiniDeviceSetPower*.

If this reversal occurs, the entire sequence looks like this:

First, the power down sequence occurs:

1.  *AVStrMiniPinSetDeviceState* is called with a request to change device state from **KSSTATE\_RUN** to KSSTATE\_PAUSE.

2.  *AVStrMiniDeviceSetPower* is called with a request to change power state from D0 to D2/D3.

3.  At this point, the system is in a sleep state.

4.  Next, the power up sequence occurs:

5.  *AVStrMiniDeviceSetPower* is called with a request to change power state from D2/D3 to D0.

6.  *AVStrMiniPinSetDeviceState* is called with a request to change device state from **KSSTATE\_PAUSE** to KSSTATE\_RUN.

In this scenario, steps 5 and 6 are the steps that are reversed from the expected order.

Additionally, when an application is streaming and the system initiates a power down sequence, a capture graph that is running is always placed in a pause state. If the graph was already stopped, it remains stopped.

 

 




