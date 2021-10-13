---
title: Versioned Interfaces
description: Versioned Interfaces
keywords:
- NDIS WDK , versioning
- versioning WDK networking
- NDIS WDK , backward compatibility
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Versioned Interfaces





NDIS 6.0 supports versioning for key structures. Also, many former function parameters are moved to structures. Moving the function parameters to versioned structures allows the function parameters to be changed in later NDIS versions without changing the function interface.

Versioned structures contain a header that specifies the version of the structure. If the set of function parameters or other structure members are changed, the structure and its version are updated.

This versioning simplifies backward compatibility and extends the life of NDIS 6.0 and later drivers. Also, NDIS drivers can support more than one version of NDIS.

For more information, see [**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/objectheader/ns-objectheader-ndis_object_header).

 

