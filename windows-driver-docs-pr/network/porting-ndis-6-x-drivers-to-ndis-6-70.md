---
title: Porting NDIS 6.x drivers to NDIS 6.70
description: For NDIS protocol, filter, and intermediate drivers, NDIS 6.70 is substantially the same as NDIS 6.60. For detailed information about new features for NDIS 6.70, see Introduction to NDIS 6.70.
ms.assetid: DB099908-E8EF-4D4B-95FF-9B17702D4A7B
ms.author: windowsdriverdev
ms.date: 06/01/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20Planning%20your%20APN%20database%20submission%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")