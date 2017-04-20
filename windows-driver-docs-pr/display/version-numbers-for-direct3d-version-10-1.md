---
title: Version Numbers for Direct3D Version 10.1
description: Version Numbers for Direct3D Version 10.1
ms.assetid: a121900a-49e9-40f6-a3a6-d391e3bf1e37
keywords:
- Direct3D version 10.1 WDK display , version numbers
- version numbers WDK display
- version numbers WDK display , Direct3D version 10.1
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Version Numbers for Direct3D Version 10.1


Direct3D versions 10.0 and 10.1 supply \#defines that the user-mode display driver uses for versioning. The user-mode display driver must examine the **Interface** member of the [**D3D10DDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff541724), [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664), and [**D3D10DDIARG\_CALCPRIVATEDEVICESIZE**](https://msdn.microsoft.com/library/windows/hardware/ff541649) structures that the driver receives in calls to the [**OpenAdapter10**](https://msdn.microsoft.com/library/windows/hardware/ff568602), [**CreateDevice(D3D10)**](https://msdn.microsoft.com/library/windows/hardware/ff540635), and [**CalcPrivateDeviceSize**](https://msdn.microsoft.com/library/windows/hardware/ff538288) functions to determine the version of the Direct3D DDI that the Direct3D runtime supports. The most significant 16 bits of the **Interface** member is the number of the Direct3D DDI major version. For Direct3D versions 10.0 and 10.1, this number is 10. The least significant 16 bits of the **Interface** member is the Direct3D DDI minor version. This minor-version value is bumped every time a Direct3D DDI breaking change is introduced. This minor-version value can also be bumped artificially to signify a stronger version change. The following \#defines associate a Direct3D DDI minor version with a released version number (that is, D3D10\_0 == x, D3D10\_1 == y, where y &gt; x).

The user-mode display driver should only examine the most significant 16 bits of the **Version** member of the [**D3D10DDIARG\_OPENADAPTER**](https://msdn.microsoft.com/library/windows/hardware/ff541724), [**D3D10DDIARG\_CREATEDEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff541664), and [**D3D10DDIARG\_CALCPRIVATEDEVICESIZE**](https://msdn.microsoft.com/library/windows/hardware/ff541649) structures to determine when the Direct3D runtime is built. This value is manually bumped every time there is a non-breaking Direct3D DDI change. The driver might come to depend on each non-breaking DDI change over time. Therefore, the driver should ensure that the passed in DDI build version is greater than or equal to the \*\_BUILD\_VERSION of the current driver and fail out if the driver is incompatible (perhaps while also providing a registry workaround). The least significant 16 bits of the **Version** member is the DDI revision version. The least significant 16 bits of **Version** is typically used to special case the driver based on bugs that are present in the Direct3D API. The driver must succeed creation for all values. However, the driver can change behavior depending on certain values. You should compare with these values by using &gt;= because the numbers might rise arbitrarily due to runtime fixes. Also, you should not use "&gt; (previous broken version)" (rather than "&gt;= working version") because new revisions might appear that have version numbers between the two known numbers and do not contain the required fixes. The following \#defines are for Direct3D DDI versioning:

```
#define D3D10_DDI_MAJOR_VERSION 10
#define D3D10_0_DDI_MINOR_VERSION 1
#define D3D10_0_DDI_INTERFACE_VERSION ((D3D10_DDI_MAJOR_VERSION << 16) | D3D10_0_DDI_MINOR_VERSION)
#define D3D10_0_DDI_BUILD_VERSION 4
#define D3D10_0_DDI_VERSION_VISTA_GOLD                          ( ( 4 << 16 ) | 6000 )
#define D3D10_0_DDI_VERSION_VISTA_GOLD_WITH_LINKED_ADAPTER_QFE  ( ( 4 << 16 ) | 6008 )
#define D3D10_0_DDI_IS_LINKED_ADAPTER_QFE_PRESENT(Version)  (Version >= D3D10_0_DDI_VERSION_VISTA_GOLD_WITH_LINKED_ADAPTER_QFE)

#if D3D10DDI_MINOR_HEADER_VERSION >= 1
#define D3D10_1_DDI_MINOR_VERSION 2
#define D3D10_1_DDI_INTERFACE_VERSION ((D3D10_DDI_MAJOR_VERSION << 16) | D3D10_1_DDI_MINOR_VERSION)
#define D3D10_1_DDI_BUILD_VERSION 1
// Note: d3d10_1 doesn&#39;t currently ship on vista gold. // This definition is included for completeness in the 
// event that it does at some point in the future:
#define D3D10_1_DDI_VERSION_VISTA_GOLD                          ( ( 1 << 16 ) | 6000 )
#define D3D10_1_DDI_VERSION_VISTA_SP1                           ( ( 1 << 16 ) | 6008 )
#define D3D10_1_DDI_IS_LINKED_ADAPTER_QFE_PRESENT(Version)  (Version >= D3D10_1_DDI_VERSION_VISTA_SP1)

#define D3D10on9_DDI_MINOR_VERSION 0
#define D3D10on9_DDI_INTERFACE_VERSION ((D3D10_DDI_MAJOR_VERSION << 16) | D3D10on9_DDI_MINOR_VERSION)
#define D3D10on9_DDI_BUILD_VERSION 0
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Version%20Numbers%20for%20Direct3D%20Version%2010.1%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




