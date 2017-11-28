---
title: KSPROPSETID\_BdaPinControl
description: KSPROPSETID\_BdaPinControl
ms.assetid: f3c6ae83-d50f-49c8-a851-763f191f1932
---

# KSPROPSETID\_BdaPinControl


## <span id="ddk_kspropsetid_bdapincontrol_ks"></span><span id="DDK_KSPROPSETID_BDAPINCONTROL_KS"></span>


KSPROPSETID\_BdaPinControl is the BDA pin control property set. It is used to retrieve some BDA-specific information about a particular pin.

The following properties are available:

<span id="KSPROPERTY_BDA_PIN_ID"></span><span id="ksproperty_bda_pin_id"></span>[**KSPROPERTY\_BDA\_PIN\_ID**](ksproperty-bda-pin-id.md)  
Returns the BDA identifier (ID) for a pin.

<span id="KSPROPERTY_BDA_PIN_TYPE"></span><span id="ksproperty_bda_pin_type"></span>[**KSPROPERTY\_BDA\_PIN\_TYPE**](ksproperty-bda-pin-type.md)  
Returns the value that specifies the type of a pin.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

After the network provider creates a pin for a filter using a KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY request of the KSMETHODSETID\_BdaDeviceConfiguration method set, the network provider uses the properties of KSPROPSETID\_BdaPinControl to update its internal representation of the actual receiver topology.

Each pin factory of a BDA filter should support this property set. If a BDA minidriver does not define this property set, then the BDA support library adds support when the pin factory is created by either the **BdaCreatePin** or **BdaInitFilter** function.

The properties in this property set return information about a pin. Typically, pins of a filter are not required to intercept any of these properties. The BDA support library provides the **BdaPropertyGetPinControl** default function to handle this property set.

### <span id="see_also"></span><span id="SEE_ALSO"></span>See Also

[**BdaCreatePin**](https://msdn.microsoft.com/library/windows/hardware/ff556445), [**BdaInitFilter**](https://msdn.microsoft.com/library/windows/hardware/ff556464), [**BdaPropertyGetPinControl**](https://msdn.microsoft.com/library/windows/hardware/ff556483), [KSMETHODSETID\_BdaDeviceConfiguration](ksmethodsetid-bdadeviceconfiguration.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSPROPSETID_BdaPinControl%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




