---
title: Sample Code to Create Custom Properties
author: windows-driver-content
description: Sample Code to Create Custom Properties
MS-HAID:
- 'WIA\_drv\_basic\_1f214d44-315e-4629-a42c-9e92d9a2dac4.xml'
- 'image.sample\_code\_to\_create\_custom\_properties'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: cf3e5e5b-8853-43a3-857f-87945cea2aa7
---

# Sample Code to Create Custom Properties


## <a href="" id="ddk-sample-code-to-create-custom-properties-si"></a>


To create a custom property, your WIA driver might have code that looks similar to the following:

```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Sample%20Code%20to%20Create%20Custom%20Properties%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


