---
title: Porting NDIS 6.x drivers to NDIS 6.70
description: For NDIS protocol, filter, and intermediate drivers, NDIS 6.70 is substantially the same as NDIS 6.60. For detailed information about new features for NDIS 6.70, see Introduction to NDIS 6.70.
ms.date: 06/01/2017
ms.localizationpriority: medium
---

# Porting NDIS 6.x drivers to NDIS 6.70

For NDIS miniport, protocol, filter, and intermediate drivers, NDIS 6.70 is substantially the same as NDIS 6.60. Starting in NDIS 6.70, however, NDIS driver developers can also write a NIC driver using the new Network Adapter WDF Class Extension, a.k.a. [NetAdapterCx](../netcx/index.md). To port an NDIS 6.x miniport driver to NetAdapterCx, see [Porting NDIS miniport drivers to NetAdapterCx](../netcx/porting-ndis-miniport-drivers-to-netadaptercx.md).

For detailed information about new features for NDIS 6.70, including implementation and compilation details specific to this version of NDIS, see [Introduction to NDIS 6.70](introduction-to-ndis-6-70.md).

If you are porting an NDIS 6.x miniport, protocol, filter, or intermediate driver to NDIS 6.70, you should be familiar with the changes to each version between your driver's version and 6.70. For more information about previous NDIS 6.x versions, see the following topics:

- [Introduction to NDIS 6.60](introduction-to-ndis-6-60.md)
- [Introduction to NDIS 6.50](introduction-to-ndis-6-50.md)
- [Introduction to NDIS 6.40](introduction-to-ndis-6-40.md)
- [Introduction to NDIS 6.30](introduction-to-ndis-6-30.md)
- [Introduction to NDIS 6.20](introduction-to-ndis-6-20.md)
- [Introduction to NDIS 6.1](introduction-to-ndis-6-1.md)
- [Introduction to NDIS 6.0](introduction-to-ndis-6-0.md)

