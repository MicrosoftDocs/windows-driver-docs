---
title: Property Contexts
description: Property Contexts
ms.date: 04/20/2017
---

# Property Contexts





A property context provides a convenient way for a minidriver to identify a number of properties it is interested in during the validation of those properties. Using a property context, a minidriver can quickly determine whether any of the identified properties are being changed. The minidriver then passes the property context to one of the WIA service library functions (for example, [**wiasGetChangedValueFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat)), which uses the context to determine whether an application is changing a property's value.

The WIA approach to validation is that when an application changes a property, any dependent properties should also be updated. If, however, the application is also changing dependent properties, you can simply check the top-level property to determine whether its new value is valid. The WIA service library functions that are concerned with property validation use this principle to decide when they should update dependent properties, and when they should just check for validity.

Context for a set of properties is maintained in a [**WIA\_PROPERTY\_CONTEXT**](/windows-hardware/drivers/ddi/wiamindr_lh/ns-wiamindr_lh-_wia_property_context) structure, which contains three members: the number of properties in the property context, a pointer to an array of property identifiers (PROPIDs), and a pointer to an array of BOOL values. The arrays are maintained in parallel (that is, the property whose property identifier is at index *N* in the property identifier array is associated with the BOOL value at the same index in the BOOL array).

The minidriver calls the WIA service library function, [**wiasCreatePropContext**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiascreatepropcontext), to allocate memory and fill in the values for a property context. Other WIA service library functions, such as [**wiasGetChangedValueFloat**](/windows-hardware/drivers/ddi/wiamdef/nf-wiamdef-wiasgetchangedvaluefloat), use a property context to determine when a property's values should be updated.

 

