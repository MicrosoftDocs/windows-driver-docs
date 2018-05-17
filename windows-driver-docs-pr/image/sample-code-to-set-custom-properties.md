---
title: Sample Code to Set Custom Properties
author: windows-driver-content
description: Sample Code to Set Custom Properties
ms.assetid: 726315eb-de5c-47b6-a35b-524ec1c97d52
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Sample Code to Set Custom Properties


## <a href="" id="ddk-sample-code-to-set-custom-properties-si"></a>


To set a custom property, your application or custom UI might have code that looks similar to the following:

```
    IWiaPropertyStorage *pItemPropertyStorage = NULL;
 
    //
    //  Get the item&#39;s Property Storage
    //
    hr = pMyItem->QueryInterface(IID_IWiaPropertyStorage, (void**)&pItemPropertyStorage);
    if (SUCCEEDED(hr)) {

 
  //
  //  Variables to store the property value and identifier.
  //

  PROPVARIANT pvMyProperty;   // PropVariant to store property value.
  PROPSPEC    psMyProperty;   // PropSpec that identifies the property.
 
  psMyProperty.ulKind = PRSPEC_PROPID;
  psMyProperty.propid = myCustomPropID;   
  //  This should be the same value 
  //  that your driver has.  The
  //  best practice is to put a
  //  define in a header file
  //  that is common to driver
  //  and UI or the application components.
 
  //
  //  Initialize the PropVariant.
  //
  PropVariantInit(&pvMyProperty);
 
  //
  //  Fill in the property value.
  //  This example fills in the number 7 to a LONG type.
  //
  pvMyProperty.vt     = VT_I4;
  pvMyProperty.lVal   = 7;
 
  //
  //  Write the property value.
  //
  hr = pItemPropertyStorage->WriteMultiple(1,
                               &psMyProperty,
                               &pvMyProperty,
                                          0);
  //
  //  Etc.  
  //
  .
  .
  .
    }
```

 

 




