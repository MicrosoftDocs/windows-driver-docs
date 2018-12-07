---
title: Feature Description
description: Feature Description
ms.assetid: 19c1378d-f8d8-42a2-9776-4f5bfdb9e39e
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Feature Description


The crash dump driver provides a new interface to add filter drivers to the crash dump stack. This interface does not follow any standard filter driver model. Instead, it exposes a proprietary interface that must be used in order to load a driver into the crash dump stack.

Crash dump filter drivers can be made part of the dump stack by adding the service name in a registry key. The crash dump driver loads these drivers when the drivers in the dump stack are loaded. A filter driver is loaded as part of both the hibernation and crash dump stacks. These filter drivers should supply a list of predefined callback routines that will be called during hibernation and crash dump.

The filter model does not allow filter drivers to be loaded only in either the hibernation or crash dump stack. After the service name is added to the filter driver list, the list will be loaded in both stacks. When the callback routines are called, a parameter is passed to indicate the callback reason. The filter driver can then determine what to do based on this parameter.

 

 




