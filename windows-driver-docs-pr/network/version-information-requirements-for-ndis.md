---
title: Version Information Requirements for NDIS
description: Version Information Requirements for NDIS
ms.assetid: b2850077-271f-4bb6-8710-ae9415ad5eda
---

# Version Information Requirements for NDIS


## <a href="" id="ddk-version-information-requirements-for-ndis-ng"></a>


NDIS supports various header version information requirements that guarantee consistent behavior between NDIS versions. To support header version information, NDIS has the following responsibilities:

-   Handles structures with lower revisions. That is, NDIS checks the header information and interprets the structure based upon the revision information in the header.

-   Fails a function call and returns an appropriate error code if a driver uses an incorrect structure revision. For example, NDIS fails the function call if an NDIS 6.30 driver uses Xxx\_REVISION\_1 structures when there is an NDIS 6.30 Xxx\_REVISION\_2 structure.

## Related topics


[NDIS Versions in Network Drivers](ndis-versions-in-network-drivers.md)

[Specifying NDIS Version Information](specifying-ndis-version-information.md)

 

 






