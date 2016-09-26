---
title: Button State Transitions
description: Button State Transitions
ms.assetid: EA2FFEBE-3805-4370-9E68-9597D42FC889
---

# Button State Transitions


Certain button state transitions are expected from devices. Devices that support hovering must include the **In-range** and **Tip** usages in their descriptor.

The transitions for these devices are listed in the following table.

| Event                                                     | Button Status         |
|-----------------------------------------------------------|-----------------------|
| Device comes in range                                     | In-range=on; Tip=off  |
| Device comes in contact with the surface of the digitizer | In-range=on; Tip=on   |
| Contact is moving on the digitizer surface                | In-range=on; Tip=on   |
| Contact is lifted off of the digitizer surface            | In-range=off; Tip=off |
| Contact goes out of range                                 | In-range=off; Tip=off |

 

**Note**  The X and Y coordinates reported for the “out of range” event must match those reported for the last “in range” event before the “out of range” event was detected. For the case when the device goes “out of range” very quickly, where “up” and “out of range” are detected in the same scan, both events or packets need to be reported. One for “up”, and another for “out of range”.

 

Devices that do not support hovering do not need to include the **In-range** usage in their descriptor. The transitions for these devices are listed in the following table.

| Event                                                     | Button Status         |
|-----------------------------------------------------------|-----------------------|
| Device comes in contact with the surface of the digitizer | Tip=on                |
| Contact is moving on the digitizer surface                | In-range=on; Tip=on   |
| Contact is lifted off of the digitizer surface            | In-range=off; Tip=off |

 

**Note**  The X and Y coordinates reported when the finger is lifted off the digitizer surface must be the same as those reported for the last “move” packet detected.

 

The transitions for pen devices that support the Eraser and Inverted usages are given in the following table. These are the only valid states. Any other state may be rejected by Windows.

| Event                                                       | Button Status                                   |
|-------------------------------------------------------------|-------------------------------------------------|
| Tip end of pen is hovering                                  | In-range=on; Tip=off; Inverted=off; Eraser=off  |
| Tip end of pen is on the surface                            | In-range=on; Tip=on; Inverted=off; Eraser=off   |
| Tip end of pen is off the surface and hovering again        | In-range=on; Tip=off; Inverted=off; Eraser=off  |
| Tip goes out of range                                       | In-range=off; Tip=off; Inverted=off; Eraser=off |
| Eraser end of the pen is hovering                           | In-range=on; Tip=off; Inverted=on; Eraser=off   |
| Eraser end of the pen is on the surface                     | In-range=on; Tip=off; Inverted=off; Eraser=on   |
| Eraser end of the pen is off the surface and hovering again | In-range=on; Tip=off; Inverted=on; Eraser=off   |
| Eraser goes out of range                                    | In-range=off; Tip=off; Inverted=off; Eraser=off |

 

 

 




