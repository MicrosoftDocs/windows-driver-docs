---
title: KS Mediums
author: windows-driver-content
description: KS Mediums
ms.assetid: c94c738c-66c6-491b-9157-28cccf95af4d
keywords: ["mediums WDK kernel streaming", "KSPIN_MEDIUM", "kernel streaming WDK , mediums", "KS WDK , mediums"]
---

# KS Mediums


## <a href="" id="ddk-ks-mediums-ksg"></a>


A *Medium* defines a type of communication bus. The minidriver indicates which mediums a pin supports by providing a pointer to an array of [**KSPIN\_MEDIUM**](https://msdn.microsoft.com/library/windows/hardware/ff563538) structures in the relevant [**KSPIN\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/hardware/ff563533) structure. A KSPIN\_MEDIUM identifies a specific connection on a communication bus.

Clients specify the medium to use for a connection by setting the **Medium** member in the [**KSPIN\_CONNECT**](https://msdn.microsoft.com/library/windows/hardware/ff563531) structure that they provide in a call to [**KsCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff561652).

Clients request a list of mediums supported by a filter or pin by using the [**KSPROPERTY\_PIN\_MEDIUMS**](https://msdn.microsoft.com/library/windows/hardware/ff565202) property.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KS%20Mediums%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


