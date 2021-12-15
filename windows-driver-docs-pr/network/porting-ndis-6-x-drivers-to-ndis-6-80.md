---
title: Porting NDIS 6.x drivers to NDIS 6.80
description: For NDIS protocol, filter, and intermediate drivers, NDIS 6.80 is substantially the same as NDIS 6.60. For detailed information about new features for NDIS 6.80, see Introduction to NDIS 6.80.
ms.date: 07/05/2017
---

# Porting NDIS 6.x drivers to NDIS 6.80

For NDIS miniport, protocol, filter, and intermediate drivers, NDIS 6.80 is substantially the same as NDIS 6.70. For NIC drivers, the NetAdapter class extension (NetAdapterCx) has been updated to from version 1.0 in NDIS 6.70 to version 1.1 in NDIS 6.80. To port an NDIS 6.x miniport driver to NetAdapterCx, see [Porting NDIS miniport drivers to NetAdapterCx](../netcx/porting-ndis-miniport-drivers-to-netadaptercx.md).

For detailed information about new features for NDIS 6.80, including implementation and compilation details specific to this version of NDIS, see [Introduction to NDIS 6.80](introduction-to-ndis-6-80.md).

If you are porting an NDIS 6.x miniport, protocol, filter, or intermediate driver to NDIS 6.80, you should be familiar with the changes to each version between your driver's version and 6.80. For more information about previous NDIS 6.x versions, see the following topics:

- [Introduction to NDIS 6.70](introduction-to-ndis-6-70.md)
- [Introduction to NDIS 6.60](introduction-to-ndis-6-60.md)
- [Introduction to NDIS 6.50](introduction-to-ndis-6-50.md)
- [Introduction to NDIS 6.40](introduction-to-ndis-6-40.md)
- [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md)
- [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md)
- [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md)
- [Introduction to NDIS 6.0](introduction-to-ndis-6-0.md)

