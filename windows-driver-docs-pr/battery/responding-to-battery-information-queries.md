---
title: Responding to Battery Information Queries
description: Responding to Battery Information Queries
keywords:
- battery information WDK
ms.date: 04/20/2017
---

# Responding to Battery Information Queries

The battery class driver calls the [*BatteryMiniQueryInformation*](/windows/win32/api/batclass/nc-batclass-bclass_query_information_callback) routine to get a variety of information about the current battery. This routine is declared as follows:

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

The *Context* parameter is a pointer to the context area that is allocated by the miniclass driver and passed to the class driver in the [**BATTERY\_MINIPORT\_INFO**](/windows/win32/api/batclass/ns-batclass-battery_miniport_info) structure at device initialization. The *BatteryTag* parameter is a value previously returned by [*BatteryMiniQueryTag*](/windows/win32/api/batclass/nc-batclass-bclass_query_tag_callback).

The *Level* parameter specifies the kind of information requested. The miniclass driver formats the information as a [**BATTERY\_INFORMATION**](/previous-versions/ff536283(v=vs.85)) structure and returns it at the address supplied by *Buffer*, with a pointer to its length in *ReturnedLength*.

A miniclass driver should be prepared to handle requests for the following:

- Battery capabilities, chemistry, capacity, low-capacity alert levels, and reserve charge

- Temperature, in tenths of a degree Kelvin

- Estimated remaining run time, in seconds

- Device name

- Manufacturer's battery model name

- Date of manufacture

- Unique ID

- Serial number

Some batteries are not capable of reporting all this information. A miniclass driver should return STATUS\_INVALID\_DEVICE\_REQUEST for any information that its device cannot supply.
