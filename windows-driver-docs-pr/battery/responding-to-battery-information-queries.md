---
title: Responding to Battery Information Queries
description: Responding to Battery Information Queries
ms.assetid: 5d215ff8-d41f-471e-bc54-570a94f3c23f
keywords:
- battery information WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Responding to Battery Information Queries


## <span id="ddk_responding_to_battery_information_queries_dg"></span><span id="DDK_RESPONDING_TO_BATTERY_INFORMATION_QUERIES_DG"></span>


The battery class driver calls the [*BatteryMiniQueryInformation*](https://msdn.microsoft.com/library/windows/hardware/ff536273) routine to get a variety of information about the current battery. This routine is declared as follows:

```cpp
typedef 
NTSTATUS
(*BCLASS_QUERY_INFORMATION)(
    IN PVOID Context,
    IN ULONG BatteryTag,
    IN BATTERY_QUERY_INFORMATION_LEVEL Level,
    IN LONG AtRate OPTIONAL,
    OUT PVOID Buffer,
    IN ULONG BufferLength,
    OUT PULONG ReturnedLength
    );
```

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the [**BATTERY\_MINIPORT\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff536287) structure at device initialization. The *BatteryTag* parameter is a value previously returned by [*BatteryMiniQueryTag*](https://msdn.microsoft.com/library/windows/hardware/ff536275).

The *Level* parameter specifies the kind of information requested. The miniclass driver formats the information as a [**BATTERY\_INFORMATION**](https://msdn.microsoft.com/library/windows/hardware/ff536283) structure and returns it at the address supplied by *Buffer*, with a pointer to its length in *ReturnedLength*.

A miniclass driver should be prepared to handle requests for the following:

-   Battery capabilities, chemistry, capacity, low-capacity alert levels, and reserve charge

-   Temperature, in tenths of a degree Kelvin

-   Estimated remaining run time, in seconds

-   Device name

-   Manufacturer's battery model name

-   Date of manufacture

-   Unique ID

-   Serial number

Some batteries are not capable of reporting all this information. A miniclass driver should return STATUS\_INVALID\_DEVICE\_REQUEST for any information that its device cannot supply.

 

 




