---
title: Flow Control Gates in AVStream
description: Flow Control Gates in AVStream
ms.assetid: c5592f92-a432-44e3-afe0-60fcf917a443
keywords:
- AVStream logic gates WDK
- logic gates WDK AVStream
- gates WDK AVStream
- AND gate WDK AVStream
- KSGATE
- flow control gates WDK AVStream
- processing control gates WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Flow Control Gates in AVStream





AVStream uses logic gates as a control flow mechanism. Each logic gate is represented by a [**KSGATE**](https://msdn.microsoft.com/library/windows/hardware/ff562566) structure.

AVStream initializes each filter or pin with a single AND gate. A minidriver can then use this mechanism to determine when that specific object can process data. To retrieve the processing control gate for a pin, the minidriver calls [**KsPinGetAndGate**](https://msdn.microsoft.com/library/windows/hardware/ff563502). To retrieve the processing control gate for a filter, call [**KsFilterGetAndGate**](https://msdn.microsoft.com/library/windows/hardware/ff562542).

To create new logic gates, the minidriver calls [**KsGateInitializeAnd**](https://msdn.microsoft.com/library/windows/hardware/ff562574) or [**KsGateInitializeOr**](https://msdn.microsoft.com/library/windows/hardware/ff562576). You can use the output of one gate as an input to another gate, thereby forwarding state transitions. To do this, supply a *NextOrGate* or *NextAndGate* parameter in these calls.

To close an existing input to a logic gate, you can call [**KsGateTurnInputOff**](https://msdn.microsoft.com/library/windows/hardware/ff562589). The minidriver might make this call to stop and close an active pin, or to suspend processing for an indefinite period of time.

Similarly, call [**KsGateTurnInputOn**](https://msdn.microsoft.com/library/windows/hardware/ff562591) to open an existing input to a specific gate.

When a thread is ready to process, it attempts to capture the *on* input of the AND gate that controls processing for the processing object. To do this, the minidriver calls [**KsGateCaptureThreshold**](https://msdn.microsoft.com/library/windows/hardware/ff562571).

If the AND gate is open, AVStream turns off an input to the gate, and processing begins. Since the gate is now closed during processing, no other thread can capture the *on* input of the gate. Only one thread can process data at a time.

To check the status of a gate without modifying it, the minidriver can call [**KsGateGetStateUnsafe**](https://msdn.microsoft.com/library/windows/hardware/ff562572). Note, however, that this function does not handle synchronization.

To delete a logic gate, call [**KsGateTerminateAnd**](https://msdn.microsoft.com/library/windows/hardware/ff562586) or [**KsGateTerminateOr**](https://msdn.microsoft.com/library/windows/hardware/ff562588). The gate that you are deleting must be at the beginning of a gate chain.

To attach a pin as an input to a logic gate, and then to connect the same logic gate as input to a filter's AND gate, call [**KsPinAttachAndGate**](https://msdn.microsoft.com/library/windows/hardware/ff563491) or [**KsPinAttachOrGate**](https://msdn.microsoft.com/library/windows/hardware/ff563492).

### Determining Gate Status

For an AND gate, the value of the **Count** member of the KSGATE structure is one minus the number of *off* inputs:

Count = 1 - (number of *off* inputs)

If this value is less than or equal to zero, the gate is closed. If this value is greater than zero, the gate is open.

For an OR gate, the value of the **Count** member of KSGATE is the number of *on* inputs to the gate:

Count = (number of *on* inputs)

If this value is equal to zero, the gate is closed. If **Count** is greater than zero, the gate is open.

AND gates have a valid **Count** range of one or less; OR gates have a valid **Count** range of zero or greater. Do not set **Count** to invalid values; *AVStream does not verify that a minidriver has set the gate to a valid state.*

 

 




