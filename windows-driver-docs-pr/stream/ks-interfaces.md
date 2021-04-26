---
title: KS Interfaces
description: KS Interfaces
keywords:
- interfaces WDK kernel streaming
- KSPIN_INTERFACE
- kernel streaming WDK , interfaces
- KS WDK , interfaces
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# KS Interfaces





An *Interface* is a descriptor parameter that defines how a pin communicates. The minidriver indicates which interfaces a pin supports by providing a pointer to an array of [**KSPIN\_INTERFACE**](/previous-versions/ff563537(v=vs.85)) structures in the relevant [**KSPIN\_DESCRIPTOR**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_descriptor) structure. KS then uses this information for determining potential connectivity and graph building.

Like mediums, interfaces are also described as a set and as an element of that set. The KSPIN\_INTERFACE structure defines a specific interface within an interface set.

The user-mode client then specifies the type of interface for a connection by using the **Interface** member of the relevant [**KSPIN\_CONNECT**](/windows-hardware/drivers/ddi/ks/ns-ks-kspin_connect) structure. The client passes this KSPIN\_CONNECT instance in a call to [**KsCreatePin**](/windows-hardware/drivers/ddi/ks/nf-ks-kscreatepin), which results in an IRP\_MJ\_CREATE being sent to the minidriver.

 

