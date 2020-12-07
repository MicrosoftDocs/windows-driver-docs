---
title: KSPROPSETID\_BdaPinControl
description: KSPROPSETID\_BdaPinControl
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSPROPSETID\_BdaPinControl


## <span id="ddk_kspropsetid_bdapincontrol_ks"></span><span id="DDK_KSPROPSETID_BDAPINCONTROL_KS"></span>


KSPROPSETID\_BdaPinControl is the BDA pin control property set. It is used to retrieve some BDA-specific information about a particular pin.

The following properties are available:

<span id="KSPROPERTY_BDA_PIN_ID"></span><span id="ksproperty_bda_pin_id"></span>[**KSPROPERTY\_BDA\_PIN\_ID**](ksproperty-bda-pin-id.md)  
Returns the BDA identifier (ID) for a pin.

<span id="KSPROPERTY_BDA_PIN_TYPE"></span><span id="ksproperty_bda_pin_type"></span>[**KSPROPERTY\_BDA\_PIN\_TYPE**](ksproperty-bda-pin-type.md)  
Returns the value that specifies the type of a pin.

### Comments

After the network provider creates a pin for a filter using a KSMETHOD\_BDA\_CREATE\_PIN\_FACTORY request of the KSMETHODSETID\_BdaDeviceConfiguration method set, the network provider uses the properties of KSPROPSETID\_BdaPinControl to update its internal representation of the actual receiver topology.

Each pin factory of a BDA filter should support this property set. If a BDA minidriver does not define this property set, then the BDA support library adds support when the pin factory is created by either the **BdaCreatePin** or **BdaInitFilter** function.

The properties in this property set return information about a pin. Typically, pins of a filter are not required to intercept any of these properties. The BDA support library provides the **BdaPropertyGetPinControl** default function to handle this property set.

### See Also

[**BdaCreatePin**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdacreatepin), [**BdaInitFilter**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdainitfilter), [**BdaPropertyGetPinControl**](/windows-hardware/drivers/ddi/bdasup/nf-bdasup-bdapropertygetpincontrol), [KSMETHODSETID\_BdaDeviceConfiguration](ksmethodsetid-bdadeviceconfiguration.md)

 

