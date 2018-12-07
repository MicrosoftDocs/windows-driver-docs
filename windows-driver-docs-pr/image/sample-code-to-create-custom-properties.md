---
title: Sample Code to Create Custom Properties
description: Sample Code to Create Custom Properties
ms.assetid: cf3e5e5b-8853-43a3-857f-87945cea2aa7
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Sample Code to Create Custom Properties

To create a custom property, your WIA driver might have code that looks similar to the following:

```cpp
  //
  // My Custom Property
  //
  PROPID  myCustomPropID = WIA_PRIVATE_DEVPROP + 1;
  WSTR    myCustomName   = L"My Property Name";
 
  //
  //  The following pieces of information are needed to 
  //  insert a property into the property stream:
  //     Property ID             (PROPID)
  //     Property Name           (Wide string)
  //     Property attributes     (WIA_PROPERTY_INFO - 
  //              contains access rights and valid value information)
  //     Initial Property Value  (PROPVARIANT)
  //

  //
  //  Decide which properties to support
  // and their names
  //
  PROPSPEC pPropSpec[NUM_PROPERTIES];
  pPropSpec[0].ulKind = PRSPEC_PROPID;  // Use PROPID
  pPropSpec[0].propid = myFirstPropID;  // My Custom Property
  .
  .
  .
  LPOLESTR pNames[NUM_PROPERTIES];
  pNames[0] = myCustomName; 
         // The string name of the property.
         // For standard WIA properties, the string names are
         // defined in wiadef.h
  .
  .
  .
  //
  //  Make the call to insert the properties.
  //
  hr = wiasSetItemPropNames(pWiasContext,
                            NUM_PROPERTIES,
                            pPropSpec,
                            pNames);
  if ( FAILED(hr) ) {
      //
      //  Failure case.
      //
  }


  //
  //  Fill in the property attributes.  
  //  In this example, My Custom Property
  //  is a WIA_PROP_RANGE value
  //

  WIA_PROPERTY_INFO pWiaPropertyInfo[NUM_PROPERTIES];
  pWiaPropertyInfo[0].vt           = VI_I4; // Valid value type
  pWiaPropertyInfo[0].lAccessFlags = WIA_PROP_RW|WIA_PROP_RANGE;
  pWiaPropertyInfo[0].ValidVal.Range.Min = 0;
  pWiaPropertyInfo[0].ValidVal.Range.Max = 10;
  pWiaPropertyInfo[0].ValidVal.Range.Nom = 5;
  pWiaPropertyInfo[0].ValidVal.Range.Inc = 1;
  //
  //  Etc.  
  //
  .
  .
  .
  //
  //  Make the call to set the property attributes.
  //
  hr = wiasSetItemPropAttribs(pWiasContext,
                            NUM_PROPERTIES,
                                 pPropSpec,
                         pWiaPropertyInfo);
        if ( FAILED(hr) ) {
            //
            //  Failure case.
            //
        }
        //
        //  Set the initial property values
        //
        PROPVARIANT pPropVariant[NUM_PROPERTIES];
        pPropVariant[0].vt   = VT_I4;     // type (in this case: LONG)
        pPropVariant[0].lVal = 5;         // value
 //
        //  Etc.  
        //
        .
        .
        .
        hr = wiasWriteMultiple(pWiasContext,
                               NUM_PROPERTIES,
                               pPropSpec,
                               pPropVariant);
  if ( FAILED(hr) ) {
      //
      //  Failure case.
      //
  }
```

 

 




