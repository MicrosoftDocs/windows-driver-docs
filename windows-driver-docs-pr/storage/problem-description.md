---
title: Problem Description
description: Problem Description
ms.assetid: 5e811011-9848-43fc-969d-abdf1ad45acf
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Problem Description


In Windows computer systems, crash dump and hibernation support is provided by the crash dump driver that has support from special storage drivers, both port and miniport. When the system crashes, dump data is written to the disk using these special sets of drivers instead of the typical storage stack. These drivers write the data without using file system or volume manager drivers and they did not previously support adding any drivers in the crash dump stack.

 

 




