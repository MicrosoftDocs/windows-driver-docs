---
title: Writing WIA Item Properties by an Application
description: Writing WIA Item Properties by an Application
ms.date: 04/20/2017
---

# Writing WIA Item Properties by an Application





When a WIA application writes to a WIA property (and updates the value stored in the property), the WIA service gives the WIA minidriver the opportunity to validate incoming values by calling the [**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties) method. The WIA minidriver compares the incoming values to any current values by reading the properties in its own driver item tree. The WIA service library provides functions for accessing these values.

The **IWiaMiniDrv::drvValidateItemProperties** method should perform the following tasks:

1.  Determine the item type.

2.  Determine whether any special validation should be performed on the incoming WIA properties. To determine which WIA properties are being written, the WIA minidriver can use an array of PROPSPEC structures (the PROPSPEC structure is described in the Microsoft Windows SDK documentation). It is recommended that the WIA minidriver determine the item type before it processes the PROPSPEC array to reduce the need to traverse the array on every **IWiaMiniDrv::drvValidateItemProperties** call. If there are no special validation requirements, or if you need to update dependent properties on the root item of the device, only write requests to child item properties will be processed.

3.  Create a WIA property context to access values that changed during WIA property validation, which is necessary to update the dependent properties for a WIA item. Use the [**wiasCreatePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext) and **wiasGetChangedValue***Xxx* service functions.

4.  Update dependent properties using the WIA service functions, [**wiasWriteMultiple**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiaswritemultiple) or **wiasWriteProp***Xxx*, which includes updating any valid values that might have changed as a result of setting a property. For example, if your WIA minidriver supports setting the [**WIA\_IPA\_DEPTH**](./wia-ipa-depth.md) property, you must update the valid list of bit depths when the application changes the [**WIA\_IPA\_DATATYPE**](./wia-ipa-datatype.md) property.

    When the value of the [**WIA\_IPA\_DATATYPE**](./wia-ipa-datatype.md) property changes from WIA\_DATA\_THRESHOLD to WIA\_DATA\_COLOR, the related WIA\_IPA\_DEPTH property changes from reporting one-bit color depth, to reporting 24 bits or 48 bits.

5.  Call the [**wiasValidateItemProperties**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasvalidateitemproperties) service function to let the WIA service validate all other property requests. This is a "catch-all" case; the WIA service has built-in property validation.

 

