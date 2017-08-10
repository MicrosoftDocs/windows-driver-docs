---
title: Power Management Minor IRPs
author: windows-driver-content
description: Power Management Minor IRPs
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: 8af0609f-168b-4455-aae8-1a3c9e40ed47
---

# Power Management Minor IRPs


## <a href="" id="ddk-power-management-minor-irps-dr"></a>


All power IRPs have the major code [**IRP\_MJ\_POWER**](irp-mj-power.md) and one of the following minor codes, indicating a specific power management request:

[**IRP\_MN\_POWER\_SEQUENCE**](irp-mn-power-sequence.md)

[**IRP\_MN\_QUERY\_POWER**](irp-mn-query-power.md)

[**IRP\_MN\_SET\_POWER**](irp-mn-set-power.md)

[**IRP\_MN\_WAIT\_WAKE**](irp-mn-wait-wake.md)

This section provides reference information for the individual IRPs in alphabetical order. For more information about when the IRPs are sent and how drivers should handle them, see [Power Management](https://msdn.microsoft.com/library/windows/hardware/ff547131). The Power Management section also includes a general introduction to power management and terminology.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Power%20Management%20Minor%20IRPs%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


