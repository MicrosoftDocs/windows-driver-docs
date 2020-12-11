---
title: Overview of the Power Management Framework
description: Starting with Windows 8, the run-time power management framework (PoFx) supports power and clock management at the component (or subdevice) level.
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# Overview of the Power Management Framework


Starting with Windows 8, the run-time power management framework (PoFx) supports power and clock management at the component (or subdevice) level. A device driver registers with PoFx to independently manage power usage in the individual components in a device. PoFx provides the fine-grained control necessary to extend the time that a Windows portable computer, tablet, phone, or other mobile device can run on a battery charge. PoFx reduces power usage in a way that maintains the appearance of a mobile device that is always on and always connected.

A component, or subdevice, is a functional hardware unit in a device that can be turned on or switched to a low-power state independently of the other components in the same device. For example, an audio device might have separate components for playback and recording whose power states can be managed independently of each other. If the playback component is being used, but the recording component is idle, the recording component can be switched to a low-power state without interfering with the activity of the playback component.


 

 




