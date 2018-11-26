---
title: Mutexes in AVStream
description: Mutexes in AVStream
ms.assetid: 011edaaa-7449-41c3-8cfb-0d319901af8b
keywords:
- AVStream mutexes WDK
- mutexes WDK AVStream
- objects WDK AVStream
- hierarchy WDK AVStream
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mutexes in AVStream





AVStream minidrivers synchronize access to objects by using mutexes and process control gates. For more information about process control gates, see [Flow Control Gates in AVStream](flow-control-gates-in-avstream.md).

AVStream has three different mutexes, all of which are directly accessible to the minidriver:

[Device Mutex in AVStream](device-mutex-in-avstream.md)

[Filter Control Mutex in AVStream](filter-control-mutex-in-avstream.md)

[Processing Mutex in AVStream](processing-mutex-in-avstream.md)

Use the device mutex to synchronize hierarchy objects from device to filter. Use the filter control mutex to synchronize objects from filter to pin.

Several AVStream API functions require that particular mutexes be held. Relevant function reference pages state if a specific mutex should be held when calling that particular function.

 

 




