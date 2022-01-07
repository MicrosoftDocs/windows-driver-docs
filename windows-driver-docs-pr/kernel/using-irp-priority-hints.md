---
title: Using IRP Priority Hints
description: Using IRP Priority Hints
ms.date: 10/17/2018
---

# Using IRP Priority Hints


An *IRP priority hint* is an [**IO\_PRIORITY\_HINT**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_io_priority_hint) value that is associated with an IRP. IRP priority hints provide a simple hinting mechanism to indicate the relative importance of IRPs. A driver can use the priority hint for an IRP when choosing the order that the IRP is processed. IRP priority hints are available on Windows Vista and later operating systems.

For more information about IRP priority hints, see the [I/O Prioritization in Windows Vista](https://go.microsoft.com/fwlink/p/?linkid=67877) white paper.

 

