---
title: ServiceInfo XML Example
description: ServiceInfo XML Example
ms.assetid: b2114044-ca4b-4c1e-ab2e-73f4f56142b5
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ServiceInfo XML Example


The following XML document uses the [ServiceInfo XML schema](serviceinfo-xml-schema.md) to specify the attributes of the Contoso Wireless service:

``` syntax
<DeviceInfo xmls="http://schemas.microsoft.com/windows/2010/05/DeviceMetadata/ServiceInfo">
    <ServiceCategoryList>
        <ServiceCategory>Network.MobileBroadband </ServiceCategory>
    </ServiceCategoryList>
    <ServiceName> </ServiceName>
    <ServiceDescription1>Fabrikam Wireless 3G network</ServiceDescription1>
    <ServiceDescription2></ServiceDescription2>
    <ServiceNumber>D4A5C6D5-8135-4A0D-9B9D-016F5D7D9F45  </ServiceNumber>
    <ServiceProvider>Contoso Wireless</ServiceProvider>
    <ServiceIcon>Contoso.ico</ServiceIcon>
    <ServiceSpecificExtension namespace="http://schemas.microsoft.com/windows/2010/12/DeviceMetadata/MobileBroadbandInfo">MobileBroadbandInfo.xml</ServiceSpecificExtension>
</ServiceInfo>
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_mb\p_mb%5D:%20ServiceInfo%20XML%20Example%20%20RELEASE:%20%281/18/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




