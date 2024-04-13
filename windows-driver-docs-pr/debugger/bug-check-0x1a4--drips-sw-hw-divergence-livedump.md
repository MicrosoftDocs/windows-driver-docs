---
title: Bug Check 0x1A4 DRIPS_SW_HW_DIVERGENCE_LIVEDUMP
description: The DRIPS_SW_HW_DIVERGENCE_LIVEDUMP live dump has a value of 0x000001A4.
keywords: ["Bug Check 0x1A4 DRIPS_SW_HW_DIVERGENCE_LIVEDUMP",  "DRIPS_SW_HW_DIVERGENCE_LIVEDUMP"]
ms.date: 05/25/2018
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIPS_SW_HW_DIVERGENCE_LIVEDUMP
api_type:
- NA
---

# Bug Check 0x1A4: DRIPS\_SW\_HW\_DIVERGENCE\_LIVEDUMP 

The DRIPS\_SW\_HW\_DIVERGENCE\_LIVEDUMP live dump has a value of 0x000001A4. 

Software and hardware DRIPS divergence exceeds default/programmed threshold time.

(This code can never be used for a real bugcheck; it is used to identify live dumps.)

## DRIPS\_SW\_HW\_DIVERGENCE\_LIVEDUMP Parameters


The following parameters are displayed on the blue screen.

Parameter | Description 
|---------|--------------|
1 | Time spent in software DRIPS in microseconds.
2 |  Time spent in hardware DRIPS in microseconds.
3 |  Reserved.
4 |  Reserved.

 
## See Also

[Kernel Live Dump Code Reference](bug-check-code-reference-live-dump.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
 




