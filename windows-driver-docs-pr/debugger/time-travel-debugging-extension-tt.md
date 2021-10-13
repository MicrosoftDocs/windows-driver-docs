---
title: Time Travel Debugging Extension !tt Command 
description: The !tt time travel debugger extension that allows you to navigate forward and backwards in time.
ms.date: 01/22/2020
ms.localizationpriority: medium
---

# !tt (time travel)

![Small time travel logo showing clock.](images/ttd-time-travel-debugging-logo.png)

The !tt (time travel) debugger extension that allows you to navigate forward and backwards in time.

## !tt navigation commands

Use the !tt extension to navigate forward or backwards in time, by traveling to a given position in the trace. 

```dbgcmd
!tt [position]
```

## <span id="ddk__analyze_dbg"></span><span id="DDK__ANALYZE_DBG"></span>Parameters

**position**

Provide a time position in any of the following formats to travel to that point in time.
           
- If {position} is a decimal number between 0 and 100, it travels to approximately that percent into the trace. For example:
    - !tt 0                   - Time travel to the beginning of the trace
    - !tt 50                  - Time travel to halfway through the trace
    - !tt 100                 - Time travel to the end of the trace
 

- If {position} is #:#, where # are a hexadecimal numbers, it travels to that position. If the number after : is omitted, it defaults to zero.
    - !tt 1A0:                - Time travel to position 1A0:0
    - !tt 1A0:0               - Time travel to position 1A0:0
    - !tt 1A0:12F             - Time travel to position 1A0:12F


   > [!NOTE]
   > Traces use a two-part instruction position that references a specific position reference in the trace, for example 12:0. or 15:7. The two elements are hexadecimal numbers defined as described here.
   >
   > xx:yy
   > 
   > xx- the first element is the sequencing number, which corresponds to a sequencing event.
   >
   > yy - the second element is a step count, which corresponds roughly to the instruction count since the sequencing event.

### <span id="DLL"></span><span id="dll"></span>DLL

ttdext.dll

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

This extension only works with time travel traces. For more information about time travel, see [Time Travel Debugging - Overview](time-travel-debugging-overview.md).

## See Also

[Time Travel Debugging - Overview](time-travel-debugging-overview.md)
