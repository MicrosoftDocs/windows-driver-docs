---
title: Mutexes in AVStream
author: windows-driver-content
description: Mutexes in AVStream
ms.assetid: 011edaaa-7449-41c3-8cfb-0d319901af8b
keywords:
- AVStream mutexes WDK
- mutexes WDK AVStream
- objects WDK AVStream
- hierarchy WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Mutexes in AVStream


## <a href="" id="ddk-mutexes-in-avstream-ksg"></a>


AVStream minidrivers synchronize access to objects by using mutexes and process control gates. For more information about process control gates, see [Flow Control Gates in AVStream](flow-control-gates-in-avstream.md).

AVStream has three different mutexes, all of which are directly accessible to the minidriver:

[Device Mutex in AVStream](device-mutex-in-avstream.md)

[Filter Control Mutex in AVStream](filter-control-mutex-in-avstream.md)

[Processing Mutex in AVStream](processing-mutex-in-avstream.md)

Use the device mutex to synchronize hierarchy objects from device to filter. Use the filter control mutex to synchronize objects from filter to pin.

Several AVStream API functions require that particular mutexes be held. Relevant function reference pages state if a specific mutex should be held when calling that particular function.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Mutexes%20in%20AVStream%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


